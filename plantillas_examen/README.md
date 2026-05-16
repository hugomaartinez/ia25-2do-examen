# Plantillas de examen

Esta carpeta sirve como chuleta de trabajo rapido para ejercicios tipicos del examen.

La idea es que aqui tengas un archivo por tipo de problema, con el flujo minimo y con comentarios sobre:

- que hay que revisar antes de entrenar
- donde suelen aparecer trampas
- que partes suelen cambiar entre ejercicios

## Como usarlo

1. Abre el archivo del tipo de ejercicio que te toque.
2. Copia la estructura base.
3. Cambia solo lo que dependa del dataset o de la consigna.
4. Revisa los comentarios antes de ejecutar el modelo.

## Archivos incluidos

- `01_regresion_supervisada.py`
- `02_clasificacion_binaria.py`
- `03_clasificacion_multiclase.py`
- `04_clustering.py`
- `05_datos_faltantes.py`
- `06_overfitting_y_hyperparametros.py`
- `07_red_neuronal_mlp.py`
- `08_cnn.py`
- `09_pipeline_end_to_end.py`

## Regla general

- No reutilices un modelo sin mirar primero el tipo de variable objetivo.
- No escales antes de separar train y test.
- No ajustes imputadores, escaladores o encoders con todo el dataset.
- En redes neuronales, revisa siempre:
  - numero de clases
  - forma de entrada
  - tipo de perdida
  - si hay NaN
  - si hace falta normalizar

