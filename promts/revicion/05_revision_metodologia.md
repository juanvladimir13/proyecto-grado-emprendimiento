# Prompt: Revisión de la Metodología (Capítulo 5)

## Cuándo usar este prompt
Al finalizar el borrador del **Capítulo 5: Metodología** (`capitulos/05_metodologia/`).

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier revisión.
2. Obtén los datos del proyecto desde `estilos/configuracion.tex` (`\tituloproyecto`, `\especialidad`).
3. Lee directamente los archivos `.tex` indicados en la sección "Archivos a revisar".
4. Lee `capitulos/02_planteamiento_problema/objetivos.tex` para verificar que la metodología cubra la validación de cada objetivo.
5. Lee `capitulos/04_desarrollo_innovacion/diseno.tex` para verificar que los instrumentos midan las variables del diseño.
6. Consulta `docs/ficha-proyecto.md` (Sección 5) para contrastar los datos metodológicos con la ficha.

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Sustituye los campos entre `[corchetes]` con los datos de tu proyecto.
3. Pega el contenido LaTeX del capítulo al final.

---

## Archivos a revisar

| Archivo | Contenido |
| :--- | :--- |
| `capitulos/05_metodologia/main.tex` | Ensamble del capítulo |
| `capitulos/05_metodologia/tipo_investigacion.tex` | Enfoque, tipo de investigación y diseño metodológico |
| `capitulos/05_metodologia/poblacion_muestra.tex` | Población objetivo y tamaño muestral de prueba |
| `capitulos/05_metodologia/tecnicas_instrumentos.tex` | Técnicas e instrumentos de recolección de datos |
| `capitulos/05_metodologia/analisis_datos.tex` | Procedimiento de procesamiento y análisis |
| **Dato cruzado:** `capitulos/02_planteamiento_problema/objetivos.tex` | Objetivos a validar metodológicamente |
| **Dato cruzado:** `capitulos/04_desarrollo_innovacion/diseno.tex` | Variables técnicas a medir |

---

## PROMPT

Actúa como un **revisor metodológico de proyectos de grado BTH** en modalidad **Innovación Tecnológica**. Evalúa el **Capítulo 5: Metodología** que te proporcionaré, verificando que el enfoque científico y las técnicas de recolección/análisis permitan validar de manera objetiva el prototipo o innovación.

### Contexto del documento
- Modalidad: Innovación Tecnológica (BTH Bolivia, RM 0912/2023)
- Especialidad técnica: [lee `\especialidad` de `estilos/configuracion.tex` o completa aquí]
- Título del proyecto: [lee `\tituloproyecto` de `estilos/configuracion.tex` o completa aquí]
- Formato: comandos LaTeX (`\section`, `\label`, `\cite`) deben preservarse.

### Qué debes evaluar
1. **Tipo y diseño de investigación**: ¿están correctamente clasificados para un proyecto tecnológico (investigación aplicada tecnológica / diseño pre-experimental o experimental)?
2. **Población y muestra**: ¿se definen con claridad los sujetos, áreas productivas o unidades de ensayo donde se aplicará la prueba piloto?
3. **Técnicas e instrumentos**: ¿los instrumentos (protocolos de prueba, hojas de verificación, encuestas) miden de manera directa las variables y métricas clave de la innovación?
4. **Procedimiento de análisis de datos**: ¿se explica claramente cómo se organizarán los datos recolectados (gráficos comparativos, promedios, tasas de error) para validar el prototipo?

### Formato de salida esperado
```
## Diagnóstico metodológico
[Enfoque, pertinencia del diseño y coherencia con la innovación]

## Matriz de alineación Técnica–Instrumento–Variable
| Variable / Parámetro a medir | Técnica aplicada | Instrumento empleado | ¿Suficiente para validar? |
|---|---|---|---|

## Evaluación de la muestra y procedimiento de análisis
[Hallazgos y recomendaciones metodológicas]

## Recomendaciones priorizadas
1. ...
```

### Contenido a analizar
[Si eres un agente con acceso al repositorio, lee directamente los archivos listados en "Archivos a revisar". Si usas este prompt manualmente, pega aquí el contenido de `capitulos/05_metodologia/`]
