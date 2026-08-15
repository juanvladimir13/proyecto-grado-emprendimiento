# Proyecto de Documentación en LaTeX

Este proyecto proporciona una estructura modular, organizada y escalable para la redacción de tesis, proyectos de grado, reportes académicos y documentación técnica avanzada utilizando **LaTeX**.

---

## 📁 Descripción de la Estructura del Proyecto

El proyecto está estructurado de manera modular y organizada para separar la configuración de estilos, el contenido de los capítulos, las tablas independientes, las ilustraciones, la bibliografía y la documentación de soporte.

```text
proyecto-grado/
├── main.tex                                # Archivo raíz que ensambla y compila el documento
├── README.md                               # Guía general de uso y comandos de compilación (este archivo)
├── ESTRUCTURA_CAPITULOS.md                 # Documentación detallada del contenido de los capítulos de ambas modalidades
├── estilos/                                # Paquete y configuraciones de diseño de LaTeX
│   ├── estilos.sty                         # Archivo de estilos (márgenes, fuentes, espaciados y paquetes)
│   └── configuracion.tex                   # Parámetros y metadatos centralizados (título, autor, tutor, etc.)
├── portada/                                # Diseños alternativos y portadas estáticas
│   └── portada.tex                         # Plantilla genérica de portada universitaria
├── preliminares/                           # Hojas preliminares con numeración romana
│   ├── caratula.tex                        # Carátula formal dinámica (usa variables de configuracion.tex)
│   ├── agradecimiento.tex                  # Página de agradecimientos
│   ├── dedicatoria.tex                     # Página de dedicatoria
│   └── resumen.tex                         # Resumen en español, lengua extranjera e indígena
├── emprendimiento-capitulos/               # Capítulos para la modalidad "Emprendimiento Productivo"
│   ├── index.tex                           # Ensamble de los 7 capítulos
│   ├── 01_introduccion/
│   │   ├── main.tex                        # Estructura del Capítulo 1
│   │   └── marco_teorico.tex               # Contenido del Marco Teórico
│   ├── ...                                 # Capítulos 2 al 6
│   └── 07_conclusiones_recomendaciones/
│       └── main.tex                        # Estructura del Capítulo 7
├── innovacion-capitulos/                   # Capítulos para la modalidad "Innovación Tecnológica"
│   ├── index.tex                           # Ensamble de los 9 capítulos
│   ├── 01_introduccion/
│   │   └── main.tex                        # Estructura del Capítulo 1
│   ├── ...                                 # Capítulos 2 al 8
│   └── 09_conclusiones_recomendaciones/
│       └── main.tex                        # Estructura del Capítulo 9
├── tablas/                                 # Tablas independientes e importables mediante \input
│   ├── tabla_ejemplo.tex                   # Ejemplo general de tabla
│   ├── estudio_mercado_ejemplo.tex         # Matriz/Tabla de mercado
│   ├── inversiones_ejemplo.tex             # Plan y presupuesto de inversiones
│   ├── costos_produccion_ejemplo.tex       # Análisis de costos de producción
│   ├── cronograma_ejemplo.tex              # Cronograma de actividades por fases
│   └── costos_ejemplo.tex                  # Resumen de estructura de costos
├── codigo/                                 # Código fuente y scripts independientes (.py, .cpp, .ino, etc.)
│   ├── README.md                           # Guía para almacenar e importar código externo
│   └── ejemplo_controlador.py              # Script de prueba importable vía \lstinputlisting
├── imagenes/                               # Repositorio de recursos gráficos e ilustraciones
│   └── README.md                           # Instrucciones para la gestión de imágenes
├── bibliografia/                           # Base de datos bibliográfica (APA 7ma Edición)
│   └── referencias.bib                     # Archivo BibLaTeX (.bib) con fuentes de citas en APA 7
├── anexos/                                 # Apéndices e información complementaria
│   └── anexo_a.tex                         # Contenido de anexos
└── docs/                                   # Regulaciones oficiales y documentos de soporte
    ├── REGLAMENTO_DE_GRADUACIN_DEL_BTH__RM_0912_2023.pdf  # Reglamento de graduación BTH (RM 0912/2023)
    └── datos-proyecto.md                   # Plantilla base de datos opcional
```

### 🔹 Detalle de los Directorios y Archivos

* **`main.tex`**: Es el punto de entrada del documento. Contiene la configuración general del tipo de documento (`report`), importa el paquete de estilos `estilos/estilos.sty`, e incluye modularmente la carátula, hojas preliminares, listas de contenido/figuras/tablas, los capítulos activos (`emprendimiento-capitulos` o `innovacion-capitulos`), la bibliografía (`\printbibliography`) y los anexos.
* **`ESTRUCTURA_CAPITULOS.md`**:
  * Documentación detallada sobre el propósito y contenido esperado para cada uno de los capítulos, tanto en la modalidad de **Emprendimiento Productivo** como en **Innovación Tecnológica**.
* **`estilos/`**:
  * `estilos.sty`: Define la apariencia visual del documento. Carga paquetes esenciales (`babel` para español, `geometry` para márgenes oficiales, `helvet` para Arial y `courier` para código fuente, `fancyhdr` para encabezados/pies, `titlesec` para dar formato a capítulos y secciones APA 7, `csquotes`, `biblatex` con estilo `apa` y backend `biber`, `listings` con sintaxis coloreada, `hyperref` para enlaces interactivos, y desactiva globalmente la división de palabras con guiones).
  * `configuracion.tex`: Permite personalizar los datos institucionales (institución, facultad, programa), del proyecto (título, subtítulo), autor (nombre, CI, email) y del tutor/asesor sin necesidad de editar el código LaTeX complejo.
* **`preliminares/`**:
  * `caratula.tex`: Carátula oficial dinámica generada a partir de los datos en `configuracion.tex`.
  * `agradecimiento.tex`, `dedicatoria.tex` y `resumen.tex`: Secciones previas al cuerpo principal que usan numeración romana.
* **`emprendimiento-capitulos/` y `innovacion-capitulos/`**:
  * Contienen las carpetas modulares para cada capítulo de su respectiva modalidad. Cada capítulo tiene su propio archivo `main.tex`. Ambas modalidades se ensamblan mediante un archivo `index.tex` en la raíz de sus directorios, el cual se llama directamente desde `main.tex`.
* **`tablas/`**:
  * Archivos LaTeX individuales que estructuran tablas complejas (cronograma, costos, presupuesto, mercado, etc.). Se importan en los capítulos utilizando la orden `\input{tablas/nombre_tabla.tex}`, permitiendo un código limpio.
* **`codigo/`**:
  * Directorio para programas, algoritmos y scripts (`.py`, `.ino`, `.cpp`, `.sql`, etc.). Se importan en cualquier capítulo o anexo mediante `\lstinputlisting[language=...]{codigo/archivo.ext}`.
* **`imagenes/`**:
  * Contiene las figuras, fotos, logotipos y esquemas en formatos compatibles (`.png`, `.jpg`, `.pdf`). La ruta de búsqueda está configurada automáticamente a nivel global.
* **`bibliografia/`**:
  * `referencias.bib`: Archivo `.bib` donde se colocan las referencias de las fuentes citadas (libros, artículos, páginas web, tesis, leyes) en formato compatible con BibLaTeX y APA 7ma Edición.
* **`anexos/`**:
  * Espacio reservado para diagramas extensos, reglamentos específicos o capturas de pantalla complementarias.
* **`docs/`**:
  * Repositorio de recursos legales e históricos del proyecto. Incluye el reglamento oficial de graduación del BTH.

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

El proyecto incluye el script ejecutable `./compilar.sh` que gestiona todo el ciclo (`pdflatex` → `biber` → `pdflatex` → `pdflatex`):

```bash
# Compilar el documento y conservar archivos auxiliares:
./compilar.sh

# Compilar el documento y eliminar archivos auxiliares al finalizar:
./compilar.sh --clean

# Solo limpiar archivos auxiliares sin compilar:
./compilar.sh --only-clean
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

### 4. Limpieza de Archivos Auxiliares

LaTeX y Biber generan múltiples archivos temporales durante la compilación (`.aux`, `.log`, `.toc`, `.lof`, `.lot`, `.out`, `.bbl`, `.blg`, `.bcf`, `.run.xml`, `.synctex.gz`).

* **Limpiar mediante script ejecutable:**
  ```bash
  ./compilar.sh --only-clean
  ```

* **Limpiar archivos auxiliares con `latexmk` (manteniendo el PDF):**
  ```bash
  latexmk -c
  ```

* **Limpiar todo (incluyendo el archivo PDF generado):**
  ```bash
  latexmk -C
  ```

---

## 💡 Guía Rápida de Uso

1. **Agregar un nuevo capítulo:**
   * Crea el directorio y archivo `emprendimiento-capitulos/08_nuevo/main.tex`.
   * En `emprendimiento-capitulos/index.tex`, agrega `\include{emprendimiento-capitulos/08_nuevo/main}` debajo de los capítulos existentes.

2. **Agregar y citar fuentes bibliográficas (Normas APA 7):**
   * Abre `bibliografia/referencias.bib` e inserta la nueva entrada (libros, artículos, webs, etc.).
   * En el texto del capítulo, cita la fuente según corresponda:
     * **Cita parentética:** `\parencite{clave}` $\rightarrow$ *(Apellido, 2024)*
     * **Cita narrativa:** `\textcite{clave}` $\rightarrow$ *Apellido (2024)*
     * **Múltiples citas:** `\parencite{clave1, clave2}` $\rightarrow$ *(Apellido1, 2020; Apellido2, 2024)*

3. **Insertar una imagen:**
   * Guarda la imagen en `imagenes/mi_diagrama.png`.
   * Inclúyela en tu capítulo con:
     ```latex
     \begin{figure}[htbp]
         \centering
         \includegraphics[width=0.8\textwidth]{mi_diagrama.png}
         \caption{Descripción del diagrama.}
         \label{fig:mi_diagrama}
     \end{figure}
     ```

4. **Insertar una tabla modular:**
   * Crea el archivo `tablas/mi_tabla.tex`.
   * Inclúyela en tu capítulo con:
     ```latex
     \input{tablas/mi_tabla.tex}
     ```

5. **Insertar código fuente coloreado (Programación):**
   * Cuenta con ajuste automático de líneas largas (*wordwrap* con autoindentación), tipografía Courier y resaltado de sintaxis.
   * Inserta un bloque directamente en el texto especificando el lenguaje (`Python`, `C++`, `Java`, `SQL`, `bash`, `HTML`, etc.):
     ```latex
     \begin{lstlisting}[language=Python, caption={Algoritmo de cálculo de humedad.}, label={lst:humedad}]
     # Lectura del sensor analógico de humedad
     def leer_humedad(pin):
         valor = analogRead(pin)
         porcentaje = (valor / 1023.0) * 100
         return round(porcentaje, 2)
     \end{lstlisting}
     ```
   * O importa un archivo de código fuente externo completo:
     ```latex
     \lstinputlisting[language=C++, caption={Controlador de riego en Arduino.}]{codigo/riego.ino}
     ```
   * Para fragmentos breves dentro de un párrafo: `\lstinline|int sensor = A0;|`.
