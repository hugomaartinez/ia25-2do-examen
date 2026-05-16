# Módulo de Visión por Computadora

Un módulo práctico que cubre visión por computadora desde los fundamentos de imágenes hasta la autenticación facial, construido con OpenCV, YOLO, CLIP y ChromaDB.

El módulo está organizado en tres áreas. Cada área puede estudiarse independientemente, aunque la progresión de una a la siguiente es intencional.

## OpenCV: Imágenes y Video

- [opencv/opencv_fundamentals.ipynb](opencv/opencv_fundamentals.ipynb): carga y manipulación de imágenes; BGR vs RGB, `uint8`, redimensionamiento, rotación, recorte, dibujo y guardado.
- [opencv/opencv_image_processing.ipynb](opencv/opencv_image_processing.ipynb): procesamiento de imágenes clásico; filtrado, convolución, detección de bordes, umbralización, morfología, contornos y CLAHE.
- [opencv/opencv_video.ipynb](opencv/opencv_video.ipynb): procesamiento de video desde archivos y webcams; bucles de fotogramas, códecs, sustracción de fondo y flujo óptico.

## YOLO: Detección de Objetos

- [yolo/object_detection_and_yolo.ipynb](yolo/object_detection_and_yolo.ipynb): conceptos de detección e inferencia; cuadros delimitadores, IoU, NMS, métricas, inferencia preentrenada, segmentación, comparación de velocidad y exportación.
- [yolo/yolo_custom_training.ipynb](yolo/yolo_custom_training.ipynb): ajuste fino de YOLO; formato de anotación, validación de conjuntos de datos, configuración de entrenamiento, gráficos, transferencia de aprendizaje y olvido catastrófico.

## Embeddings, Bases de Datos y Reconocimiento

- [vectors_and_embeddings.ipynb](vectors_and_embeddings.ipynb): embeddings de imágenes; aritmética de vectores, distancia coseno vs euclidiana, CLIP, PCA y enlaces a NLP y RAG.
- [chromadb_intro.ipynb](chromadb_intro.ipynb): bases de datos vectoriales; búsqueda HNSW, distancia coseno, filtrado de metadatos y clientes efímeros vs persistentes.
- [face_recognition_pipeline.ipynb](face_recognition_pipeline.ipynb): verificación facial de extremo a extremo; captura, detección, embedding, almacenamiento, verificación, flujo de trabajo de webcam y mapa de calor de similitud.

## Proyecto Sugerido: Autenticación Facial con Webcam

Los notebooks anteriores proporcionan todas las piezas necesarias para construir un pequeño sistema de autenticación facial — del tipo utilizado para verificación de asistencia o acceso a salas.

**Objetivo**: inscribir a un conjunto de personas capturando su rostro desde una webcam, luego verificar su identidad en tiempo real.

**Pasos sugeridos**:

1. Utiliza el patrón de webcam en [face_recognition_pipeline.ipynb](face_recognition_pipeline.ipynb) para capturar varios fotogramas por persona en la inscripción.
2. Para cada fotograma, detecta y recorta el rostro utilizando el pipeline de YOLO mostrado en el mismo notebook.
3. Incrusta cada recorte con CLIP y almacena en una [colección persistente de ChromaDB](chromadb_intro.ipynb).
4. En la verificación, captura un nuevo fotograma, incrústalo y consulta la base de datos. Aplica el umbral de similitud de 0.85 como punto de partida — ajusta según tu hardware e iluminación.
5. Agrega una verificación de calidad (detección de desenfoque, límites de brillo) antes de incrustar para evitar almacenar capturas deficientes; la sección de webcam en [face_recognition_pipeline.ipynb](face_recognition_pipeline.ipynb) muestra este patrón.

**Extensiones a considerar**:

- Utiliza `yolov8n-face.pt` en lugar del modelo general para recortes de rostro más ajustados.
- Inscribe múltiples fotogramas por persona y compara la consulta contra todos ellos (votación suave).
- Almacena datos de inscripción con marcas de tiempo; marca los embeddings más antiguos que N días como obsoletos.
- Agrega un paso de registro para intentos rechazados.

La brecha entre este prototipo basado en notebooks y un despliegue real es principalmente ingeniería de confiabilidad, no complejidad algorítmica, lo que lo convierte en un alcance de proyecto útil para el aprendizaje.

## Estructura del Repositorio

```text
.
├── opencv/
│   ├── opencv_fundamentals.ipynb
│   ├── opencv_image_processing.ipynb
│   └── opencv_video.ipynb
├── yolo/
│   ├── object_detection_and_yolo.ipynb
│   └── yolo_custom_training.ipynb
├── vectors_and_embeddings.ipynb
├── chromadb_intro.ipynb
├── face_recognition_pipeline.ipynb
├── resources/
│   ├── images/           # imágenes estáticas usadas por los notebooks
│   │   ├── lenna.png
│   │   ├── baboon.png
│   │   ├── peppers.jpg
│   │   ├── bus.jpg
│   │   ├── scene1.jpg
│   │   ├── scene2.jpg
│   │   └── scene3.jpg
│   └── models/           # ignorado por git; pesos descargados de YOLO
└── artifacts/
    ├── outputs/          # ignorado por git; imágenes generadas, videos y ejecuciones de YOLO
    └── face_db/          # ignorado por git; datos de demostración persistentes de ChromaDB
```

## Entorno

Python ≥ 3.13, gestionado con [uv](https://docs.astral.sh/uv/).

```bash
uv sync          # instala todas las dependencias de pyproject.toml
```

Dependencias clave: `ultralytics`, `opencv-python`, `sentence-transformers`, `chromadb`, `scikit-learn`, `matplotlib`.
