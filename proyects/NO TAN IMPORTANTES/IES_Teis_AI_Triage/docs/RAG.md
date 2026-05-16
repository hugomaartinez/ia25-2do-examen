# RAG (Generación Recovery-Aumentada)

Es una técnica que combina la generación de texto de grandes modelos de lenguaje (como ChatGPT, Gemini o Claude) con la recuperación de información específica desde una base de datos o base de conocimiento. En términos prácticos, esta técnica mezcla las habilidades conversacionales de la inteligencia artificial con la capacidad de consultar documentos precios antes de entregar una respuesta al usuario. 

Su utilidad principal radica en solucionar las limitaciones de conocimiento de los modelos de inteligencia artificial tradicional, brindando los siguientes beneficios:

- **Erradicar las asignaciones**: Es ideal para aplicaciones donde se requiere exacto, ya que evita que el modelo de lenguaje inventa respuestas (alucina) obligando a fundamentar su contestación en los documentos externos.
- **Acceso a información actualizada y privada**: Los modelos genéticos tienen un conocimiento estadístico (por ejemplo, desconocer un cambio de presidente reciente o noticias futuras) o ignorar datos internos de una empresa. RAG permite que el modelo busque la última versión de la información o consulte datos de nicho al instante.
- **Personalización sin reentrenamiento**: Permita adaptar el conocimiento del modelo a un caso de uso particular y mantener sus datos al día sin tener que volver a los procesos de reentrenamiento de la IA, los cuales son sumamente caros y requieren de servicios gigantes.

En reafirmación, el RAG funciona como un puente que le permite al modelo de lenguaje leer tus documentos relevantes justo antes de responder, asegurando una interacción inteligente, actualizada y totalmente confiable.

En la técnica de RAG, el flujo de trabajo para que la inteligencia artificial responda con información precisa se divide en tres macroprocesos: Indexing (Indexación), Retrieval (Recuperación) y Generation (Generación).

## INDICE

Este es el proceso de preparación y carga de tu base de datos o documentos para que el sistema los pueda mostrar. En esta fase inicial, se toman todos los documentos de la base de conocimiento (por ejemplo, archivos PDF, páginas web, documentos de Word, etc.) y se procesan para convertirlos en un formato que la IA puede mostrar y consultar eficientemente. Este proceso implica dividir los documentos en fragmentos más pequeños, generar representacións numéricas de su contenido y conservarlos en una base de datos especializada llamada vector store (base de datos vectorial). Esta base de datos permite realizar búsquedas rápidas basadas en la simulación semántica del contenido.

### DIVISIÓN DE FRAGMENTOS

Primero, los documentos de texto se dividen en partes más pequeñas conocidas como trozos o pedacitos. Esto se hace porque los modelos de lenguaje tienen un límite en su "ventana de contexto" (la capacidad de información que pueden leer a la vez) y porque extraer pedazos específicos ayuda a que la información seleccionada sea mucho más relevante para el usuario.

Para crear los trozos (fragmentos de texto) de manera efectiva en un sistema RAG, se debe considerar los siguientes aspectos técnicos y estructurales:

- **Mantener un tamaño equilibrado**: Los documentos extensos no pueden procesarse por completo debido a que los modelos de lenguaje tienen una "ventana de contexto" limitada. Por él, el tamaño de cada trozo no debe ser ni muy grande ni muy pequeño. Si el fragmento es excesivo, se dificulta la selección de datos exactos, pero si es muy discreto, se vuelve complicado realizar una búsqueda de información que tenga sentido. Un ejemplo práctico es estable un tamaño de fragmento de 1.000 unidades.
- **Realizar divisiones lógicas**: Es crucial evitar cortar el texto a la mitad de una palabra o de una fracción. Para registrar esto, se emplean herramientas (como divisores de oraciones o divisores de texto recursivos de librerías como LangChain) que intentan separar la información agrupando por párrafos o privilegiando los cortes donde hay un punto seguido.
- **Aplicar solapamiento (Chunk Overlap)**: A la hora de realizar los cortes, se debe incluir un margen de superposición, lo cual significa que una canción determinada de caracteres del final de un trock se incluirá al principio del siguiente. Esta técnica es indispensable para que las ideas no pasen su contexto si una oración importante llegue a dividirse entre dos fragmentos separados.

Las herramientas y librerías destacadas para facilitar la división de documentos en trozos son:

- **LangChain**: Es un framework que ofrece procesos automáticos y librerías especializadas para la división de textos. Una de sus herramientas más utilizadas es el Recursive Character Text Splitter, el cual intenta dividir la información acumulada en párrafos y privilegios hacer los cortes donde hay un punto seguido, evitando así cortar oraciones o palabras por la mitad.
- **LlamaIndex**: Es otra herramienta que permite leer documentos (como PDFs) y fragmentarlos. LlamaIndex utiliza herramientas como el Divisor de oraciones, con el cual se puede configurar de manera exacta el tamaño de cada trozo y la cantidad de solapamiento entre un fragmento y el siguiente.

### CONVERSIÓN A NÚMEROS

La fase de embeddings es el proceso mediante el cual los fragmentos de texto (chunks) o documentos se transforman en representacións numéricas, conocidas matemáticamente como vectores. Dado que las máquinas no entenden español ni ningún otro idioma humano, necesitario convertir las frases en listas de números para poder procesar la información. 

Esta facilidad funciona de la siguiente manera:

- **Captura del significado**: Un modelo de embeddings no asigna números alzar, sino que está entrenado para capturar matemáticamente el significado semántico de las palabras y oraciones. Puedes imaginar el resultado como un "mapa" o un espacio vectorial multidimensional.
- **Coordenadas de simulación**: En este mapa, los conceptos que comparten significado se encuentran cerca unos de otros. Por ejemplo, si el texto menciona "manzanas" y "peras", el modelo les asignará coordenadas numéricas muy similares, agrupandolas en la misma zona. Lo mismo sucede con conceptos como "rey" y "reina". Por el contrario, un concepto completamente distante, como "mecánica cuántica", recibirá números que lo ubicarán muy lejos de las frutas.
- **Alta complejidad (Dimensiones)**: Para lograr capturar todos los aspectos del lenguaje, los modelos no usan solo dos o tres coordinadas. Un modelo de embeddings moderno (como los de OpenAI) puede utilizar miles de valores para un solo fragmento, por ejemplo, 1.536 dimensiones o números distintos, los cuatro suelen ser valores que oscilan entre el -1 y el 1.
- **Matemáticas con el lenguaje**: Esta conversación numérica es tan profunda que permite encontrar relaciones lógicas haciendo cambios. Por ejemplo, en este espacio vectorial, si toman los números que representan la palabra "rey", las restauraciones los de la palabra "hombre" y las sumas los de "mujer", el resultado numérico es equivalente a la palabra "reina".

#### ¿Por qué es fundamental en un sistema RAG? 
Tener los textos convertidos a embeddings es lo que hace posible que la IA encuentre respuestas exactas a una velocidad increíble. Cuando el usuario realiza una pregunta, esta consulta también se transforma en números utilizando el mismo modelo.
A partir de ahí, el sistema ya no busca coincidencias exactas de palabras, sino que utiliza fórmulas matemáticas (como el **producto punto** o la **similitud coseno**) para medir la distancia entre los números de la pregunta y los números de los documentos. Asumiendo que los vectores matemáticos más cercanos son semánticamente los más relevantes, el sistema extrae el fragmento exacto que necesita y se lo entrega al modelo de lenguaje para que redacto tu respuesta

**El producto punto**: Es una métrica directa que se utiliza para calcular la distancia espacial exacta entre el vector de la pregunta original y los vectores de los fragmentos de texto conservados en tu base de datos.
**La similitud supuesto**: Es otro algoritmo para calcular la distancia entre diferentes puntos en la base de datos. Al mostrar una búsqueda con simulación supuesto, el sistema no solo revela el texto recuperado, sino también un "score" (puntuación) de confianza o simulación. Si este score es muy bajo, le indica al sistema que la información encontrada no es lo suficiente relevante, lo cual es un mecanismo vital para evitar que el modelo de lenguaje termina alucinando o inventando respuestas

#### Modelos de incrustaciones especializadas

Existen modelos de embeddings especializados para puertas industriales, incluyendo el ámbito legal y el técnico o de programación.
Aunque los modelos de uso general (como los de OpenAI) son muy populares, utilizando un modelo especializado puede mejorar significativamente la forma en que el sistema entre la información. Esto se debe a que:

**En documentos legales**: Si administras exclusivamente archivos legales, un modelo de embeddings entrenado específicamente para este sector logrará capturar mucho mejor los significados específicos y los matices de la terminología jurídica, algo que un modelo general podría pasar por alto. Los textos legales son un reto enorme para la IA. Utilizan un vocabulario muy rígido, frases extremamente largas, referencias cruzadas (ej. "en virtud del artículo 4.2 b") y la sutil diferencia entre un "debe" y un "puede" cambia por completo el sentido del documento.

- **Voyage-Law-2 (de Voyage AI)**: Es uno de los modelos comerciales más potentes ahora mismo para el sector legal.
- **LEGAL-BERT / CaseLawBERT**: Son modelos open-source (de código abierto) basados en la arquitectura clásica de BERT, pero entrenados exclusivamente con textos legales desde cero.


**En documentos técnicos o código**: Para áreas como la programación, existen modelos que comprenden la importancia de elementos técnicos que un modelo amplio ignoraría. Por ejemplo, en el código, un coche invisible como el "tab" (tabulación) tiene un significado estructural crucial que un modelo especializado sí logra interpretar correctamente.

- **Qwen3-Embedding / Familia Qwen2.5-Coder**: Son de lo mejor en el panorama open-source real para entender código y documentos técnicos.

- **jina-embeddings-v2-base-code**: Un modelo de código abierto de Jina AI entrenado específicamente para áreas de búsqueda de código.

**Un detalle clave que a veces se olvida**
Para entornos hiper-especializados como el legal o la programación, la forma en la que "troceas" los documentos es casi tan importante como el modelo de embeddings. Por ejemplo, al vectorizar código, es un error fatal cortar una función por la mitad; y en textos legales, siempre es mejor dividir semánticamente por artículos o células completas que por un número fichero de palabras.

### ALMACENAMIENTO

La fase de almacenamiento es el paso donde los fragmentos de texto (chunks) que ya fueron convertidos a representación matemática se guardan de manera estructurada para que el sistema pueda consultarlos e interpretarlos de forma rápida.
Para que esta facilidad funcione de manera eficiente, el proceso depende de tecnologías y estructuras específicas:

- **Bases de datos vectoriales**: A diferencia de las bases tradicionales (SQL), la información se almacena en motores diseñados nativamente para comprender e indexar listas de números multidimensionales, estableciendo opciones como **Chroma DB** o **Qdrant**. Un año en pruebas de concepto pequeñas se puede guardar temporalmente en una tabla común o un DataFrame de **Pandas**, en detalles reales es indispensable contar con una base de datos vectorial.
    
- ** Estructura de la información (Point Struct)**: Al momento de insertar la información en la base de datos, no se guardan únicamente los números alzar. Cada fragmento se encapsula con tres elementos fundamentales:
- **El vector**: La representación numérica (por ejemplo, miles de dimensiones) del texto.
- **El Payload (Carga útil)**: Es el contenido real que entienden los humanos. Contiene el texto original del trock y sus metados (como el nombre del archivo y el número de página), lo cual es vital para que la IA, después de hacer la coincidencia matemática, pueda leer la información y citar sus fuentes.
- **El ID único**: Un identificador generado criptográfico (como un hash MD5 o un UUID) que se le asigna a cada fragmento para evitar que la base de datos se llene de información duplicada si se procesa el mismo archivo más de una vez.
- **Velocidad de búsqueda**: Para poder manejar gigabytes de datos sin colapsar, estas bases de datos agrupan los vectores utilizando algoritmos de indexación avanzada (como HNSW, Jerarquía Navigable Small World). Esto transforma las búsquedas de un modo lineal a un modo logarítmico, permitiendo encontrar el dato exacto entre miles de archivos casi instantáneamente.
- **Persistencia en disco duro**: Un parámetro crítico en la fase de almacenamiento es configurar la base de datos para que persista (guarde) la información en el disco físico del servidor o computadora, y no solitario en la memoria RAM. Si los datos solo residen en memoria, al añadir el script se perderán todas las horas de indexación y el costo invertido en la API que generó los embeddings. Al persistirlos, la base de conocimiento se carga en misiles en usos futuros

## RETRIEVAL (Recuperación)

Es el proceso donde el sistema busca y extrae la información exacta que necesita para responder la duda del usuario. Cuando un usuario realiza una consulta, el sistema primero analiza esa pregunta y la convierte en un vector numérico. Lucego, busca en la base de datos vectorial los fragmentos de documentos que son más relevantes semánticamente para la consulta. Estos fragmentos recuperados se consideran el "contexto" relevante para la pregunta del usuario.

- **Traducción de la pregunta**: Cuando el usuario realiza una pregunta, el sistema toma ese texto y lo transforma en una lista de números o vectores (embeddings) utilizando el mismo modelo que se aplicó en la fase de indexación. Esto se hace porque las máquinas necesitan comparar "números con números" para encontrar información.
- **Comparación matemática**: Una vez que la pregunta está en formato numérico, el sistema busca en la base de datos vectorial y compara el vector de la pregunta con los vectores de todos los fragmentos de texto (chunks) almacenados. Para medir qué tan cerca o lejos están estos puntos en el espacio vectorial, utiliza fórmulas matemáticas como el producto punto o la simulación coseno.
- ** Selección por relevancia semántica**: El sistema asume que los números que matemáticamente más se parecen son los más relevantes. De esta forma, selecciona el fragmento o los fragmentos de la base de datos que mayor similitud o score más alto tienen con la pregunta del usuario.

- **Recuperación y entrega**: Finalmente, el sistema extrae esos fragmentos altos relevantes de la base de datos y los deja listados para entregarlos al modelo de lenguaje (junto con la pregunta original del usuario), dando paso así a la fase final de generación de la respuesta.
  
**En revelación**, la fase de recuperación actuará como un buscador matemático ultra rápido que, en lugar de buscar coincidencias exactas de palabras, busca ideas o significados similares utilizando geometría y vectores para encontrar el documento exacto que el modelo de IA necesita leer

## GENERACIÓN

Es el paso final donde la inteligencia artificial formula la respuesta para el usuario. Finalmente, el modelo de lenguaje grande recibe la consulta original del usuario junto con los fragmentos de documentos recuperados en la fase anterior. El modelo utiliza esta información contextual para generar una respuesta precisa y fundada, evitando soluciones y proponiendo información actualizada basada en los documentos propuestos.

- **Construcción del Contexto**: El sistema toma el fragmento o los fragmentos de texto alto relevantes que extrajo de la base de datos en el paso anterior y los junta con la pregunta original del usuario.
- **Diseño del Prompt (Instrucciones Estrictas)**: Toda esta información se ensambla en un prompt o instrucción maestra. Aquí indica el secreto del RAG: se le exige al modelo que actúa como un asistente servicial, pero con la regla inquebrantable de responder única y exclusivamente bajo dosis en el texto de referencia propio. Tambíen se le suele construir explícitamente que evite inventar datos si no los encuentra en el texto y que, de ser posible, cite las fuentes exactas de su respuesta.
- **Instrucción al modelo (Prompting)**: Este paquete completo (las instrucciones, el contexto recuperado y la pregunta) se enviaba a un Modelo de Lenguaje Grande o LLM (como GPT-4, Llama 3, Mistral o Gemini). Al tener la información real justo a su lado (como en un examen a libro abierto), la IA no necesita dependiente de su memoria de entrenamiento predeterminada.
- **Respuesta final**: El modelo lee esos párrafos precios, procesa la respuesta y la articulación perfectamente en lenguaje natural para el usuario.

**En revelación**, gracias a estas restricciones impugnadas en la fase de generación, se llama erradicar el problema de las alteraciones, asegurando que la IA se base en hechos reales y en la documentación entregada, en lugar de su imaginación.

