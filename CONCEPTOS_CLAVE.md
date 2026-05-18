# 📚 CONCEPTOS CLAVE + FÓRMULAS - EXAMEN IA25

**Ultima actualización:** 18 Mayo 2026  
**Enfoque:** 80% UNITS 1-5 (ML Clásico) + 20% UNITS 6-10 (Deep Learning)

---

## 🎯 UNIT 1: FUNDAMENTOS

### 1️⃣ **AI, ML, DL - Diferencias**
| Concepto | Definición |
|----------|-----------|
| **AI (Inteligencia Artificial)** | Máquinas que imitan comportamiento humano |
| **ML (Machine Learning)** | Máquinas aprenden de datos (sin programación explícita) |
| **DL (Deep Learning)** | Redes neuronales con múltiples capas ocultas |

**Relación:** AI ⊃ ML ⊃ DL (DL es subconjunto de ML)

### 2️⃣ **Paradigmas de Aprendizaje**

**a) Supervised Learning (Aprendizaje Supervisado)**
- ✅ Tienes etiquetas (y, x)
- 📊 Tareas: Regresión, Clasificación
- Ejemplo: Predecir precio de casa con datos históricos

**b) Unsupervised Learning (No supervisado)**
- ❌ Sin etiquetas (solo X)
- 📊 Tareas: Clustering, Dimensionality Reduction
- Ejemplo: Agrupar clientes por comportamiento

**c) Reinforcement Learning**
- 🎮 Agente aprende por reward/penalty
- Ejemplo: Juego de ajedrez, robots

---

## 🎯 UNIT 2: ECOSYSTEM PYTHON

### 📦 **Librerías Clave**

| Librería | Uso |
|----------|-----|
| **NumPy** | Arrays, cálculos numéricos |
| **Pandas** | DataFrames, análisis datos |
| **Scikit-learn** | Modelos ML clásicos (KNN, SVM, Random Forest) |
| **Matplotlib/Seaborn** | Visualización |
| **PyTorch/TensorFlow** | Deep Learning |

---

## 🎯 UNIT 3: PARADIGMAS BÁSICOS

### 1️⃣ **KNN (K-Nearest Neighbors)**

**Concepto:** Clasifica/regresa basándose en los K vecinos más cercanos

**Fórmula de distancia Euclidiana:**
```
d(x₁, x₂) = √[(x₁₁-x₂₁)² + (x₁₂-x₂₂)² + ... + (x₁ₙ-x₂ₙ)²]
```

**Ventajas:** Simple, no paramétrico  
**Desventajas:** Lento para muchos datos, sensible a outliers

**Hiperparámetro crítico:** K (número de vecinos)
- K pequeño → Overfitting
- K grande → Underfitting

---

### 2️⃣ **K-Means (Clustering)**

**Concepto:** Agrupa datos en K clusters

**Algoritmo:**
1. Inicializar K centroides aleatoriamente
2. Asignar cada punto al centroide más cercano
3. Actualizar centroide = promedio de puntos en cluster
4. Repetir hasta convergencia

**Fórmula del centroide:**
```
μₖ = (1/Nₖ) × Σ(xᵢ) para todos xᵢ en cluster k
```

**Método del Codo (Elbow Method):**
- Graficar Inercia vs K
- Inercia = Σ distancias dentro de clusters
- Elegir K donde "codo" (cambio se hace suave)

---

### 3️⃣ **Q-Learning (Reinforcement Learning Básico)**

**Concepto:** Agente aprende qué acción tomar en cada estado para maximizar reward

**Fórmula de actualización Q:**
```
Q(s,a) = Q(s,a) + α × [r + γ × max(Q(s',a')) - Q(s,a)]
```

**Donde:**
- `Q(s,a)` = Valor de tomar acción `a` en estado `s`
- `α` = Learning rate (qué tan rápido aprende)
- `r` = Reward recibido
- `γ` (gamma) = Discount factor (importancia del futuro, típicamente 0.9-0.99)
- `max(Q(s',a'))` = Mejor recompensa futura

---

## 🎯 UNIT 4: SUPERVISED LEARNING (⭐ MÁS IMPORTANTE)

### 1️⃣ **REGRESIÓN LINEAL**

**Concepto:** Predecir valor continuo con relación lineal

**Fórmula:**
```
ŷ = β₀ + β₁×x₁ + β₂×x₂ + ... + βₙ×xₙ

Donde:
- β₀ = intercepto (cuando x=0)
- β₁, β₂, ... = coeficientes (cuánto cambia y por cada unidad de x)
```

**Interpretación de coeficientes:**
- Si β₁ = 2.5, significa: "Por cada unidad que aumenta x₁, y aumenta 2.5 unidades"

**Métrica de pérdida (MSE):**
```
MSE = (1/n) × Σ(yᵢ - ŷᵢ)²
```

**Métrica de evaluación (R²):**
```
R² = 1 - (SS_res / SS_tot)

SS_res = Σ(yᵢ - ŷᵢ)²  [errores del modelo]
SS_tot = Σ(yᵢ - ȳ)²   [errores si usáramos el promedio]

Rango: 0 a 1
- R² = 1: Predicción perfecta
- R² = 0: Modelo tan malo como usar el promedio
- R² < 0: Modelo peor que usar el promedio
```

---

### 2️⃣ **REGRESIÓN LOGÍSTICA (Clasificación Binaria)**

**Concepto:** Predecir probabilidad de clase (0 o 1)

**Fórmula:**
```
P(y=1|x) = 1 / (1 + e^-(β₀ + β₁×x))  [Función Sigmoid]

Donde:
- P(y=1|x) = Probabilidad de clase 1
- e ≈ 2.71828
```

**Gráfica Sigmoid:**
```
P(y=1)
   1.0  ___---___
   0.5 _/-       -\_
   0.0-----------
       -∞   0   +∞
```

**Regla de decisión:**
- Si P(y=1) > 0.5 → Predecir clase 1
- Si P(y=1) ≤ 0.5 → Predecir clase 0

---

### 3️⃣ **CLASIFICACIÓN MULTICLASE**

**Métodos:**

**One-vs-Rest:**
- Para 3 clases: entrenar 3 modelos binarios
- Modelo 1: Clase A vs (B+C)
- Modelo 2: Clase B vs (A+C)
- Modelo 3: Clase C vs (A+B)

**Softmax (para redes neuronales):**
```
P(y=k) = e^(zₖ) / Σ(e^(zⱼ)) para todas las clases j
```

---

### 4️⃣ **MATRIZ DE CONFUSIÓN Y MÉTRICAS** ⭐⭐⭐

**Matriz (para 2 clases):**
```
                Predicción
                Pos    Neg
Actual  Pos | TP   | FN  |
        Neg | FP   | TN  |

TP = True Positive (predicción correcta: sí es sí)
FP = False Positive (predicción incorrecta: no es sí)
FN = False Negative (predicción incorrecta: sí es no)
TN = True Negative (predicción correcta: no es no)
```

**Fórmulas (las MÁS IMPORTANTES):**

```
Accuracy = (TP + TN) / (TP + FP + FN + TN)
├─ Qué mide: % de predicciones correctas
├─ Rango: 0 a 1
└─ Problema: ❌ Mala con clases desbalanceadas

Precision = TP / (TP + FP)
├─ Qué mide: De las que predije POS, ¿cuántas eran correctas?
├─ Rango: 0 a 1
└─ Uso: Cuando FP es costoso (ej: diagnóstico falso positivo)

Recall (Sensibilidad) = TP / (TP + FN)
├─ Qué mide: De las que ERAN POS, ¿cuántas encontré?
├─ Rango: 0 a 1
└─ Uso: Cuando FN es costoso (ej: no detectar cáncer)

F1-Score = 2 × (Precision × Recall) / (Precision + Recall)
├─ Qué mide: Promedio armónico de Precision-Recall
├─ Rango: 0 a 1
└─ Uso: Balance entre Precision y Recall

Specificity = TN / (TN + FP)
├─ Qué mide: De las que ERAN NEG, ¿cuántas predije NEG?
└─ Similar a Recall pero para clase negativa
```

**Ejemplo práctico:**
```
Modelo diagnóstico cáncer: 100 pacientes, 10 con cáncer

Predicción modelo:
TP=8, FP=5, FN=2, TN=85

Accuracy = (8+85)/100 = 93% ✅ (parece bueno)
Precision = 8/(8+5) = 61% (de 13 positivos, 8 correctos)
Recall = 8/(8+2) = 80% (de 10 cánceres, encontré 8)
Specificity = 85/(85+5) = 94% (no me equivoco con sanos)
```

---

### 5️⃣ **Métricas para Regresión**

```
MAE (Mean Absolute Error) = (1/n) × Σ|yᵢ - ŷᵢ|
├─ Qué mide: Error promedio (en mismas unidades que y)
├─ Rango: 0 a ∞
└─ Ventaja: No castiga outliers tan fuerte como MSE

MSE (Mean Squared Error) = (1/n) × Σ(yᵢ - ŷᵢ)²
├─ Qué mide: Error cuadrático promedio
├─ Rango: 0 a ∞
└─ Ventaja: Diferenciable, penaliza errores grandes

RMSE (Root Mean Squared Error) = √MSE
├─ Qué mide: √(MSE), en mismas unidades que y
└─ Interpretación: Desviación típica del error

R² (Coeficiente de determinación) = 1 - (MSE_modelo / Var_y)
├─ Qué mide: % de varianza explicada
├─ Rango: 0 a 1 (a veces negativo)
└─ Interpretación: R²=0.8 → explico 80% de la varianza
```

---

### 6️⃣ **OVERFITTING vs UNDERFITTING**

```
       Error
         |
         |     _____ Test
         |    /\
         |   /  \___
Optimal  |__/        \_____ Train
         |
         +-------------------> Complejidad modelo
         
         ↑           ↑         ↑
      UNDER      ÓPTIMO      OVER
```

**Underfitting:** Modelo muy simple
- Train error ALTO
- Test error ALTO
- No captura patrones

**Overfitting:** Modelo muy complejo
- Train error BAJO ✅
- Test error ALTO ❌
- Memoriza ruido

**Soluciones:**
1. Cross-validation
2. Regularización (L1, L2)
3. Early stopping
4. Más datos
5. Simplicidad (menos features)

---

### 7️⃣ **NORMALIZACIÓN vs ESTANDARIZACIÓN**

```
Min-Max Normalization:
x_normalized = (x - min) / (max - min)
├─ Rango: [0, 1]
└─ Uso: Cuando quiero rango específico

Estandarización (Z-score):
x_std = (x - μ) / σ
├─ Rango: [-∞, +∞] típicamente [-3, 3]
├─ μ = media, σ = desviación estándar
└─ Uso: General (regresión, KNN, etc.)

Cuándo usar:
✅ KNN: OBLIGATORIO (distancias sensibles a escala)
✅ Regresión lineal: Recomendado
✅ Árboles: NO necesario (invariantes a escala)
✅ Deep Learning: OBLIGATORIO
```

---

### 8️⃣ **Manejo de Datos Faltantes**

```
Opciones:
1. Eliminar filas con NaN
   - Rápido pero pierde datos
   
2. Imputación media/mediana
   - mean(x[x != NaN])
   - Mantiene media, pierde varianza
   
3. Imputación KNN
   - Usar K vecinos más cercanos
   - Mantiene estructura local
   
4. Forward Fill / Backward Fill (series temporales)
   - Propagar último valor conocido
```

---

## 🎯 UNIT 5: UNSUPERVISED LEARNING

### 1️⃣ **Clustering K-Means**
(Ya explicado en UNIT 3)

**Inercia:** Suma de distancias dentro de clusters
```
Inercia = Σ (distancia punto a su centroide)²
```

---

### 2️⃣ **PCA (Principal Component Analysis)**

**Concepto:** Reducir dimensionalidad manteniendo máxima varianza

**Pasos:**
1. Estandarizar datos (media 0, varianza 1)
2. Calcular matriz de covarianza
3. Calcular eigenvectors y eigenvalues
4. Ordenar por eigenvalue (varianza explicada)
5. Seleccionar top K componentes

**Varianza explicada:**
```
Var_PC1 = eigenvalue₁ / Σ(todos eigenvalues)

Si PC1 = 0.7, explica el 70% de varianza
```

**Cuándo usar:**
- Visualización (reducir a 2D/3D)
- Eliminar ruido
- Acelerar modelos

**CUIDADO:** Pierde interpretabilidad (PCA son combinaciones de features)

---

## 🎯 UNIT 6: DEEP LEARNING FUNDAMENTALS

### 1️⃣ **Perceptrón Simple**

**Estructura:**
```
Input → [Suma ponderada] → [Función Activación] → Output

z = β₀ + Σ(wᵢ × xᵢ)
ŷ = f(z)  donde f es función activación
```

**Limitación:** Solo resuelve problemas linealmente separables

**Ejemplo XOR (no puede):**
```
   Input      Output
   (0,0) → 0
   (0,1) → 1
   (1,0) → 1
   (1,1) → 0
   
❌ No hay línea que separe
✅ Necesitas múltiples capas (MLP)
```

---

### 2️⃣ **MLP (Multi-Layer Perceptron)**

**Arquitectura:**
```
Input Layer → Hidden Layer 1 → Hidden Layer 2 → Output Layer
   (3)            (5)              (3)           (2)
```

**Cálculo forward:**
```
z¹ = β₀⁰ + W⁰ × X
a¹ = ReLU(z¹)

z² = β₀¹ + W¹ × a¹
a² = ReLU(z²)

z³ = β₀² + W² × a²
ŷ = Softmax(z³)
```

**Funciones de activación:**
```
ReLU(z) = max(0, z)
├─ Ventaja: Simple, evita vanishing gradient
└─ Típicamente en capas ocultas

Sigmoid(z) = 1 / (1 + e^-z)
└─ Para clasificación binaria (capa final)

Softmax(z) = e^zᵢ / Σ(e^zⱼ)
└─ Para multiclase (capa final)

Tanh(z) = (e^z - e^-z) / (e^z + e^-z)
└─ Rango [-1, 1], similar a Sigmoid
```

---

### 3️⃣ **Backpropagation**

**Concepto:** Calcular gradientes usando regla de la cadena

```
∂L/∂w = (∂L/∂a) × (∂a/∂z) × (∂z/∂w)

Esto va de atrás hacia adelante, de ahí el nombre
```

**Pasos:**
1. Forward: Calcular predicción
2. Calcular pérdida L
3. Backward: Calcular gradientes (∂L/∂w)
4. Update: w ← w - α × (∂L/∂w)

---

### 4️⃣ **Funciones de Pérdida**

```
Cross-Entropy (Clasificación):
L = -Σ(yᵢ × log(ŷᵢ))

├─ y = etiqueta verdadera (one-hot)
├─ ŷ = predicción (probabilidad)
└─ Mide diferencia entre distribuciones

MSE (Regresión):
L = (1/n) × Σ(yᵢ - ŷᵢ)²
```

---

## 🎯 UNIT 7: CONVOLUTIONAL NEURAL NETWORKS (CNN)

### 1️⃣ **Convolución**

**Concepto:** Filtro deslizante que detecta patrones locales

```
Input (28×28)
    ↓ Convolución (32 filtros 3×3)
Feature Maps (26×26×32)
    ↓ Max Pooling (2×2)
Feature Maps (13×13×32)
    ↓ Flatten
Vector (5408)
    ↓ Dense layers
Output (10)
```

**Fórmula convolución:**
```
y[i,j] = Σ Σ w[m,n] × x[i+m, j+n] + b
```

---

### 2️⃣ **Max Pooling**

**Concepto:** Reducir dimensionalidad tomando máximo en ventana

```
Original:        Max Pooling (2×2):
[1  2]           [2]
[3  4]

Reduce 4×4 → 2×2, mantiene features importantes
```

---

## 🎯 UNIT 8: TRANSFORMERS & RECURRENT NETWORKS

### 1️⃣ **RNN (Recurrent Neural Networks)**

**Concepto:** Procesar secuencias manteniendo estado

```
h_t = RNN(x_t, h_{t-1})

h_t = estado oculto al tiempo t
x_t = input al tiempo t
h_{t-1} = estado anterior
```

**Problema:** Vanishing gradient con secuencias largas

---

### 2️⃣ **LSTM (Long Short-Term Memory)**

**Mejoría:** Mantiene "cell state" a largo plazo

```
Componentes:
1. Forget gate: ¿Olvidar estado anterior?
2. Input gate: ¿Escribir nuevo valor?
3. Output gate: ¿Mostrar qué?
```

---

### 3️⃣ **Transformers & Attention**

**Mecanismo Attention:**
```
Attention(Q, K, V) = softmax(QK^T / √d_k) × V

Q = Query (qué busco)
K = Key (etiquetas)
V = Value (valores)
d_k = dimensión Keys
```

**Ventaja:** Procesa secuencias en paralelo (más rápido que LSTM)

---

## 🎯 UNIT 9: GENERATIVE AI & LLMs

### 1️⃣ **Transformers para generación de texto**

**BERT:**
- Bidireccional (lee izq y derecha)
- Usa Masked Language Modeling
- Para clasificación, parecidos semánticos

**GPT:**
- Unidireccional (solo lee pasado)
- Generación de texto
- Predicción siguiente token

---

### 2️⃣ **RAG (Retrieval Augmented Generation)**

**Concepto:** Combinar búsqueda + generación

```
1. User pregunta: "¿Cuál es la capital de Francia?"
2. Retrieval: Buscar en base de datos relevantes
   → Encuentra: "París es la capital de Francia"
3. Generation: LLM genera respuesta basada en contexto
   → "La capital de Francia es París"

Ventaja: Respuestas más precisas, con fuentes
```

---

## 🎯 UNIT 10: MLOps

### 1️⃣ **Pipeline ML**

```
Data → Preprocess → Feature Eng → Model → Evaluation → Deploy
├─────────────────────────────────────────────────────────────
                    CI/CD, Monitoring, Logging
```

### 2️⃣ **Model Evaluation en Producción**

- **Train/Test Split:** 80/20 o 70/30
- **Cross-validation:** 5-fold o 10-fold
- **A/B Testing:** Comparar modelos viejos vs nuevos

---

---

## 📊 RESUMEN RÁPIDO POR MÉTRICA

### Cuando el problema es...

**REGRESIÓN:**
- ✅ Métrica: R², RMSE, MAE
- ✅ Modelo: Linear Regression, Random Forest Regressor
- ✅ Loss: MSE

**CLASIFICACIÓN BINARIA:**
- ✅ Métricas: Accuracy, Precision, Recall, F1, ROC-AUC
- ✅ Modelo: Logistic Regression, SVM, Random Forest
- ✅ Loss: Binary Cross-Entropy

**CLASIFICACIÓN MULTICLASE:**
- ✅ Métricas: Accuracy, Precision (macro/micro), Recall (macro/micro), F1 (macro/micro)
- ✅ Modelo: Softmax Regression, Random Forest, Neural Network
- ✅ Loss: Categorical Cross-Entropy

**CLUSTERING:**
- ✅ Métricas: Silhouette Score, Davies-Bouldin Index, Inercia
- ✅ Modelo: K-Means, DBSCAN, Hierarchical
- ✅ Método: Elbow Method para elegir K

**SECUENCIAS/SERIES TEMPORALES:**
- ✅ Modelo: LSTM, GRU, Transformer
- ✅ Loss: MSE (regresión) o Cross-Entropy (clasificación)

---

## 🔥 ERRORES COMUNES EN EXAMEN

1. **Confundir Precision ↔ Recall**
   - Precision: "De los que predije POS, ¿cuántos acerté?"
   - Recall: "De los que ERAN POS, ¿cuántos encontré?"

2. **Olvidar normalizar antes de KNN**
   - KNN usa distancia → escala importa

3. **No usar Cross-Validation**
   - Evita overfitting, mide rendimiento real

4. **Elegir métrica incorrecta para problema**
   - Imbalance → F1, no Accuracy
   - Costo FN alto → Recall
   - Costo FP alto → Precision

5. **Confundir TP con Accuracy**
   - TP es un número
   - Accuracy es un porcentaje (métrica)

6. **No estandarizar features**
   - Árboles: No necesario
   - KNN, SVM, Neural Networks: OBLIGATORIO

---

## 💡 TIPS PARA EXAMEN TEÓRICO

1. **Lee completamente la pregunta**
2. **Identifica palabras clave:** "penaliza", "sensible", "garantiza"
3. **Descarta opciones absurdas primero**
4. **Si no sabes:** Busca en TEORÍA.md con Ctrl+F
5. **Gestiona tiempo:** 22 preguntas en 1.5-2 horas

---

## 📝 FÓRMULAS CRÍTICAS A MEMORIZAR

```
✅ R² = 1 - (SS_res / SS_tot)
✅ Sigmoid(z) = 1 / (1 + e^-z)
✅ Softmax(z_i) = e^z_i / Σ(e^z_j)
✅ Precision = TP / (TP + FP)
✅ Recall = TP / (TP + FN)
✅ F1 = 2 × (Precision × Recall) / (Precision + Recall)
✅ Distance Euclidiana = √[Σ(x_i - y_i)²]
✅ Centroide K-Means = (1/N_k) × Σ(x_i)
✅ Q-Learning: Q(s,a) = Q(s,a) + α[r + γ max(Q(s',a')) - Q(s,a)]
✅ Gradient Descent: w ← w - α × (∂L/∂w)
```

---

**¡Éxito en tu examen! 💪**
