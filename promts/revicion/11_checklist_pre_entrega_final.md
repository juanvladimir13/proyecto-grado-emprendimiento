# Prompt: Checklist Pre-Entrega y Defensa Final (BTH RM 0912/2023)

## Cuándo usar este prompt
Como última verificación previa a la impresión, encuadernación o entrega formal del documento PDF ante el tribunal de titulación del Bachillerato Técnico Humanístico (BTH).

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` completo y verifica el cumplimiento de todas sus reglas (formato, estilos de títulos, macros, compilación).
2. Obtén los datos del proyecto desde `estilos/configuracion.tex` para verificar que no haya texto quemado (hardcodeado) en otros archivos y la modalidad sea `EMPRENDIMIENTO PRODUCTIVO`.
3. Ejecuta `./compilar.sh --clean` y verifica que compile sin errores `LaTeX Error` ni advertencias `Unresolved references`.
4. Lee `main.tex` para verificar la estructura completa de inclusión.
5. Lee `capitulos/index.tex` para verificar el ensamble de los 7 capítulos.
6. Verifica la existencia de todos los archivos de `preliminares/`, `capitulos/`, `tablas/`, `anexos/` y `bibliografia/`.
7. Ejecuta `./compilar.sh --check-tablas` para certificar que el 100% de las tablas cumplan con APA 7 y no desborden los márgenes.

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Pega el índice final del documento y los datos del PDF compilado al final.

---

## Archivos a verificar

| Componente | Archivo(s) |
| :--- | :--- |
| Entrada principal | `main.tex` |
| Configuración | `estilos/configuracion.tex`, `estilos/estilos.sty`, `estilos/caratula.sty` |
| Preliminares | `preliminares/caratula.tex`, `preliminares/dedicatoria.tex`, `preliminares/agradecimiento.tex`, `preliminares/resumen.tex` |
| Capítulos 1 al 7 | `capitulos/index.tex` → 7 carpetas con `main.tex` y secciones `.tex` |
| Tablas activas | `tablas/*.tex` (`estudio_mercado`, `estructura_organizacional`, `inversiones`, `costos_produccion`, `indicadores_financieros`, `resultados_piloto`) |
| Bibliografía | `bibliografia/referencias.bib` |
| Anexos | `anexos/index.tex` → `anexo_a_canvas.tex`, `anexo_b_fichas_tecnicas.tex`, `anexo_c_codigo_fuente.tex` |
| Código fuente | `codigo/` (archivos importados vía `\lstinputlisting`) |
| Compilación | `./compilar.sh --clean` → `main.pdf` |

---

## PROMPT

Actúa como el **presidente de tribunal de titulación del Bachillerato Técnico Humanístico (BTH)** para la modalidad de **Emprendimiento Productivo** (Resolución Ministerial RM 0912/2023, Anexo 1, inciso A). Realiza la auditoría final y definitiva del documento de proyecto de grado según el checklist oficial.

### Contexto del documento
- Modalidad: Proyecto de Grado — Emprendimiento Productivo (BTH Bolivia)
- Compilación oficial: Ejecutado mediante `./compilar.sh --clean` (generación de `main.pdf`)
- Formato tipográfico y márgenes:
  * Papel carta (`letterpaper`), Arial 11pt, interlineado 1.5 en texto principal.
  * Margen izquierdo: 3.0 cm | Márgenes superior, inferior y derecho: 2.5 cm.
  * Silabación/guionado desactivado globalmente.
  * Sin encabezados de página (`headrulewidth=0pt`), números de página centrados al pie en arábigos (Capítulos 1 al 7).

### Checklist Oficial a Verificar

1. **Hojas preliminares (numeración romana minúscula):**
   - [ ] Carátula oficial BTH modular (`\imprimircaratulabth` / `\begin{estilocaratulabth}`) con marco perimetral (`\insertarmarcobth` / `marco_portada_bth.png`), logotipo institucional (`\rutalogobth`), datos del postulante(s) (1 o 2 autores dinámicos sin C.I.), tutor, institución, especialidad, modalidad y año de gestión.
   - [ ] Dedicatoria y Agradecimiento con formato semántico unificado (`\begin{estilodedicatoria}{Título}`) alineado a la parte inferior de la hoja incluyendo título, cursiva a la derecha y registro en TOC.
   - [ ] Resumen en castellano (máx. 300 palabras), con `\palabrasclave{...}`.
   - [ ] Resumen en lengua originaria (quechua/aymara/guaraní) con `\simikuna{...}`.
   - [ ] Resumen en lengua extranjera (Abstract) con `\keywords{...}`.
   - [ ] Índices automáticos actualizados: Tabla de Contenidos (TOC), Índice de Figuras (LOF) e Índice de Tablas (LOT).

2. **Cuerpo del documento (Capítulos 1 al 7 con numeración arábiga):**
   - [ ] **Capítulo 1: Introducción:** Contexto del sector productivo, identificación fundamentada de la oportunidad de mercado, propuesta de valor diferenciada y marco teórico del modelo de negocio.
   - [ ] **Capítulo 2: Planteamiento del Emprendimiento Productivo:** Diagnóstico del contexto productivo con instrumentos aplicados, objetivo general y específicos formulados en viñetas (`itemize`), justificación económica, social y técnica.
   - [ ] **Capítulo 3: Desarrollo del Emprendimiento Productivo:** Localización (macro/micro), estudio de mercado y ventaja competitiva, estrategia de distribución y precios, estructura organizacional y cargos, diseño y presentación del producto/servicio, ciclo de procesos operativos.
   - [ ] **Capítulo 4: Viabilidad y Sostenibilidad:** Presupuesto detallado de inversión fija y capital de operación, cálculo exacto de costos variables y costos fijos, precio unitario de venta y determinación del punto de equilibrio operativo.
   - [ ] **Capítulo 5: Resultados:** Datos numéricos de prueba piloto o comercialización de campo, evaluación cualitativa de percepción del cliente y contraste de metas financieras empíricas vs. proyectadas.
   - [ ] **Capítulo 6: Proyecto de Vida:** Aspiraciones académicas/profesionales, competencias empresariales/socioemocionales consolidadas e independencia económica y compromiso comunitario.
   - [ ] **Capítulo 7: Conclusiones y Recomendaciones:** Cierre directo y riguroso de cada objetivo específico formulado, presentado obligatoriamente en viñetas (`itemize`); recomendaciones estratégicas para la consolidación comercial.

3. **Secciones finales (sin numeración de páginas ni cabeceras con `\configurarseccionfinal`):**
   - [ ] **Bibliografía:** Citas en APA 7ma Edición generadas con BibLaTeX/Biber, sin entradas huérfanas ni citas rotas.
   - [ ] **Anexos:** Ensamble con `\capitulopreliminar{ANEXOS}` y secciones con `\seccionanexo{...}` (Modelo Canvas, fichas técnicas, cotizaciones).

4. **Calidad de tablas y diagramación:**
   - [ ] Todas las tablas construidas con `booktabs` (`\toprule`, `\midrule`, `\bottomrule`, sin líneas verticales ni `\hline`).
   - [ ] Rótulo `\caption` arriba de cada tabla y fuentes al pie con la macro `\notatabla{Fuente: ...}`.
   - [ ] Verificación con `./compilar.sh --check-tablas` superada con 0 errores y 0 advertencias.
   - [ ] Formato numérico SI/ISO 80000-1 aplicado estrictamente (punto decimal `.`, sin coma de millares).

5. **Compilación y entrega técnica:**
   - [ ] Compilación limpia ejecutada con `./compilar.sh --clean`.
   - [ ] Ausencia de advertencias críticas en `main.log`.
   - [ ] Archivo `main.pdf` listo para entrega o impresión final.

### Formato de salida esperado
```
## Informe de Auditoría Pre-Defensa de Grado BTH
- Estado global: [APROBADO PARA DEFENSA / OBSERVACIONES PENDIENTES / RECHAZADO]
- Modalidad verificada: Emprendimiento Productivo (RM 0912/2023)

## Tabla de Verificación por Áreas
| Área de Evaluación | Estado | Observación |
|---|---|---|
| Hojas Preliminares | | |
| Estructura de 7 Capítulos | | |
| Viabilidad y Rigor Financiero | | |
| Validación en Resultados | | |
| Bibliografía APA 7 | | |
| Anexos y Canvas | | |
| Compilación Técnica PDF | | |

## Observaciones Críticas a Subsanar antes de la Entrega
1. ...
```
