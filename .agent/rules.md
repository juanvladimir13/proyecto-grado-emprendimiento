# Antigravity Rules & Guidelines

Este proyecto de LaTeX modular sigue pautas estrictas para mantener la consistencia, modularidad y cumplimiento de la normativa del Bachillerato Técnico Humanístico (BTH - RM 0912/2023) en Bolivia bajo la modalidad de **Innovación Tecnológica**.

> [!IMPORTANT]
> Consulta siempre la especificación principal en [AGENTS.md](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/AGENTS.md) y la estructura de capítulos en [ESTRUCTURA_CAPITULOS.md](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/ESTRUCTURA_CAPITULOS.md) antes de crear o modificar archivos.

---

## 🎯 Resumen de Reglas Críticas para Antigravity

1. **Variables Centralizadas:**
   - **NUNCA** quemes nombres de autores, tutores, institución, especialidad o título en archivos `.tex` (`caratula.tex`, `portada_universitaria.tex` o capítulos).
   - Toda modificación de metadatos y espaciado de párrafos (`\espacioposteriorparrafo`, `\sangriaprimeralinea`) se realiza en [estilos/configuracion.tex](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/estilos/configuracion.tex). Soporta 1 o 2 autores dinámicamente (`\autoruno`, `\autordos`).

2. **Estructura Modular de Capítulos (Innovación Tecnológica):**
   - Todos los capítulos se encuentran en [capitulos/](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/capitulos/) (Capítulos 1 al 9).
   - Cada capítulo reside en su propia subcarpeta (`01_introduccion/` a `09_conclusiones_recomendaciones/`) con su respectivo `main.tex` que ensambla las secciones.
   - Las inclusiones dentro de cada capítulo usan el prefijo `capitulos/` (ej. `\input{capitulos/02_planteamiento_problema/diagnostico}`).

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
   - Pies de página: numeración arábiga centrada abajo (`\cfoot{\thepage}`) en Capítulos 1 al 9.
   - Páginas preliminares en números romanos (`\pagenumbering{roman}`).
   - Bibliografía y Anexos: no numerados (`numberless`) y limpios de numeración de página y cabeceras (`\pagestyle{empty}`, `\assignpagestyle{\chapter}{empty}`).

5. **Bibliografía (BibLaTeX + Biber):**
   - Motor `biblatex` con `style=apa` y backend `biber` sobre [bibliografia/referencias.bib](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/bibliografia/referencias.bib).
   - En texto: `\parencite{clave}` para citas parentéticas *(Apellido, Año)* y `\textcite{clave}` para narrativas *Apellido (Año)*.
   - Inclusión en `main.tex`: `\printbibliography[heading=bibintoc, title={Bibliografía}]`.

6. **Código Fuente y Algoritmos:**
   - Motor `listings` con estilo `estilocodigo` predeterminado y tipografía Courier (`courier`).
   - Guardar scripts en [codigo/](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/codigo/) e importar con:
     `\lstinputlisting[language=Python, caption={...}, label={lst:...}]{codigo/archivo.py}`
   - Ajuste automático de línea (`breaklines=true`) y rótulos en español (`Código`).

7. **Tablas e Ilustraciones:**
   - Tablas independientes en [tablas/](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/tablas/) e importar vía `\input{tablas/archivo.tex}`.
   - Normas APA 7: usar `booktabs` (`\toprule`, `\midrule`, `\bottomrule`), PROHIBIDO el uso de líneas verticales (`|`) y de `\hline`. El `\caption` debe ubicarse obligatoriamente arriba de la tabla.
   - Para tablas anchas o con descripciones extensas, usar `tabularx` con columnas auto-ajustables `L`, `C`, `R` o `X` para evitar desbordamientos del margen derecho (`\textwidth`).
   - Auditar tablas con `./compilar.sh --check-tablas` (o [scripts/verificar_tablas.py](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/scripts/verificar_tablas.py)).
   - Figuras en [imagenes/](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/imagenes/) e incluir con `\includegraphics{archivo.ext}` (ruta ya preconfigurada).

8. **Control de Silabación:**
   - División de palabras desactivada globalmente (`\hyphenpenalty=10000`, `\exhyphenpenalty=10000`).

9. **Compilación y Limpieza:**
   - Usar siempre el script ejecutable [compilar.sh](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/compilar.sh):
     * `./compilar.sh` (compilación completa de 4 pasos).
     * `./compilar.sh --clean` (compilación completa + eliminación de temporales).
     * `./compilar.sh --fast` (compilación rápida de 1 sola pasada pdflatex).
     * `./compilar.sh --only-clean` (limpieza de temporales sin compilar).
     * `./compilar.sh --check-tablas` (auditoría de tablas APA 7 y diagramación).

10. **Modalidad y Ensamble:**
    - Modalidad activa: **Innovación Tecnológica** (Capítulos 1 al 9).
    - Ensamble raíz en [main.tex](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/main.tex) vía `\input{capitulos/index.tex}`.
    - Metadatos institucionales y del estudiante centralizados en [estilos/configuracion.tex](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/estilos/configuracion.tex).
    - Ficha de datos del proyecto en [docs/ficha-proyecto.md](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/docs/ficha-proyecto.md) (alimentada desde `docs/proyecto.rtf` o `docs/proyecto.md` y consultas interactivas).
    - Preliminares: [agradecimiento.tex](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/preliminares/agradecimiento.tex) y [dedicatoria.tex](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/preliminares/dedicatoria.tex) comparten el mismo formato (`\vspace*{3cm}`, `\begin{raggedleft}` y `\textit{...}`).

11. **Prompts de Apoyo (`promts/`):**
    - Guiar la redacción con [promts/migracion/ficha-proyecto.md](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/promts/migracion/ficha-proyecto.md).
    - Revisar consistencia y rigor académico con la suite de 16 prompts modulares en [promts/revicion/](file:///home/juanvladimir13/Projects/proyecto-grado-innovacion/promts/revicion/) adaptada a los 9 capítulos de Innovación Tecnológica (BTH RM 0912/2023).

12. **Formato de Números, Decimales y Separador de Miles (Norma SI/ISO 80000-1):**
    - **Parte decimal:** Usar obligatoriamente punto (`.`) (ej. `12.50`, `3.1416`, `98.5%`, `0.75`). **PROHIBIDO** el uso de coma (`,`) en decimales.
    - **Separador de miles:** **PROHIBIDO** el uso de comas (`,`) o puntos (`.`) como separadores de millares (evitar `1,000` y `1.000`).
    - Cifras de 4 dígitos se escriben juntas sin separación (`1000`, `3500`, `4500.00`, `7700.00`).
    - Cifras de 5 o más dígitos se escriben continuas o con espacio (`25 000.00` o `25000.00`, `46 500.00`), nunca con comas ni puntos.
