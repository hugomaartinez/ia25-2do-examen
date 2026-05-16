# Directrices para la Carpeta PIA-SAA

## Reglas Generales de Chat

- **PROTOCOLO DE REFLEXIÓN:** Si alguna vez señalo un error, bug u omisión que cometiste, tu respuesta DEBE comenzar con una sección `### Por Qué Pasó Esto`. DEBES explicar de manera rigurosa la limitación interna, lapso de atención o error lógico que te llevó a cometer ese error específico. No simplemente te disculpes o corrijas el problema ciegamente sin este análisis.
- **Mejora Continua:** Sugiere constantemente mejoras a estas propias instrucciones para hacerlas mejores.
- **Autocrítica:** Sé siempre crítico con tus propias respuestas y señala posibles limitaciones o errores.
- **Crítica de Instrucciones:** Sé también crítico con mis instrucciones. No dudes en señalar posibles errores o mejoras.
- **Rigor Supremo:** El rigor es primordial. Es importante que todas las explicaciones sean técnicamente correctas.

## Directrices para Jupyter Notebooks

- Es importante proceder paso a paso, utilizando cada celda para mostrar su propia salida y usando celdas markdown para explicar los pasos.
- Los encabezados deben estar solos en sus propias celdas (Markdown) para que puedan plegarse/desplegarse fácilmente.
- No numeres los encabezados, para que puedan reordenarse fácilmente.
- Las importaciones deben hacerse en la primera celda que las requiera, no en una celda separada en la parte superior. De esa manera, si un notebook se divide en diferentes partes, cada parte tendrá sus propias importaciones. También ayuda a entender las dependencias.
- Las explicaciones deben estar en celdas markdown, nunca en prints o comentarios en celdas python.
- Los comentarios en celdas de código deben usarse para explicar líneas o bloques de código específicos, no para explicaciones generales.
- Se deben usar celdas pequeñas para proceder paso a paso. Evita celdas grandes con salidas largas. En particular, evita varias figuras como salida de la misma celda.

## Directrices de Python

- Usa en general las prácticas más modernas para código Python (el proyecto requiere Python ≥3.13).
- Type hints: Usa sintaxis moderna para Python 3.13+
- Usa `str | None` (no `Optional[str]`).
- Genéricos integrados: list[str], dict[str, int], tuple[int, ...] (no List, Dict, Tuple)
- Colecciones: collections.abc.Callable, collections.abc.Iterator (no typing.Callable, typing.Iterator)
- Entorno: usa `uv` para entornos virtuales y gestión de dependencias (usando `uv sync` para mantener el entorno actualizado).
- Trata las advertencias como errores tanto como sea posible.
- Formato: YAPF (configuración en pyproject.toml, límite de 120 caracteres)
- Importaciones: Solo explícitas, no uses archivos “**init**.py”
- El código debe ser autodocumentado tanto como sea posible, con nombres de variables verbosos. Usa docstrings solo cuando sea necesario.
- Usa comentarios para explicar solo las partes más complejas del código.
- Sin registro: Sin declaraciones de logger


## Descripción General

Este repositorio contiene **notas y proyectos** diseñados para cursos de **programación en Inteligencia Artificial (IA) y Machine Learning (ML)**. El objetivo es proporcionar a los estudiantes materiales rigurosos, educativos y desafiantes que enfaticen la claridad y la corrección. Se aprecia un enfoque pedagógico, pero no debe comprometer la precisión de la información.
Aunque habrá algunas referencias y notas particulares sobre terminología en español, todos los materiales deben escribirse en **inglés claro y correcto**.

## Directrices de Notas

Las notas están diseñadas para servir como **material de referencia didáctico** para los estudiantes. Deben ser:

- **Detalladas y rigurosas**: Cada explicación debe ser precisa y técnicamente correcta.
- **Basadas en ejemplos**: Incluye ejemplos prácticos e ilustrativos (código, diagramas, conjuntos de datos) siempre que sea posible. La herramienta principal será Jupyter notebooks con explicaciones incrustadas y código python.
- **Paso a paso**: Desglosé conceptos complejos en partes manejables.
- **Enfocadas**: Presenta solo el contenido en sí. Evita introducciones (“esta nota explica…”) o resúmenes al final.

## Estándares de Desarrollo y Codificación

- Las soluciones utilizarán notebooks, scripts python o proyectos simples (en sus propias carpetas).
- Los Jupyter Notebooks son preferidos para notas y proyectos más simples, para que las explicaciones sean más interactivas, mientras que los proyectos python son mejores para implementaciones más complejas.
- Si un archivo markdown incluye fragmentos de código, probablemente sea preferible un notebook.
- El código debe estar bien documentado, con comentarios claros que expliquen el propósito y la funcionalidad de cada sección.
- Se utilizará `uv` para entornos virtuales y gestión de dependencias (usando `uv sync` para mantener el entorno actualizado).
- El curso será en línea, por lo que todos los materiales deben ser autosuficientes y fáciles de seguir sin orientación en persona.

### Directrices de Proyectos

Cada proyecto debe diseñarse como una **unidad de aprendizaje** que incluya:

1. **Definición**:

   - Una clara declaración del problema. Como esta es la única parte que el estudiante verá, debe ser autosuficiente. Normalmente será un único archivo markdown: README.md.
   - Requisitos y restricciones específicos.
   - Entregables esperados (código, informe, presentación).
   - No incluyas requisitos técnicos o bibliotecas aquí; el estudiante debe decidir eso.
   - Todo el trabajo se realizará en repositorios de GitHub.
   - Todos los proyectos deben requerir un archivo README detallado con:
     - Explicación personal detallada del código, decisiones de diseño, desafíos, etc.

2. **Análisis** e **Implementación de la Solución**:

   - Antecedentes y contexto teórico.
   - Desafíos esperados y pasos de razonamiento que los estudiantes deben seguir.
   - Un esquema de solución detallado o una implementación de referencia.
   - Explicaciones para cada paso de la solución, no solo el código final.

3. **Lista de Verificación de Evaluación**:

   - Un conjunto de criterios para evaluar el trabajo del estudiante.
   - Debe cubrir corrección, robustez, calidad del código y claridad del razonamiento.
   - La puntuación máxima debe ser de 10 puntos, con un desglose de pesos para diferentes aspectos.
   - Deben ser listas de verificación simples y fáciles de seguir, no rúbricas complejas.
   - Como los proyectos son abiertos, la evaluación se enfocará en la calidad de la comprensión e implementación, no solo en los resultados finales. La evaluación cualitativa del profesor es aceptable.

4. **Propuestas para Verificación de Examen**:

   - El examen final requerirá que los estudiantes demuestren su comprensión y autoría de los proyectos desarrollados durante el curso. Cada proyecto debe incluir propuestas para tal verificación.
   - Los proyectos se pueden resolver con la ayuda de herramientas de IA, pero en el examen los estudiantes no tendrán acceso a Internet, solo a todo lo que traigan descargado antes.
   - Teniendo esto en cuenta, el examen consistirá en:
     - Explicaciones sobre los proyectos
     - Pequeñas modificaciones o extensiones, que no requieran codificación nueva desde cero sino adaptar o extender código existente.
     - Preguntas de prueba

5. **Rúbrica de Calificación de Examen**:
   - Para la calificación del examen, debe haber una rúbrica con un máximo de 10 puntos, con un desglose de pesos para diferentes aspectos. Esta rúbrica debe ser muy clara y no estar abierta a interpretación.

#### Principios Fundamentales

- **Problemas Paradigmáticos**: Los proyectos deben abordar problemas representativos de aplicaciones de IA/ML en el mundo real. Deben:

  - Involucrar múltiples pasos o componentes (procesamiento de datos, entrenamiento de modelos, evaluación).
  - Requerir pensamiento crítico y resolución de problemas, no solo aplicación mecánica de algoritmos.

- **Complejidad y Profundidad**: Los proyectos deben:

  - Ir más allá de ejercicios introductorios simples.
  - Fomentar la exploración de preguntas abiertas, pipelines multietapa o conjuntos de datos del mundo real.

- **Resultados de Aprendizaje**: Los proyectos deben conectar **teoría y práctica**, asegurando que los estudiantes:
  - Entiendan los conceptos subyacentes.
  - Puedan implementar, probar y analizar críticamente las soluciones.

### Directrices de Conjunto de Datos y Definición de Problema

Los conjuntos de datos y las declaraciones de problemas deben diseñarse para **desafiar suposiciones** y fomentar soluciones robustas. Para lograr esto:

- **Introduce Variaciones y Ruido**:

  - Renombra o mezcla columnas.
  - Agrega características irrelevantes.
  - Inyecta ruido en los datos.
  - Invierte o redefine variables de destino (con documentación clara).
  - Incluye valores faltantes o inconsistentes.
  - Mezcla formatos de datos.

- **Propósito**:  
  Estas “imperfecciones” controladas son intencionales. Entrenan a los estudiantes para:
  - Analizar datos cuidadosamente.
  - Cuestionar suposiciones.
  - Desarrollar soluciones resilientes y generalizables.
