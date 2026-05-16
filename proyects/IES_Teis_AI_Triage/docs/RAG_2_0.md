# EVOLUCIÓN DE LOS RAG

El salto de los sistemas RAG tradicionales (lo que ahora llamamos RAG 1.0) a RAG 2.0 y arquitecturas avanzadas como MemoRAG representa la evolución natural para solucionar los "puntos ciegos" que tenían los primeros sistemas.

Para entender su evolución, hay que mirar cuál era el problema original: el RAG clásico era como un estudiante buscando en un libro de texto usando solo el índice. Cortaba los documentos en trozos (chunks), buscaba los más parecidos a la pregunta y se los daba a la IA. Funcionaba muy bien para datos concretos ("¿Cuál es el capital de la empresa?"), pero fracasaba estrepitosamente en preguntas que requerían ver la imagen completa ("¿Cuál es el tono general de todas las comunicaciones de este cliente?").

Aquí tienes cómo estas nuevas arquitecturas resuelven esos problemas:

## RAG 2.0: El enfoque "End-to-End" (De principio a fin)

El término RAG 2.0 (popularizado por empresas como Contextual AI) no es una herramienta nueva, sino un cambio total de paradigma en cómo se construye el sistema.

- **Optimización conjunta (El gran cambio)**: En RAG 1.0, usabas un modelo de embeddings (como los que vimos antes) y un LLM (como GPT-4 o Gemini) por separado. Eran como dos extraños trabajando juntos. En RAG 2.0, el buscador (retriever) y el generador (LLM) se entrenan o se ajustan juntos. El LLM aprende qué tipo de documentos necesita recuperar, y el buscador aprende cómo el LLM prefiere recibir la información.

- **Flujos de trabajo Agénticos**: En lugar de ser un proceso lineal (Pregunta -> Buscar -> Responder), RAG 2.0 introduce agentes. Si el sistema recupera información que no responde del todo a la pregunta, el propio agente "se da cuenta", reformula la búsqueda automáticamente, vuelve a buscar, y solo te responde cuando está seguro de tener la respuesta correcta.

- **GraphRAG integrado**: Muchos sistemas RAG 2.0 incorporan Grafos de Conocimiento. No solo buscan por similitud de palabras, sino que entienden las relaciones. Saben que "Persona A" es "CEO" de "Empresa B", y pueden seguir ese hilo lógico.

## MemoRAG: La revolución de la "Memoria Global"

MemoRAG es una arquitectura específica (surgida a finales de 2024) que ataca directamente el problema de no poder ver el "bosque completo por culpa de los árboles". Introduce un paso intermedio brillante.

- **El modelo de memoria dual**: En lugar de ir directamente a buscar trozos de texto, MemoRAG utiliza un modelo más pequeño y eficiente para leer y comprimir toda tu base de datos en una "memoria global".

- **Generación de "pistas" (Clues)**: Cuando haces una pregunta compleja, MemoRAG primero consulta su memoria global y genera una "pista" o un borrador mental de la respuesta.

- **Búsqueda guiada**: Luego, utiliza esa pista para decirle al buscador exactamente qué trozos de texto originales necesita extraer para validar y enriquecer la respuesta.

Un ejemplo práctico de la evolución:
Imagina que tienes un repositorio legal con 500 sentencias de un mismo juez.

RAG 1.0: Si preguntas "¿Qué opina este juez sobre los delitos fiscales?", buscará los 5 trozos de texto donde más se mencionen esas palabras. Te dará una respuesta sesgada basada solo en esos 5 párrafos aislados.

MemoRAG: Su memoria global recuerda la tendencia general de las 500 sentencias. Generará una pista como "Este juez suele ser severo, pero aplica atenuantes si hay confesión". Luego, buscará los casos exactos que demuestran esto y te dará una respuesta que refleja la realidad de todo el repositorio, no solo de unos pocos fragmentos.

En resumen: pasamos de sistemas que buscan a ciegas (RAG 1.0), a sistemas que piensan antes de buscar y aprenden en conjunto (RAG 2.0 y MemoRAG).

## BM25 (Best Matching 25)

BM25, o **Best Matching 25**, es una función de clasificación utilizada por los motores de búsqueda para estimar la relevancia de los documentos frente a una consulta de búsqueda determinada. Se basa en el modelo probabilístico de recuperación de información y se considera una mejora significativa respecto al modelo tradicional TF-IDF (Term Frequency-Inverse Document Frequency).

### Conceptos Clave de BM25

BM25 calcula una puntuación para cada documento basada en la presencia y frecuencia de los términos de búsqueda. A diferencia del TF-IDF simple, BM25 incorpora la **saturación de la frecuencia del término** y la **normalización de la longitud del documento**.

#### 1. Saturación de la Frecuencia del Término (TF)
En los modelos básicos, la puntuación aumenta linealmente con el número de veces que un término aparece en un documento. BM25 reconoce que, después de cierto punto, ver un término "una vez más" añade rendimientos decrecientes en cuanto a relevancia. Utiliza un parámetro de saturación (generalmente denotado como `k1`) para limitar este efecto.

#### 2. Normalización de la Longitud del Documento
BM25 penaliza los documentos que son excesivamente largos y premia aquellos que son concisos, en relación con la longitud promedio de los documentos en el corpus. Esto está controlado por un parámetro `b`.

### La Fórmula de BM25

La puntuación para un documento `D` dada una consulta `Q` se calcula de la siguiente manera:

$$Score(D, Q) = \sum_{i=1}^{n} IDF(q_i) \cdot \frac{TF(q_i, D) \cdot (k_1 + 1)}{TF(q_i, D) + k_1 \cdot (1 - b + b \cdot \frac{|D|}{avgdl})}$$

Donde:
* **`q_i`**: Términos de la consulta.
* **`TF(q_i, D)`**: Frecuencia del término en el documento.
* **`IDF(q_i)`**: Frecuencia Inversa de Documento (Inverse Document Frequency), que mide qué tan raro es el término en todo el corpus.
* **`|D|`**: Longitud del documento.
* **`avgdl`**: Longitud promedio de los documentos en el corpus.
* **`k1`**: Un parámetro (típicamente entre 1.2 y 2.0) que controla la saturación de la frecuencia del término.
* **`b`**: Un parámetro (típicamente 0.75) que controla la cantidad de normalización por la longitud del documento.

### ¿Por qué usar BM25?

* **Mejor Rendimiento:** Maneja la frecuencia de los términos de manera más intuitiva que TF-IDF.
* **Robustez:** Es altamente efectivo en diversos tipos de documentos y longitudes de consulta.
* **Estándar de la Industria:** Es el algoritmo de clasificación predeterminado para los principales motores de búsqueda y bibliotecas como **Elasticsearch**, **Lucene** y **Solr**.