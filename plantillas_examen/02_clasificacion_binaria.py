import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# ---------------------------------------------------------------------------
# 1. CARGA DE DATOS
# ---------------------------------------------------------------------------
df = pd.read_csv("data.csv")

# Revisa bien que la target sea binaria:
# - 0/1
# - false/true
# - no/si
# Si viene como texto, conviertela antes de entrenar.
X = df.drop(columns=["target"])
y = df["target"]


# ---------------------------------------------------------------------------
# 2. SPLIT
# ---------------------------------------------------------------------------
# Usa stratify si hay desbalance de clases.
# Asi mantienes proporciones parecidas en train y test.
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
# LogisticRegression suele ser la opcion base.
# Si hay desbalance fuerte, revisa class_weight="balanced".
model = Pipeline(
    steps=[
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=1000)),
    ]
)


# ---------------------------------------------------------------------------
# 4. ENTRENAMIENTO
# ---------------------------------------------------------------------------
model.fit(X_train, y_train)


# ---------------------------------------------------------------------------
# 5. PREDICCION
# ---------------------------------------------------------------------------
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]


# ---------------------------------------------------------------------------
# 6. EVALUACION
# ---------------------------------------------------------------------------
# Trampa tipica:
# - accuracy sola puede engañar si la clase positiva es rara
# - si el problema es medico o critico, mira recall
# - si quieres evitar falsas alarmas, mira precision
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print(cm)
print(f"TN={tn}, FP={fp}, FN={fn}, TP={tp}")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1:        {f1:.4f}")
print(classification_report(y_test, y_pred, zero_division=0))


# ---------------------------------------------------------------------------
# 7. COSAS A REVISAR SI VA MAL
# ---------------------------------------------------------------------------
# - Si la precision es alta pero el recall bajo, el modelo se esta pasando de conservador.
# - Si el recall es alto pero la precision baja, hay muchas falsas alarmas.
# - Si hay desbalance, prueba class_weight o cambia la metrica principal.
# - Si hay categorias, codificalas con one-hot antes de escalar.

