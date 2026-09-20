# Proyecto de Grado BTH — Emprendimiento Productivo (LaTeX Modular)

Este proyecto proporciona una estructura modular, organizada y escalable para la redacción de proyectos de grado y planes de negocio bajo la modalidad de **Emprendimiento Productivo**, en estricto cumplimiento del **Reglamento de Graduación del Bachillerato Técnico Humanístico (BTH)** en Bolivia (Resolución Ministerial RM 0912/2023, Anexo 1, inciso A) y contextos académicos utilizando **LaTeX**.

---

## 📁 Descripción de la Estructura del Proyecto

El proyecto está estructurado de manera modular para separar la configuración de metadatos, el contenido de los 7 capítulos de emprendimiento productivo, las tablas independientes, el código fuente, las ilustraciones, la bibliografía, los prompts de apoyo y la documentación oficial.

```text
proyecto-grado-emprendimiento/
├── main.tex                                # Archivo raíz que ensambla y compila el documento (\input{capitulos/index.tex})
├── README.md                               # Guía general de uso y comandos de compilación (este archivo)
├── AGENTS.md                               # Directrices y normas para agentes de IA
├── ESTRUCTURA_CAPITULOS.md                 # Detalle temático de los 7 capítulos de Emprendimiento Productivo
├── compilar.bat                            # Wrapper CMD/Batch para compilación en Windows
├── compilar.ps1                            # Script nativo de PowerShell para compilación en Windows
├── compilar.sh                             # Script de compilación y limpieza (soporta --clean, --fast, etc.)
├── estilos/                                # Paquete y configuraciones de diseño de LaTeX
│   ├── estilos.sty                         # Archivo de estilos (márgenes, fuentes, espaciados y paquetes)
│   ├── caratula.sty                        # Estilos, dimensiones, marco perimetral y diagramación de la carátula BTH
│   └── configuracion.tex                   # Metadatos centralizados (título, autor(es), tutor, institución, modalidad)
├── preliminares/                           # Hojas preliminares con numeración romana
│   ├── caratula.tex                        # Portada oficial BTH ministerial modular (\imprimircaratulabth)
│   ├── agradecimiento.tex                  # Página de agradecimientos (\begin{estilodedicatoria}{Agradecimiento})
│   ├── dedicatoria.tex                     # Página de dedicatoria (\begin{estilodedicatoria}{Dedicatoria})
│   └── resumen.tex                         # Resumen (\capitulopreliminar, \palabrasclave, \keywords, \simikuna)
├── capitulos/                              # Modalidad: Emprendimiento Productivo (Capítulos 1 al 7)
│   ├── index.tex                           # Ensamble de los 7 capítulos
│   ├── 01_introduccion/                    # Cap. 1: main.tex, contexto_general.tex, oportunidad_negocio.tex, propuesta_valor.tex, marco_teorico.tex
│   ├── 02_planteamiento_emprendimiento/    # Cap. 2: main.tex, diagnostico.tex, objetivos.tex, justificacion.tex
│   ├── 03_desarrollo_emprendimiento/       # Cap. 3: main.tex, localizacion.tex, analisis_mercado.tex, estrategia_promocion.tex, estructura_organizacional.tex, diseno_producto.tex, ciclo_produccion.tex
│   ├── 04_viabilidad_sostenibilidad/       # Cap. 4: main.tex, calculo_inversiones.tex, costo_produccion.tex
│   ├── 05_resultados/                      # Cap. 5: main.tex, resultados_cuantitativos.tex, resultados_cualitativos.tex, indicadores_validados.tex
│   ├── 06_proyecto_vida/                   # Cap. 6: main.tex (aspiraciones académicas, competencias empresariales, compromiso ético)
│   └── 07_conclusiones_recomendaciones/    # Cap. 7: main.tex, conclusiones.tex, recomendaciones.tex
├── tablas/                                 # Tablas independientes e importables mediante \input
│   ├── README.md                           # Guía de diseño de tablas APA 7 con booktabs
│   ├── tabla_ejemplo.tex                   # Ejemplo general de tabla
│   ├── estudio_mercado_ejemplo.tex         # Matriz/Tabla de mercado (Cap. 3)
│   ├── estructura_organizacional_ejemplo.tex # Matriz de estructura organizacional, cargos y remuneraciones (Cap. 3)
│   ├── inversiones_ejemplo.tex             # Plan y presupuesto de inversiones fijas y capital de operación (Cap. 4)
│   ├── costos_produccion_ejemplo.tex       # Análisis de costos de producción variables y fijos (Cap. 4)
│   ├── indicadores_financieros_ejemplo.tex # Resumen de indicadores financieros y punto de equilibrio (Cap. 4)
│   ├── resultados_piloto_ejemplo.tex       # Resultados obtenidos en prueba piloto vs metas (Cap. 5)
│   ├── costos_ejemplo.tex                  # Plantilla alternativa de costos generales
│   ├── cronograma_ejemplo.tex              # Cronograma de actividades por fases
│   ├── especificaciones_tecnicas_ejemplo.tex # Matriz de especificaciones técnicas
│   ├── plan_mejora_ejemplo.tex             # Matriz de mejora continua
│   └── comparacion_antes_despues_ejemplo.tex # Matriz comparativa antes vs después
├── codigo/                                 # Código fuente y scripts (.py, .cpp, .ino, .sql, etc.)
│   ├── README.md                           # Guía para almacenar e importar código externo
│   └── ejemplo_controlador.py              # Script de prueba importable vía \lstinputlisting
├── scripts/                                # Scripts de utilidad y validación
│   ├── verificar_figuras.py                # Auditoría de figuras e imágenes bajo normas APA 7
│   └── verificar_tablas.py                 # Auditoría de tablas APA 7 y prevención de desbordamientos
├── imagenes/                               # Repositorio de recursos gráficos e ilustraciones
│   ├── README.md                           # Guía técnica de inclusión de figuras bajo APA 7
│   ├── figura_ejemplo.tex                  # Plantilla de ejemplo de figuras (entorno, macro y subfiguras)
│   ├── ejemplo_figura.png                  # Gráfico de prueba para diagrama de flujo de producción
│   ├── logo_bth.png                        # Logotipo oficial del Módulo Tecnológico Productivo BTH
│   └── marco_portada_bth.png               # Marco ornamental perimetral oficial BTH con transparencia
├── bibliografia/                           # Base de datos bibliográfica (APA 7ma Edición)
│   └── referencias.bib                     # Archivo BibLaTeX (.bib) con fuentes de citas en APA 7
├── anexos/                                 # Apéndices e información complementaria
│   ├── README.md                           # Guía para añadir anexos
│   ├── index.tex                           # Ensamble general de anexos (\capitulopreliminar{ANEXOS})
│   ├── anexo_a_canvas.tex                  # Anexo A: Modelo Canvas (\seccionanexo)
│   ├── anexo_b_fichas_tecnicas.tex         # Anexo B: Cotizaciones y fichas técnicas (\seccionanexo)
│   └── anexo_c_codigo_fuente.tex           # Anexo C: Código fuente importado (\seccionanexo)
├── promts/                                 # Prompts de apoyo para redacción y revisión con IA
│   ├── migracion/                          # Prompts para recopilación, copia y redacción de capítulos
│   │   ├── crear-contexto.md               # Prompt para generar o actualizar archivos de contexto Markdown
│   │   ├── ficha-proyecto.md               # Flujo estructurado paso a paso con ficha técnica
│   │   └── copiar-documento.md             # Flujo de copia textual directa sin modificar redacción
│   └── revicion/                           # Set de prompts para revisión académica por etapas
│       ├── 00_README_flujo_revision.md     # Guía del flujo de revisión
│       ├── 00_analisis_capitulos_emprendimiento.md # Prompt de análisis global de coherencia
│       └── 01_ a 12_*.md                   # Suite de 15 prompts de revisión modular (7 capítulos), humanización y checklist pre-defensa
└── docs/                                   # Regulaciones oficiales y documentos de soporte
    ├── REGLAMENTO_BTH__RM_0912_2023.pdf    # Reglamento oficial de graduación BTH (RM 0912/2023)
    ├── ficha-proyecto.md                   # Ficha de datos y requerimientos del proyecto
    ├── proyecto.md                         # Documento base de entrada del proyecto (texto/Markdown)
    └── proyecto.rtf                        # Documento base de entrada del proyecto (formato enriquecido RTF)
```

---

## 📦 Requisitos Previos e Instalación

Para compilar el proyecto en sistemas basados en Linux (Debian, Ubuntu, Linux Mint):

```bash
sudo apt-get update
sudo apt-get install -y texlive-latex-base texlive-latex-recommended texlive-latex-extra \
                        texlive-bibtex-extra biber texlive-publishers texlive-lang-spanish
```

---

## 🛠️ Comandos de Compilación

A continuación se detallan los comandos disponibles en la terminal para compilar el documento y gestionar los archivos auxiliares.

### 1. Compilación Automatizada con Script (Recomendado)

El proyecto incluye scripts multiplataforma que gestionan todo el ciclo (`pdflatex` → `biber` → `pdflatex` → `pdflatex`):
- **Linux / macOS:** `./compilar.sh`
- **Windows (PowerShell):** `.\compilar.ps1`
- **Windows (CMD / Batch):** `compilar.bat`

```bash
# --- Linux / macOS ---
# Compilar el documento completo y conservar archivos auxiliares:
./compilar.sh

# Compilar el documento completo y eliminar archivos auxiliares al finalizar:
./compilar.sh --clean

# Compilación rápida de 1 sola pasada (ideal durante redacción de texto):
./compilar.sh --fast

# Auditar la conformidad de las tablas con normas APA 7ma Edición y diagramación:
./compilar.sh --check-tablas

# Auditar la conformidad de las figuras e imágenes con normas APA 7ma Edición:
./compilar.sh --check-figuras

# Auditar conjuntamente tablas y figuras:
./compilar.sh --check-recursos

# Solo limpiar archivos auxiliares sin compilar:
./compilar.sh --only-clean
```

```cmd
REM --- Windows (CMD o PowerShell) ---
REM Uso con el wrapper batch (CMD o PowerShell):
compilar.bat
compilar.bat --clean
compilar.bat --fast
compilar.bat --check-tablas
compilar.bat --check-figuras
compilar.bat --check-recursos
compilar.bat --only-clean

REM O directamente con PowerShell:
.\compilar.ps1 --clean
```

---

### 2. Compilación Automática con `latexmk`

Si utilizas `latexmk`, este detectará automáticamente el backend `biber` configurado en `estilos.sty`:

```bash
latexmk -pdf main.tex
```

#### Modo de compilación continua (Watch Mode):
Recompila automáticamente el PDF cada vez que guardas cambios en cualquiera de los archivos `.tex` o `.bib`:

```bash
latexmk -pvc -pdf main.tex
```

---

### 3. Compilación Manual por Pasos (`pdflatex` + `biber`)

Si prefieres ejecutar el flujo de compilación estándar paso a paso desde la terminal:

```bash
# 1. Genera la estructura inicial y el archivo de control bibliográfico (.bcf)
pdflatex main.tex

# 2. Procesa la base de datos bibliográfica APA 7ma Edición con Biber
biber main

# 3. Compila para enlazar las citas bibliográficas formateadas
pdflatex main.tex

# 4. Compila para resolver las referencias cruzadas y la tabla de contenidos final
pdflatex main.tex
```

---

## 💡 Guía Rápida de Uso

1. **Configurar Datos Institucionales y del Autor:**
   * Abre `estilos/configuracion.tex` y actualiza el título, institución, especialidad, modalidad (`EMPRENDIMIENTO PRODUCTIVO`), tutor y datos del o los autores (soporta 1 o 2 autores automáticamente; no requiere C.I.).
   * Personaliza si lo requieres el espaciado de párrafos estilo Word con `\espacioposteriorparrafo` (por defecto `8pt`), la sangría con `\sangriaprimeralinea` (por defecto `0pt`) y los espaciados de dedicatorias/agradecimientos con `\espacioinferiordedicatoria` (por defecto `1.5cm`) y `\espaciotitulodedicatoria` (por defecto `0.6cm`).

2. **Estructura y Redacción de Capítulos (Emprendimiento Productivo):**
   * El documento compila los 7 capítulos modulares ubicados en `capitulos/` a través de `capitulos/index.tex`.
   * Completa los datos en `docs/ficha-proyecto.md` (a partir del documento base `docs/proyecto.rtf` o `docs/proyecto.md`) y redacta cada sección en su respectiva subcarpeta (`01_introduccion/` a `07_conclusiones_recomendaciones/`).

3. **Citar Fuentes Bibliográficas (Normas APA 7):**
   * Agrega entradas a `bibliografia/referencias.bib`.
   * En el texto usa `\parencite{clave}` para citas entre paréntesis *(Apellido, 2024)* o `\textcite{clave}` para citas narrativas *Apellido (2024)*.

4. **Insertar y Auditar Tablas e Imágenes (Normas APA 7ma Edición):**
   * **Tablas:** Crear tablas en `tablas/` e importarlas con `\input{tablas/mi_tabla.tex}` usando `booktabs`. Para notas al pie de tabla usar siempre `\notatabla{Fuente: ...}`. Para tablas anchas o con descripciones extensas usar `tabularx` (columnas `L`, `C`, `R` o `X`) para evitar desbordamiento de márgenes.
   * **Imágenes y Figuras:** Guardar en `imagenes/`. En APA 7 el número y título van **ARRIBA** de la imagen y la nota **ABAJO**. Insertar usando el entorno estándar con `\caption{...}`, `\label{fig:...}`, `\centering`, `\includegraphics[width=...]{nombre.png}` y `\notafigura{Fuente: ...}`, o mediante la macro directa `\figuraapa[ancho]{archivo}{Título}{label}{Nota}` (o `\insertarfigura`).
   * **Auditoría Automatizada:** Validar en cualquier momento la conformidad de tablas y figuras con `./compilar.sh --check-tablas`, `./compilar.sh --check-figuras` o `./compilar.sh --check-recursos`.

5. **Insertar Código Fuente:**
   * Almacena scripts en `codigo/` e impórtalos con `\lstinputlisting[language=Python, caption={...}, label={lst:...}]{codigo/script.py}`.

6. **Listas y Viñetas:**
   * Priorizar obligatoriamente el uso de viñetas (`\begin{itemize}`) sobre listas numeradas (`\begin{enumerate}`), reservando estas últimas únicamente para secuencias cronológicas estrictas o procedimientos paso a paso.
