# Plantillas de examen

Esta carpeta sirve como chuleta rapida para llevar al examen.

No esta pensada como material de estudio largo, sino como una referencia para:

- identificar rapido el tipo de ejercicio
- abrir la plantilla adecuada
- revisar las trampas tipicas antes de ejecutar

## Como usarlo

1. Abre el archivo del tipo de ejercicio que te toque.
2. Lee la primera celda para confirmar que es el tipo de problema correcto.
3. Ejecuta o adapta las celdas por orden.
4. Cambia solo lo que dependa del dataset o de la consigna.
5. Revisa la seccion "Si falla" antes de perder tiempo tocando cosas al azar.

## Orden recomendado

1. `00_indice_rapido.ipynb`
2. la plantilla del tipo de ejercicio
3. revisar las trampas que aparecen al final de cada notebook

## Archivos incluidos

- `00_indice_rapido.ipynb`
- `01_regresion_supervisada.ipynb`
- `02_clasificacion_binaria.ipynb`
- `03_clasificacion_multiclase.ipynb`
- `04_clustering.ipynb`
- `05_datos_faltantes.ipynb`
- `06_overfitting_y_hyperparametros.ipynb`
- `07_red_neuronal_mlp.ipynb`
- `08_cnn.ipynb`
- `09_pipeline_end_to_end.ipynb`
- `10_mapa_proyectos_y_mejoras_examen.ipynb`

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

## Consejo de examen

Si no sabes por donde empezar, abre `00_indice_rapido.ipynb`, ejecuta el mini diagnostico del dataframe y decide la plantilla por el tipo de `target`.

Si el ejercicio se basa en alguno de los proyectos del repositorio, abre `10_mapa_proyectos_y_mejoras_examen.ipynb` para ver que proyectos son viables sin internet y que mejoras son mas probables.
