# Proyecto de Grado BTH (LaTeX Modular)

Este proyecto proporciona una estructura modular, organizada y escalable para la redacción de proyectos de grado y tesis técnicas bajo la normativa del **Bachillerato Técnico Humanístico (BTH)** en Bolivia (Resolución Ministerial RM 0912/2023) y contextos académicos utilizando **LaTeX**.

---

## 📁 Descripción de la Estructura del Proyecto

El proyecto está estructurado de manera modular para separar la configuración de metadatos, el contenido de los capítulos, las tablas independientes, el código fuente, las ilustraciones, la bibliografía y la documentación oficial.

```text
proyecto-grado/
├── main.tex                                # Archivo raíz que ensambla y compila el documento
├── README.md                               # Guía general de uso y comandos de compilación (este archivo)
├── AGENTS.md                               # Directrices y normas para agentes de IA
├── ESTRUCTURA_CAPITULOS.md                 # Detalle temático de capítulos de ambas modalidades
├── compilar.sh                             # Script de compilación y limpieza (soporta --clean, --fast, etc.)
├── estilos/                                # Paquete y configuraciones de diseño de LaTeX
│   ├── estilos.sty                         # Archivo de estilos (márgenes, fuentes, espaciados y paquetes)
│   └── configuracion.tex                   # Metadatos centralizados (título, autor(es), tutor, institución)
├── preliminares/                           # Hojas preliminares con numeración romana
│   ├── caratula.tex                        # Carátula formal BTH (1 o 2 autores dinámicos)
│   ├── portada_universitaria.tex           # Portada alternativa estilo universitario
│   ├── agradecimiento.tex                  # Página de agradecimientos
│   ├── dedicatoria.tex                     # Página de dedicatoria
│   └── resumen.tex                         # Resumen en español, lengua extranjera e indígena
├── emprendimiento-capitulos/               # Modalidad 1: "Emprendimiento Productivo" (Capítulos 1-7)
│   ├── index.tex                           # Ensamble de los 7 capítulos
│   ├── datos-proyecto.md                   # Ficha de recopilación de datos
│   ├── datos-prueba-desayunos.md           # Ficha con datos de prueba
│   ├── 01_introduccion/                    # Cap. 1: main.tex, contexto_general.tex, oportunidad_negocio.tex, propuesta_valor.tex, marco_teorico.tex
│   ├── 02_planteamiento_emprendimiento/    # Cap. 2: main.tex, diagnostico.tex, objetivos.tex, justificacion.tex
│   ├── 03_desarrollo_emprendimiento/       # Cap. 3: main.tex, localizacion.tex, analisis_mercado.tex, estrategia_promocion.tex, estructura_organizacional.tex, diseno_producto.tex, ciclo_produccion.tex
│   ├── 04_viabilidad_sostenibilidad/       # Cap. 4: main.tex, calculo_inversiones.tex, costo_produccion.tex
│   ├── 05_resultados/                      # Cap. 5: main.tex, resultados_cuantitativos.tex, resultados_cualitativos.tex, indicadores_validados.tex
│   ├── 06_proyecto_vida/                   # Cap. 6: main.tex
│   └── 07_conclusiones_recomendaciones/    # Cap. 7: main.tex, conclusiones.tex, recomendaciones.tex
├── innovacion-capitulos/                   # Modalidad 2: "Innovación Tecnológica" (Capítulos 1-9)
│   ├── index.tex                           # Ensamble de los 9 capítulos
│   ├── datos-proyecto.md                   # Ficha de recopilación de datos
│   ├── datos-prueba-control-bovino.md      # Ficha con datos de prueba
│   ├── 01_introduccion/                    # Cap. 1: main.tex, contexto_general.tex, motivacion_pertinencia.tex, contribucion_esperada.tex
│   ├── 02_planteamiento_problema/          # Cap. 2: main.tex, diagnostico.tex, identificacion_problema.tex, formulacion_problema.tex, objetivos.tex, justificacion.tex
│   ├── 03_marco_referencial/               # Cap. 3: main.tex, antecedentes.tex, bases_teoricas.tex, marco_conceptual.tex
│   ├── 04_desarrollo_innovacion/           # Cap. 4: main.tex, diseno.tex, planificacion.tex, recursos.tex, calculo_costos.tex
│   ├── 05_metodologia/                     # Cap. 5: main.tex, tipo_investigacion.tex, poblacion_muestra.tex, tecnicas_instrumentos.tex, analisis_datos.tex
│   ├── 06_estrategia_mejora/               # Cap. 6: main.tex, plan_mejora.tex, proyeccion_escalamiento.tex
│   ├── 07_resultados/                      # Cap. 7: main.tex, resultados_obtenidos.tex, beneficios_impacto.tex, comparacion_antes_despues.tex
│   ├── 08_proyecto_vida/                   # Cap. 8: main.tex
│   └── 09_conclusiones_recomendaciones/    # Cap. 9: main.tex, conclusiones.tex, recomendaciones.tex
├── tablas/                                 # Tablas independientes e importables mediante \input
│   ├── README.md                           # Guía de diseño de tablas APA 7 con booktabs
│   ├── tabla_ejemplo.tex                   # Ejemplo general de tabla
│   ├── estudio_mercado_ejemplo.tex         # Matriz/Tabla de mercado
│   ├── estructura_organizacional_ejemplo.tex # Matriz de estructura organizacional, cargos y remuneraciones
│   ├── inversiones_ejemplo.tex             # Plan y presupuesto de inversiones
│   ├── costos_produccion_ejemplo.tex       # Análisis de costos de producción
│   ├── indicadores_financieros_ejemplo.tex # Resumen de indicadores financieros y punto de equilibrio
│   ├── resultados_piloto_ejemplo.tex       # Resultados obtenidos en prueba piloto vs metas
│   ├── costos_ejemplo.tex                  # Resumen de estructura de costos
│   ├── cronograma_ejemplo.tex              # Cronograma de actividades por fases
│   ├── especificaciones_tecnicas_ejemplo.tex # Matriz de especificaciones técnicas
│   ├── plan_mejora_ejemplo.tex             # Matriz del plan de mejora continua
│   └── comparacion_antes_despues_ejemplo.tex # Matriz de comparación antes vs después


├── codigo/                                 # Código fuente y scripts (.py, .cpp, .ino, .sql, etc.)
│   ├── README.md                           # Guía para almacenar e importar código externo
│   └── ejemplo_controlador.py              # Script de prueba importable vía \lstinputlisting
├── imagenes/                               # Repositorio de recursos gráficos e ilustraciones
│   └── README.md                           # Instrucciones para la gestión de imágenes
├── bibliografia/                           # Base de datos bibliográfica (APA 7ma Edición)
│   └── referencias.bib                     # Archivo BibLaTeX (.bib) con fuentes de citas en APA 7
├── anexos/                                 # Apéndices e información complementaria
│   ├── README.md                           # Guía para añadir anexos
│   ├── index.tex                           # Ensamble general de anexos
│   ├── anexo_a_canvas.tex                  # Anexo A: Modelo Canvas
│   ├── anexo_b_fichas_tecnicas.tex         # Anexo B: Cotizaciones y fichas técnicas
│   └── anexo_c_codigo_fuente.tex           # Anexo C: Código fuente importado
└── docs/                                   # Regulaciones oficiales y documentos de soporte
    ├── README.md                           # Guía de documentos oficiales
    ├── REGLAMENTO_DE_GRADUACIN_DEL_BTH__RM_0912_2023.pdf  # Reglamento oficial de graduación BTH (RM 0912/2023)
    └── datos-proyecto.md                   # Índice de fichas de recopilación de datos
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

El proyecto incluye el script ejecutable `./compilar.sh` que gestiona todo el ciclo (`pdflatex` → `biber` → `pdflatex` → `pdflatex`):

```bash
# Compilar el documento completo y conservar archivos auxiliares:
./compilar.sh

# Compilar el documento completo y eliminar archivos auxiliares al finalizar:
./compilar.sh --clean

# Compilación rápida de 1 sola pasada (ideal durante redacción de texto):
./compilar.sh --fast

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

## 💡 Guía Rápida de Uso

1. **Configurar Datos Institucionales y del Autor:**
   * Abre `estilos/configuracion.tex` y actualiza el título, institución, especialidad, tutor y datos del o los autores (soporta 1 o 2 autores automáticamente).

2. **Seleccionar la Modalidad:**
   * En `main.tex`, descomenta la modalidad deseada (`emprendimiento-capitulos/index.tex` o `innovacion-capitulos/index.tex`) y comenta la otra.

3. **Citar Fuentes Bibliográficas (Normas APA 7):**
   * Agrega entradas a `bibliografia/referencias.bib`.
   * En el texto usa `\parencite{clave}` para citas entre paréntesis *(Apellido, 2024)* o `\textcite{clave}` para citas narrativas *Apellido (2024)*.

4. **Insertar Tablas e Imágenes:**
   * Crea tablas en `tablas/` e impórtalas con `\input{tablas/mi_tabla.tex}`.
   * Guarda imágenes en `imagenes/` e inclúyelas con `\includegraphics[width=...]{nombre.png}`.

5. **Insertar Código Fuente:**
   * Almacena scripts en `codigo/` e impórtalos con `\lstinputlisting[language=Python, caption={...}, label={lst:...}]{codigo/script.py}`.
