# 🤖 AI Agent Guidelines & Project Definition (AGENTS.md)

Este archivo define la estructura, reglas y flujos de trabajo del proyecto para agentes de inteligencia artificial (como Antigravity, Cline, Cursor, Copilot, etc.). Si eres un agente de IA, lee estas instrucciones antes de modificar o crear archivos en este repositorio.

---

## 📋 Resumen del Proyecto

* **Nombre:** Proyecto de Grado BTH (LaTeX Modular)
* **Objetivo:** Plantilla modular y parametrizada en LaTeX para la redacción de proyectos de grado y tesis académicas.
* **Normativa:** Cumple con el Reglamento de Graduación del Bachillerato Técnico Humanístico (BTH) en Bolivia (Resolución Ministerial RM 0912/2023, ver [docs/REGLAMENTO_DE_GRADUACIN_DEL_BTH__RM_0912_2023.pdf](docs/REGLAMENTO_DE_GRADUACIN_DEL_BTH__RM_0912_2023.pdf)).
* **Modalidades Soportadas:**
  1. **Emprendimiento Productivo:** Directorio `emprendimiento-capitulos/` (Capítulos 1 al 7). (Activa por defecto en `main.tex`)
  2. **Innovación Tecnológica:** Directorio `innovacion-capitulos/` (Capítulos 1 al 9).

---

## 🛠️ Stack Tecnológico & Formato

* **Motor de Documento:** LaTeX (`report` class).
* **Motor Bibliográfico:** `biblatex` con estilo `apa` (APA 7ma Edición) y backend `biber`, con `csquotes` (`autostyle`).
* **Tipografía:** Arial (`helvet`) de tamaño `11pt` en cuerpo principal, y Courier (`courier`) para código fuente y texto monoespaciado.
* **Código Fuente y Programación:** Entorno `listings` con sintaxis coloreada, soporte UTF-8 (español), tipografía Courier y estilo predeterminado `estilocodigo`.
* **Tamaño de Hoja:** Carta (`letterpaper`).
* **Márgenes:** Izquierdo: 3.0 cm | Derecho, Superior e Inferior: 2.5 cm.
* **Interlineado:** 1.5 líneas (`\onehalfspacing`) en párrafos.
* **División de Palabras (Silabación):** Desactivada globalmente (`\hyphenpenalty=10000`, `\exhyphenpenalty=10000`).
* **Compilación:** Automatizada con el script ejecutable `./compilar.sh` en la raíz (utiliza `pdflatex` y `biber`).
* **Dependencias de Sistema (TeX Live en Linux/Debian/Ubuntu):**
  ```bash
  sudo apt-get install -y texlive-latex-base texlive-latex-recommended texlive-latex-extra \
                          texlive-bibtex-extra biber texlive-publishers texlive-lang-spanish
  ```

---

## 📁 Estructura del Directorio

```text
proyecto-grado/
├── main.tex                                # Entrada principal de compilación LaTeX
├── README.md                               # Guía del usuario para compilar y usar la plantilla
├── AGENTS.md                               # Instrucciones y reglas para Agentes de IA (este archivo)
├── ESTRUCTURA_CAPITULOS.md                 # Detalle temático de capítulos de ambas modalidades
├── compilar.sh                             # Script ejecutable de compilación (pdflatex + biber) y limpieza
├── estilos/
│   ├── estilos.sty                         # Estilos, carga de paquetes (biblatex-apa), títulos APA 7
│   └── configuracion.tex                   # Variables centralizadas de autor(es), título, tutor e institución
├── preliminares/                           # Hojas frontales (numeración romana)
│   ├── caratula.tex                        # Carátula oficial BTH (1 o 2 autores automáticos)
│   ├── portada_universitaria.tex           # Portada alternativa estilo académico/universitario
│   ├── agradecimiento.tex                  # Agradecimientos
│   ├── dedicatoria.tex                     # Dedicatorias
│   └── resumen.tex                         # Resúmenes (castellano, extranjero y originario)
├── emprendimiento-capitulos/               # Modalidad: Emprendimiento Productivo (Capítulos 1-7)
│   ├── index.tex                           # Ensamble de los 7 capítulos
│   ├── datos-proyecto.md                   # Ficha de recopilación de datos
│   ├── datos-prueba-desayunos.md           # Ficha con datos de prueba
│   ├── 01_introduccion/                    # Cap. 1: main.tex, contexto_oportunidad.tex, propuesta_valor.tex, marco_teorico.tex
│   ├── 02_planteamiento_emprendimiento/    # Cap. 2: main.tex, diagnostico.tex, objetivos.tex, justificacion.tex
│   ├── 03_desarrollo_emprendimiento/       # Cap. 3: main.tex, localizacion.tex, analisis_mercado.tex, estrategia_promocion.tex, etc.
│   ├── 04_viabilidad_sostenibilidad/       # Cap. 4: main.tex, calculo_inversiones.tex, costo_produccion.tex
│   ├── 05_resultados/                      # Cap. 5: main.tex
│   ├── 06_proyecto_vida/                   # Cap. 6: main.tex
│   └── 07_conclusiones_recomendaciones/    # Cap. 7: main.tex, conclusiones.tex, recomendaciones.tex
├── innovacion-capitulos/                   # Modalidad: Innovación Tecnológica (Capítulos 1-9)
│   ├── index.tex                           # Ensamble de los 9 capítulos
│   ├── datos-proyecto.md                   # Ficha de recopilación de datos
│   ├── datos-prueba-control-bovino.md      # Ficha con datos de prueba
│   ├── 01_introduccion/                    # Cap. 1: main.tex
│   ├── 02_planteamiento_problema/          # Cap. 2: main.tex, diagnostico.tex, objetivos.tex, justificacion.tex, etc.
│   ├── 03_marco_referencial/               # Cap. 3: main.tex, antecedentes.tex, bases_teoricas.tex, marco_conceptual.tex
│   ├── 04_desarrollo_innovacion/           # Cap. 4: main.tex, diseno.tex, planificacion.tex, recursos.tex, calculo_costos.tex
│   ├── 05_metodologia/                     # Cap. 5: main.tex, tipo_investigacion.tex, tecnicas_instrumentos.tex
│   ├── 06_estrategia_mejora/               # Cap. 6: main.tex
│   ├── 07_resultados/                      # Cap. 7: main.tex, beneficios_impacto.tex
│   ├── 08_proyecto_vida/                   # Cap. 8: main.tex
│   └── 09_conclusiones_recomendaciones/    # Cap. 9: main.tex, conclusiones.tex, recomendaciones.tex
├── tablas/                                 # Tablas independientes incluidas vía \input{}
│   ├── README.md                           # Guía para estructurar tablas APA 7 con booktabs
│   ├── tabla_ejemplo.tex                   # Plantilla base de tabla
│   ├── estudio_mercado_ejemplo.tex         # Tabla de análisis de mercado
│   ├── inversiones_ejemplo.tex             # Plan de inversión
│   ├── costos_produccion_ejemplo.tex       # Tabla de costos operativos de producción
│   ├── cronograma_ejemplo.tex              # Cronograma de actividades por fases
│   └── costos_ejemplo.tex                  # Resumen de estructura de costos
├── codigo/                                 # Código fuente y scripts (.py, .cpp, .ino, .sql, etc.)
│   ├── README.md                           # Guía para almacenar e importar código externo
│   └── ejemplo_controlador.py              # Script de prueba importable vía \lstinputlisting
├── imagenes/                               # Gráficos, diagramas y logotipos
│   └── README.md
├── bibliografia/                           # Bibliografía BibLaTeX (APA 7ma Edición)
│   └── referencias.bib                     # Base de datos de referencias (.bib) formateada en APA 7
├── anexos/                                 # Apéndices del documento
│   ├── README.md                           # Guía para añadir y estructurar anexos
│   ├── index.tex                           # Ensamble de anexos
│   ├── anexo_a_canvas.tex                  # Anexo A: Modelo Canvas
│   ├── anexo_b_fichas_tecnicas.tex         # Anexo B: Cotizaciones y fichas técnicas
│   └── anexo_c_codigo_fuente.tex           # Anexo C: Código fuente importado
└── docs/                                   # Regulaciones oficiales y guías
    ├── README.md                           # Guía de documentos oficiales
    ├── REGLAMENTO_DE_GRADUACIN_DEL_BTH__RM_0912_2023.pdf  # Reglamento Ministerial oficial
    └── datos-proyecto.md                   # Índice y guía general de recopilación de datos
```

---

## 🎯 Reglas Críticas para la IA

### 1. Modificaciones de Datos Personales o Institucionales
* **REGLA:** **NUNCA** quemes (hardcodees) nombres de estudiantes, tutores, instituciones o títulos del proyecto directamente en los archivos `.tex` como `caratula.tex`, `portada_universitaria.tex` o capítulos.
* **ACCIÓN:** Utiliza o actualiza las macros correspondientes en `estilos/configuracion.tex` (`\institucion`, `\modalidad`, `\especialidad`, `\autoruno`, `\autordos`, `\tutorproyecto`, etc.).

### 2. Estructuración Modular de Capítulos
* **REGLA:** Conserva el diseño modular. Cada capítulo reside en su propia carpeta dentro de `emprendimiento-capitulos/` o `innovacion-capitulos/` y contiene un archivo `main.tex` que ensambla las secciones individuales.
* **Rutas Internas:** Los archivos secundarios dentro de cada capítulo deben incluirse con el prefijo del directorio de su modalidad (ej. `\input{emprendimiento-capitulos/02_planteamiento_emprendimiento/diagnostico}`).

### 3. Estilos de Títulos y Alineación (Normas APA 7 Adaptadas)
* **Color:** Todos los títulos y enlaces internos (TOC, LOF, LOT, referencias cruzadas) deben mostrarse en **negro** (`linkcolor=black`).
* **Interlineado:** Aplicar interlineado sencillo (`1.0`) interno en títulos de Nivel 1 al 4 (`\setstretch{1.0}`) para evitar separaciones excesivas cuando ocupan más de una línea.
* **Nivel 1 (`\chapter`):** Debe alinearse a la **izquierda**, no debe contener el prefijo de palabra "Capítulo" (ej. `1. INTRODUCCIÓN`), y debe usar un espaciado anterior negativo de `-15pt` en `titlesec` para elevar la posición inicial de inicio de hoja.
* **Otros Niveles:**
  - Nivel 2 (`\section`): Alineado izquierda, Negrita.
  - Nivel 3 (`\subsection`): Alineado izquierda, Negrita y Cursiva.
  - Nivel 4 (`\subsubsection`): Sangría de 1.27 cm, Negrita, tipo *run-in* terminando con punto.
  - Nivel 5 (`\paragraph`): Sangría de 1.27 cm, Negrita y Cursiva, tipo *run-in* terminando con punto.

### 4. Encabezados y Pies de Página
* **Encabezados:** Están totalmente deshabilitados. No debe mostrarse texto de cabecera superior ni línea horizontal separadora (`headrulewidth=0pt`).
* **Pies de Página:** La numeración de páginas debe mostrarse centrada en la parte inferior de las hojas que lo requieran (Capítulos 1 al 7 u 1 al 9).

### 5. Secciones Finales, Citas y Bibliografía (APA 7ma Edición)
* **Motor:** Se utiliza `biblatex` con `style=apa` y backend `biber`.
* **Citas en el Texto:**
  - Cita parentética (entre paréntesis): `\parencite{clave}` produce *(Apellido, Año)*.
  - Cita narrativa (en el flujo del texto): `\textcite{clave}` produce *Apellido (Año)*.
  - Citas múltiples: `\parencite{clave1, clave2}`.
* **Inclusión de la Lista de Referencias:** Se imprime en `main.tex` mediante `\printbibliography[heading=bibintoc, title={Bibliografía}]`.
* **Numeración de Capítulos:** La bibliografía y los anexos deben ser no numerados (`numberless` en `titlesec`) para evitar prefijos decimales o de capítulo.
* **Numeración de Página:** Toda la sección de Bibliografía y Anexos debe estar totalmente limpia de números de página y cabeceras (`\pagestyle{empty}` y `\assignpagestyle{\chapter}{empty}`).

### 6. Inserción de Tablas e Imágenes
* **Tablas:** Guardar en `tablas/` e importar vía `\input{tablas/archivo.tex}`. Usar `booktabs` y `array`.
* **Imágenes:** Guardar en `imagenes/` e incluirlas sin prefijo de ruta (ya configurado en `estilos.sty`).

### 7. Inserción de Código Fuente y Algoritmos
* **Motor:** Se utiliza el paquete `listings` con el estilo `estilocodigo` predeterminado y tipografía Courier.
* **Rótulo:** Configurado en español como `Código` (ej. `Código 1: ...`).
* **Ajuste de Línea (Wordwrap):** Activado automáticamente (`breaklines=true`, `breakautoindent=true`) con sangría de continuación (`breakindent=1.5em`) para líneas que superan el margen.
* **Archivos Externos en `codigo/`:** Guardar los programas y scripts en `codigo/` e importarlos modularmente con `\lstinputlisting[language=Python, caption={...}, label={lst:...}]{codigo/archivo.py}`.
* **Bloques Embebidos:** Usar `\begin{lstlisting}[language=Python, caption={...}, label={lst:...}]` indicando el lenguaje apropiado (ej. `Python`, `C`, `C++`, `Java`, `SQL`, `bash`, `HTML`).
* **Código en Línea:** Usar `\lstinline|codigo|` o `\texttt{codigo}`.

### 8. Compilación y Limpieza
* **REGLA:** Utilizar exclusivamente el script ejecutable `./compilar.sh` en lugar de comandos manuales aislados:
  - `./compilar.sh` (compila PDF completo ejecutando `pdflatex` + `biber` + 2x `pdflatex` y conserva temporales).
  - `./compilar.sh --clean` (compila PDF completo y elimina archivos temporales).
  - `./compilar.sh --only-clean` (elimina archivos temporales sin compilar).
  - `./compilar.sh --fast` (compilación rápida de 1 sola pasada pdflatex para redacción continua).

---

## 🔄 Procedimiento para Cambiar de Modalidad

El documento soporta nativamente ambas modalidades mediante inclusión condicional en `main.tex`.
Si el usuario solicita cambiar de modalidad (ej. de Emprendimiento a Innovación):
1. Abre el archivo `main.tex` en la raíz del proyecto.
2. Localiza la sección `=== SELECCIÓN DE MODALIDAD ===`.
3. Comenta la instrucción de inclusión de la modalidad inactiva (ej. `% \input{emprendimiento-capitulos/index.tex}`).
4. Descomenta la instrucción de la modalidad solicitada (ej. `\input{innovacion-capitulos/index.tex}`).
5. Asegúrate de actualizar las macros institucionales en `estilos/configuracion.tex` (`\modalidad`, `\tituloproyecto`, `\especialidad`, etc.).
6. Compila el proyecto con `./compilar.sh`.

---

## 🚫 Archivos Ignorados por Agentes de IA

Para evitar el consumo innecesario de contexto y tokens, los agentes de IA deben ignorar por completo todos los archivos auxiliares generados durante la compilación de LaTeX y los archivos de estado temporal de herramientas de IA.

Estos archivos se han excluido formalmente en los siguientes archivos de configuración del repositorio:
* `.gitignore`: Evita que archivos temporales entren al control de versiones.
* `.cursorignore`: Previene que Cursor indexe archivos compilados y PDFs en su base de conocimiento.
* `.clineignore`: Previene la lectura innecesaria de archivos binarios por Cline.
* `.agentignore`: Regulación neutral para otros motores de IA.

### Lista de Patrones Excluidos:
1. **Temporales de LaTeX:** `*.aux`, `*.log`, `*.toc`, `*.lof`, `*.lot`, `*.out`, `*.bbl`, `*.blg`, `*.fdb_latexmk`, `*.fls`, `*.synctex.gz`, `*.upa`, `*.upb`, `*.listing` (incluyendo directorios recursivos).
2. **Archivos de Salida Binaria:** `*.pdf`, `main.pdf` (excepto `docs/*.pdf` regulatorios).
3. **Directorios de Agentes/IDEs:** `.antigravitycli/`, `.cline/`, `.cursor/`, `.vscode/`, `.idea/`.
