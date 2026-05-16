"""
engine.py

El orquestador central del chatbot.

Este módulo es el único que importa de todos los demás. Todo lo demás
está aislado: las salvaguardas no conocen los backends, los backends no se conocen
entre sí, y main.py solo conoce este módulo.

Flujo de mensajes para cada turno:
    entrada del usuario
        ↓
    [input_guard.validate()]  ← rechaza si no es seguro (sin tokens gastados)
        ↓ (si está ok)
    history.append(mensaje del usuario)
        ↓
    [backend.get_response()]  ← llama al LLM (local o remoto)
        ↓
    [output_guard.validate()] ← rechaza si la respuesta es problemática
        ↓ (si está ok)
    history.append(mensaje del asistente)
        ↓
    devuelve respuesta al llamador (main.py)

Si la llamada al backend genera una excepción (error de red, modelo no encontrado…),
o si la salvaguarda de salida bloquea la respuesta, el mensaje del usuario se elimina
del historial para que el siguiente turno comience desde un estado limpio.
"""

from chatbot.config import BaseChatConfig
from chatbot.backends.factory import create_backend, create_judge_backend
from chatbot.guardrails import input_guard, output_guard


class ChatEngine:
    """
    Gestiona una sesión de conversación completa.

    Esta clase es el corazón de la aplicación. Mantiene el estado de la
    conversación (historial) y ejecuta cada mensaje a través del pipeline completo:
    salvaguardas → backend → salvaguardas.

    Una instancia de ChatEngine = una sesión de conversación.
    Para iniciar una nueva conversación, crea un nuevo ChatEngine (o llama a history.clear()).
    """

    def __init__(self, config: BaseChatConfig) -> None:
        self.config = config
        # El historial es una lista de dicts {"role": ..., "content": ...}.
        # Roles: "user" para mensajes del usuario; backend.assistant_role para mensajes del bot.
        self.history: list[dict] = []
        self.backend = create_backend(config)
        self.judge_backend = create_judge_backend(config)

    def check_connection(self) -> None:
        """Verifica que el backend sea alcanzable. Genera una excepción en caso de fallo."""
        self.backend.ping()

    def _trim_history(self) -> None:
        """
        Descarta mensajes antiguos cuando el historial excede el límite de turnos configurado.

        Por qué importa:
            Los LLMs tienen una "ventana de contexto" — un número máximo de tokens que
            pueden procesar en una única llamada. Enviar el historial completo de una
            conversación larga puede exceder ese límite (y aumenta el costo de API para
            modelos remotos).

            1 turno = 1 mensaje del usuario + 1 mensaje del asistente = 2 entradas de lista.
            Solo mantenemos los turnos más recientes max_history_turns.
        """
        max_messages = self.config.max_history_turns * 2
        if len(self.history) > max_messages:
            # Corte desde el final: mantén los mensajes más recientes
            self.history = self.history[-max_messages:]

    def chat(self, user_input: str) -> str:
        """
        Procesa un mensaje del usuario y devuelve la cadena de respuesta del chatbot.

        Este método nunca genera excepciones — captura todos los errores del
        backend y devuelve un mensaje de error amigable para el usuario en su lugar.
        Esto mantiene el código llamador (main.py) simple.

        Devuelve:
            La respuesta del bot, o un mensaje de error/advertencia prefijado con
            ⚠️ (rechazo de salvaguarda) o ❌ (error de backend/red).
        """

        def llm_judge(prompt: str) -> str:
            judge_history = [{"role": "user", "content": prompt}]
            try:
                return self.judge_backend.get_response(judge_history)
            except Exception as exc:
                return "ERROR"

        # ── PASO 1: SALVAGUARDA DE ENTRADA ───────────────────────────────────────────
        ok, reason = input_guard.validate(user_input, llm_judge)
        if not ok:
            return f"⚠️  {reason}"

        # ── PASO 2: AGREGAR AL HISTORIAL ────────────────────────────────────────────
        self.history.append({"role": "user", "content": user_input})
        self._trim_history()

        # ── PASO 3: LLAMAR AL BACKEND ────────────────────────────────────────────────
        try:
            raw = self.backend.get_response(self.history)
        except Exception as exc:
            self.history.pop()
            return f"❌  Error al conectar con el modelo: {exc}"

        # ── PASO 4: SALVAGUARDA DE SALIDA ────────────────────────────────────────────
        ok, result = output_guard.validate(raw, llm_judge)
        if not ok:
            self.history.pop()
            return f"⚠️  {result}"

        # ── PASO 5: GUARDAR RESPUESTA Y DEVOLVER ────────────────────────────────────
        # Cada backend declara su propio nombre de rol asistente (p.ej. "model" para
        # Gemini, "assistant" para Ollama). Usamos eso para mantener la consistencia.
        self.history.append({"role": self.backend.assistant_role, "content": result})

        return result
