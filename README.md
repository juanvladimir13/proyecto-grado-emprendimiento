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
│   └── costos_produccion_ejemplo.tex       # Análisis de costos de producción
├── imagenes/                               # Repositorio de recursos gráficos e ilustraciones
│   └── README.md                           # Instrucciones para la gestión de imágenes
├── bibliografia/                           # Base de datos de referencias bibliográficas
│   └── referencias.bib                     # Archivo BibTeX conteniendo las fuentes de citas
├── anexos/                                 # Apéndices e información complementaria
│   └── anexo_a.tex                         # Contenido de anexos
└── docs/                                   # Regulaciones oficiales y documentos de soporte
    ├── REGLAMENTO_DE_GRADUACIN_DEL_BTH__RM_0912_2023.pdf  # Reglamento de graduación BTH (RM 0912/2023)
    └── datos-proyecto.md                   # Plantilla base de datos opcional
```

### 🔹 Detalle de los Directorios y Archivos

* **`main.tex`**: Es el punto de entrada del documento. Contiene la configuración general del tipo de documento (`report`), importa el paquete de estilos `estilos/estilos.sty`, e incluye modularmente la carátula, hojas preliminares, listas de contenido/figuras/tablas, los capítulos activos (`emprendimiento-capitulos` o `innovacion-capitulos`), la bibliografía y los anexos.
* **`ESTRUCTURA_CAPITULOS.md`**:
  * Documentación detallada sobre el propósito y contenido esperado para cada uno de los capítulos, tanto en la modalidad de **Emprendimiento Productivo** como en **Innovación Tecnológica**.
* **`estilos/`**:
  * `estilos.sty`: Define la apariencia visual del documento. Carga paquetes esenciales (`babel` para español, `geometry` para márgenes oficiales, `fancyhdr` para encabezados/pies, `titlesec` para dar formato a capítulos y secciones, y `hyperref` para enlaces interactivos).
  * `configuracion.tex`: Permite personalizar los datos institucionales (institución, facultad, programa), del proyecto (título, subtítulo), autor (nombre, CI, email) y del tutor/asesor sin necesidad de editar el código LaTeX complejo.
* **`preliminares/`**:
  * `caratula.tex`: Carátula oficial dinámica generada a partir de los datos en `configuracion.tex`.
  * `agradecimiento.tex`, `dedicatoria.tex` y `resumen.tex`: Secciones previas al cuerpo principal que usan numeración romana.
* **`emprendimiento-capitulos/` y `innovacion-capitulos/`**:
  * Contienen las carpetas modulares para cada capítulo de su respectiva modalidad. Cada capítulo tiene su propio archivo `main.tex`. Ambas modalidades se ensamblan mediante un archivo `index.tex` en la raíz de sus directorios, el cual se llama directamente desde `main.tex`.
* **`tablas/`**:
  * Archivos LaTeX individuales que estructuran tablas complejas (de presupuesto, mercado, costos, etc.). Se importan en los capítulos utilizando la orden `\input{tablas/nombre_tabla.tex}`, permitiendo un código limpio.
* **`imagenes/`**:
  * Contiene las figuras, fotos, logotipos y esquemas en formatos compatibles (`.png`, `.jpg`, `.pdf`). La ruta de búsqueda está configurada automáticamente a nivel global.
* **`bibliografia/`**:
  * `referencias.bib`: Archivo BibTeX donde se colocan las referencias de las fuentes citadas (libros, artículos, manuales, páginas web).
* **`anexos/`**:
  * Espacio reservado para diagramas extensos, reglamentos específicos o capturas de pantalla complementarias.
* **`docs/`**:
  * Repositorio de recursos legales e históricos del proyecto. Incluye el reglamento oficial de graduación del BTH.


---

## 🛠️ Comandos de Compilación

A continuación se detallan los comandos disponibles en la terminal para compilar el documento y gestionar los archivos auxiliares.

### 1. Compilación Automática (Recomendado)

Utilizando `latexmk`, la herramienta resolverá automáticamente las dependencias de referencias cruzadas y bibliografía en una sola ejecución:

```bash
latexmk -pdf main.tex
```

#### Modo de compilación continua (Watch Mode):
Recompila automáticamente el PDF cada vez que guardas cambios en cualquiera de los archivos `.tex` o `.bib`:

```bash
latexmk -pvc -pdf main.tex
```

---

### 2. Compilación Manual por Pasos (`pdflatex` + `bibtex`)

Si prefieres ejecutar el flujo de compilación estándar paso a paso:

```bash
# 1. Genera la estructura inicial y archivos auxiliares (.aux)
pdflatex main.tex

# 2. Procesa la base de datos bibliográfica de referencias.bib
bibtex main

# 3. Compila para enlazar las citas bibliográficas
pdflatex main.tex

# 4. Compila para resolver las referencias cruzadas y la tabla de contenidos
pdflatex main.tex
```

---

### 3. Limpieza de Archivos Auxiliares

LaTeX genera múltiples archivos temporales durante la compilación (`.aux`, `.log`, `.toc`, `.lof`, `.lot`, `.out`, `.bbl`, `.blg`).

* **Limpiar archivos auxiliares manteniendo el PDF generado:**
  ```bash
  latexmk -c
  ```

* **Limpiar todo (incluyendo el archivo PDF generado):**
  ```bash
  latexmk -C
  ```

* **Limpieza manual vía terminal (Linux/macOS):**
  ```bash
  rm -f *.aux *.log *.toc *.lof *.lot *.out *.bbl *.blg emprendimiento-capitulos/**/*.aux innovacion-capitulos/**/*.aux anexos/*.aux
  ```

---

## 💡 Guía Rápida de Uso

1. **Agregar un nuevo capítulo:**
   * Crea el directorio y archivo `emprendimiento-capitulos/08_nuevo/main.tex`.
   * En `emprendimiento-capitulos/index.tex`, agrega `\include{emprendimiento-capitulos/08_nuevo/main}` debajo de los capítulos existentes.

2. **Agregar una nueva cita bibliográfica:**
   * Abre `bibliografia/referencias.bib` e inserta la nueva entrada BibTeX.
   * En tu texto, cita la fuente usando `\cite{clave_referencia}`.

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
