import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# ---------------------------------------------------------------------------
# 1. CARGA
# ---------------------------------------------------------------------------
df = pd.read_csv("data.csv")

# Revisa:
# - tipos de columnas
# - NaN
# - variables categoricas
# - target
X = df.drop(columns=["target"])
y = df["target"]


# ---------------------------------------------------------------------------
# 2. SPLIT
# ---------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y if y.nunique() > 1 else None,
)


# ---------------------------------------------------------------------------
# 3. IDENTIFICAR COLUMNAS
# ---------------------------------------------------------------------------
numeric_cols = X_train.select_dtypes(include="number").columns
categorical_cols = X_train.select_dtypes(exclude="number").columns


# ---------------------------------------------------------------------------
# 4. PREPROCESAMIENTO
# ---------------------------------------------------------------------------
# Esta es la plantilla mas reutilizable para ejercicios tabulares.
# Si hay columnas muy raras, adapta los grupos a mano.
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

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_pipeline, numeric_cols),
        ("cat", categorical_pipeline, categorical_cols),
    ]
)


# ---------------------------------------------------------------------------
# 5. MODELO
# ---------------------------------------------------------------------------
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000)),
    ]
)


# ---------------------------------------------------------------------------
# 6. ENTRENAMIENTO Y EVALUACION
# ---------------------------------------------------------------------------
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred, zero_division=0))


# ---------------------------------------------------------------------------
# 7. COSAS A REVISAR SI VA MAL
# ---------------------------------------------------------------------------
# - Si el pipeline falla, suele ser por columnas categoricas no detectadas.
# - Si el problema es de regresion, cambia el modelo y las metricas.
# - Si es deep learning, esta estructura sirve solo como preprocesado previo.
# - No metas el test dentro del fit del preprocessor.

