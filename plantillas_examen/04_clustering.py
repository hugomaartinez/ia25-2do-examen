import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


# ---------------------------------------------------------------------------
# 1. DATOS
# ---------------------------------------------------------------------------
# En clustering no hay target.
# Solo hay X y queremos descubrir grupos.
X = np.array(
    [
        [1, 2],
        [2, 3],
        [3, 4],
        [10, 11],
        [11, 12],
        [12, 13],
    ]
)


# ---------------------------------------------------------------------------
# 2. ESCALADO
# ---------------------------------------------------------------------------
# Trampa tipica:
# - si una variable esta en miles y otra en unidades, KMeans se sesga.
# - por eso suele ser obligatorio escalar.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# ---------------------------------------------------------------------------
# 3. ELEGIR K
# ---------------------------------------------------------------------------
inertias = []
silhouette_scores = []
ks = range(2, 8)

for k in ks:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X_scaled)
    inertias.append(model.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, labels))


# ---------------------------------------------------------------------------
# 4. AJUSTE FINAL
# ---------------------------------------------------------------------------
# El codo de la inercia y el silhouette te orientan.
# Si dos valores parecen similares, elige el mas interpretable.
final_k = 2
model = KMeans(n_clusters=final_k, random_state=42, n_init=10)
labels = model.fit_predict(X_scaled)


# ---------------------------------------------------------------------------
# 5. INSPECCION
# ---------------------------------------------------------------------------
print("Labels:", labels)
print("Silhouette:", silhouette_score(X_scaled, labels))
print("Centroides:", model.cluster_centers_)


# ---------------------------------------------------------------------------
# 6. VISUALIZACION
# ---------------------------------------------------------------------------
plt.plot(list(ks), inertias, marker="o")
plt.xlabel("k")
plt.ylabel("Inercia")
plt.title("Metodo del codo")
plt.show()


# ---------------------------------------------------------------------------
# 7. COSAS A REVISAR SI VA MAL
# ---------------------------------------------------------------------------
# - KMeans asume clusters mas o menos esfericos.
# - Si hay mucho ruido o formas raras, prueba otro metodo.
# - Si no escalas, los resultados pueden no tener sentido.
# - Si silhouette es muy bajo, el numero de clusters no esta bien elegido.

