import torch
import torch.nn as nn
from torch.utils.data import DataLoader


# ---------------------------------------------------------------------------
# 1. DATOS
# ---------------------------------------------------------------------------
# Este template vale para imagenes tipo MNIST/CIFAR.
# Revisa:
# - forma de entrada: [batch, canales, alto, ancho]
# - numero de clases
# - si la transformacion normaliza las imagenes
train_loader = ...
test_loader = ...


# ---------------------------------------------------------------------------
# 2. MODELO
# ---------------------------------------------------------------------------
class CNN(nn.Module):
    def __init__(self, num_classes: int = 10) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(7 * 7 * 64, 128)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))

        # Ojo con esta linea:
        # el tamaño 7*7*64 solo vale si la entrada y los pooling coinciden con ese dibujo.
        x = x.view(x.size(0), -1)
        x = torch.relu(self.fc1(x))
        return self.fc2(x)


model = CNN(num_classes=10)


# ---------------------------------------------------------------------------
# 3. ENTRENAMIENTO
# ---------------------------------------------------------------------------
# En vision, la funcion de perdida tipica es CrossEntropyLoss.
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(10):
    model.train()
    epoch_loss = 0.0

    for images, labels in train_loader:
        optimizer.zero_grad()
        logits = model(images)
        loss = criterion(logits, labels)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()

    print(f"Epoch {epoch + 1}: loss={epoch_loss / len(train_loader):.4f}")


# ---------------------------------------------------------------------------
# 4. EVALUACION
# ---------------------------------------------------------------------------
# En test no uses gradientes.
model.eval()
correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        logits = model(images)
        preds = logits.argmax(dim=1)
        total += labels.size(0)
        correct += (preds == labels).sum().item()

print(f"Accuracy: {correct / total:.4f}")


# ---------------------------------------------------------------------------
# 5. COSAS A REVISAR SI VA MAL
# ---------------------------------------------------------------------------
# - Si la forma de entrada no cuadra, el flatten rompe.
# - Si la imagen es RGB, el primer canal ya no es 1 sino 3.
# - Si las imagenes no estan normalizadas, el entrenamiento puede ser inestable.
# - Si ves overfitting, añade dropout o data augmentation.

