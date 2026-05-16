import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# ---------------------------------------------------------------------------
# 1. CARGA
# ---------------------------------------------------------------------------
df = pd.read_csv("data.csv")

# Mira primero esto:
# - que columnas tienen NaN
# - si los NaN son aleatorios o tienen significado
# - si hay columnas que se pueden eliminar por demasiado vacio
print(df.isnull().sum())

X = df.drop(columns=["target"])
y = df["target"]


# ---------------------------------------------------------------------------
# 2. SPLIT
# ---------------------------------------------------------------------------
# Siempre separa antes de imputar.
# Si imputas con todo el dataset, el test deja de ser realmente test.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y if y.nunique() > 1 else None,
)


# ---------------------------------------------------------------------------
# 3. PREPROCESAMIENTO
# ---------------------------------------------------------------------------
# Ajusta el tipo de imputacion segun la columna:
# - numericas: mediana suele ser una buena base
# - categoricas: moda
# - si hay muchos vacios, a veces conviene crear una bandera de "faltante"
numeric_cols = X_train.select_dtypes(include="number").columns
categorical_cols = X_train.select_dtypes(exclude="number").columns

numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ]
)


# ---------------------------------------------------------------------------
# 4. EJEMPLO DE USO
# ---------------------------------------------------------------------------
# En un examen normalmente lo montarias con ColumnTransformer.
# Aqui queda la idea principal:
# - imputar
# - codificar
# - escalar
# - entrenar sin NaN


# ---------------------------------------------------------------------------
# 5. COSAS A REVISAR SI VA MAL
# ---------------------------------------------------------------------------
# - Si una columna tiene casi todos NaN, puede ser mejor descartarla.
# - Si el missingness es informativo, una bandera puede mejorar mucho.
# - No uses la misma estrategia para todas las columnas sin pensar.
# - No olvides que el modelo final no debe recibir NaN si no lo soporta.

