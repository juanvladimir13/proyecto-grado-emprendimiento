# Prompt para Generar Archivos de Contexto Markdown del Proyecto

> **Propósito:** Generar o actualizar los archivos de contexto Markdown en la raíz del repositorio (`AGENTS.md`, `GLOSARIO.md`, `ESTILO.md`, `ESTADO.md`, `METODOLOGIA.md`) para sincronizar el trabajo de agentes de inteligencia artificial y desarrolladores con la estructura real del proyecto LaTeX bajo la modalidad de **Emprendimiento Productivo** (BTH RM 0912/2023, Anexo 1, inciso A).

---

## 📋 Instrucción Principal

Actúa como especialista en ingeniería de prompts, documentación técnica y estructuración de proyectos de grado en LaTeX. Tu tarea es generar o actualizar los archivos de contexto Markdown en la raíz del repositorio basándote en los datos del proyecto, la arquitectura modular de 7 capítulos de Emprendimiento Productivo y las convenciones institucionales descritas a continuación.

---

## 📌 Datos del Proyecto

- **Repositorio:** `proyecto-grado-emprendimiento`
- **Nombre de la Plantilla:** Proyecto de Grado BTH — Emprendimiento Productivo (LaTeX Modular)
- **Normativa Oficial:** Reglamento de Graduación del Bachillerato Técnico Humanístico (BTH, Resolución Ministerial RM 0912/2023 en Bolivia, Anexo 1, inciso A)
- **Modalidad de Graduación:** **Emprendimiento Productivo** (Estructura formal de 7 capítulos)
- **Unidad Educativa / Institución:** [INSTITUCIÓN / U.E., ej. Unidad Educativa Técnico Humanístico San Antonio]
- **Distrito Educativo y Departamento:** [DISTRITO EDUCATIVO / DEPARTAMENTO, ej. Cochabamba 1 - Cochabamba - Bolivia]
- **Especialidad Técnica BTH:** [ESPECIALIDAD, ej. Transformación de Alimentos / Sistemas Informáticos / Mecánica Automotriz / Gastronomía / Belleza Integral / Electromecánica]
- **Nivel de Formación:** TÉCNICO MEDIO
- **Título del Proyecto:** [TÍTULO DEL PROYECTO, ej. Producción y comercialización de ...]
- **Subtítulo / Nombre Comercial:** [SUBTÍTULO O NOMBRE DE LA MARCA/EMPRENDIMIENTO]
- **Autor(es):** [AUTOR 1] / [AUTOR 2 (opcional)]
- **Tutor / Asesor Guía:** [NOMBRE DEL TUTOR] ([GRADO/CARGO])
- **Localidad y Gestión:** [LOCALIDAD, ej. Cochabamba - Bolivia] | [GESTIÓN, ej. 2026]
- **Fecha de Presentación:** [MES Y AÑO, ej. Noviembre de 2026]
- **Objetivo General:** [OBJETIVO GENERAL DEL EMPRENDIMIENTO]
- **Objetivos Específicos:**
  - [Objetivo específico 1: Diagnóstico del entorno, análisis de mercado, oferta y demanda insatisfecha]
  - [Objetivo específico 2: Planificación técnica, operativa, organizacional y especificaciones del producto/servicio]
  - [Objetivo específico 3: Plan de inversiones, estructura de costos (fijos/variables) y punto de equilibrio]
  - [Objetivo específico 4: Validación comercial mediante prueba piloto y evaluación de satisfacción del cliente]
- **Misión y Visión Empresarial:** [MISIÓN Y VISIÓN (opcional)]
- **Tema / Rubro Productivo:** [ej. Alimentos y bebidas, servicios tecnológicos, confección textil, agroindustria, manufactura, servicios mecánicos]
- **Estilo de Citación y Bibliografía:** `biblatex` con estilo `apa` (APA 7ma Edición), backend `biber` y paquete `csquotes` (`autostyle`)
- **Tipografía y Formato:** Arial 11pt (`helvet`), interlineado 1.5 (`\onehalfspacing`), espaciado entre párrafos 8pt (`parskip`), sangría de primera línea 0pt (`\sangriaprimeralinea`), Courier (`courier`) para código, papel Carta (`letterpaper`), márgenes (Izquierdo: 3.0 cm, Superior/Inferior/Derecho: 2.5 cm), silabación desactivada (`\hyphenpenalty=10000`, `\exhyphenpenalty=10000`)
- **Motor y Script de Compilación:** `./compilar.sh` (`pdflatex` + `biber`), con opciones `--fast`, `--clean`, `--only-clean`, `--check-tablas`, `--check-figuras`, `--check-recursos`

---

## 📁 Estructura Real de Archivos y Carpetas del Repositorio

El proyecto utiliza una estructura modular donde cada capítulo, tabla, imagen, código y anexo se organiza de forma independiente:

```text
proyecto-grado-emprendimiento/
├── main.tex                                # Entrada principal de compilación LaTeX (\input{capitulos/index.tex})
├── README.md                               # Guía del usuario para compilar y usar la plantilla
├── AGENTS.md                               # Instrucciones, reglas y lineamientos para Agentes de IA
├── ESTRUCTURA_CAPITULOS.md                 # Detalle temático y archivos de los 7 capítulos de Emprendimiento Productivo
├── compilar.sh                             # Script ejecutable de compilación (pdflatex + biber) y limpieza
├── estilos/
│   ├── estilos.sty                         # Estilos, carga de paquetes (biblatex-apa, listings), títulos APA 7
│   ├── caratula.sty                        # Estilos, dimensiones, marco perimetral y diagramación de la carátula BTH
│   └── configuracion.tex                   # Variables centralizadas de autor(es), título, tutor, institución y modalidad
├── preliminares/                           # Hojas frontales (numeración romana)
│   ├── caratula.tex                        # Portada oficial BTH ministerial modular (\imprimircaratulabth)
│   ├── dedicatoria.tex                     # Dedicatorias (\begin{estilodedicatoria}{Dedicatoria})
│   ├── agradecimiento.tex                  # Agradecimientos (\begin{estilodedicatoria}{Agradecimiento})
│   └── resumen.tex                         # Resúmenes (\capitulopreliminar, \palabrasclave, \keywords, \simikuna)
├── capitulos/                              # Modalidad: Emprendimiento Productivo (Capítulos 1 al 7)
│   ├── index.tex                           # Ensamble maestro de los 7 capítulos
│   ├── 01_introduccion/                    # Cap. 1: main.tex, contexto_general.tex, oportunidad_negocio.tex, propuesta_valor.tex, marco_teorico.tex
│   ├── 02_planteamiento_emprendimiento/    # Cap. 2: main.tex, diagnostico.tex, objetivos.tex, justificacion.tex
│   ├── 03_desarrollo_emprendimiento/       # Cap. 3: main.tex, localizacion.tex, analisis_mercado.tex, estrategia_promocion.tex, estructura_organizacional.tex, diseno_producto.tex, ciclo_produccion.tex
│   ├── 04_viabilidad_sostenibilidad/       # Cap. 4: main.tex, calculo_inversiones.tex, costo_produccion.tex
│   ├── 05_resultados/                      # Cap. 5: main.tex, resultados_cuantitativos.tex, resultados_cualitativos.tex, indicadores_validados.tex
│   ├── 06_proyecto_vida/                   # Cap. 6: main.tex (aspiraciones académicas, competencias empresariales, compromiso ético)
│   └── 07_conclusiones_recomendaciones/    # Cap. 7: main.tex, conclusiones.tex, recomendaciones.tex
├── tablas/                                 # Tablas independientes importadas vía \input{tablas/...}
│   ├── README.md                           # Guía para estructurar tablas APA 7 con booktabs
│   ├── tabla_ejemplo.tex                   # Plantilla base de tabla
│   ├── estudio_mercado_ejemplo.tex         # Matriz de análisis de mercado y competencia (Cap. 3)
│   ├── estructura_organizacional_ejemplo.tex # Matriz de estructura organizacional, cargos y remuneraciones (Cap. 3)
│   ├── inversiones_ejemplo.tex             # Plan de inversión fija, diferida y capital de operación (Cap. 4)
│   ├── costos_produccion_ejemplo.tex       # Tabla de costos operativos variables y fijos (Cap. 4)
│   ├── indicadores_financieros_ejemplo.tex # Resumen de indicadores financieros y punto de equilibrio (Cap. 4)
│   ├── resultados_piloto_ejemplo.tex       # Resultados obtenidos en prueba piloto vs metas (Cap. 5)
│   ├── costos_ejemplo.tex                  # Plantilla alternativa de costos generales
│   ├── cronograma_ejemplo.tex              # Cronograma de actividades por fases
│   ├── especificaciones_tecnicas_ejemplo.tex # Matriz de especificaciones técnicas
│   ├── plan_mejora_ejemplo.tex             # Matriz de mejora continua
│   └── comparacion_antes_despues_ejemplo.tex # Matriz de comparación antes vs después
├── codigo/                                 # Código fuente y scripts (.py, .cpp, .ino, .sql, etc.)
│   ├── README.md                           # Guía para almacenar e importar código externo
│   └── ejemplo_controlador.py              # Script importable vía \lstinputlisting
├── scripts/                                # Scripts de utilidad y validación
│   ├── verificar_figuras.py                # Auditoría de figuras e imágenes bajo normas APA 7
│   └── verificar_tablas.py                 # Auditoría de tablas APA 7 y prevención de desbordamientos
├── imagenes/                               # Gráficos, diagramas y logotipos
│   ├── README.md                           # Instrucciones para la gestión de recursos gráficos
│   ├── figura_ejemplo.tex                  # Plantilla modular de figura bajo APA 7
│   ├── ejemplo_figura.png                  # Gráfico de prueba para diagrama de flujo de producción
│   ├── marco_portada_bth.png               # Marco ornamental perimetral oficial BTH con transparencia
│   └── logo_bth.png                        # Logotipo institucional
├── bibliografia/                           # Bibliografía BibLaTeX (APA 7ma Edición)
│   └── referencias.bib                     # Base de datos de referencias (.bib) formateada en APA 7
├── anexos/                                 # Apéndices del documento
│   ├── README.md                           # Guía para añadir y estructurar anexos
│   ├── index.tex                           # Ensamble de anexos con \capitulopreliminar{ANEXOS}
│   ├── anexo_a_canvas.tex                  # Anexo A: Modelo Canvas (\seccionanexo)
│   ├── anexo_b_fichas_tecnicas.tex         # Anexo B: Cotizaciones y fichas técnicas (\seccionanexo)
│   └── anexo_c_codigo_fuente.tex           # Anexo C: Código fuente importado (\seccionanexo)
├── promts/                                 # Prompts de apoyo y guías de revisión para agentes de IA
│   ├── migracion/                          # crear-contexto.md, ficha-proyecto.md, copiar-documento.md
│   └── revicion/                           # Suite de 14 prompts de revisión temática y checklist pre-defensa
└── docs/                                   # Regulaciones oficiales y documentos fuente
    ├── REGLAMENTO_BTH__RM_0912_2023.pdf    # Reglamento Ministerial oficial RM 0912/2023
    ├── ficha-proyecto.md                   # Ficha de datos y requerimientos del proyecto
    ├── proyecto.md                         # Documento base en texto/Markdown
    └── proyecto.rtf                        # Documento base en formato RTF
```

---

## 🛠️ Archivos de Contexto a Crear / Actualizar

Genera o actualiza en la raíz del proyecto los siguientes 5 archivos Markdown:

---

### 1. `AGENTS.md` (en la raíz)
Debe definir con rigor las directrices para cualquier agente de IA:
- **Resumen del Proyecto:** Nombre, objetivo, marco normativo (BTH RM 0912/2023, Anexo 1, inciso A) y modalidad de Emprendimiento Productivo en 7 capítulos.
- **Stack y Formato:** LaTeX `report`, `biblatex-apa` (Biber), Arial 11pt (`helvet`), interlineado 1.5 (`\onehalfspacing`), espaciado de párrafos 8pt (`parskip`), sangría 0pt (`\sangriaprimeralinea`), márgenes carta (3.0 cm izq / 2.5 cm otros), sin silabación.
- **Estructura de Directorios:** Árbol completo del repositorio explicando el propósito de cada carpeta y archivo modular.
- **Reglas Críticas de la IA:**
  1. *Parametrización:* Prohibido hardcodear datos personales o institucionales en archivos `.tex`; centralizarlos en `estilos/configuracion.tex`. El C.I. no se utiliza.
  2. *Modularidad:* Respetar el ensamble por capítulos y subarchivos `capitulos/XX_nombre/subarchivo.tex`.
  3. *Títulos APA 7:* Formato de Nivel 1 a 5, alineación a la izquierda, color negro e interlineado sencillo `\setstretch{1.0}`.
  4. *Tablas:* Uso estricto de `booktabs` (`\toprule`, `\midrule`, `\bottomrule`), sin líneas verticales (`|`) ni `\hline`, caption arriba y macro semántica `\notatabla{...}` abajo. Tablas extensas con `tabularx`.
  5. *Figuras:* Caption arriba (negrita y cursiva APA 7), imagen centrada y macro semántica `\notafigura{...}` abajo.
  6. *Código Fuente:* Uso de `listings` con estilo `estilocodigo` y `\lstinputlisting`.
  7. *Formato Numérico (SI/ISO 80000-1):* Punto decimal (`12.50`), sin separador de miles en 4 dígitos (`4500.00`) y espacio en 5+ dígitos (`25 000.00`).
  8. *Prioridad de Viñetas:* Priorizar obligatoriamente `itemize` sobre `enumerate`.
  9. *Macros Semánticas:* Uso obligatorio de `\capitulopreliminar`, `\begin{estilodedicatoria}`, `\seccionanexo`, `\configurarseccionfinal`, `\palabrasclave`, etc.
  10. *Sección "No tocar sin confirmar":* Proteger `estilos/estilos.sty`, `estilos/caratula.sty` y la diagramación oficial.
- **Comandos de Compilación:** `./compilar.sh`, `./compilar.sh --fast`, `./compilar.sh --clean`, `./compilar.sh --only-clean`, `./compilar.sh --check-tablas`, `./compilar.sh --check-figuras`, `./compilar.sh --check-recursos`.

---

### 2. `GLOSARIO.md`
Tabla con columnas: `Término | Definición Técnica / Contextual | Forma Correcta de Escribirlo / Uso en el Documento`.
Debe incluir:
- **Términos Normativos e Institucionales:** Bachillerato Técnico Humanístico (BTH), Resolución Ministerial RM 0912/2023, Emprendimiento Productivo, Proyecto de Grado, Módulo Tecnológico Productivo, Técnico Medio.
- **Términos Comerciales y Metodológicos del Emprendimiento:** Propuesta de valor, Modelo Canvas, análisis de mercado, oferta, demanda proyectada, público objetivo, segmentación de mercado, macrolocalización, microlocalización, canal de distribución, ventaja competitiva.
- **Términos Financieros y Contables:** Activo fijo, activo diferido (gastos preoperativos), capital de operación (capital de trabajo), costo fijo, costo variable unitario, margen de contribución, precio de venta sugerido, punto de equilibrio (en unidades y en bolivianos), prueba piloto, validación comercial, retorno de inversión (ROI).
- **Términos Técnicos Específicos del Dominio del Negocio:** Insumos, materia prima, formulación, flujo de procesos, ficha técnica, capacidad instalada, empaque, rotulado bromatológico, control de calidad (según la especialidad técnica del proyecto).

---

### 3. `ESTILO.md`
Guía editorial y de redacción académica:
- **Registro y Tono:** Registro académico formal, voz impersonal (tercera persona), precisión léxica y objetividad comercial y técnica.
- **Tiempos Verbales por Capítulo (7 Capítulos de Emprendimiento Productivo):**
  - *Capítulo 1 (Introducción):* Presente para caracterizar el sector productivo y la problemática del entorno; presente/futuro para formular la oportunidad de negocio y propuesta de valor; pretérito/presente para fundamentar el marco teórico y autores de referencia.
  - *Capítulo 2 (Planteamiento del Emprendimiento Productivo):* Presente para describir el diagnóstico y necesidades insatisfechas; infinitivo para objetivos generales y específicos; presente para sustentar la justificación económica, social y técnica.
  - *Capítulo 3 (Desarrollo del Emprendimiento Productivo):* Presente descriptivo para localización, análisis de mercado, mezcla de mercadotecnia, estructura organizacional y diseño del producto; pretérito/impersonal para describir etapas del flujo productivo.
  - *Capítulo 4 (Viabilidad y Sostenibilidad):* Presente e impersonal para el desglose de inversiones, costos fijos/variables, margen de contribución, cálculo del precio de venta y punto de equilibrio operativo.
  - *Capítulo 5 (Resultados):* Pretérito para pruebas piloto realizadas, ventas ejecutadas y datos de encuestas recolectados; presente para el contraste empírico de indicadores validados frente a metas proyectadas.
  - *Capítulo 6 (Proyecto de Vida):* Presente reflexivo y futuro propositivo para metas vocacionales/universitarias, competencias empresariales y socioemocionales adquiridas, compromiso ético e independencia económica a 5 años.
  - *Capítulo 7 (Conclusiones y Recomendaciones):* Pretérito/presente para sintetizar conclusiones en torno al cumplimiento de objetivos específicos; infinitivo o condicional propositivo para recomendaciones comerciales, operativas y estratégicas.
- **Normas Numéricas y Símbolos:** Uso estricto de punto decimal según ISO 80000-1 (`15.75 Bs.`, `99.2%`), escritura de magnitudes con espacio no separable (`\ ` o `~`), tablas APA 7 con `\notatabla{Fuente: ...}`.
- **Estructura de Citas APA 7:** Cita parentética `\parencite{clave}` y cita narrativa `\textcite{clave}`.

---

### 4. `ESTADO.md`
Matriz de seguimiento y control de completitud de todos los archivos del documento.
Tabla con columnas: `Capítulo / Sección | Archivo Fuente (.tex) | Estado (No iniciado / En progreso / Completo / En revisión) | Pendientes / Notas | Última Actualización`.

Debe desglosar los 7 capítulos y secciones preliminares, tablas, imágenes, anexos y bibliografía:
- **Páginas Preliminares:** `preliminares/caratula.tex`, `preliminares/dedicatoria.tex`, `preliminares/agradecimiento.tex`, `preliminares/resumen.tex`.
- **Capítulo 1 (Introducción):** `01_introduccion/contexto_general.tex`, `oportunidad_negocio.tex`, `propuesta_valor.tex`, `marco_teorico.tex`.
- **Capítulo 2 (Planteamiento del Emprendimiento Productivo):** `02_planteamiento_emprendimiento/diagnostico.tex`, `objetivos.tex`, `justificacion.tex`.
- **Capítulo 3 (Desarrollo del Emprendimiento Productivo):** `03_desarrollo_emprendimiento/localizacion.tex`, `analisis_mercado.tex`, `estrategia_promocion.tex`, `estructura_organizacional.tex`, `diseno_producto.tex`, `ciclo_produccion.tex`.
- **Capítulo 4 (Viabilidad y Sostenibilidad):** `04_viabilidad_sostenibilidad/calculo_inversiones.tex`, `costo_produccion.tex`.
- **Capítulo 5 (Resultados):** `05_resultados/resultados_cuantitativos.tex`, `resultados_cualitativos.tex`, `indicadores_validados.tex`.
- **Capítulo 6 (Proyecto de Vida):** `06_proyecto_vida/main.tex`.
- **Capítulo 7 (Conclusiones y Recomendaciones):** `07_conclusiones_recomendaciones/conclusiones.tex`, `recomendaciones.tex`.
- **Tablas Independientes:** `tablas/estudio_mercado_ejemplo.tex`, `estructura_organizacional_ejemplo.tex`, `inversiones_ejemplo.tex`, `costos_produccion_ejemplo.tex`, `indicadores_financieros_ejemplo.tex`, `resultados_piloto_ejemplo.tex`.
- **Bibliografía y Anexos:** `bibliografia/referencias.bib`, `anexos/anexo_a_canvas.tex`, `anexos/anexo_b_fichas_tecnicas.tex`, `anexos/anexo_c_codigo_fuente.tex`.

---

### 5. `METODOLOGIA.md`
Resumen metodológico y de formulación del plan de negocio transversal al proyecto:
- **Enfoque Metodológico:** Enfoque aplicado, mixto (cualitativo y cuantitativo) orientado a la formulación y validación de planes de negocio.
- **Fases del Proceso Metodológico:**
  1. *Fase 1: Diagnóstico de Mercado y Detección de Oportunidad:* Identificación de necesidades insatisfechas, caracterización del público objetivo y levantamiento de requerimientos.
  2. *Fase 2: Planificación Técnica y Operacional:* Definición de la propuesta de valor, localización, estructura organizacional, diseño del producto y flujo de procesos operativos.
  3. *Fase 3: Estudio Financiero y Estructura de Costos:* Determinación de activos fijos, capital de operación, costos unitarios variables, costos fijos, precio y punto de equilibrio.
  4. *Fase 4: Validación Comercial y Prueba Piloto:* Colocación de lote inicial, medición de ventas efectivas, aplicación de instrumentos de satisfacción del cliente y evaluación de rentabilidad real.
- **Técnicas e Instrumentos de Recolección de Datos:** Encuestas a consumidores potenciales, fichas de observación directa de la competencia, cotizaciones de proveedores, matrices de costeo y fichas de evaluación organoléptica/satisfacción.
- **Métricas e Indicadores Clave de Desempeño (KPIs):** Inversión inicial total, margen de contribución unitario, punto de equilibrio mensual (unidades y Bs.), volumen colocado en prueba piloto, porcentaje de cobertura de costos y tasa de satisfacción del cliente.

---

## 🎯 Instrucciones Finales

1. Utiliza sintaxis Markdown estándar, limpia y estructurada con encabezados jerárquicos `##` y `###`.
2. No inventes datos que no hayan sido suministrados; utiliza placeholders claros `[DATO PENDIENTE]` o `[PENDIENTE]` donde falte información por parte del usuario.
3. Al finalizar la generación o actualización, presenta un reporte resumido indicando:
   - Los archivos creados o actualizados.
   - La lista de placeholders pendientes de definición por el usuario.
   - El estado de alineación con la estructura de 7 capítulos de Emprendimiento Productivo (BTH RM 0912/2023, Anexo 1, inciso A).
