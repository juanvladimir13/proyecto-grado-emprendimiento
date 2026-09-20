# Prompts para completar el proyecto de grado BTH (modalidad Emprendimiento Productivo)

Repo: `proyecto-grado-emprendimiento`. Pensados para pegarse EN ORDEN en un agente con acceso
a archivos (Antigravity, Cursor, Cline, Copilot Chat, etc.) sobre el repo
clonado localmente. Revisa la salida de cada prompt antes de lanzar el siguiente.

---

## 📁 Estructura del Directorio `capitulos/` (Emprendimiento Productivo)

El proyecto organiza los 7 capítulos de manera modular bajo el directorio `capitulos/`:

```text
capitulos/
├── index.tex                                          # Ensamble maestro de los 7 capítulos
├── 01_introduccion/
│   ├── main.tex                                       # Cap. 1 — INTRODUCCIÓN (ensamble)
│   ├── contexto_general.tex                           #   └ Contexto general del emprendimiento
│   ├── oportunidad_negocio.tex                        #   └ Identificación de la oportunidad de negocio
│   ├── propuesta_valor.tex                            #   └ Propuesta de valor y diferenciación
│   └── marco_teorico.tex                              #   └ Marco teórico y conceptual
├── 02_planteamiento_emprendimiento/
│   ├── main.tex                                       # Cap. 2 — PLANTEAMIENTO DEL EMPRENDIMIENTO PRODUCTIVO
│   ├── diagnostico.tex                                #   └ Diagnóstico del contexto productivo
│   ├── objetivos.tex                                  #   └ Objetivos (general, específicos, misión, visión)
│   └── justificacion.tex                              #   └ Justificación económica, social y técnica
├── 03_desarrollo_emprendimiento/
│   ├── main.tex                                       # Cap. 3 — DESARROLLO DEL EMPRENDIMIENTO PRODUCTIVO
│   ├── localizacion.tex                               #   └ Macrolocalización y microlocalización
│   ├── analisis_mercado.tex                           #   └ Oferta, demanda, público objetivo, ventaja competitiva
│   ├── estrategia_promocion.tex                       #   └ Canales de distribución, precios y promoción
│   ├── estructura_organizacional.tex                  #   └ Forma jurídica, organigrama y manual de funciones
│   ├── diseno_producto.tex                            #   └ Características, atributos, empaque y marca
│   └── ciclo_produccion.tex                           #   └ Flujo de procesos, capacidad y equipamiento
├── 04_viabilidad_sostenibilidad/
│   ├── main.tex                                       # Cap. 4 — VIABILIDAD Y SOSTENIBILIDAD
│   ├── calculo_inversiones.tex                        #   └ Capital de inversión y capital de operación
│   └── costo_produccion.tex                           #   └ Costos variables, fijos, rentabilidad y punto de equilibrio
├── 05_resultados/
│   ├── main.tex                                       # Cap. 5 — RESULTADOS
│   ├── resultados_cuantitativos.tex                   #   └ Validación comercial y ventas piloto
│   ├── resultados_cualitativos.tex                    #   └ Percepción y satisfacción del cliente
│   └── indicadores_validados.tex                      #   └ Contraste financiero empírico vs metas
├── 06_proyecto_vida/
│   └── main.tex                                       # Cap. 6 — PROYECTO DE VIDA (redacción directa en main.tex)
└── 07_conclusiones_recomendaciones/
    ├── main.tex                                       # Cap. 7 — CONCLUSIONES Y RECOMENDACIONES
    ├── conclusiones.tex                               #   └ Conclusiones
    └── recomendaciones.tex                            #   └ Recomendaciones
```

---

## Prompt 1 — Cargar `docs/ficha-proyecto.md` desde `docs/proyecto.rtf` o `docs/proyecto.md` y consultar datos pendientes

```
Actúa como asistente de redacción y estructuración de proyectos de grado en modalidad
Emprendimiento Productivo. Antes de tocar cualquier archivo, lee AGENTS.md y sigue sus reglas.

1. Localización y lectura del documento base:
   - Busca dentro de la carpeta docs/ el archivo con la información base del proyecto:
     `docs/proyecto.rtf` o `docs/proyecto.md`.
   - Si el archivo es `docs/proyecto.rtf`, extrae y procesa el texto plano limpio,
     descartando etiquetas de formato y comandos de control RTF. Si es `docs/proyecto.md`,
     léelo directamente.

2. Carga inicial de la ficha técnica:
   - Abre `docs/ficha-proyecto.md` y lee detenidamente todos los campos solicitados
     en cada sección (desde la Sección 0 hasta la Sección 7).
   - Vuelca de manera estructurada en `docs/ficha-proyecto.md` todos los datos reales,
     cifras, nombres y especificaciones disponibles en el documento base.
   - Conserva la etiqueta `[DATO PENDIENTE]` únicamente en los campos donde no exista
     información en el documento base.

3. Consulta interactiva de datos pendientes durante la migración:
   - Identifica todos los campos que hayan quedado con `[DATO PENDIENTE]`.
   - No des por terminada la migración dejando datos vacíos: consulta de forma activa
     e interactiva al usuario para completar la información faltante.
   - Presenta las preguntas al usuario de manera clara, estructurada y agrupada por
     bloques temáticos lógicos para facilitar sus respuestas:
     * Bloque Institucional y Preliminares (Sección 0): Título del proyecto, autor(es),
       institución educativa, tutor/asesor, fecha/gestión, dedicatoria y agradecimiento.
     * Bloque Oportunidad y Planteamiento (Secciones 1 y 2): Oportunidad de negocio,
       propuesta de valor, diagnóstico del entorno y objetivos (general y específicos).
     * Bloque Mercado y Operaciones (Sección 3): Localización, competencia, público
       objetivo, estructura de personal, características del producto y procesos.
     * Bloque Financiero y Resultados (Secciones 4 y 5): Monto de inversión, costos
       fijos y variables, precio de venta, punto de equilibrio y métricas piloto.
     * Bloque Proyecto de Vida y Cierre (Secciones 6 y 7): Metas vocacionales,
       competencias desarrolladas, conclusiones y recomendaciones.
   - Conforme el usuario responda cada consulta, actualiza de inmediato `docs/ficha-proyecto.md`,
     reemplazando los `[DATO PENDIENTE]` por los datos concretos proporcionados.

4. Resumen de estado:
   - Al finalizar las consultas, genera un resumen detallando qué campos fueron completados
     satisfactoriamente y cuáles quedaron pendientes si el usuario indicó no disponer de la cifra aún.
   - No modifiques ningún otro archivo del repositorio en este paso.
```

---

## Prompt 2 — Volcar los datos institucionales a `estilos/configuracion.tex`

```
Lee docs/ficha-proyecto.md (ya completado y validado con el usuario) y estilos/configuracion.tex.

1. Extrae únicamente los datos institucionales/personales consolidados en la Sección 0:
   - Título del proyecto (\tituloproyecto).
   - Subtítulo o nombre comercial (\subtituloproyecto).
   - Nombre(s) del/los autor(es) (\autoruno, \autordos).
   - Datos del autor principal (\emailautoruno, \lugarproyecto).
   - Nombre y cargo del tutor (\tutorproyecto).
   - Institución educativa, departamento/distrito y especialidad (\institucion, \distritoeducativo, \especialidad).
   - Modalidad fijada en "EMPRENDIMIENTO PRODUCTIVO" (\modalidad).
   - Fecha y gestión académica (\fechaproyecto, \gestionproyecto).

2. Actualiza las macros correspondientes en `estilos/configuracion.tex`, siguiendo la Regla 1 de AGENTS.md:
   nunca quemes (hardcodees) estos datos directamente en los archivos .tex de capítulos,
   preliminares o carátula.

3. Verifica que en `main.tex` esté activa la inclusión `\input{capitulos/index.tex}`.

4. No modifiques ningún otro archivo. Muestra el diff de `estilos/configuracion.tex` al terminar.
```

---

## Prompt 3 — Redactar el contenido de los 7 capítulos con los datos de la ficha

```
Lee por completo `docs/ficha-proyecto.md`, `AGENTS.md` y `ESTRUCTURA_CAPITULOS.md`
(sección "Estructura de los 7 Capítulos (capitulos/)").

Redacta el contenido de cada archivo .tex dentro de `capitulos/`, capítulo por
capítulo, usando EXCLUSIVAMENTE la información consolidada en `docs/ficha-proyecto.md`.
No inventes cifras, nombres ni especificaciones que no estén ahí; si excepcionalmente falta
un dato puntual, deja un comentario LaTeX %% FALTA DATO: ... en su lugar.

Recorre en este orden estricto, respetando la estructura modular:

- 01_introduccion/:
  * contexto_general.tex
  * oportunidad_negocio.tex
  * propuesta_valor.tex
  * marco_teorico.tex
- 02_planteamiento_emprendimiento/:
  * diagnostico.tex
  * objetivos.tex
  * justificacion.tex
- 03_desarrollo_emprendimiento/:
  * localizacion.tex
  * analisis_mercado.tex (incluye tabla de estudio de mercado)
  * estrategia_promocion.tex
  * estructura_organizacional.tex (incluye tabla de estructura organizacional)
  * diseno_producto.tex
  * ciclo_produccion.tex
- 04_viabilidad_sostenibilidad/:
  * calculo_inversiones.tex (incluye tabla de presupuesto de inversión)
  * costo_produccion.tex (incluye tablas de costos de producción e indicadores financieros)
- 05_resultados/:
  * resultados_cuantitativos.tex
  * resultados_cualitativos.tex
  * indicadores_validados.tex (incluye tabla de resultados piloto)
- 06_proyecto_vida/:
  * main.tex
- 07_conclusiones_recomendaciones/:
  * conclusiones.tex
  * recomendaciones.tex

Reglas mientras redactas:
1. Español académico, tono formal e impersonal (tercera persona), normativa APA 7ma Edición
   y lineamientos BTH descritos en AGENTS.md.
2. Respeta el ensamble modular: el main.tex de cada capítulo ya hace \input{capitulos/...}
   a sus secciones; no dupliques \chapter{} dentro de las secciones individuales.
3. Tablas e ilustraciones: Toda información cuantitativa estructurada (análisis de mercado,
   organigrama/cargos, plan de inversión, desglose de costos, punto de equilibrio y pruebas piloto)
   debe alojarse como tabla independiente en tablas/ (siguiendo los archivos _ejemplo.tex con booktabs)
   e importarse con \input{tablas/...}.
4. Citas y bibliografía: Registra las fuentes en bibliografia/referencias.bib bajo estándar
   BibLaTeX APA 7 y cítalas en el texto con \parencite{} o \textcite{}.
5. No toques estilos/, preliminares/ ni configuracion.tex en este paso.
6. Al terminar cada capítulo, lista las secciones completadas y las que hayan quedado con %% FALTA DATO.
7. Reemplazo de contenido: Sustituye el texto de plantilla/guía de cada archivo .tex con la nueva redacción formal fundamentada, conservando intactas las etiquetas `\section{...}` y `\label{...}` existentes para preservar la integridad de la estructura y referencias cruzadas.
8. Prioridad de viñetas: Prioriza obligatoriamente `\begin{itemize}` sobre `\begin{enumerate}`, reservando este último solo para secuencias algorítmicas o procedimentales estrictas.
9. Formato numérico (SI/ISO 80000-1): Usa punto decimal (ej. 12.50, 98.5%), nunca comas decimales ni comas/puntos de miles (cifras de 4 dígitos juntas: 4500.00, 5 o más con espacio: 25 000.00).
10. Notas en tablas: Usa la macro semántica `\notatabla{Fuente: ...}` para notas o procedencia al pie de tablas APA 7.
11. Figuras e ilustraciones (APA 7): Guarda imágenes en `imagenes/` e inclúyelas centradas (`\centering`), con `\caption` ARRIBA y nota ABAJO con `\notafigura{Fuente: ...}` (o utiliza la macro semántica `\figuraapa[ancho]{archivo}{Título}{label}{Nota}`).

Al terminar los 7 capítulos, entrega un resumen general del contenido redactado.
```

---

## Prompt 4 — Compilar y validar el documento final

```
Ejecuta la compilación de prueba y verificación de consistencia:

1. Ejecuta primero `./compilar.sh --fast` (o en Windows `compilar.bat --fast` / `.\compilar.ps1 --fast`) para verificar rápidamente que no existan
   errores de sintaxis LaTeX, comandos no cerrados o rutas rotas.
2. Ejecuta `./compilar.sh --check-recursos` (o en Windows `compilar.bat --check-recursos`, o individualmente `--check-tablas` y `--check-figuras`)
   para auditar la conformidad estricta de las tablas y figuras con normas APA 7ma Edición.
3. Si la compilación rápida y auditoría pasan sin errores, ejecuta `./compilar.sh --clean` (o en Windows `compilar.bat --clean`)
   para realizar el ciclo completo de 4 pasos (pdflatex + biber + pdflatex x2) y limpiar archivos auxiliares.
4. Notifica el resultado final: confirma la generación exitosa de `main.pdf`, el conteo total
   de páginas e informa si se resolvió el índice de contenidos, bibliografía y referencias cruzadas.
```
