# Traductores de sentencias

La librería **Sentence-Transformers** (tambien conocida como **SBERT**) es una de las herramientas más potentes y sencillas en Python para trabajar con **embeddings** de texto. Su propósito principal es transformar frases, párrafos o imágenes en vectores numéricos (densos) que capturan su significado semántico.

A diferencia de los modelos BERT tradicionales, que son lenos para comparar textos entre sí, SBERT optimiza este proceso para que pueda calcular la similitud entre millas de documentos en misiles.


## Características Principales

* **Embedings Semánticos:** No se basa en palabras clave (como una búsqueda tradicional), sino en el **contexto**. Tienes que "perro" y "canino" son conceptos similares.
* **Eficiencia:** Permite realizar comparaciones masivas de texto de forma extremamente rápida gracias a su arquitectura de bi-codificadores (*bi-encoders*).
* **Multilingüe:** Soporte modelos que funcionan en más de 100 idiomas, permitiendo incluir comparar una frase en español con una en inglés.
* **Versatilidad:** Además de texto, puede manipular imágenes (modelos CLIP) y búsquedas híbridas.
* **Integración:** Se conecta nativamente con **Hugging Face**, lo que te da acceso a miles de modelos pre-entrados.


## Funciones Clave para RAG (Retrieval-Aumentated Generation)

En un sistema RAG, esta biblioteca se carga de la fase de **Retrieval** (recuperación). Estas son las funciones que más usarás:

### 1. `SentenceTransformer(modelo_nombre)`
Es el constructor para cargar el modelo. Para RAG, los más comunes son `all-MiniLM-L6-v2` (rápido) o `all-mpnet-base-v2` (más precio).

### 2. «model.encode(sentencias)»
Es la función estrella. Convierte tu lista de documentos (o la pregunta del usuario) en vectores.
* **En RAG:** Se usa para indexar el conocimiento en una base de datos vectorial y para vectorizar la duda del usuario.

### 3. «__PATH0_search»
Busca automáticamente los $k$ documentos más similares a una consulta dentro de un corpus de embeddings.

### 4. ‘__PATH0_sim’ (o ‘__PATH1_score’)
Calcula la **similitud de coseno** entre dos vectores. Es único si quieres construir tu propia lógica de filtrado o ranking manual.

### 5. `CrossEncoder`
Aunque es más pesado, se usa en RAG para el **Re-ranking**. Una vez recuperados los 10 mejores resultados con el buscador rápido, el `CrossEncoder` los reordena para asegurar que el más relevante sea el que se le pase al LLM.


## Documentación Oficial

Puedes encontrar tutoriales destacados y la referencia de la API aquí:
> **[https://www.sbert.net/](https://www.sbert.net/)**