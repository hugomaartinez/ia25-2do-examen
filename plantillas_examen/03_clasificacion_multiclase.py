import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


# ---------------------------------------------------------------------------
# 1. CARGA DE DATOS
# ---------------------------------------------------------------------------
df = pd.read_csv("data.csv")

# Revisa:
# - cuantas clases hay
# - si las etiquetas estan bien distribuidas
# - si la target ya viene codificada o en texto
X = df.drop(columns=["target"])
y = df["target"]


# ---------------------------------------------------------------------------
# 2. SPLIT
# ---------------------------------------------------------------------------
# En multiclase casi siempre conviene stratify.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)


# ---------------------------------------------------------------------------
# 3. MODELO
# ---------------------------------------------------------------------------
# RandomForest es una base muy solida para multiclase tabular.
# Ojo con:
# - variables categoricas sin codificar
# - NaN si la libreria no los soporta en ese caso concreto
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
)


# ---------------------------------------------------------------------------
# 4. ENTRENAMIENTO
# ---------------------------------------------------------------------------
model.fit(X_train, y_train)


# ---------------------------------------------------------------------------
# 5. PREDICCION
# ---------------------------------------------------------------------------
y_pred = model.predict(X_test)


# ---------------------------------------------------------------------------
# 6. EVALUACION
# ---------------------------------------------------------------------------
# En multiclase, no te limites a accuracy.
# Mira la matriz de confusion y el classification_report.
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, zero_division=0))


# ---------------------------------------------------------------------------
# 7. COSAS A REVISAR SI VA MAL
# ---------------------------------------------------------------------------
# - Si una clase sale siempre mal, puede haber desbalance.
# - Si hay muchas features numericas con escalas distintas, prueba un pipeline.
# - Si el modelo sobreajusta, limita max_depth o aumenta min_samples_leaf.
# - Si el dataset tiene pocas muestras por clase, no abuses de modelos demasiado complejos.

