# Flujo de Revisión Académica — Emprendimiento Productivo (BTH)

Este set de **14 prompts** está diseñado para evaluar y perfeccionar el proyecto de grado en la modalidad de **Emprendimiento Productivo** por etapas modulares, respetando la estructura oficial de **7 capítulos** normada por el Reglamento de Graduación del Bachillerato Técnico Humanístico (Resolución Ministerial RM 0912/2023, Anexo 1, inciso A).

---

## 📋 Matriz del Flujo de Revisión

| # | Archivo | Qué revisa | Correspondencia en `capitulos/` |
|---|---|---|---|
| 00 | `00_analisis-capitulos-tesis.md` | Análisis integral de coherencia comercial, viabilidad financiera y sincronía | Todo el documento consolidado |
| 01 | `01_revision_estructura_general.md` | Estructura global, carátula, preliminares, 7 capítulos y anexos | Estructura global y `main.tex` |
| 01b | `01b_revision_introduccion.md` | Contexto general, oportunidad de negocio, propuesta de valor y marco teórico | Cap. 1 (`01_introduccion/`) |
| 02 | `02_revision_planteamiento_emprendimiento.md` | Diagnóstico de mercado, objetivos (general/específicos/misión/visión) y justificación | Cap. 2 (`02_planteamiento_emprendimiento/`) |
| 03 | `03_revision_desarrollo_emprendimiento.md` | Localización, mercado, promoción, organización, producto y ciclo de producción | Cap. 3 (`03_desarrollo_emprendimiento/`) |
| 04 | `04_revision_viabilidad_sostenibilidad.md` | Presupuesto de inversiones, costos fijos/variables, rentabilidad y punto de equilibrio | Cap. 4 (`04_viabilidad_sostenibilidad/`) |
| 05 | `05_revision_resultados.md` | Pruebas piloto, ventas de validación comercial, satisfacción del cliente y métricas | Cap. 5 (`05_resultados/`) |
| 06 | `06_revision_proyecto_vida.md` | Aspiraciones vocacionales, competencias empresariales y compromiso socioeconómico | Cap. 6 (`06_proyecto_vida/`) |
| 07 | `07_revision_conclusiones_recomendaciones.md` | Cumplimiento verificable de objetivos, conclusiones y recomendaciones | Cap. 7 (`07_conclusiones_recomendaciones/`) |
| 08 | `08_revision_coherencia_sincronia_global.md` | Sincronía integral entre los 7 capítulos y consistencia de variables | Capítulos 1 al 7 |
| 09 | `09_revision_redaccion_estilo_academico.md` | Registro formal, redacción impersonal, estilo APA 7, normas numéricas y viñetas | Redacción de todos los capítulos |
| 10 | `10_revision_citas_bibliografia.md` | Correspondencia de citas parentéticas/narrativas con `referencias.bib` | `bibliografia/` y citas en texto |
| 11 | `11_checklist_pre_entrega_final.md` | Verificación institucional y técnica antes de encuadernación y defensa | Documento final y compilación PDF |

---

## 🛠️ Cómo utilizar cada prompt

### Para agentes de IA con acceso al repositorio
1. Abre el archivo del prompt correspondiente al capítulo o fase que deseas validar.
2. El agente debe leer `AGENTS.md` y seguir sus reglas antes de ejecutar la revisión.
3. Los datos del proyecto se obtienen automáticamente de `estilos/configuracion.tex` y `docs/ficha-proyecto.md`.
4. El agente lee directamente los archivos `.tex` del capítulo listados en cada prompt (sección "Archivos a revisar").

### Para uso manual (copiar y pegar)
1. Abre el archivo del prompt correspondiente al capítulo o fase que deseas validar.
2. Copia su contenido y pégalo en la conversación con el asistente de IA.
3. Rellena los campos entre `[corchetes]` con los datos específicos de tu proyecto (extraídos de `docs/ficha-proyecto.md` o del borrador del capítulo).
4. Pega el contenido LaTeX de los archivos `.tex` del capítulo a evaluar.
5. Los comandos LaTeX (`\section`, `\input`, `\cite`, `\ref`, `\label`, `\begin{table}`) deben conservarse intactos.
