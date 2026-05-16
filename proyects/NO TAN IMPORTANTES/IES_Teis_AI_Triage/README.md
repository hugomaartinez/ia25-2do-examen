# Agente de Triaje de Emails — Atención al Cliente TechPyme

Una pequeña tienda online recibe decenas de correos al día. El dueño perfora 2 horas diarias respondiendo dudas básicas o derivando mensajes al departamento correcto.

Nuestro cliente nos pide automatizar este proceso. Para ellos creamos un agente de triaje de emails que actuará como el primer filtro inteligente.

El agente responderá a los correos si sigue encontrando la respuesta en la base de datos creada a partir de las FAQs de TechPyme. Si no sigues encontrado la respuesta lo solicitará al departamento de atención al cliente.

## Simulación

Para simplificar el proceso se simulará la entrada de correos. Se usará un archivo JSON con 4 casos de prueba: un correo fácil (pregunta por el horario), un correo sobre un envío (pregunta por devoluciones) y un correo completo/queja (producto roto, que debe ser escalado).

- Los correos respondidos se registrarán en un archivo CSV llamado correos_respondidos.csv

- Los correos escalados se grabarán en un archivo CSV llamado correos_escalados.csv

- Al finalizar de procesar el archivo JSON se eliminará para no volver a procesar y permitir una nueva ejecución con otro archivo JSON.

## Estructura del Repositorio

A continuación se detalla la estructura principal del proyecto y el contenido de sus directorios:

- **`automation/`**: Contene los scripts principales del agente de la automatización (`agent.py_`, `rag.py_`), creación de la base de conocimiento y el agente que se encarga de responder o derivar los correos. 
- **`desafío/`**: Incluye los derechos y próximos pasos a desarrollar en el proyecto.
- **`docs/`**: Carpeta de documentación. Dentro se encuentra el directorio **`docs/web/`**, que contiene las páginas y recursos a los que acceden **`index.html_`**.
- **`how_to_do_it/`**: Contiene guías paso a paso sobre el desarrollo del proyecto.
- **«index.html_**: Es la página web principal de presentación del repositorio. Sirve como punto de entrada visual para entender el proyecto. [_URL0_](__URL1_).
- **`main.py_**: Script principal que orquesta la ejecución del proyecto, iniciando la base de datos vectorial si es necesario y lanzando el agente.
