import numpy as np
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from torch.utils.data import DataLoader, TensorDataset


# ---------------------------------------------------------------------------
# 1. DATOS
# ---------------------------------------------------------------------------
# Este esquema sirve para datos tabulares con target categórica.
df = ...

# Revisa:
# - si hay NaN
# - si las categoricas ya estan codificadas
# - si la target es binaria o multiclase
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
    stratify=y,
)


# ---------------------------------------------------------------------------
# 3. ESCALADO
# ---------------------------------------------------------------------------
# Las redes neuronales casi siempre necesitan variables normalizadas.
# Ojo: fit solo en train.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ---------------------------------------------------------------------------
# 4. LABEL ENCODING
# ---------------------------------------------------------------------------
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)


# ---------------------------------------------------------------------------
# 5. TENSORES
# ---------------------------------------------------------------------------
X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train_encoded, dtype=torch.long)
y_test_tensor = torch.tensor(y_test_encoded, dtype=torch.long)


# ---------------------------------------------------------------------------
# 6. DATA LOADERS
# ---------------------------------------------------------------------------
# Trampa tipica:
# - shuffle=True en train
# - shuffle=False en test
train_loader = DataLoader(
    TensorDataset(X_train_tensor, y_train_tensor),
    batch_size=32,
    shuffle=True,
)
test_loader = DataLoader(
    TensorDataset(X_test_tensor, y_test_tensor),
    batch_size=32,
    shuffle=False,
)


# ---------------------------------------------------------------------------
# 7. MODELO
# ---------------------------------------------------------------------------
class MLP(nn.Module):
    def __init__(self, input_size: int, num_classes: int) -> None:
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)


model = MLP(input_size=X_train_tensor.shape[1], num_classes=len(label_encoder.classes_))


# ---------------------------------------------------------------------------
# 8. ENTRENAMIENTO
# ---------------------------------------------------------------------------
# CrossEntropyLoss ya espera logits, asi que no pongas softmax dentro del modelo.
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(20):
    model.train()
    total_loss = 0.0

    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        logits = model(X_batch)
        loss = criterion(logits, y_batch)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    print(f"Epoch {epoch + 1}: loss={total_loss / len(train_loader):.4f}")


# ---------------------------------------------------------------------------
# 9. EVALUACION
# ---------------------------------------------------------------------------
# En multiclasificacion, usa argmax sobre los logits.
model.eval()
all_preds = []
all_targets = []

with torch.no_grad():
    for X_batch, y_batch in test_loader:
        logits = model(X_batch)
        preds = logits.argmax(dim=1)
        all_preds.extend(preds.tolist())
        all_targets.extend(y_batch.tolist())


# ---------------------------------------------------------------------------
# 10. COSAS A REVISAR SI VA MAL
# ---------------------------------------------------------------------------
# - Si el loss no baja, revisa escalado, learning rate y target encoding.
# - Si la red no aprende nada, prueba una arquitectura mas pequena.
# - Si hay desbalance, usa class weights.
# - Si hay NaN en la entrada, la red fallara antes de empezar.

