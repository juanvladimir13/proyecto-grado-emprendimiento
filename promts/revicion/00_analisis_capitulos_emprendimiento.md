# Prompt: Análisis de Coherencia, Rigor Técnico y Sincronía en Emprendimiento Productivo

## Cuándo usar este prompt
Como primer paso de una revisión integral, cuando se dispone de al menos 3 o más capítulos redactados y se desea un diagnóstico panorámico antes de las revisiones puntuales por capítulo.

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier revisión.
2. Obtén los datos del proyecto desde `estilos/configuracion.tex` (`\tituloproyecto`, `\especialidad`, `\modalidad`).
3. Lee los archivos `.tex` de todos los capítulos ensamblados desde `capitulos/index.tex`.
4. Lee `bibliografia/referencias.bib` para verificar correspondencia de citas.
5. Consulta `docs/ficha-proyecto.md` para contrastar los datos de la ficha con lo redactado.

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Sustituye los campos entre `[corchetes]` con los datos de tu proyecto.
3. Pega el contenido LaTeX de los capítulos a analizar al final.

---

## Archivos a revisar

| Capítulo | Archivo de ensamble | Secciones |
| :--- | :--- | :--- |
| Cap. 1 | `capitulos/01_introduccion/main.tex` | `contexto_general.tex`, `oportunidad_negocio.tex`, `propuesta_valor.tex`, `marco_teorico.tex` |
| Cap. 2 | `capitulos/02_planteamiento_emprendimiento/main.tex` | `diagnostico.tex`, `objetivos.tex`, `justificacion.tex` |
| Cap. 3 | `capitulos/03_desarrollo_emprendimiento/main.tex` | `localizacion.tex`, `analisis_mercado.tex`, `estrategia_promocion.tex`, `estructura_organizacional.tex`, `diseno_producto.tex`, `ciclo_produccion.tex` |
| Cap. 4 | `capitulos/04_viabilidad_sostenibilidad/main.tex` | `calculo_inversiones.tex`, `costo_produccion.tex` |
| Cap. 5 | `capitulos/05_resultados/main.tex` | `resultados_cuantitativos.tex`, `resultados_cualitativos.tex`, `indicadores_validados.tex` |
| Cap. 6 | `capitulos/06_proyecto_vida/main.tex` | *(contenido directo en main.tex)* |
| Cap. 7 | `capitulos/07_conclusiones_recomendaciones/main.tex` | `conclusiones.tex`, `recomendaciones.tex` |
| Bibliografía | `bibliografia/referencias.bib` | Base de datos BibLaTeX |

---

## PROMPT

Actúa como un **revisor académico y de proyectos de inversión productiva** especializado en trabajos de grado de la modalidad **Emprendimiento Productivo** bajo la normativa del Bachillerato Técnico Humanístico (BTH, RM 0912/2023, Anexo 1, inciso A). Tu tarea es analizar los capítulos que te proporcionaré a continuación para garantizar **coherencia comercial**, **rigor financiero-operativo** y **sincronía perfecta** entre todas sus partes.

### Contexto del documento
- Modalidad: Proyecto de Grado — Emprendimiento Productivo (BTH Bolivia)
- Especialidad técnica: [lee `\especialidad` de `estilos/configuracion.tex` o completa aquí]
- Título del proyecto: [lee `\tituloproyecto` de `estilos/configuracion.tex` o completa aquí]
- Capítulos incluidos en este análisis: [los 7 capítulos ensamblados desde `capitulos/index.tex`]
- Formato fuente: el texto incluye comandos LaTeX (`\chapter`, `\section`, `\cite`, `\ref`, `\label`, `\input`, etc.) — consérvalos intactos en tus citas y no los interpretes como errores.

### Criterios de evaluación

**1. Coherencia integral del modelo de negocio**
- Consistencia terminológica: mismos términos técnicos, denominaciones de producto y unidades de medida usados de forma uniforme en todos los capítulos.
- Coherencia conceptual: que la oportunidad de mercado detectada (Cap. 1) y el diagnóstico (Cap. 2) sustenten directamente el análisis de mercado y la propuesta de valor del Cap. 3.
- Alineación estricta entre Objetivos Específicos (Cap. 2), Desarrollo Operativo (Cap. 3), Viabilidad Financiera (Cap. 4), Resultados Piloto (Cap. 5) y Conclusiones (Cap. 7): cada objetivo específico debe tener su desarrollo técnico, su evaluación de costo, su validación empírica y su conclusión explícita.
- Alineación del título del emprendimiento con el bien o servicio ofrecido y las conclusiones finales.

**2. Rigor comercial, técnico y financiero**
- Estimación de demanda y oferta fundamentada con instrumentos aplicados o fuentes estadísticas citadas.
- Coherencia entre capacidad de producción instalada, costos variables unitarios y volumen del punto de equilibrio.
- Precisión matemática en inversiones, costos fijos/variables, precio unitario de venta y punto de equilibrio (sin contradicciones de cifras entre tablas y texto).
- Formato numérico SI/ISO 80000-1: punto decimal (`.`), sin comas decimales ni separadores de miles con coma o punto.

**3. Cumplimiento de normas BTH y formato**
- Tono académico formal, impersonal (tercera persona, "se determinó", "se diseñó").
- Citas en formato APA 7ma Edición (`\parencite`, `\textcite`).
- Prioridad de viñetas (`itemize`) en objetivos, conclusiones y listas descriptivas.
- Tablas en booktabs (`\toprule`, `\midrule`, `\bottomrule`, sin líneas verticales ni `\hline`) con notas normalizadas mediante `\notatabla`.

### Formato de salida esperado
```
## Diagnóstico Panorámico del Emprendimiento Productivo
[Visión global: solidez del modelo de negocio, viabilidad y consistencia]

## Matriz de Trazabilidad y Sincronía
| Objetivo Específico (Cap. 2) | Desarrollo Operativo (Cap. 3) | Presupuesto/Costo (Cap. 4) | Validación Piloto (Cap. 5) | Conclusión (Cap. 7) | Estado de Sincronía |
|---|---|---|---|---|---|

## Inconsistencias Críticas Detectadas
- [Capítulo X, Sección Y]: [Problema detectado y sugerencia de corrección con texto LaTeX propuesto]

## Recomendaciones Prioritarias
1. [Acción correctiva inmediata]
```
