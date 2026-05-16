# Casos de Prueba

Este documento describe la estrategia de prueba y los escenarios cubiertos por nuestra suite de pruebas automatizadas en el directorio `tests/`.

## 1. Salvaguarda de Entrada (`test_input_guard.py`)

La salvaguarda de entrada valida la entrada del usuario antes de enviarla al LLM principal. Actúa como la primera línea de defensa.

### Escenarios de Prueba
- **Restricción de Longitud**: Verifica que las cadenas vacías y las cadenas excesivamente largas (p.ej., > 500 caracteres) se rechacen inmediatamente.
- **Fragmentos Bloqueados**: Verifica que las cadenas maliciosas conocidas (como `<script>`, `DROP TABLE`) se bloqueen mediante verificaciones heurísticas.
- **Patrones de Inyección con Regex**: Verifica que se detecten intentos comunes de inyección de prompts (p.ej., "ignora todas las instrucciones anteriores").
- **Juez LLM**: Verifica que los intentos maliciosos complejos u ofuscados que evaden heurísticas se bloqueen por el evaluador de seguridad LLM.

## 2. Salvaguarda de Salida (`test_output_guard.py`)

La salvaguarda de salida asegura que las respuestas del bot no violen políticas ni filtren datos sensibles.

### Escenarios de Prueba
- **Respuestas Vacías**: Verifica que si el backend del LLM devuelve una cadena vacía o solo espacios en blanco, se sustituya un error apropiado.
- **Filtraciones Sensibles**: Verifica que si el bot incluye accidentalmente "api_key" o "system prompt", la respuesta se bloquee.
- **Evaluación del Juez LLM**: Verifica que el evaluador LLM identifique y bloquee correctamente las violaciones de política matizadas en la salida del asistente.
- **Formato**: Asegura que la respuesta final aprobada tenga espacios en blanco iniciales y finales eliminados.

## 3. Orquestador del Engine (`test_engine.py`)

El `ChatEngine` gestiona el estado de la conversación, el enrutamiento del backend y la integración de salvaguardas.

### Escenarios de Prueba
- **Turno Exitoso**: Verifica que un mensaje seguro del usuario se agregue correctamente al historial, se pase al backend, se devuelva la respuesta segura e se actualice el historial.
- **Manejo de Fallos del Backend**: Verifica que si el backend lanza una excepción (p.ej., error de red), el orquestador la intercepte, devuelva un error elegante al usuario, y elimine el mensaje del usuario del historial para que la sesión no se corrompa.
- **Trimado del Historial (Límite de Ventana de Contexto)**: Verifica que cuando la conversación excede `MAX_HISTORY_TURNS`, se evicten los mensajes más antiguos, manteniendo el historial estrictamente dentro de los límites.
