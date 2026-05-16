# ChromaDB

ChromaDB es una base de datos vectorial de código abierto diseñada específicamente para construir aplicaciones de Inteligencia Artificial (IA).

A diferencia de las bases de datos que almacenan texto simple, ChromaDB almacena vectores (también conocidos como embeddings). Un embedding es una representación matemática de un dato (como un fragmento de texto, una imagen o un audio) convertida en una larga lista de números. Los modelos de IA utilizan estos vectores para entender el "significado" o el contexto derás del texto.

Si dos frases tienen un significado similar (por ejemplo, "pero juguetón" y "cachorro feliz"), sus vectores estarán ubicados muy cerca el uno del otro en este espacio matemático multidimensional. ChromaDB se carga de almacenar millones de estos vectores y de buscar rápidamente cuáles están más cerca entre sí.

## ¿En qué se diferencia de una base de datos SQL?

La diferencia principal radica en cómo recordaran la información y cómo la buscaran.

**Bases de Datos SQL** (como PostgreSQL o MySQL):

- ** Estructura**: Guardan la información en tablas rígidas con filas y columnas.

- **Búsqueda**: Utilizan coincidencia exacta o palabras clave. Si buscas DÓNDE el título COMO '%perro%', la base de datos solo te devolvirá resultado que contengan la palabra exacta "perro". Si un documento habla de un "cachorro" o un "sabueso", SQL no lo encontrará a menos que le programas reglas completas.

**ChromaDB** (Base de Datos Vectorial):

- ** Estructura**: Guarda listas de números junto con metadatos.

- **Búsqueda**: Utiliza similitud semántica. No busca palabras exactas, sino conceptos similares. Si buscas "animales domésticos de cuatro patas", ChromaDB calculará el vector de tu pregunta y encontrarás los vectores más cercanos a él, devolvéndote documentos sobre "peros" o "gatos", incluido si las palabras exactas de tu búsqueda no aparecen en el texto.

**En resumen**: Se usan bases de datos vectoriales como ChromaDB para RAG porque los LLMs no pueden leer una biblioteca entera de documentos cada vez que les hacen una pregunta (sería prestado y muy costoso). ChromaDB actuará como un bibliotecario ultrarrápido que, bajo dosis en el "significado" de tu pregunta, va a la estantería, Saca solo las 3 o 4 páginas que tienen la respuesta correcta, y se las entrega al LLM para que te explique la solución.

## ¿Porqué ChromaDB usa SQLite entonces?

Para mostrar por qué ChromaDB usa SQLite, primero hay que declarar un detalle arquitectónico clave: ChromaDB no usa SQLite para buscar los vectores (embeddings). La búsqueda de similitud vectorial la manipulación un motor especializado (típicamente hnswlib). Entonces, ¿para qué usa SQLite? Lo utiliza exclusivamente para conservar y consultar los metadatos, los IDs y los documentos asociados a eso vectores.

Principales por las que los creadores de ChromaDB eliminaron SQLite para esta zona:

- **Fracción cero** (Experiencia de desarrollo)

El objetivo principal de ChromaDB en sus inicios fue ser la base de datos vectorial más fácil de usar para los desarrolladores. Al integrar SQLite, puede usar ChromaDB simplemente haciendo un pip install cromadb en Python.

No requiere configuración: No es necesario ganar un servidor Docker, ni configurar credenciales, ni instalar dependencias pesadas como PostgreSQL o MySQL. Funciona directamente "fuera de la caja".

- **Arquitectura Embebida** (Embebido)

SQLite es una base de datos "embebida", lo que significa que se ejecute dentro del mismo proceso que tu aplicación.

Esto hace que ChromaDB sea ideal para protegido rápido, entornos locales, notebooks de Jupyter (como Google Colab) y aplicaciones de escritorio. No hay latencia de red al comunicarse con la base de datos de metadatos porque todo ocurre en la memoria o en el disco local de tu máquina.

- **Filtado eficiente de Metadatos**

En las aplicaciones de Inteligencia Artificial (como RAG - Retrieval-Aumentated Generation), casi nunca buscas solo por similitud vectorial. Normalmente quieres hacer búsquedas combinadas: "Búsqueda los vectores más similares a X, pero solo si el documento es del año 2023 y el autor es 'Juan'".

SQLite es increíblemente maduro, rápido y eficiente haciendo este tipo de filtrado estructurado (cláusulas WHERE). ChromaDB usa SQLite para pre-filtrar o post-filtrar los resultados según los metadatos antes de devolver la respuesta final.

- **Persistencia simple basada en archivos**

Cuando le indica a ChromaDB que guarda los datos en disco de forma persistente, SQLite guarda toda la información relacional y los metadatos en un único archivo estádar (.sqlite3). Esto hace que hagan copias de seguridad, migraciones o compartir la base de datos con un compañero sea tan fácil como copiar y pegar un archivo.

**En reanudación**, ChromaDB usa una arquitectura híbrida inteligente. Usa algoritmos en C++ (hnswlib) para la matemática pesada de los vectores, y usa SQLite porque es el estado de oro para guardar datos construidos localmente sin complicar la vida al desarrollador.
