# Tipos de Estimadores en scikit-learn

Es importante aclarar ciertos términos utilizados en scikit-learn:

- **Estimadores**: cualquier objeto que pueda estimar parámetros basándose en un conjunto de datos se llama estimador. La estimación en sí se realiza a través del método **`fit()`**.

    - **Transformadores**: estimadores que también pueden transformar datos usando el método **`transform()`**. Por ejemplo, `SimpleImputer` es un transformador: estima valores con `fit()` e imputa los valores con `transform()`.
        - Escaladores: transformadores que escalan datos.
        - Imputadores: transformadores que imputan valores faltantes.
        - Codificadores: transformadores que codifican variables categóricas.
        - Reductores de dimensionalidad: transformadores que reducen el número de variables.
        - ...

    - **Predictores**: aquellos estimadores que son capaces de hacer predicciones basándose en un conjunto de datos. Por ejemplo, el modelo de regresión lineal es un predictor: estima hiperparámetros con `fit()` y hace predicciones con **`predict()`**.
        - Clasificadores: predictores que predicen etiquetas categóricas.
        - Regressores: predictores que predicen valores continuos.
        - Agrupadores: predictores que agrupan datos en clusters.
        - ...

El término "predictor" puede ser confuso ya que también se usa, en general, para referirse a las *características* o variables independientes de un modelo, y a veces solo para aquellas variables que son efectivamente **predictivas**, excluyendo aquellas características que no tienen capacidad predictiva.

Además, el término "transformador" no debe confundirse con la popular arquitectura de red neuronal "transformer", que es la base en la cual se construyen modelos de lenguaje como GPT.

https://scikit-learn.org/stable/developers/develop.html

<!-- TODO: Explicar por separado los principios de diseño de scikit-learn en detalle con ejemplos (es una buena forma de trabajar en conceptos de ingeniería de software en Python)-->
