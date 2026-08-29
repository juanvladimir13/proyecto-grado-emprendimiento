# Prompt: Revisión de Estructura General e Índice (7 Capítulos BTH)

## Cuándo usar este prompt
Al iniciar el proceso de revisión, con el índice general o el árbol de capítulos definido, para verificar el estricto cumplimiento de la normativa BTH (Resolución Ministerial RM 0912/2023, Anexo 1, inciso A).

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier revisión.
2. Lee `main.tex` para verificar la estructura de inclusión de preliminares, capítulos, bibliografía y anexos.
3. Lee `capitulos/index.tex` para verificar el ensamble de los 7 capítulos.
4. Verifica la existencia de cada `main.tex` de capítulo y sus subsecciones `.tex`.
5. Lee `estilos/configuracion.tex` para verificar que los datos institucionales estén definidos como macros y la modalidad sea `EMPRENDIMIENTO PRODUCTIVO`.

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Pega el índice de contenidos o la estructura de archivos del documento al final.

---

## Archivos a revisar

| Componente | Archivo(s) |
| :--- | :--- |
| Entrada principal | `main.tex` |
| Ensamble de capítulos | `capitulos/index.tex` |
| Preliminares | `preliminares/caratula.tex`, `preliminares/dedicatoria.tex`, `preliminares/agradecimiento.tex`, `preliminares/resumen.tex` |
| Cap. 1 | `capitulos/01_introduccion/main.tex` → `contexto_general.tex`, `oportunidad_negocio.tex`, `propuesta_valor.tex`, `marco_teorico.tex` |
| Cap. 2 | `capitulos/02_planteamiento_emprendimiento/main.tex` → `diagnostico.tex`, `objetivos.tex`, `justificacion.tex` |
| Cap. 3 | `capitulos/03_desarrollo_emprendimiento/main.tex` → `localizacion.tex`, `analisis_mercado.tex`, `estrategia_promocion.tex`, `estructura_organizacional.tex`, `diseno_producto.tex`, `ciclo_produccion.tex` |
| Cap. 4 | `capitulos/04_viabilidad_sostenibilidad/main.tex` → `calculo_inversiones.tex`, `costo_produccion.tex` |
| Cap. 5 | `capitulos/05_resultados/main.tex` → `resultados_cuantitativos.tex`, `resultados_cualitativos.tex`, `indicadores_validados.tex` |
| Cap. 6 | `capitulos/06_proyecto_vida/main.tex` *(contenido directo en main.tex)* |
| Cap. 7 | `capitulos/07_conclusiones_recomendaciones/main.tex` → `conclusiones.tex`, `recomendaciones.tex` |
| Bibliografía | `bibliografia/referencias.bib` |
| Anexos | `anexos/index.tex` → `anexo_a_canvas.tex`, `anexo_b_fichas_tecnicas.tex`, `anexo_c_codigo_fuente.tex` |
| Configuración | `estilos/configuracion.tex`, `estilos/estilos.sty`, `estilos/caratula.sty` |

---

## PROMPT

Actúa como un **revisor metodológico de proyectos de grado BTH**. Tu tarea es evaluar la **estructura general** del documento que te proporcionaré, verificando que cumpla con la organización oficial de **7 capítulos** establecida para la modalidad de **Emprendimiento Productivo** (Reglamento BTH, Resolución Ministerial RM 0912/2023, Anexo 1, inciso A).

### Contexto del documento
- Modalidad: Proyecto de Grado — Emprendimiento Productivo (BTH)
- Estructura oficial requerida:
  1. Preliminares: Carátula oficial BTH, Dedicatoria, Agradecimiento, Resúmenes (castellano, originario, extranjero), Índices (TOC, tablas, figuras).
  2. Capítulo 1: Introducción (contexto general, oportunidad de negocio, propuesta de valor, marco teórico y conceptual).
  3. Capítulo 2: Planteamiento del Emprendimiento Productivo (diagnóstico del contexto productivo, objetivos general/específicos/misión/visión, justificación).
  4. Capítulo 3: Desarrollo del Emprendimiento Productivo (localización macro/micro, análisis de mercado, estrategia de promoción y distribución, estructura organizacional, diseño de producto o servicio, ciclo de producción).
  5. Capítulo 4: Viabilidad y Sostenibilidad (cálculo de inversiones, costo de producción, indicadores de rentabilidad y punto de equilibrio).
  6. Capítulo 5: Resultados (resultados cuantitativos y validación de mercado, resultados cualitativos y percepción del cliente, indicadores de rentabilidad validados).
  7. Capítulo 6: Proyecto de Vida (aspiraciones académicas y profesionales, competencias empresariales y socioemocionales adquiridas, compromiso ético e independencia económica).
  8. Capítulo 7: Conclusiones y Recomendaciones (conclusiones y recomendaciones operativas/estratégicas).
  9. Bibliografía (APA 7ma Edición con BibLaTeX).
  10. Anexos (Modelo Canvas, fichas técnicas, presupuestos/cotizaciones).

### Qué debes evaluar
1. **Completitud estructural:** ¿figuran los 7 capítulos requeridos en el orden exacto normado por el RM 0912/2023?
2. **Modularidad:** ¿cada capítulo cuenta con su carpeta propia y su archivo `main.tex` que importa las subsecciones correspondientes mediante `\input{capitulos/...}`?
3. **Jerarquía y numeración:** ¿se respetan los niveles de titulación APA 7 adaptados (Capítulos sin la palabra "Capítulo", secciones y subsecciones sin salto de nivel)?
4. **Preliminares y páginas finales:** ¿la carátula y preliminares utilizan las macros semánticas (`\imprimircaratulabth`, `\begin{estilocaratulabth}`, `\capitulopreliminar`, `\begin{estilodedicatoria}{Título}`, `\palabrasclave`)? ¿Bibliografía y Anexos usan `\configurarseccionfinal` y `\seccionanexo`?
5. **Alineación con `estilos/configuracion.tex`:** ¿los metadatos institucionales están centralizados sin quemar datos en el código de capítulos?

### Formato de salida esperado
```
## Diagnóstico de Estructura General
[Evaluación general del cumplimiento de la normativa BTH RM 0912/2023]

## Matriz de Conformidad Estructural
| Componente | Estado (Cumple / Incompleto / Falta) | Observaciones |
|---|---|---|
| Preliminares | | |
| Cap. 1: Introducción | | |
| Cap. 2: Planteamiento del Emprendimiento | | |
| Cap. 3: Desarrollo del Emprendimiento | | |
| Cap. 4: Viabilidad y Sostenibilidad | | |
| Cap. 5: Resultados | | |
| Cap. 6: Proyecto de Vida | | |
| Cap. 7: Conclusiones y Recomendaciones | | |
| Bibliografía | | |
| Anexos | | |

## Correcciones Requeridas
- [Archivo / Ubicación]: [Acción correctiva específica]
```
