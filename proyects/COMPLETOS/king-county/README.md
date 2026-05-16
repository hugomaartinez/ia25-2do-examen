# Ventas de Casas en King County - Proyecto de Regresión de Extremo a Extremo

Este repositorio contiene un proyecto completo de Machine Learning de extremo a extremo para predecir los precios de las casas en King County, USA. Trabajar con datos del mundo real a menudo requiere manejar la suciedad de los datos, posibles filtraciones de datos y estrategias de validación cuidadosas. Este proyecto demuestra estos desafíos y sus soluciones.

## Descripción General del Proyecto

**Objetivo:** Predecir el precio de una casa basándose en características como metros cuadrados, número de dormitorios, ubicación, etc.
**Tipo:** Regresión.
**Aprendizajes Clave:**
- Limpieza de datos del mundo real (manejo de duplicados).
- Prevención de **Filtraciones de Datos Temporales** en conjuntos de datos dependientes del tiempo.
- Ingeniería de Características y pipelines de Preprocesamiento.
- Selección de modelo y evaluación rigurosa utilizando divisiones Entrenamiento/Validación/Prueba.

## Conjunto de Datos

El conjunto de datos es el famoso conjunto de datos **King County House Sales**.
- **Fuente:** Kaggle (descargado automáticamente en el notebook).
- **Tamaño:** ~21k observaciones.
- **Características:** 21 variables (Fecha, Dormitorios, Baños, Metros cuadrados, Pisos, Frente de agua, Vista, Condición, Grado, Año Construido, etc.).

## Flujo de Trabajo del Proyecto

El proyecto está estructurado en notebooks secuenciales, cada uno enfocándose en una etapa crítica del pipeline de ML:

| Notebook | Descripción | Conceptos Clave |
|----------|-------------|--------------|
| `01-eda.ipynb` | **Análisis Exploratorio de Datos**. Primer vistazo a la estructura de datos, distribuciones y posibles problemas. | EDA, Carga de Datos, Visualización. |
| `02-repeated_ids.ipynb` | **Limpieza de Datos**. Manejo de entradas duplicadas para la misma casa vendida múltiples veces. | Limpieza de Datos, Duplicados, Consistencia. |
| `03-temporal_leakage.ipynb` | **Estrategia de División**. Por qué la división aleatoria es peligrosa para datos similares a series temporales. Análisis de tendencias de precios a lo largo del tiempo. | **División Temporal**, Fuga de Datos, División Entrenamiento/Prueba. |
| `04a-preprocessing-step-by-step.ipynb` | **Ingeniería de Características (Paso a Paso)**. Recorrido detallado de cada paso de preprocesamiento con fines educativos. | Ingeniería de Características Manual, Prevención de Fuga de Datos, Paradigma Fit/Transform. |
| `04b-preprocessing-pipeline.ipynb` | **Ingeniería de Características (Producción)**. Pipeline completo de sklearn para inferencia de extremo a extremo. | `sklearn.pipeline`, Transformadores Personalizados, Implementación en Producción. |
| `05-modeling.ipynb` | **Modelado y Evaluación**. Selección de algoritmos (Ridge, Lasso, RandomForest, GradientBoosting, XGBoost), ajuste de hiperparámetros multi-candidatos y evaluación final. | Línea Base, Modelos Lineales, Ensambles, XGBoost, GridSearchCV, TimeSeriesSplit, Ajuste Multi-modelo. |
| `06-deep-learning.ipynb` | **Aprendizaje Profundo**. Construcción y entrenamiento de una red neuronal con PyTorch y comparación contra el mejor modelo del notebook 05. | PyTorch, Escalado de Objetivo, Normalización por Lote, Dropout, Parada Temprana, Modo Entrenamiento/Evaluación. |


## Requisitos

El proyecto utiliza bibliotecas estándar de ciencia de datos de Python:
- `numpy`, `pandas`
- `matplotlib`, `seaborn`
- `scikit-learn`
- `xgboost` (para notebook 05)
- `torch` (para notebook 06)
- `kagglehub` (para descarga de datos)

Asegúrate de tener estos instalados en tu entorno (se recomienda usar `uv` de acuerdo con las directrices del curso).
