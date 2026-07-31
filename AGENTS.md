# 🤖 AI Agent Guidelines & Project Definition (AGENTS.md)

Este archivo define la estructura, reglas y flujos de trabajo del proyecto para agentes de inteligencia artificial (como Antigravity, Cline, Cursor, Copilot, etc.). Si eres un agente de IA, lee estas instrucciones antes de modificar o crear archivos en este repositorio.

---

## 📋 Resumen del Proyecto

* **Nombre:** Proyecto de Grado BTH (LaTeX Modular)
* **Objetivo:** Plantilla modular y parametrizada en LaTeX para la redacción de proyectos de grado y tesis académicos.
* **Normativa:** Cumple con el Reglamento de Graduación del Bachillerato Técnico Humanístico (BTH) en Bolivia (Resolución Ministerial RM 0912/2023, ver [docs/REGLAMENTO_DE_GRADUACIN_DEL_BTH__RM_0912_2023.pdf](docs/REGLAMENTO_DE_GRADUACIN_DEL_BTH__RM_0912_2023.pdf)).
* **Modalidades Soportadas:**
  1. **Emprendimiento Productivo:** Directorio `emprendimiento-capitulos/`. (Activa por defecto en `main.tex`)
  2. **Innovación Tecnológica:** Directorio `innovacion-capitulos/`.

---

## 🛠️ Stack Tecnológico & Formato

* **Motor de Documento:** LaTeX (`report` class).
* **Tipografía:** Arial (`helvet`), tamaño de fuente `11pt` en cuerpo principal.
* **Tamaño de Hoja:** Carta (`letterpaper`).
* **Márgenes:** Izquierdo: 3.0 cm | Derecho, Superior e Inferior: 2.5 cm.
* **Interlineado:** 1.5 líneas (`\onehalfspacing`) en párrafos.
* **Compilación:** Automatizada con el script ejecutable `./compilar.sh` en el raíz.

---

## 📁 Estructura del Directorio

```text
proyecto-grado/
├── main.tex                                # Entrada principal de compilación LaTeX
├── README.md                               # Guía del usuario para compilar y usar la plantilla
├── AGENTS.md                               # Instrucciones y reglas para Agentes de IA (este archivo)
├── compilar.sh                             # Script ejecutable de compilación y limpieza LaTeX
├── estilos/
│   ├── estilos.sty                         # Estilos, carga de paquetes y personalización de títulos
│   └── configuracion.tex                   # Variables de autor, título, tutor y universidad
├── preliminares/                           # Hojas frontales (numeración romana)
│   ├── caratula.tex                        # Portada dinámica (usa variables de configuracion.tex)
│   ├── agradecimiento.tex                  # Agradecimientos
│   ├── dedicatoria.tex                     # Dedicatorias
│   └── resumen.tex                         # Resúmenes (castellano, extranjero y originario)
├── emprendimiento-capitulos/               # Modalidad: Emprendimiento Productivo (Capítulos 1-7)
│   ├── index.tex                           # Ensamble de los 7 capítulos
│   ├── datos-proyecto.md                   # Ficha de recopilación de datos
│   ├── 01_introduccion/
│   ├── ...
│   └── 07_conclusiones_recomendaciones/
├── innovacion-capitulos/                   # Modalidad: Innovación Tecnológica (Capítulos 1-9)
│   ├── index.tex                           # Ensamble de los 9 capítulos
│   ├── datos-proyecto.md                   # Ficha de recopilación de datos
│   ├── 01_introduccion/
│   ├── ...
│   └── 09_conclusiones_recomendaciones/
├── tablas/                                 # Tablas independientes incluidas vía \input{}
│   ├── tabla_ejemplo.tex                   # Plantilla base de tabla
│   ├── estudio_mercado_ejemplo.tex         # Tabla de análisis de mercado
│   ├── inversiones_ejemplo.tex             # Plan de inversión
│   └── costos_produccion_ejemplo.tex       # Tabla de costos operativos
├── imagenes/                               # Gráficos, diagramas y logotipos
│   └── README.md
├── bibliografia/                           # Bibliografía BibTeX
│   └── referencias.bib                     # Base de datos de referencias (.bib)
├── anexos/                                 # Apéndices del documento
│   └── anexo_a.tex                         # Contenido de los anexos
└── docs/                                   # Regulaciones oficiales y documentos
    ├── REGLAMENTO_DE_GRADUACIN_DEL_BTH__RM_0912_2023.pdf  # Reglamento Ministerial
    └── datos-proyecto.md                   # Plantilla base de datos (opcional)
```

---

## 🎯 Reglas Críticas para la IA

### 1. Modificaciones de Datos Personales o Institucionales
* **REGLA:** **NUNCA** quemes (hardcodees) nombres de estudiantes, tutores, instituciones o títulos del proyecto directamente en los archivos `.tex` como `caratula.tex`, `portada.tex` o capítulos.
* **ACCIÓN:** Utiliza o actualiza las macros correspondientes en `estilos/configuracion.tex`.

### 2. Estructuración de Capítulos
* **REGLA:** Conserva el diseño modular. Cada capítulo debe residir en su propia carpeta dentro de `emprendimiento-capitulos/` o `innovacion-capitulos/` y contener un archivo `main.tex`. Los capítulos se incluyen mediante el archivo `index.tex` en la raíz de su respectiva carpeta.

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

### 5. Secciones Finales (Bibliografía y Anexos)
* **Numeración de Capítulos:** Deben ser no numerados (`numberless` en `titlesec`) para evitar prefijos decimales o de capítulo.
* **Numeración de Página:** Toda la sección de Bibliografía y Anexos debe estar totalmente limpia de números de página y cabeceras (`\pagestyle{empty}` y `\assignpagestyle{\chapter}{empty}`).

### 6. Inserción de Tablas e Imágenes
* **Tablas:** Guardar en `tablas/` e importar vía `\input{tablas/archivo.tex}`. Usar `booktabs` y `array`.
* **Imágenes:** Guardar en `imagenes/` e incluirlas sin prefijo de ruta (ya configurado en `estilos.sty`).

### 7. Compilación y Limpieza
* **REGLA:** Utilizar exclusivamente el script ejecutable `./compilar.sh` en lugar de comandos manuales aislados de `pdflatex` o `latexmk` para compilar el proyecto y realizar tareas de limpieza:
  - `./compilar.sh` (compila PDF completo y conserva temporales).
  - `./compilar.sh --clean` (compila PDF completo y elimina archivos temporales).
  - `./compilar.sh --only-clean` (elimina archivos temporales sin compilar).

---

## 🔄 Procedimiento para Cambiar de Modalidad

El documento soporta nativamente ambas modalidades mediante inclusión condicional en `main.tex`.
Si el usuario solicita cambiar de modalidad (ej. de Emprendimiento a Innovación):
1. Abre el archivo `main.tex` en la raíz del proyecto.
2. Localiza la sección `=== SELECCIÓN DE MODALIDAD ===`.
3. Comenta la instrucción de inclusión de la modalidad inactiva (ej. `% \input{emprendimiento-capitulos/index.tex}`).
4. Descomenta la instrucción de la modalidad solicitada (ej. `\input{innovacion-capitulos/index.tex}`).
5. Asegúrate de actualizar las macros institucionales en `estilos/configuracion.tex` si es necesario.
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
1. **Temporales de LaTeX:** `*.aux`, `*.log`, `*.toc`, `*.lof`, `*.lot`, `*.out`, `*.bbl`, `*.blg`, `*.fdb_latexmk`, `*.fls`, `*.synctex.gz` (incluyendo directorios recursivos como `capitulos/**/*.aux`, `preliminares/**/*.aux`, etc.).
2. **Archivos de Salida Binaria:** `*.pdf`, `main.pdf` (no analizables como texto y muy costosos en tamaño).
3. **Directorios de Agentes/IDEs:** `.antigravitycli/`, `.cline/`, `.cursor/`, `.vscode/`, `.idea/`.
