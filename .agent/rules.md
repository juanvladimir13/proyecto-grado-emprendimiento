# Antigravity Rules & Guidelines

Este proyecto de LaTeX modular sigue pautas estrictas para mantener la consistencia, modularidad y cumplimiento de la normativa del Bachillerato Técnico Humanístico (BTH - RM 0912/2023) en Bolivia.

> [!IMPORTANT]
> Consulta siempre la especificación principal en [AGENTS.md](file:///home/juanvladimir13/Projects/proyecto-grado/AGENTS.md) y la estructura de capítulos en [ESTRUCTURA_CAPITULOS.md](file:///home/juanvladimir13/Projects/proyecto-grado/ESTRUCTURA_CAPITULOS.md) antes de crear o modificar archivos.

---

## 🎯 Resumen de Reglas Críticas para Antigravity

1. **Variables Centralizadas:**
   - **NUNCA** quemes nombres de autores, tutores, institución, especialidad o título en archivos `.tex` (`caratula.tex`, `portada_universitaria.tex` o capítulos).
   - Toda modificación de metadatos se realiza en [estilos/configuracion.tex](file:///home/juanvladimir13/Projects/proyecto-grado/estilos/configuracion.tex). Soporta 1 o 2 autores dinámicamente (`\autoruno`, `\autordos`).

2. **Estilo de Títulos APA 7ma Edición Adaptado:**
   - Todos los títulos y enlaces internos (TOC, LOF, LOT, referencias) en **negro** (`linkcolor=black`).
   - Interlineado sencillo (`1.0` / `\setstretch{1.0}`) para títulos de Nivel 1 al 4.
   - Nivel 1 (`\chapter`): Alineado a la **izquierda**, sin prefijo de palabra "Capítulo" (ej. `1. INTRODUCCIÓN`), con espaciado anterior a `-15pt` en `titlesec`.
   - Nivel 2 (`\section`): Alineado a la izquierda, Negrita.
   - Nivel 3 (`\subsection`): Alineado a la izquierda, Negrita y Cursiva.
   - Nivel 4 (`\subsubsection`): Sangría de 1.27 cm, Negrita, tipo *run-in* terminando con punto.
   - Nivel 5 (`\paragraph`): Sangría de 1.27 cm, Negrita y Cursiva, tipo *run-in* terminando con punto.

3. **Encabezados y Pies de Página:**
   - Encabezados deshabilitados (`headrulewidth=0pt`, sin texto superior).
   - Pies de página: numeración arábiga centrada abajo (`\cfoot{\thepage}`).
   - Páginas preliminares en números romanos (`\pagenumbering{roman}`).
   - Bibliografía y Anexos: no numerados (`numberless`) y limpios de numeración de página y cabeceras (`\pagestyle{empty}`, `\assignpagestyle{\chapter}{empty}`).

4. **Bibliografía (BibLaTeX + Biber):**
   - Motor `biblatex` con `style=apa` y backend `biber` sobre [bibliografia/referencias.bib](file:///home/juanvladimir13/Projects/proyecto-grado/bibliografia/referencias.bib).
   - En texto: `\parencite{clave}` para citas parentéticas *(Apellido, Año)* y `\textcite{clave}` para narrativas *Apellido (Año)*.
   - Inclusión en `main.tex`: `\printbibliography[heading=bibintoc, title={Bibliografía}]`.

5. **Código Fuente y Algoritmos:**
   - Motor `listings` con estilo `estilocodigo` predeterminado y tipografía Courier (`courier`).
   - Guardar scripts en [codigo/](file:///home/juanvladimir13/Projects/proyecto-grado/codigo/) e importar con:
     `\lstinputlisting[language=Python, caption={...}, label={lst:...}]{codigo/archivo.py}`
   - Ajuste automático de línea (`breaklines=true`) y rótulos en español (`Código`).

6. **Tablas e Ilustraciones:**
   - Tablas independientes en [tablas/](file:///home/juanvladimir13/Projects/proyecto-grado/tablas/) e importar vía `\input{tablas/archivo.tex}` usando `booktabs`.
   - Figuras en [imagenes/](file:///home/juanvladimir13/Projects/proyecto-grado/imagenes/) e incluir con `\includegraphics{archivo.ext}` (ruta ya preconfigurada).

7. **Control de Silabación:**
   - División de palabras desactivada globalmente (`\hyphenpenalty=10000`, `\exhyphenpenalty=10000`).

8. **Compilación y Limpieza:**
   - Usar siempre el script ejecutable [compilar.sh](file:///home/juanvladimir13/Projects/proyecto-grado/compilar.sh):
     * `./compilar.sh` (compilación completa de 4 pasos).
     * `./compilar.sh --clean` (compilación completa + eliminación de temporales).
     * `./compilar.sh --fast` (compilación rápida de 1 sola pasada pdflatex).
     * `./compilar.sh --only-clean` (limpieza de temporales sin compilar).

9. **Cambio de Modalidad:**
   - Cambiar la inclusión condicional en [main.tex](file:///home/juanvladimir13/Projects/proyecto-grado/main.tex) entre `emprendimiento-capitulos/index.tex` e `innovacion-capitulos/index.tex`.
   - Actualizar `\modalidad`, `\tituloproyecto` y `\especialidad` en [estilos/configuracion.tex](file:///home/juanvladimir13/Projects/proyecto-grado/estilos/configuracion.tex).

10. **Idioma y Estilo:**
    - Documento y comentarios redactados en español (exceptuando resumen en inglés/lengua originaria).
