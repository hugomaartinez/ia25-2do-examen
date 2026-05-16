"""
main.py

Punto de entrada para el chatbot con salvaguardas.

Responsabilidades de este archivo (y SOLO este archivo):
    - Cargar configuración usando Pydantic Settings
    - Configurar registro
    - Instanciar ChatEngine
    - Ejecutar el bucle de conversación de terminal
"""

from chatbot.config import load_config
from chatbot.engine import ChatEngine

def main() -> None:
    
    try:
        config = load_config()
    except Exception as e:
        print(f"❌ Error de configuración: {e}")
        return

    engine = ChatEngine(config)

    try:
        engine.check_connection()
    except Exception as e:
        print(f"❌ No se pudo conectar al modelo: {e}")
        return

    print(f"\n🤖  Chatbot con Salvaguardas  |  Modo: {config.mode.upper()}")
    print("    Escribe 'exit' para salir.\n")

    while True:

        # ── Obtener entrada del usuario ─────────────────────────────────────────
        try:
            user_input = input("Tú: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBot: ¡Adiós!")
            break

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit", "bye", "salir"}:
            print("Bot: ¡Adiós!")
            break

        # ── Obtener respuesta del bot ─────────────────────────────────────────
        response = engine.chat(user_input)
        print(f"\nBot: {response}\n")

if __name__ == "__main__":
    main()
