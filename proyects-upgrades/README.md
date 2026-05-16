# Proyects Upgrades

Carpeta con mejoras probables de examen para los proyectos de `proyects/`.

La idea no es modificar los proyectos originales, sino tener recetas listas para adaptar si el profesor pide "mejora esto", "evita este problema" o "haz que funcione sin internet".

## Orden recomendado

1. `00_preparar_examen_sin_internet.ipynb`
2. Notebook del proyecto que caiga
3. Copiar/adaptar solo la mejora que encaje con el enunciado

## Notebooks

- `00_preparar_examen_sin_internet.ipynb`: descarga/cachea datasets y modelos antes de que corten internet.
- `01_california_e2e_mejoras.ipynb`: pipeline avanzado para California Housing con ratios, logs, clustering geográfico y búsqueda de hiperparámetros.
- `02_king_county_mejoras.ipynb`: split temporal, feature engineering y evaluación para King County.
- `03_thyroid_mejoras.ipynb`: clasificación médica con F2, desbalance y datos faltantes.
- `04_ai_chat_guardrails_mejoras.ipynb`: mejoras de tests, configuración, base_url de Ollama e historial.
- `05_ies_triage_mejoras.ipynb`: procesado robusto de múltiples JSON y mejoras offline para el agente de correos.
- `06_computer_vision_mejoras_offline.ipynb`: mejoras seguras de OpenCV y comprobación de modelos locales.

## Kaggle y examen sin internet

Si un proyecto usa Kaggle, lo mejor es ejecutar la descarga antes de que corten internet y copiar el CSV a esta carpeta.

No dependas solo de `kagglehub.dataset_download()` durante el examen. Puede funcionar si la cache existe, pero es menos visible. Mejor tener rutas locales como:

- `proyects-upgrades/datasets/king-county/kc_house_data.csv`
- `proyects-upgrades/datasets/thyroid/thyroidDF.csv`

Luego en el examen puedes hacer directamente:

```python
pd.read_csv("proyects-upgrades/datasets/king-county/kc_house_data.csv")
```

o:

```python
pd.read_csv("proyects-upgrades/datasets/thyroid/thyroidDF.csv")
```

