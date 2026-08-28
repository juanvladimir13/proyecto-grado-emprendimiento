# 🤖 AI Agent Guidelines & Project Definition (AGENTS.md)

Este archivo define la estructura, reglas y flujos de trabajo del proyecto para agentes de inteligencia artificial (como Antigravity, Cline, Cursor, Copilot, etc.). Si eres un agente de IA, lee estas instrucciones antes de modificar o crear archivos en este repositorio.

---

### 📋 Resumen del Proyecto

* **Nombre:** Proyecto de Grado BTH - Emprendimiento Productivo (LaTeX Modular)
* **Objetivo:** Plantilla modular y parametrizada en LaTeX para la redacción de proyectos de grado y planes de negocio bajo la modalidad de Emprendimiento Productivo.
* **Normativa:** Cumple con el Reglamento de Graduación del Bachillerato Técnico Humanístico (BTH) en Bolivia (Resolución Ministerial RM 0912/2023, Anexo 1, inciso A; ver [docs/REGLAMENTO_BTH__RM_0912_2023.pdf](docs/REGLAMENTO_BTH__RM_0912_2023.pdf)).
* **Modalidad Implementada:** **Emprendimiento Productivo** estructurada en 7 capítulos dentro del directorio `capitulos/`.

---

## 🛠️ Stack Tecnológico & Formato

* **Motor de Documento:** LaTeX (`report` class).
* **Motor Bibliográfico:** `biblatex` con estilo `apa` (APA 7ma Edición) y backend `biber`, con `csquotes` (`autostyle`).
* **Tipografía:** Arial (`helvet`) de tamaño `11pt` en cuerpo principal, y Courier (`courier`) para código fuente y texto monoespaciado.
* **Código Fuente y Programación:** Entorno `listings` con sintaxis coloreada, soporte UTF-8 (español), tipografía Courier y estilo predeterminado `estilocodigo`.
* **Tamaño de Hoja:** Carta (`letterpaper`).
* **Márgenes:** Izquierdo: 3.0 cm | Derecho, Superior e Inferior: 2.5 cm.
* **Interlineado:** 1.5 líneas (`\onehalfspacing`) en párrafos.
* **Espaciado entre Párrafos (Estilo Microsoft Word):** Espaciado posterior configurable (`\espacioposteriorparrafo`, por defecto `8pt`) y sangría de primera línea (`\sangriaprimeralinea`, por defecto `0pt`) centralizados en `estilos/configuracion.tex` y aplicados con el paquete `parskip`.
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
proyecto-grado-emprendimiento/
├── main.tex                                # Entrada principal de compilación LaTeX (\input{capitulos/index.tex})
├── README.md                               # Guía del usuario para compilar y usar la plantilla
├── AGENTS.md                               # Instrucciones y reglas para Agentes de IA (este archivo)
├── ESTRUCTURA_CAPITULOS.md                 # Detalle temático de los 7 capítulos de Emprendimiento Productivo
├── compilar.sh                             # Script ejecutable de compilación (pdflatex + biber) y limpieza
├── estilos/
│   ├── estilos.sty                         # Estilos, carga de paquetes (biblatex-apa, listings), títulos APA 7
│   └── configuracion.tex                   # Variables centralizadas de autor(es), título, tutor, institución y modalidad
├── preliminares/                           # Hojas frontales (numeración romana)
│   ├── caratula.tex                        # Carátula oficial BTH (\titulocaratula, \subtitulocaratula)
│   ├── portada_universitaria.tex           # Portada alternativa estilo académico/universitario
│   ├── agradecimiento.tex                  # Agradecimientos (\capitulopreliminar y \begin{estilodedicatoria})
│   ├── dedicatoria.tex                     # Dedicatorias (\capitulopreliminar y \begin{estilodedicatoria})
│   └── resumen.tex                         # Resúmenes (\capitulopreliminar, \palabrasclave, \keywords, \simikuna)
├── capitulos/                              # Modalidad: Emprendimiento Productivo (Capítulos 1 al 7)
│   ├── index.tex                           # Ensamble de los 7 capítulos
│   ├── 01_introduccion/                    # Cap. 1: main.tex, contexto_general.tex, oportunidad_negocio.tex, propuesta_valor.tex, marco_teorico.tex
│   ├── 02_planteamiento_emprendimiento/    # Cap. 2: main.tex, diagnostico.tex, objetivos.tex, justificacion.tex
│   ├── 03_desarrollo_emprendimiento/       # Cap. 3: main.tex, localizacion.tex, analisis_mercado.tex, estrategia_promocion.tex, estructura_organizacional.tex, diseno_producto.tex, ciclo_produccion.tex
│   ├── 04_viabilidad_sostenibilidad/       # Cap. 4: main.tex, calculo_inversiones.tex, costo_produccion.tex
│   ├── 05_resultados/                      # Cap. 5: main.tex, resultados_cuantitativos.tex, resultados_cualitativos.tex, indicadores_validados.tex
│   ├── 06_proyecto_vida/                   # Cap. 6: main.tex (aspiraciones académicas, competencias empresariales, compromiso ético)
│   └── 07_conclusiones_recomendaciones/    # Cap. 7: main.tex, conclusiones.tex, recomendaciones.tex
├── tablas/                                 # Tablas independientes incluidas vía \input{}
│   ├── README.md                           # Guía para estructurar tablas APA 7 con booktabs
│   ├── tabla_ejemplo.tex                   # Plantilla base de tabla
│   ├── estudio_mercado_ejemplo.tex         # Tabla de análisis de mercado (Cap. 3)
│   ├── estructura_organizacional_ejemplo.tex # Matriz de estructura organizacional, cargos y remuneraciones (Cap. 3)
│   ├── inversiones_ejemplo.tex             # Plan de inversión fija y capital de operación (Cap. 4)
│   ├── costos_produccion_ejemplo.tex       # Tabla de costos operativos de producción variables y fijos (Cap. 4)
│   ├── indicadores_financieros_ejemplo.tex # Resumen de indicadores financieros y punto de equilibrio (Cap. 4)
│   └── resultados_piloto_ejemplo.tex       # Resultados obtenidos en prueba piloto vs metas (Cap. 5)
├── codigo/                                 # Código fuente y scripts (.py, .cpp, .ino, .sql, etc.)
│   ├── README.md                           # Guía para almacenar e importar código externo
│   └── ejemplo_controlador.py              # Script de prueba importable vía \lstinputlisting
├── scripts/                                # Scripts de utilidad y validación de calidad
│   └── verificar_tablas.py                 # Auditoría de tablas APA 7 y prevención de desbordamientos
├── imagenes/                               # Gráficos, diagramas y logotipos
│   └── README.md                           # Instrucciones para la gestión de recursos gráficos
├── bibliografia/                           # Bibliografía BibLaTeX (APA 7ma Edición)
│   └── referencias.bib                     # Base de datos de referencias (.bib) formateada en APA 7
├── anexos/                                 # Apéndices del documento
│   ├── README.md                           # Guía para añadir y estructurar anexos
│   ├── index.tex                           # Ensamble de anexos con \capitulopreliminar{ANEXOS}
│   ├── anexo_a_canvas.tex                  # Anexo A: Modelo Canvas (\seccionanexo)
│   ├── anexo_b_fichas_tecnicas.tex         # Anexo B: Cotizaciones y fichas técnicas (\seccionanexo)
│   └── anexo_c_codigo_fuente.tex           # Anexo C: Código fuente importado (\seccionanexo)
├── promts/                                 # Prompts de apoyo y guías de revisión para agentes de IA
│   ├── migracion/                          # Prompts para migración de datos y llenado de fichas
│   │   └── ficha-proyecto.md               # Flujo paso a paso para completar ficha y redactar los 7 capítulos
│   └── revicion/                           # Flujo de revisión por etapas y análisis global (7 capítulos)
│       ├── 00_README_flujo_revision.md     # Guía del flujo de revisión por etapas
│       ├── 00_analisis-capitulos-tesis.md  # Prompt de análisis integral de coherencia y rigor comercial
│       ├── 01_revision_estructura_general.md # Estructura general de 7 capítulos BTH RM 0912/2023
│       ├── 01b_revision_introduccion.md    # Cap. 1: Contexto general, oportunidad de negocio, propuesta de valor, marco teórico
│       ├── 02_revision_planteamiento_emprendimiento.md # Cap. 2: Diagnóstico, objetivos, justificación
│       ├── 03_revision_desarrollo_emprendimiento.md    # Cap. 3: Localización, mercado, promoción, organización, producto, ciclo
│       ├── 04_revision_viabilidad_sostenibilidad.md   # Cap. 4: Inversiones, costos fijos/variables, rentabilidad y punto de equilibrio
│       ├── 05_revision_resultados.md                  # Cap. 5: Resultados cuantitativos, cualitativos e indicadores validados
│       ├── 06_revision_proyecto_vida.md               # Cap. 6: Aspiraciones, competencias empresariales, independencia económica
│       ├── 07_revision_conclusiones_recomendaciones.md # Cap. 7: Cierre de objetivos, conclusiones y recomendaciones
│       ├── 08_revision_coherencia_sincronia_global.md # Sincronía integral entre los 7 capítulos
│       ├── 09_revision_redaccion_estilo_academico.md  # Registro formal impersonal y estilo APA 7
│       ├── 10_revision_citas_bibliografia.md          # Normalización BibLaTeX APA 7ma Edición
│       └── 11_checklist_pre_entrega_final.md          # Checklist institucional BTH pre-defensa
└── docs/                                   # Regulaciones oficiales y guías
    ├── REGLAMENTO_BTH__RM_0912_2023.pdf    # Reglamento Ministerial oficial RM 0912/2023
    └── ficha-proyecto.md                   # Ficha de datos y requerimientos del proyecto
```

---

## 🎯 Reglas Críticas para la IA

### 1. Modificaciones de Datos Personales o Institucionales
* **REGLA:** **NUNCA** quemes (hardcodees) nombres de estudiantes, tutores, instituciones o títulos del proyecto directamente en los archivos `.tex` como `caratula.tex`, `portada_universitaria.tex` o capítulos.
* **ACCIÓN:** Utiliza o actualiza las macros correspondientes en `estilos/configuracion.tex` (`\institucion`, `\modalidad`, `\especialidad`, `\autoruno`, `\autordos`, `\tutorproyecto`, `\espacioposteriorparrafo`, `\sangriaprimeralinea`, `\espaciosuperiordedicatoria`, etc.).
* **Campos C.I.:** El número de C.I. del estudiante no forma parte de la plantilla y fue removido de las macros y de la carátula oficial.

### 2. Estructuración Modular de Capítulos
* **REGLA:** Conserva el diseño modular. Cada capítulo reside en su propia carpeta dentro de `capitulos/` y contiene un archivo `main.tex` que ensambla las secciones individuales.
* **Rutas Internas:** Los archivos secundarios dentro de cada capítulo deben incluirse con el prefijo `capitulos/` (ej. `\input{capitulos/02_planteamiento_emprendimiento/diagnostico}`).

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
* **Pies de Página:** La numeración de páginas debe mostrarse centrada en la parte inferior de las hojas que lo requieran (Capítulos 1 al 7).

### 5. Secciones Finales, Citas y Bibliografía (APA 7ma Edición)
* **Motor:** Se utiliza `biblatex` con `style=apa` y backend `biber`.
* **Citas en el Texto:**
  - Cita parentética (entre paréntesis): `\parencite{clave}` produce *(Apellido, Año)*.
  - Cita narrativa (en el flujo del texto): `\textcite{clave}` produce *Apellido (Año)*.
  - Citas múltiples: `\parencite{clave1, clave2}`.
* **Inclusión de la Lista de Referencias:** Se imprime en `main.tex` mediante `\printbibliography[heading=bibintoc, title={Bibliografía}]`.
* **Numeración de Capítulos:** La bibliografía y los anexos deben ser no numerados (`numberless` en `titlesec`) para evitar prefijos decimales o de capítulo.
* **Numeración de Página:** Toda la sección de Bibliografía y Anexos debe estar totalmente limpia de números de página y cabeceras mediante la macro global `\configurarseccionfinal` (`\pagestyle{empty}` y `\assignpagestyle{\chapter}{empty}`).
* **Estructura de Anexos:** Cada anexo individual debe declararse mediante `\seccionanexo{Título del Anexo}` para registrarse automáticamente en la tabla de contenidos sin numeración. El ensamble general en `anexos/index.tex` usa `\capitulopreliminar{ANEXOS}`.

### 6. Inserción y Verificación de Tablas e Imágenes
* **Tablas (Normas APA 7ma Edición):** Guardar en `tablas/` e importar vía `\input{tablas/archivo.tex}`.
  - Usar siempre `booktabs` (`\toprule`, `\midrule`, `\bottomrule`). **PROHIBIDO** el uso de líneas verticales (`|`) y de `\hline`.
  - El título `\caption{...}` debe ubicarse obligatoriamente **arriba** de la tabla, seguido de `\label{tab:...}` y `\centering`.
  - Para notas explicativas o fuentes al pie de la tabla, usar obligatoriamente la macro semántica `\notatabla{Fuente: ...}` (aplica tamaño pequeño, cursiva e interlineado ajustado según APA 7).
  - Para tablas con descripciones extensas, usar el entorno `tabularx` con ancho `\textwidth` y columnas auto-ajustables `L`, `C`, `R` o `X` (definidas en `estilos.sty`) para evitar desbordamientos del margen derecho.
  - **Auditoría de Tablas:** Ejecutar `./compilar.sh --check-tablas` (o `python3 scripts/verificar_tablas.py`) para validar que ninguna tabla rompa la diagramación ni viole APA 7.
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
  - `./compilar.sh --check-tablas` (audita la conformidad de tablas con APA 7 y booktabs).

### 9. Estructura y Flujo de la Modalidad Emprendimiento Productivo
Este proyecto está configurado para la modalidad de **Emprendimiento Productivo**:
* La inclusión principal en `main.tex` carga directamente `capitulos/index.tex`.
* Los 7 capítulos se ensamblan desde `capitulos/index.tex` conectando cada carpeta de capítulo (`capitulos/01_introduccion/` a `capitulos/07_conclusiones_recomendaciones/`).
* Para alimentar el contenido con datos de un proyecto real, se completa la ficha `docs/ficha-proyecto.md` a partir del documento base `docs/proyecto.rtf` o `docs/proyecto.md`, consultando de manera interactiva los datos pendientes al usuario.
* Los metadatos institucionales y del estudiante deben ajustarse en `estilos/configuracion.tex`.

### 10. Uso de Prompts de Apoyo para Agentes (`promts/`)
* **Migración y redacción:** Consultar `promts/migracion/ficha-proyecto.md` para el flujo ordenado de ingesta de datos a la ficha y posterior redacción capítulo a capítulo.
* **Revisión y calidad:** Utilizar la suite especializada de 14 prompts en `promts/revicion/` adaptada a los 7 capítulos de Emprendimiento Productivo (BTH RM 0912/2023): estructura general (`01`), capítulo 1 (`01b`), capítulos 2 al 7 modulares (`02` a `07`), auditoría de sincronía global (`08`), estilo y gramática (`09`), citas y bibliografía APA 7 (`10`), y checklist pre-entrega/defensa (`11`).

### 11. Formato de Números, Decimales y Separador de Miles (Norma SI/ISO 80000-1)
* **REGLA:** En todo el proyecto (capítulos, tablas y anexos) se sigue la convención internacional técnica y de la RAE:
  - **Parte decimal:** Usar obligatoriamente **punto (`.`)** (ej. `12.50`, `3.1416`, `98.5%`, `0.75 Bs.`). **PROHIBIDO** el uso de coma (`,`) para decimales (ej. evitar `12,50`).
  - **Separador de miles:** **PROHIBIDO** el uso de comas (`,`) o puntos (`.`) como separadores de millares (ej. evitar `1,000` y `1.000`).
  - **Cifras de 4 dígitos:** Escribir juntas sin espacio ni separador (ej. `1000`, `3500`, `4500.00`, `7700.00`).
  - **Cifras de 5 o más dígitos:** Escribir continuas o con espacio como separador de grupos de tres dígitos (ej. `25000.00` o `25 000.00`, `46 500.00`), nunca con comas ni puntos.

### 12. Listas y Elementos de Enumeración (Prioridad de Viñetas)
* **REGLA:** Priorizar obligatoriamente el uso de viñetas (`\begin{itemize}`) en lugar de listas numeradas (`\begin{enumerate}`).
* **Criterio de Uso:**
  - Emplear siempre el entorno `itemize` para listas de objetivos específicos, conclusiones, recomendaciones, características técnicas, componentes, ventajas, requerimientos y elementos descriptivos generales.
  - Reservar el entorno de lista numerada (`enumerate`) **exclusivamente** para secuencias algorítmicas estrictas, pasos procedimentales ordenados o cronologías donde la numeración correlativa sea indispensable e inherente a la explicación técnica.

### 13. Macros Semánticas Estandarizadas de la Plantilla
* **REGLA:** Utilizar obligatoriamente las macros semánticas provistas en `estilos.sty` para preservar la coherencia y mantenibilidad del documento:
  - `\capitulopreliminar{Título}`: Capítulos preliminares no numerados con entrada automática al TOC (`Agradecimiento`, `Dedicatoria`, `Resumen`, `ANEXOS`), en sustitución de `\chapter*{...}\addcontentsline{...}` manual.
  - `\begin{estilodedicatoria}...\end{estilodedicatoria}`: Entorno semántico para dedicatoria y agradecimiento (alineación derecha, cursiva y espaciado vertical configurable vía `\espaciosuperiordedicatoria` en `estilos/configuracion.tex`).
  - `\seccionanexo{Título}`: Encabezados de secciones de anexos con inclusión automática en el TOC (`\seccionanexo{Anexo A: Modelo Canvas...}`).
  - `\configurarseccionfinal`: Macro global que desactiva numeración de página y cabeceras (`empty`) para Bibliografía y Anexos.
  - `\palabrasclave{...}`, `\keywords{...}`, `\simikuna{...}`: Bloques semánticos normalizados para palabras clave en resúmenes (castellano, extranjero y lengua originaria).
  - `\notatabla{...}`: Formato estandarizado para notas y fuentes al pie de tablas e ilustraciones bajo APA 7ma Edición.
  - `\titulocaratula{...}` y `\subtitulocaratula{...}`: Formato tipográfico y paleta institucional en la portada oficial.

---

## 🚫 Archivos Ignorados por Agentes de IA

Para evitar el consumo innecesario de contexto y tokens, los agentes de IA deben ignorar por completo todos los archivos auxiliares generados durante la compilación de LaTeX y los archivos de estado temporal de herramientas de IA.

Estos archivos se han excluido formalmente en los siguientes archivos de configuración del repositorio:
* `.gitignore`: Evita que archivos temporales entren al control de versiones.
* `.cursorignore`: Previene que Cursor indexe archivos compilados y PDFs en su base de conocimiento.
* `.clineignore`: Previene la lectura innecesaria de archivos binarios por Cline.
* `.agentignore`: Regulación neutral para otros motores de IA.

### Lista de Patrones Excluidos:
1. **Temporales de LaTeX:** `*.aux`, `*.log`, `*.toc`, `*.lof`, `*.lot`, `*.out`, `*.bbl`, `*.blg`, `*.run.xml`, `*.bcf`, `*.fdb_latexmk`, `*.fls`, `*.synctex.gz`, `*.upa`, `*.upb`, `*.listing`, `*-blx.bib` (incluyendo `capitulos/**/*.aux`, `preliminares/**/*.aux`, `tablas/**/*.aux`, etc.).
2. **Archivos de Salida Binaria:** `*.pdf`, `main.pdf` (excepto `docs/*.pdf` regulatorios).
3. **Directorios de Agentes/IDEs:** `.antigravitycli/`, `.cline/`, `.cursor/`, `.vscode/`, `.idea/`.
