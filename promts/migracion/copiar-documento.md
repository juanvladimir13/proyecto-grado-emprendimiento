# Prompts para Copia Directa del Documento Fuente (RTF/MD) a Capítulos LaTeX (Sin Modificación de Contenido)

**Repo:** `proyecto-grado-emprendimiento`  
**Modalidad:** Emprendimiento Productivo (BTH RM 0912/2023, Anexo 1, inciso A)  
**Propósito:** Este conjunto de prompts está diseñado para migrar de forma **directa, fiel y literal (verbatim)** el contenido existente en `docs/proyecto.rtf` o `docs/proyecto.md` hacia los archivos modulares `.tex` de la plantilla (`capitulos/`, `estilos/configuracion.tex`, `preliminares/`, `tablas/` y `bibliografia/`), **sin modificar, inventar, parafrasear ni alterar la redacción original del autor**.

---

## ⚖️ Diferencia con el Flujo de `ficha-proyecto.md`

| Aspecto | Flujo `ficha-proyecto.md` | Flujo `copiar-documento.md` (Este archivo) |
| :--- | :--- | :--- |
| **Objetivo** | Extraer datos a una ficha intermedia, consultar datos faltantes y redactar/expandir en prosa académica formal. | Copiar y transferir **directa y textualmente** el contenido ya redactado en el documento fuente hacia los archivos LaTeX. |
| **Modificación de texto** | Sí (redacta, complementa y sintetiza según normas). | **NO** (fidelidad textual absoluta al documento fuente original). |
| **Ficha intermedia** | Obligatoria (`docs/ficha-proyecto.md`). | Omitida (migración directa de archivo a archivo). |
| **Tratamiento de vacíos** | Consulta al usuario o marca `[DATO PENDIENTE]`. | Aplica protocolo preventivo: deja comentario `%% [SIN CONTENIDO]`, evita entornos vacíos y no inventa texto. |

---

## 🛡️ Protocolo de Prevención de Bugs ante Datos o Contenido Faltante

Si el documento fuente (`docs/proyecto.rtf` o `docs/proyecto.md`) carece de información para alguna sección o metadato, **deben aplicarse estrictamente las siguientes reglas para evitar errores de compilación o páginas defectuosas**:

1. **Dedicatoria y Agradecimientos ausentes:**
   - ⚠️ **Bug prevenido:** Abrir `\begin{estilodedicatoria}...\end{estilodedicatoria}` sin contenido genera una página en blanco con título huérfano y entrada fantasma en el índice (TOC).
   - 🛠️ **Fix:** Si el documento fuente no contiene dedicatoria o agradecimiento, dejar el archivo `.tex` con solo un comentario `%% [SIN DEDICATORIA EN DOCUMENTO FUENTE]` y **SIN** el entorno `estilodedicatoria`.

2. **Resumen en lengua originaria o extranjera ausente:**
   - 🛠️ **Fix:** Si el documento fuente solo tiene resumen en español, no inventar traducciones en inglés ni en lenguas originarias. Omitir o comentar `\keywords{...}` y `\simikuna{...}`.

3. **Proyecto individual vs. en pareja:**
   - 🛠️ **Fix:** Si el proyecto tiene un solo autor, dejar `\newcommand{\autordos}{}` estrictamente vacío en `estilos/configuracion.tex`. La carátula detecta automáticamente la ausencia del segundo autor y ajusta el rótulo sin dejar espacios vacíos.

4. **Secciones de capítulos sin contenido en el origen:**
   - ⚠️ **Bug prevenido:** Si se inventa texto falso se viola la fidelidad; si se deja un entorno `itemize` vacío `\begin{itemize}\end{itemize}` se produce un error fatal de LaTeX (`LaTeX Error: Something's wrong--perhaps a missing \item`).
   - 🛠️ **Fix:** Conservar la cabecera `\section{...}` y `\label{...}` del archivo con un comentario `%% [SECCIÓN SIN CONTENIDO EN DOCUMENTO FUENTE]`. **NUNCA** dejar entornos `\begin{itemize}` sin elementos `\item`.

5. **Tablas o figuras no presentes en el documento fuente:**
   - ⚠️ **Bug prevenido:** Incluir un `\input{tablas/archivo.tex}` que no existe detiene la compilación con `Fatal Error: File not found`.
   - 🛠️ **Fix:** Si el documento original no tiene datos para una tabla, no crear archivos vacíos ni incluir `\input{tablas/...}` inexistentes.

6. **Ausencia de bibliografía o fuentes citadas:**
   - 🛠️ **Fix:** Si el origen no tiene referencias bibliográficas, dejar `bibliografia/referencias.bib` vacío con un comentario. `biber` y `pdflatex` compilarán sin errores.

7. **Escape de caracteres reservados de LaTeX en el texto fuente:**
   - ⚠️ **Bug prevenido:** Símbolos como `%`, `_`, `&`, `#`, `$`, `{`, `}` provocan fallos de sintaxis al compilar.
   - 🛠️ **Fix:** Escapar obligatoriamente estos símbolos en el texto copiado (`\%`, `\_`, `\&`, `\#`, `\$`, `\{`, `\}`).

---

## 📁 Mapeo de Archivos Destino (`capitulos/` - Emprendimiento Productivo)

El proyecto estructura los 7 capítulos de manera modular bajo el directorio `capitulos/`:

```text
capitulos/
├── index.tex                                          # Ensamble maestro de los 7 capítulos
├── 01_introduccion/
│   ├── main.tex                                       # Cap. 1 — INTRODUCCIÓN (ensamble)
│   ├── contexto_general.tex                           #   └ Contexto general del sector y entorno productivo
│   ├── oportunidad_negocio.tex                        #   └ Identificación de la oportunidad de negocio y demanda
│   ├── propuesta_valor.tex                            #   └ Propuesta de valor diferencial e innovación
│   └── marco_teorico.tex                              #   └ Marco teórico y conceptual
├── 02_planteamiento_emprendimiento/
│   ├── main.tex                                       # Cap. 2 — PLANTEAMIENTO DEL EMPRENDIMIENTO PRODUCTIVO
│   ├── diagnostico.tex                                #   └ Diagnóstico del contexto productivo y brechas
│   ├── objetivos.tex                                  #   └ Objetivos (general, específicos, misión y visión)
│   └── justificacion.tex                              #   └ Justificación económica, social y técnica
├── 03_desarrollo_emprendimiento/
│   ├── main.tex                                       # Cap. 3 — DESARROLLO DEL EMPRENDIMIENTO PRODUCTIVO
│   ├── localizacion.tex                               #   └ Macrolocalización y microlocalización
│   ├── analisis_mercado.tex                           #   └ Oferta, demanda, público objetivo y competencia
│   ├── estrategia_promocion.tex                       #   └ Canales de distribución, precios y promoción
│   ├── estructura_organizacional.tex                  #   └ Forma jurídica, organigrama y manual de funciones
│   ├── diseno_producto.tex                            #   └ Características técnicas, formulación, empaque y marca
│   └── ciclo_produccion.tex                           #   └ Flujo de procesos operativos, capacidad y equipamiento
├── 04_viabilidad_sostenibilidad/
│   ├── main.tex                                       # Cap. 4 — VIABILIDAD Y SOSTENIBILIDAD
│   ├── calculo_inversiones.tex                        #   └ Presupuesto de inversión fija/diferida y capital de trabajo
│   └── costo_produccion.tex                           #   └ Costos variables, fijos, rentabilidad y punto de equilibrio
├── 05_resultados/
│   ├── main.tex                                       # Cap. 5 — RESULTADOS
│   ├── resultados_cuantitativos.tex                   #   └ Validación comercial y ventas piloto
│   ├── resultados_cualitativos.tex                    #   └ Percepción y satisfacción del cliente
│   └── indicadores_validados.tex                      #   └ Contraste financiero empírico vs metas proyectadas
├── 06_proyecto_vida/
│   └── main.tex                                       # Cap. 6 — PROYECTO DE VIDA (redacción directa en main.tex)
└── 07_conclusiones_recomendaciones/
    ├── main.tex                                       # Cap. 7 — CONCLUSIONES Y RECOMENDACIONES
    ├── conclusiones.tex                               #   └ Conclusiones del emprendimiento (por objetivos)
    └── recomendaciones.tex                            #   └ Recomendaciones estratégicas y comerciales
```

---

## 🚀 Opción A: Flujo Modular Paso a Paso

---

### Prompt 1 — Volcar datos institucionales y preliminares (Sin modificar texto)

```text
Actúa como asistente técnico de estructuración LaTeX. Tu objetivo en este paso es leer el documento fuente y extraer los datos generales y páginas preliminares EXACTAMENTE como están escritos, sin modificar el contenido.

1. Localización y lectura del documento fuente:
   - Revisa `docs/proyecto.rtf` o `docs/proyecto.md`.
   - Si es un archivo RTF, procesa el texto plano descartando las etiquetas de control RTF. Si es Markdown, léelo directamente.

2. Configuración institucional (`estilos/configuracion.tex`):
   - Extrae los valores textuales presentes en la portada/encabezado del documento y asígnalos a las macros correspondientes en `estilos/configuracion.tex`:
     * \departamento{...}
     * \distritoeducativo{...}
     * \institucion{...}
     * \facultad{...} (si aplica)
     * \modalidad{EMPRENDIMIENTO PRODUCTIVO}
     * \especialidad{...}
     * \nivelformacion{TÉCNICO MEDIO}
     * \tituloproyecto{...}
     * \subtituloproyecto{...} (si existe)
     * \autoruno{...}, \autordos{...} (dejar \autordos vacío si es individual)
     * \emailautoruno{...}, \emailautordos{...} (si existen)
     * \tutorproyecto{...}, \cargotutorproyecto{...}
     * \lugarproyecto{...}
     * \gestionproyecto{...}
     * \fechaproyecto{...}
   - Regla 1 de AGENTS.md: NUNCA quemes (hardcodees) estos datos directamente en los archivos .tex de capítulos ni carátula.

3. Páginas preliminares (`preliminares/`):
   - `preliminares/dedicatoria.tex`: Copia el texto exacto de la dedicatoria dentro del entorno semántico `\begin{estilodedicatoria}{Dedicatoria} ... \end{estilodedicatoria}`. Si no existe en el documento fuente, deja el archivo vacío con `%% [SIN DEDICATORIA EN DOCUMENTO FUENTE]`.
   - `preliminares/agradecimiento.tex`: Copia el texto exacto de los agradecimientos dentro de `\begin{estilodedicatoria}{Agradecimiento} ... \end{estilodedicatoria}`. Si no existe, deja `%% [SIN AGRADECIMIENTO EN DOCUMENTO FUENTE]`.
   - `preliminares/resumen.tex`: Copia literalmente el resumen en castellano, el abstract (si existe) y el resumen en lengua originaria (si existe), utilizando las macros `\palabrasclave{...}`, `\keywords{...}` y `\simikuna{...}` con las palabras clave exactas del texto original.

4. Verificación:
   - Verifica que en `main.tex` se mantenga activo `\input{capitulos/index.tex}`.
   - Muestra el diff de los cambios realizados en este paso y NO toques aún los archivos de `capitulos/`.
```

---

### Prompt 2 — Copiar el contenido literal a los 7 Capítulos y Tablas (Sin Modificar Contenido)

```text
Lee por completo el documento fuente (`docs/proyecto.rtf` o `docs/proyecto.md`) y las reglas de `AGENTS.md`.

Tu tarea es copiar el contenido del documento fuente a los archivos .tex de `capitulos/` y `tablas/`, distribuyéndolo según la estructura modular de Emprendimiento Productivo (7 capítulos), respetando con TOTAL FIDELIDAD la redacción y palabras originales del autor.

REGLAS CRÍTICAS DE COPIA TEXTUAL:
1. NO MODIFICAR EL CONTENIDO: Está terminantemente PROHIBIDO parafrasear, reescribir, resumir, embellecer o inventar texto. Conserva intactos los párrafos, términos técnicos, explicaciones, datos y conclusiones tal como fueron redactados en el documento fuente.
2. Adaptación sintáctica a LaTeX:
   - Escapa caracteres especiales de LaTeX si aparecen en el texto (% -> \%, _ -> \_, & -> \&, # -> \#, $ -> \$, etc.).
   - Convierte listas a viñetas `\begin{itemize}\item ... \end{itemize}` (o `\begin{enumerate}` solo si son secuencias numéricas correlativas explícitas).
   - Mantén intactas las etiquetas `\section{...}` y `\label{...}` existentes en cada archivo modular.
3. Modularidad:
   - No agregues `\chapter{...}` dentro de los archivos secundarios de sección (el archivo `main.tex` de cada capítulo ya contiene la cabecera del capítulo).
4. Mapeo de Secciones (7 Capítulos de Emprendimiento Productivo):
   - Cap. 1 (`capitulos/01_introduccion/`):
     * `contexto_general.tex` -> Contexto general, entorno sectorial y geográfico del emprendimiento.
     * `oportunidad_negocio.tex` -> Identificación de la oportunidad de negocio y demanda insatisfecha.
     * `propuesta_valor.tex` -> Propuesta de valor, diferenciación y ventajas competitivas.
     * `marco_teorico.tex` -> Fundamentos teóricos y conceptuales (modelo de negocio, costeo, cadena de valor).
   - Cap. 2 (`capitulos/02_planteamiento_emprendimiento/`):
     * `diagnostico.tex` -> Diagnóstico del contexto productivo y análisis de brechas de oferta.
     * `objetivos.tex` -> Objetivo general, objetivos específicos, misión y visión empresarial (con `itemize`).
     * `justificacion.tex` -> Justificación económica, social y técnica.
   - Cap. 3 (`capitulos/03_desarrollo_emprendimiento/`):
     * `localizacion.tex` -> Macrolocalización y microlocalización de la unidad productiva.
     * `analisis_mercado.tex` -> Análisis de mercado (oferta, demanda, público objetivo, competencia y ventaja competitiva).
     * `estrategia_promocion.tex` -> Canales de distribución, política de precios y estrategias de promoción comercial.
     * `estructura_organizacional.tex` -> Forma jurídica, organigrama funcional y manual de funciones/cargos.
     * `diseno_producto.tex` -> Características técnicas, formulación, empaque, rotulado y marca comercial.
     * `ciclo_produccion.tex` -> Flujo de procesos operativos, capacidad instalada y equipamiento principal.
   - Cap. 4 (`capitulos/04_viabilidad_sostenibilidad/`):
     * `calculo_inversiones.tex` -> Plan de inversión (activos fijos, diferidos) y capital de operación inicial.
     * `costo_produccion.tex` -> Costos variables, costos fijos, margen de contribución, precio sugerido y punto de equilibrio.
   - Cap. 5 (`capitulos/05_resultados/`):
     * `resultados_cuantitativos.tex` -> Validación comercial, volumen producido/colocado y ventas piloto en bolivianos.
     * `resultados_cualitativos.tex` -> Percepción del cliente y nivel de satisfacción con el producto/servicio.
     * `indicadores_validados.tex` -> Contraste empírico de metas proyectadas vs. resultados de prueba piloto.
   - Cap. 6 (`capitulos/06_proyecto_vida/main.tex`):
     * Aspiraciones académicas y profesionales, competencias empresariales y socioemocionales adquiridas, compromiso ético, independencia económica y proyección a futuro.
   - Cap. 7 (`capitulos/07_conclusiones_recomendaciones/`):
     * `conclusiones.tex` -> Conclusiones del emprendimiento por objetivos (con `itemize`).
     * `recomendaciones.tex` -> Recomendaciones estratégicas, operativas y comerciales (con `itemize`).
5. Tablas y datos estructurados:
   - Si el documento fuente contiene tablas (estudio de mercado, organigrama/cargos, presupuesto de inversiones, costos de producción, indicadores financieros, resultados piloto, etc.), crea el archivo correspondiente en `tablas/` usando `booktabs` (normas APA 7: `\toprule`, `\midrule`, `\bottomrule`, sin líneas verticales) e impórtalo con `\input{tablas/nombre_tabla.tex}`. Agrega `\notatabla{Fuente: ...}` si la tabla indica fuente original.
6. Secciones sin contenido en el documento fuente:
   - Si el documento fuente NO tiene información para alguna sección en particular, NO inventes texto ficticio. Deja la sección con un comentario LaTeX:
     `%% [SECCIÓN SIN CONTENIDO EN EL DOCUMENTO FUENTE]`
   - NUNCA dejes entornos `\begin{itemize}\end{itemize}` sin elementos `\item` (esto genera error fatal de compilación). Si no hay viñetas, no abras el entorno.
   - Si no hay tablas para una sección, NO invoques `\input{tablas/...}` con archivos inexistentes ni dejes referencias `\ref{tab:...}` rotas.
7. Al concluir, presenta un reporte listando:
   - Archivos .tex completados con texto literal.
   - Archivos que quedaron vacíos por ausencia de datos en el documento fuente.
   - Tablas extraídas e integradas.
```

---

### Prompt 3 — Transferir bibliografía a `bibliografia/referencias.bib` (Sin Modificar Fuentes)

```text
Revisa el apartado de Bibliografía, Referencias o Fuentes del documento fuente (`docs/proyecto.rtf` o `docs/proyecto.md`).

1. Extrae todas las fuentes y referencias bibliográficas listadas en el documento original.
2. Conviértelas al formato BibLaTeX estándar en `bibliografia/referencias.bib`, usando los tipos de entrada correspondientes (@book, @article, @online, @manual, @techreport, etc.):
   - Conserva con total exactitud los apellidos y nombres de autores, títulos, años de publicación, editoriales y enlaces URL.
   - No inventes referencias adicionales que no figuren en el documento fuente.
3. En los capítulos donde se mencionen estas fuentes, utiliza `\parencite{clave}` o `\textcite{clave}` según corresponda, sin alterar el texto circundante.
4. Muestra un resumen de las entradas bibliográficas agregadas a `bibliografia/referencias.bib`.
```

---

### Prompt 4 — Compilar y validar el documento final

```text
Ejecuta la compilación y validación del documento LaTeX generado tras la copia literal:

1. Ejecuta `./compilar.sh --fast` para verificar que la sintaxis LaTeX, escape de caracteres y enlaces modulares sean completamente válidos.
2. Ejecuta `./compilar.sh --check-recursos` (o `./compilar.sh --check-tablas` y `./compilar.sh --check-figuras`) para auditar la conformidad estricta de tablas y figuras con normas APA 7ma Edición.
3. Si la compilación rápida y auditoría pasan sin advertencias críticas ni errores, ejecuta `./compilar.sh --clean` para generar el PDF definitivo con el ciclo completo (pdflatex + biber + pdflatex x2) y limpiar archivos temporales.
4. Notifica el resultado:
   - Confirma la generación de `main.pdf`.
   - Indica el número total de páginas generadas.
   - Informa el estado de resolución del índice general, tablas, figuras y bibliografía.
```

---

## ⚡ Opción B: Prompt Todo-en-Uno (All-in-One Direct Migration)

Para ejecutar toda la copia directa en una sola instrucción sin pausas:

```text
Actúa como especialista en migración y estructuración de proyectos de grado en LaTeX para la modalidad Emprendimiento Productivo (BTH RM 0912/2023, Anexo 1, inciso A).

Lee atentamente `AGENTS.md` y el documento fuente (`docs/proyecto.rtf` o `docs/proyecto.md`).

OBJETIVO EXCLUSIVO: Copiar y transferir TODO el contenido disponible en el documento fuente a la estructura modular de LaTeX del proyecto (`estilos/configuracion.tex`, `preliminares/`, `capitulos/`, `tablas/` y `bibliografia/`), conservando el texto de forma LITERAL Y EXACTA, SIN MODIFICAR, RESUMIR, PARAFRASEAR NI INVENTAR CONTENIDO.

INSTRUCCIONES DE EJECUCIÓN:

1. Metadatos Institucionales (`estilos/configuracion.tex`):
   - Extrae el departamento, distrito educativo, unidad educativa, especialidad, título, subtítulo, autor(es), tutor, gestión, fecha y localidad tal como están escritos y asígnalos a las macros de `estilos/configuracion.tex`. No quemes estos datos en capítulos ni carátula.

2. Preliminares (`preliminares/`):
   - Copia la dedicatoria en `preliminares/dedicatoria.tex` (`\begin{estilodedicatoria}{Dedicatoria}`).
   - Copia los agradecimientos en `preliminares/agradecimiento.tex` (`\begin{estilodedicatoria}{Agradecimiento}`).
   - Copia los resúmenes y palabras clave en `preliminares/resumen.tex` (`\palabrasclave`, `\keywords`, `\simikuna`).
   - Si no existen en el origen, deja el archivo con un comentario `%% [SIN CONTENIDO EN FUENTE]` sin abrir entornos vacíos.

3. Capítulos Modulares (`capitulos/` — 7 Capítulos de Emprendimiento Productivo):
   - Vuelca textualmente el contenido de cada sección en su respectivo archivo .tex:
     * Cap. 1: `contexto_general.tex`, `oportunidad_negocio.tex`, `propuesta_valor.tex`, `marco_teorico.tex`.
     * Cap. 2: `diagnostico.tex`, `objetivos.tex`, `justificacion.tex`.
     * Cap. 3: `localizacion.tex`, `analisis_mercado.tex`, `estrategia_promocion.tex`, `estructura_organizacional.tex`, `diseno_producto.tex`, `ciclo_produccion.tex`.
     * Cap. 4: `calculo_inversiones.tex`, `costo_produccion.tex`.
     * Cap. 5: `resultados_cuantitativos.tex`, `resultados_cualitativos.tex`, `indicadores_validados.tex`.
     * Cap. 6: `06_proyecto_vida/main.tex`.
     * Cap. 7: `conclusiones.tex`, `recomendaciones.tex`.
   - Reglas de fidelidad textual: No alteres la redacción, ideas ni palabras del autor. Mantén las etiquetas `\section{...}` y `\label{...}` existentes. Aplica escape de caracteres especiales de LaTeX (% -> \%, _ -> \_, & -> \&, # -> \#). Usa `\begin{itemize}` para listas de viñetas (nunca dejes un `itemize` vacío sin `\item`).
   - Si una sección no tiene contenido en el origen, deja `%% [SECCIÓN SIN CONTENIDO EN EL DOCUMENTO FUENTE]`. NUNCA inventes información.
   - Si no hay tablas para una sección, no incluyas `\input{tablas/...}` inexistentes.

4. Tablas (`tablas/`) y Bibliografía (`bibliografia/referencias.bib`):
   - Extrae tablas a `tablas/*.tex` con formato APA 7 (`booktabs`, `\toprule`, `\midrule`, `\bottomrule`, sin líneas verticales) e impórtalas con `\input{tablas/...}`.
   - Vuelca las referencias bibliográficas a `bibliografia/referencias.bib` en formato BibLaTeX APA 7. Si no existen fuentes, deja el archivo vacío con un comentario.

5. Validación y Compilación:
   - Ejecuta `./compilar.sh --fast`, `./compilar.sh --check-recursos` y luego `./compilar.sh --clean`.
   - Presenta un informe final con el resumen de secciones migradas, tablas extraídas y confirmación de generación de `main.pdf`.
```

