import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# ---------------------------------------------------------------------------
# 1. CARGA DE DATOS
# ---------------------------------------------------------------------------
df = pd.read_csv("data.csv")

# Revisa siempre esto primero:
# - que la columna objetivo sea continua
# - que no haya valores raros en la variable target
# - que no estés metiendo la target dentro de las features
X = df.drop(columns=["target"])
y = df["target"]


# ---------------------------------------------------------------------------
# 2. SPLIT
# ---------------------------------------------------------------------------
# Importante: separar antes de ajustar escaladores o imputadores.
# Si haces fit con todo el dataset, contaminas el test.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)


# ---------------------------------------------------------------------------
# 3. PREPROCESAMIENTO + MODELO
# ---------------------------------------------------------------------------
# En regresion clasica suele bastar con imputacion + escalado.
# Si hay outliers fuertes, prueba Ridge o Lasso y revisa la distribucion.
model = Pipeline(
    steps=[
        ("scaler", StandardScaler()),
        ("regressor", LinearRegression()),
    ]
)

# Si el ejercicio pide regularizacion:
# model = Pipeline([
#     ("scaler", StandardScaler()),
#     ("regressor", Ridge(alpha=1.0)),
# ])
#
# model = Pipeline([
#     ("scaler", StandardScaler()),
#     ("regressor", Lasso(alpha=0.01)),
# ])


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
# Trampa tipica:
# - MSE penaliza mucho los errores grandes
# - MAE es mas facil de interpretar
# - R2 te dice cuanta varianza explicas
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE:  {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE:  {mae:.4f}")
print(f"R2:   {r2:.4f}")


# ---------------------------------------------------------------------------
# 7. COSAS A REVISAR SI VA MAL
# ---------------------------------------------------------------------------
# - Si R2 sale muy bajo, puede haber features poco utiles o relacion no lineal.
# - Si hay outliers extremos, prueba transformar la variable target.
# - Si el modelo es muy malo, mira si hay variables categoricas sin codificar.
# - Si hay una distribucion sesgada, usa metrics robustas y no te quedes solo con MSE.

