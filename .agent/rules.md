# Antigravity Rules & Guidelines

Este proyecto de LaTeX modular sigue pautas estrictas para mantener la consistencia, modularidad y cumplimiento de la normativa del Bachillerato Técnico Humanístico (BTH - RM 0912/2023) en Bolivia bajo la modalidad de **Emprendimiento Productivo**.

> [!IMPORTANT]
> Consulta siempre la especificación principal en [AGENTS.md](AGENTS.md) y la estructura de capítulos en [ESTRUCTURA_CAPITULOS.md](ESTRUCTURA_CAPITULOS.md) antes de crear o modificar archivos.

---

## 🎯 Resumen de Reglas Críticas para Antigravity

1. **Variables Centralizadas:**
   - **NUNCA** quemes nombres de autores, tutores, institución, especialidad o título en archivos `.tex` (`caratula.tex`, `portada_universitaria.tex` o capítulos).
   - Toda modificación de metadatos, espaciado de párrafos (`\espacioposteriorparrafo`, `\sangriaprimeralinea`), diagramación (`\espaciosuperiordedicatoria`) y parámetros de figuras (`\anchofigurapredeterminado`, `\anchografico`, `\espacionotafigura`, `\espacionotagrafico`) se realiza en [estilos/configuracion.tex](estilos/configuracion.tex). Soporta 1 o 2 autores dinámicamente (`\autoruno`, `\autordos`).
   - Los campos de C.I. del estudiante fueron removidos y no forman parte de la plantilla.

2. **Estructura Modular de Capítulos (Emprendimiento Productivo):**
   - Todos los capítulos se encuentran en [capitulos/](capitulos/) (Capítulos 1 al 7).
   - Cada capítulo reside en su propia subcarpeta (`01_introduccion/` a `07_conclusiones_recomendaciones/`) con su respectivo `main.tex` que ensambla las secciones.
   - Las inclusiones dentro de cada capítulo usan el prefijo `capitulos/` (ej. `\input{capitulos/02_planteamiento_emprendimiento/diagnostico}`).

3. **Estilo de Títulos APA 7ma Edición Adaptado:**
   - Todos los títulos y enlaces internos (TOC, LOF, LOT, referencias) en **negro** (`linkcolor=black`).
   - Interlineado sencillo (`1.0` / `\setstretch{1.0}`) para títulos de Nivel 1 al 4.
   - Nivel 1 (`\chapter`): Alineado a la **izquierda**, sin prefijo de palabra "Capítulo" (ej. `1. INTRODUCCIÓN`), con espaciado anterior a `-15pt` en `titlesec`.
   - Nivel 2 (`\section`): Alineado a la izquierda, Negrita.
   - Nivel 3 (`\subsection`): Alineado a la izquierda, Negrita y Cursiva.
   - Nivel 4 (`\subsubsection`): Sangría de 1.27 cm, Negrita, tipo *run-in* terminando con punto.
   - Nivel 5 (`\paragraph`): Sangría de 1.27 cm, Negrita y Cursiva, tipo *run-in* terminando con punto.

4. **Encabezados y Pies de Página:**
   - Encabezados deshabilitados (`headrulewidth=0pt`, sin texto superior).
   - Pies de página: numeración arábiga centrada abajo (`\cfoot{\thepage}`) en Capítulos 1 al 7.
   - Páginas preliminares en números romanos (`\pagenumbering{roman}`).
   - Bibliografía y Anexos: no numerados (`numberless`) y limpios de numeración de página y cabeceras mediante `\configurarseccionfinal`.

5. **Bibliografía (BibLaTeX + Biber):**
   - Motor `biblatex` con `style=apa` y backend `biber` sobre [bibliografia/referencias.bib](bibliografia/referencias.bib).
   - En texto: `\parencite{clave}` para citas parentéticas *(Apellido, Año)* y `\textcite{clave}` para narrativas *Apellido (Año)*.
   - Inclusión en `main.tex`: `\printbibliography[heading=bibintoc, title={Bibliografía}]`.
   - Anexos estructurados con `\seccionanexo{Título del Anexo}` y ensamble raíz mediante `\capitulopreliminar{ANEXOS}`.

6. **Código Fuente y Algoritmos:**
   - Motor `listings` con estilo `estilocodigo` predeterminado y tipografía Courier (`courier`).
   - Guardar scripts en [codigo/](codigo/) e importar con:
     `\lstinputlisting[language=Python, caption={...}, label={lst:...}]{codigo/archivo.py}`
   - Ajuste automático de línea (`breaklines=true`) y rótulos en español (`Código`).

7. **Tablas, Figuras y Gráficos (Normas APA 7ma Edición):**
   - **Tablas:** Guardar en [tablas/](tablas/) e importar vía `\input{tablas/archivo.tex}`. Usar `booktabs` (`\toprule`, `\midrule`, `\bottomrule`), PROHIBIDO líneas verticales (`|`) y `\hline`. El `\caption` va obligatoriamente **arriba** de la tabla. Notas al pie alineadas a la izquierda con `\notatabla{Fuente: ...}`. Para textos largos usar `tabularx` (columnas `L`, `C`, `R`, `X`) que respeten `\textwidth`. Auditar con `./compilar.sh --check-tablas`.
   - **Figuras y Gráficos:** Guardar imágenes en [imagenes/](imagenes/) e invocar sin prefijo de ruta.
     * En APA 7, el `\caption` (número en negrita, salto de línea y título en cursiva) se coloca obligatoriamente **ARRIBA** de la imagen.
     * Elemento visual centrado con `\centering`.
     * Notas al pie obligatorias abajo con `\notafigura{Fuente: ...}` (antepone *Nota.* en cursiva y alinea a la izquierda).
     * Macro semántica directa de una línea: `\figuraapa[ancho]{archivo}{Título}{label}{Nota}` (o alias `\insertarfigura`, `\graficoapa`, `\insertargrafico`).
     * Soporte para diagramas vectoriales nativos con `tikz` y control estricto de posición con `float` (`[H]`).
     * Auditar figuras con `./compilar.sh --check-figuras` (o [scripts/verificar_figuras.py](scripts/verificar_figuras.py)).
     * Auditar conjuntamente con `./compilar.sh --check-recursos`.

8. **Control de Silabación:**
   - División de palabras desactivada globalmente (`\hyphenpenalty=10000`, `\exhyphenpenalty=10000`).

9. **Compilación y Limpieza:**
   - Usar siempre el script ejecutable [compilar.sh](compilar.sh):
     * `./compilar.sh` (compilación completa de 4 pasos: pdflatex + biber + pdflatex x2).
     * `./compilar.sh --clean` (compilación completa + eliminación de temporales).
     * `./compilar.sh --fast` (compilación rápida de 1 sola pasada pdflatex).
     * `./compilar.sh --only-clean` (limpieza de temporales sin compilar).
     * `./compilar.sh --check-tablas` (auditoría de tablas APA 7 y diagramación).
     * `./compilar.sh --check-figuras` (auditoría de figuras e imágenes APA 7).
     * `./compilar.sh --check-recursos` (auditoría conjunta de tablas y figuras).

10. **Modalidad y Ensamble:**
    - Modalidad activa: **Emprendimiento Productivo** (Capítulos 1 al 7).
    - Ensamble raíz en [main.tex](main.tex) vía `\input{capitulos/index.tex}`.
    - Metadatos institucionales y del estudiante centralizados en [estilos/configuracion.tex](estilos/configuracion.tex).
    - Ficha de datos del proyecto en [docs/ficha-proyecto.md](docs/ficha-proyecto.md) (alimentada desde `docs/proyecto.rtf` o `docs/proyecto.md` y consultas interactivas).
    - Preliminares: [agradecimiento.tex](preliminares/agradecimiento.tex) y [dedicatoria.tex](preliminares/dedicatoria.tex) utilizan `\capitulopreliminar` y el entorno global `\begin{estilodedicatoria}` (con espaciado superior configurable `\espaciosuperiordedicatoria`).
    - Resúmenes en [preliminares/resumen.tex](preliminares/resumen.tex) formatean palabras clave con `\palabrasclave{...}`, `\keywords{...}` y `\simikuna{...}`.
    - Portada oficial BTH en [preliminares/portada_bth.tex](preliminares/portada_bth.tex) con marco ornamental perimetral (`\marcoportadabth`), escudo institucional y bloques semánticos (con carátula ministerial clásica en [preliminares/caratula.tex](preliminares/caratula.tex)).

11. **Prompts de Apoyo (`promts/`):**
    - Guiar la recopilación y redacción con [promts/migracion/ficha-proyecto.md](promts/migracion/ficha-proyecto.md).
    - Revisar consistencia y rigor comercial y técnico con la suite de 14 prompts modulares en [promts/revicion/](promts/revicion/) adaptada a los 7 capítulos de Emprendimiento Productivo (BTH RM 0912/2023), iniciando con `00_analisis_capitulos_emprendimiento.md`.

12. **Formato de Números, Decimales y Separador de Miles (Norma SI/ISO 80000-1):**
    - **Parte decimal:** Usar obligatoriamente punto (`.`) (ej. `12.50`, `3.1416`, `98.5%`, `0.75`). **PROHIBIDO** el uso de coma (`,`) en decimales.
    - **Separador de miles:** **PROHIBIDO** el uso de comas (`,`) o puntos (`.`) como separadores de millares (evitar `1,000` y `1.000`).
    - Cifras de 4 dígitos se escriben juntas sin separación (`1000`, `3500`, `4500.00`, `7700.00`).
    - Cifras de 5 o más dígitos se escriben continuas o con espacio (`25 000.00` o `25000.00`, `46 500.00`), nunca con comas ni puntos.

13. **Listas y Elementos de Enumeración (Prioridad de Viñetas):**
    - Priorizar obligatoriamente el uso del entorno de viñetas (`\begin{itemize}`) frente a listas numeradas (`\begin{enumerate}`).
    - Emplear siempre `itemize` para listar objetivos específicos, conclusiones, recomendaciones, características técnicas, componentes y elementos descriptivos generales.
    - Reservar `\begin{enumerate}` exclusivamente para secuencias algorítmicas estrictas, cronologías o pasos procedimentales secuenciales donde la numeración sea indispensable.

14. **Macros Semánticas Estandarizadas de la Plantilla:**
    - Utilizar obligatoriamente las macros semánticas provistas en `estilos.sty`:
      * `\capitulopreliminar{Título}`: Capítulos preliminares y Anexos sin numerar agregados a TOC.
      * `\begin{estilodedicatoria}...\end{estilodedicatoria}`: Entorno semántico para dedicatoria y agradecimiento.
      * `\seccionanexo{Título}`: Encabezados de secciones de anexos agregados a TOC.
      * `\configurarseccionfinal`: Estilo de página limpio (`empty`) para bibliografía y anexos.
      * `\palabrasclave{...}`, `\keywords{...}`, `\simikuna{...}`: Bloques semánticos de palabras clave.
      * `\notatabla{...}`: Notas al pie de tablas bajo APA 7.
      * `\notafigura{...}`, `\notaimagen{...}`, `\notagrafico{...}`: Notas al pie de figuras y gráficos bajo APA 7.
      * `\figuraapa[ancho]{archivo}{Título}{label}{Nota}` (y sus aliases `\insertarfigura`, `\graficoapa`, `\insertargrafico`): Inserción estandarizada de figuras APA 7.
      * `\titulocaratula{...}` y `\subtitulocaratula{...}`: Formato tipográfico en carátula clásica.
      * `\marcoportadabth`, `\marcoportadatikzbth`, `\institucionportadabth`, `\carreraportadabth`, `\tituloportadabth`, `\mencionportadabth`, `\bloquepostulantesbth`, `\bloquetutorbth`: Macros estructuradas de la portada oficial BTH.
