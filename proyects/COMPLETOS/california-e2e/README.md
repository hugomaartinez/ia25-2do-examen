# Precios de Viviendas en California
## Proyecto de Machine Learning de Extremo a Extremo

Este notebook es una adaptación del [original de *Aurélien Gerón*](https://github.com/ageron/handson-ml3/blob/main/02_end_to_end_machine_learning_project.ipynb), del [segundo capítulo](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/ch02.html) de su libro: [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, 3rd Edition. Aurélien Géron](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)

Este proyecto demuestra un flujo de trabajo completo de machine learning utilizando el conjunto de datos California Housing Prices. El objetivo es predecir los precios de las viviendas basándose en diversas características como la ubicación, número de habitaciones y población.

Es un conjunto de datos clásico para tareas de regresión y es ampliamente utilizado con fines educativos en machine learning. El proyecto está estructurado para guiarte a través de todo el proceso, desde la carga y exploración de datos hasta el entrenamiento y evaluación del modelo; y es un ejemplo paradigmático de un problema de **regresión con aprendizaje supervisado**.



## Notebooks

1. [**Encuadramiento del Problema**](e2e010_framing.ipynb) — Definición del problema, primer vistazo a los datos y métricas de rendimiento
2. [**Análisis Exploratorio de Datos (EDA)**](e2e020_eda.ipynb) — Visualización de datos, correlaciones y análisis de valores atípicos
3. [**División Entrenamiento/Prueba**](e2e025_train_test.ipynb) — Estrategias de muestreo aleatorio y estratificado
4. [**Ingeniería de Características**](e2e030_feature_engineering.ipynb) — Creación de nuevas características a partir de las existentes

### Preprocesamiento
5. [**Valores Faltantes**](e2e041_missing.ipynb) — Manejo de datos no disponibles con estrategias de imputación
6. [**Variables Categóricas**](e2e042_categorical.ipynb) — Codificación ordinal y one-hot
7. [**Escalado de Características**](e2e043_scaling.ipynb) — Normalización, estandarización y distribuciones de cola pesada

### Pipelines y Transformadores
8. [**Pipelines**](e2e050_pipelines.ipynb) — Construcción de pipelines de preprocesamiento con scikit-learn
9. [**Transformadores Personalizados**](e2e051_custom_transformers.ipynb) — Creación de transformadores personalizados para pipelines
10. [**Clustering Espacial**](e2e060_spatial_clustering.ipynb) — Manejo de coordenadas geográficas con K-means y kernels RBF

### Entrenamiento y Evaluación del Modelo
11. [**Evaluación del Modelo**](e2e070_model_evaluation.ipynb) — Entrenamiento de modelos, validación cruzada y comparación de rendimiento
12. [**Optimización de Hiperparámetros**](e2e080_hyperparameters.ipynb) — Búsqueda en malla y búsqueda aleatoria
13. [**Ajuste de Hiperparámetros (Práctica)**](e2e081_hyperparameters2.ipynb) — Ejercicio práctico de ajuste de hiperparámetros
14. [**Redes Neuronales**](e2e090_neural_network/e2e090_neural_network.ipynb) — Regresión con PyTorch
