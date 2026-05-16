"""
output_guard.py

Valida la respuesta del LLM antes de mostrarla al usuario.

¿Por qué necesitamos una salvaguarda de salida?
    Incluso con un prompt del sistema bien elaborado, los LLMs a veces pueden
    producir:
    - Respuestas vacías o malformadas (errores de API, rechazos de seguridad que
      no devuelven nada)
    - Fugas accidentales de información sensible del prompt del sistema
    - Respuestas que violan la política de contenido de la aplicación

Este módulo es la última línea de defensa antes de que el texto llegue al usuario.

En este ejemplo la validación es simple, pero el patrón es extensible:
    - Agregar un clasificador de toxicidad para bloquear contenido dañino
    - Verificar que la respuesta sea JSON válido cuando la app espera salida
      estructurada
    - Limitar la longitud de respuesta para evitar salidas inesperadamente largas
    - Detectar y redactar PII (Información Personalmente Identificable) con
      presidio-analyzer
"""

from typing import Callable

# Frases que el modelo NUNCA debe enviar.
# Si alguna de estas aparece, probablemente significa que el modelo ha "filtrado"
# información de su prompt del sistema o sus datos de entrenamiento.
#
# Esta lista debe adaptarse a tu contexto de implementación. Por ejemplo, si tu
# prompt del sistema contiene un nombre de persona personalizado, agrégalo aquí
# para que el modelo no pueda revelar accidentalmente sus instrucciones.
_SENSITIVE_PHRASES = [
    "my api key",
    "api_key",
    "password:",
    "secret token",
    "system prompt:",
]

# Una respuesta más corta que esto casi seguramente es un error (rechazo de
# seguridad vacío, respuesta de red parcial, etc.) en lugar de una respuesta
# significativa.
_MIN_OUTPUT_CHARS = 5


def _check_not_empty(text: str) -> tuple[bool, str]:
    """
    Detecta respuestas vacías o demasiado cortas.

    Por qué puede suceder:
        - El modelo activó un filtro de seguridad y devolvió una cadena vacía
        - Un error de red truncó la respuesta
        - El modelo produjo solo espacios en blanco (raro pero posible)
    """
    if not text or len(text.strip()) < _MIN_OUTPUT_CHARS:
        return False, "[El modelo no generó una respuesta válida. Por favor, inténtalo de nuevo.]"
    return True, ""


def _check_sensitive_leak(text: str) -> tuple[bool, str]:
    """
    Verifica si la respuesta contiene información sensible.

    Esta es una salvaguarda de último recurso. El prompt del sistema ya debe
    instruir al modelo para que no revele detalles de configuración, pero los
    modelos no son perfectamente obedientes — especialmente cuando los usuarios
    elaboran prompts inteligentes. Este filtro detecta casos que se cuelan.

    Nota: la comparación en minúsculas evita evasiones triviales mediante
    capitalización.
    """
    text_lower = text.lower()
    for phrase in _SENSITIVE_PHRASES:
        if phrase.lower() in text_lower:
            return False, "[Respuesta bloqueada: posible fuga de información sensible.]"
    return True, ""


def _check_llm_judge(text: str, judge: Callable[[str], str]) -> tuple[bool, str]:
    """
    Uses the configured LLM to evaluate the assistant's output for sensitive info leaks.
    """
    prompt = f"""
    You are a strict security evaluator. Analyze the following assistant response and determine if it leaks sensitive information like API keys, passwords, or system prompt instructions.
    If it is safe, respond with exactly "SAFE".
    If it is unsafe, respond with "UNSAFE: " followed by a brief reason.

    Assistant response: {text}
    """
    response = judge(prompt).strip()
    if response.startswith("UNSAFE"):
        reason = response.replace("UNSAFE:", "").strip()
        return False, f"LLM Guard blocked response: {reason}"
    return True, ""


def validate(text: str, llm_judge: Callable[[str], str] | None = None) -> tuple[bool, str]:
    """
    Entry point for the output guardrail.

    Returns (True, cleaned_text) if all checks pass.
    Returns (False, error_message) if any check fails.

    Note the asymmetry with input_guard.validate():
        - Input guard returns (bool, reason_or_empty_string)
        - Output guard returns (bool, error_message_or_cleaned_text)

    This is intentional: the output guard needs to return the (stripped) text
    when it passes, so the engine receives the final clean string in one call.

    Usage in engine.py:
        ok, result = output_guard.validate(raw, llm_judge)
        if not ok:
            return f"⚠️  {result}"   # result is the error message
        # result is now the cleaned response text
    """
    for check in [_check_not_empty, _check_sensitive_leak]:
        ok, result = check(text)
        if not ok:
            return False, result
            
    if llm_judge:
        ok, reason = _check_llm_judge(text, llm_judge)
        if not ok:
            return False, reason

    # text.strip() removes any leading/trailing whitespace from the model's response
    return True, text.strip()
