# Langchain-Ollama

La librería **`langchain-ollama`** es el puente oficial que conecta el ecosistema de **LangChain** con **Ollama**. Su función principal es permitir ejercer Modelos de Lenguaje Grandes (LLMs) de forma **local** (en tu propia computadora) e integrarlos fácilmente en aplicaciones completas, cadenas y agentes.


## Características Principales

* **Ejecución Local:** Permita usar modelos como Llama 3, Mistral o Phi-3 sin dependiente de APIs de pago (como OpenAI) ni envidiar datos a la nube.
* ** Integración Nativa:** Está diseñada específicamente para el nuevo estado de LangChain (`langchain-core`), lo que garantiza competitividad con herramientas modernas como LangGraph.
* ** Soporte Multimodal:** No solo maneja texto; si el modelo lo permite (como LAVA), puedes procesar imágenes.
* **Streaming y JSON Mode:** Soporta respuestas en tiempo real (palabra por palabra) y puede formar al modelo a responder en formato JSON, algo vital para que los agentes extraigan datos estructurados.

## Funciones Clave para Crear Agentes

Para que un agente funcione, necesita un "cerebro" (el modelo), "manos" (herramientas) y un "sistema de razonamiento". Aquí las funciones esenciales:

### 1. `ChatOllama`
Es la clase principal para instalar el modelo. Para agentes, es crucial activar el parámetro `format="json"` o usar modelos que soportan **Tool Calling**.

### 2. «bind_tools()»
Esta es la función más importante para agentes modernos. "Vincula" una lista de herramientas (funciones de Python) al modelo para que este sepa que pueda usarlas.

### 3. `create_react_agent` (o LangGraph)
Unque LangChain tiene funciones *legacy*, la forma estádar real de crear agentes es mediana **LangGraph**. Se utiliza para definir el ciclo de: *Razonamiento -> Acción -> Observación*.

### 4. `OllamaEmbedings`
Unque los agentes rasonan con el chat, a menú neceitan memoria o buscar documentos. Esta función convierte texto en vectores localmente para alimentar la base de datos del agente.


## Ejemplo Rápido de Agente

Para crear un agente que use herramientas con Ollama, el flujo lógico es:
1.  **Definir la herramienta:** Una función decorada con "tool".
2.  **Preparar el Prompt:** Usar un `ChatPromptTemplate` que indica al agente como actuar.
3.  **Ejecutar el Loop:** Usar un ejecutor que procese la salida del modelo y llame a la función de Python correspondiente.


## Documentación Oficial

Puedes encontrar todos los detalles técnicos y guías de migración aquí:
> **[Paquete de socios de LangChain Ollama](https://python.langchain.com/docs/integrations/chat/ollama/_)**