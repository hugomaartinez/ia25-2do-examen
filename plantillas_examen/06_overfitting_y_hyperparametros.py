import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, train_test_split


# ---------------------------------------------------------------------------
# 1. DATOS
# ---------------------------------------------------------------------------
df = pd.read_csv("data.csv")
X = df.drop(columns=["target"])
y = df["target"]


# ---------------------------------------------------------------------------
# 2. SPLIT
# ---------------------------------------------------------------------------
X_train, X_valid, y_train, y_valid = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)


# ---------------------------------------------------------------------------
# 3. MODELO BASE
# ---------------------------------------------------------------------------
# Trampa tipica:
# - si entrenas un modelo demasiado libre, memoriza train y cae en validacion.
# - mira la diferencia entre train y validacion.
base_model = RandomForestClassifier(random_state=42)
base_model.fit(X_train, y_train)

train_pred = base_model.predict(X_train)
valid_pred = base_model.predict(X_valid)

print(f"Train accuracy: {accuracy_score(y_train, train_pred):.4f}")
print(f"Valid accuracy: {accuracy_score(y_valid, valid_pred):.4f}")


# ---------------------------------------------------------------------------
# 4. BUSQUEDA DE HIPERPARAMETROS
# ---------------------------------------------------------------------------
# Si el ejercicio pide tunear el modelo, empieza por pocos parametros.
# No metas una grid gigante si no hace falta.
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5],
}

search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1,
)
search.fit(X_train, y_train)

print("Mejores parametros:", search.best_params_)
print("Mejor score CV:", search.best_score_)


# ---------------------------------------------------------------------------
# 5. COSAS A REVISAR SI VA MAL
# ---------------------------------------------------------------------------
# - Si train es muy alto y valid muy bajo, hay overfitting.
# - Si ambos son bajos, hay underfitting o features poco utiles.
# - Si el problema es desbalanceado, accuracy puede engañar.
# - Si haces CV, recuerda que el split final de test debe quedar aparte.

