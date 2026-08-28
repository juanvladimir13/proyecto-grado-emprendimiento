# 📋 Ficha de Datos del Proyecto — Innovación Tecnológica

> **Propósito:** Este archivo recopila los datos crudos (cifras, nombres, fechas, fuentes) que alimentan la redacción de cada capítulo del documento LaTeX de Innovación Tecnológica.
> No escriba prosa formal aquí; solo responda con datos concretos. Los valores marcados `[DATO PENDIENTE]` deben ser completados antes de redactar.

---

## Estructura del directorio `capitulos/`

```text
capitulos/
├── index.tex                                          # Ensamble de los 9 capítulos
├── 01_introduccion/
│   ├── main.tex                                       # Cap. 1 — INTRODUCCIÓN (ensamble)
│   ├── contexto_general.tex                           #   └ Contexto general del sector
│   ├── motivacion_pertinencia.tex                     #   └ Motivación y pertinencia
│   └── contribucion_esperada.tex                      #   └ Contribución esperada
├── 02_planteamiento_problema/
│   ├── main.tex                                       # Cap. 2 — PLANTEAMIENTO DEL PROBLEMA
│   ├── diagnostico.tex                                #   └ Diagnóstico y descripción de la realidad
│   ├── identificacion_problema.tex                    #   └ Identificación del problema
│   ├── formulacion_problema.tex                       #   └ Formulación del problema
│   ├── objetivos.tex                                  #   └ Objetivos (general + específicos)
│   └── justificacion.tex                              #   └ Justificación
├── 03_marco_referencial/
│   ├── main.tex                                       # Cap. 3 — MARCO REFERENCIAL
│   ├── antecedentes.tex                               #   └ Antecedentes del proyecto
│   ├── bases_teoricas.tex                             #   └ Bases teóricas
│   └── marco_conceptual.tex                           #   └ Marco conceptual y normativo
├── 04_desarrollo_innovacion/
│   ├── main.tex                                       # Cap. 4 — DESARROLLO DE LA INNOVACIÓN
│   ├── diseno.tex                                     #   └ Diseño (características, utilidad, calidad)
│   ├── planificacion.tex                              #   └ Planificación y cronograma
│   ├── recursos.tex                                   #   └ Recursos (humanos, materiales, financieros)
│   └── calculo_costos.tex                             #   └ Cálculo de costos (inversión, operación, variables, fijos)
├── 05_metodologia/
│   ├── main.tex                                       # Cap. 5 — METODOLOGÍA
│   ├── tipo_investigacion.tex                         #   └ Tipo de investigación
│   ├── poblacion_muestra.tex                          #   └ Población y muestra
│   ├── tecnicas_instrumentos.tex                      #   └ Técnicas e instrumentos
│   └── analisis_datos.tex                             #   └ Procedimiento de análisis de datos
├── 06_estrategia_mejora/
│   ├── main.tex                                       # Cap. 6 — ESTRATEGIA DE MEJORA Y PROYECCIÓN
│   ├── plan_mejora.tex                                #   └ Plan de mejora continua
│   └── proyeccion_escalamiento.tex                    #   └ Proyección y escalamiento
├── 07_resultados/
│   ├── main.tex                                       # Cap. 7 — RESULTADOS
│   ├── resultados_obtenidos.tex                       #   └ Resultados obtenidos
│   ├── beneficios_impacto.tex                         #   └ Beneficios e impacto
│   └── comparacion_antes_despues.tex                  #   └ Comparación antes vs. después
├── 08_proyecto_vida/
│   └── main.tex                                       # Cap. 8 — PROYECTO DE VIDA
└── 09_conclusiones_recomendaciones/
    ├── main.tex                                       # Cap. 9 — CONCLUSIONES Y RECOMENDACIONES
    ├── conclusiones.tex                               #   └ Conclusiones
    └── recomendaciones.tex                            #   └ Recomendaciones
```

---

## 0. Datos Generales e Institucionales

> Estos datos alimentan `estilos/configuracion.tex`, la carátula y las páginas preliminares.

- **Nombre de la institución educativa:** [DATO PENDIENTE]
- **Departamento / Provincia / Localidad:** [DATO PENDIENTE]
- **Programa o carrera:** [DATO PENDIENTE] _(ej. "Programa de Innovación Tecnológica")_
- **Título del proyecto de grado:** [DATO PENDIENTE]
- **Subtítulo o nombre comercial del producto/servicio:** [DATO PENDIENTE]
- **Nombre(s) completo(s) del/los autor(es):** [DATO PENDIENTE]
- **C.I. del autor principal:** [DATO PENDIENTE]
- **Correo electrónico del autor:** [DATO PENDIENTE]
- **Nombre completo del tutor/asesor:** [DATO PENDIENTE]
- **Grado académico y cargo del tutor:** [DATO PENDIENTE] _(ej. "Lic. en Ingeniería, Docente de Física")_
- **Ciudad y país de presentación:** [DATO PENDIENTE] _(ej. "La Paz, Bolivia")_
- **Fecha de presentación (mes y año):** [DATO PENDIENTE] _(ej. "Diciembre 2026")_
- **Gestión académica:** [DATO PENDIENTE] _(ej. "Gestión 2026")_

### Páginas preliminares

- **Dedicatoria** — ¿A quién(es) se dedica y por qué en una frase?: [DATO PENDIENTE]
- **Agradecimiento** — personas o instituciones a mencionar (nombre + relación): [DATO PENDIENTE]
- **Resumen en castellano** — ¿cuál es el problema, qué se hizo y qué resultado se obtuvo? (3 frases factuales): [DATO PENDIENTE]
- **Resumen en lengua extranjera** (inglés, portugués u otro): [DATO PENDIENTE]
- **Resumen en lengua originaria** (aymara, quechua u otra): [DATO PENDIENTE]
- **Palabras clave** (mínimo 3, máximo 6): [DATO PENDIENTE]

> **Nutre:** `estilos/configuracion.tex`, `preliminares/caratula.tex`, `preliminares/dedicatoria.tex`, `preliminares/agradecimiento.tex`, `preliminares/resumen.tex`

---

## 1. INTRODUCCIÓN

### 1.1 Contexto general

- **Sector o área de aplicación del proyecto:** [DATO PENDIENTE] _(ej. "Agropecuario", "Tecnología educativa", "Energías renovables")_
- **Ámbito geográfico donde se implementa:** [DATO PENDIENTE] _(ej. "Comunidad Rosaspata, municipio de Achacachi, La Paz")_
- **Población o grupo social al que se dirige:** [DATO PENDIENTE] _(ej. "50 familias productoras de quinua")_
- **Situación actual del sector en Bolivia — cifra o dato relevante:** [DATO PENDIENTE]
  - **Fuente:** [DATO PENDIENTE] _(ej. "INE, Censo 2024")_

### 1.2 Motivación y pertinencia

- **¿Qué evento, experiencia o necesidad personal originó la idea?:** [DATO PENDIENTE]
- **¿Por qué esta solución es relevante ahora?** (política pública, tendencia, normativa): [DATO PENDIENTE]
  - **Fuente o referencia de la pertinencia:** [DATO PENDIENTE] _(ej. "PDES 2021-2025, Pilar 6")_

### 1.3 Contribución esperada

- **¿Qué tipo de solución se propone?** (producto físico, app, sistema, servicio): [DATO PENDIENTE]
- **¿Qué mejora concreta genera respecto a la situación actual?:** [DATO PENDIENTE] _(ej. "Reducir el tiempo de riego de 4 horas a 30 minutos")_
- **¿La innovación es incremental (mejora algo existente) o disruptiva (algo nuevo)?:** [DATO PENDIENTE]

> **Nutre:** `capitulos/01_introduccion/main.tex` → `contexto_general.tex`, `motivacion_pertinencia.tex`, `contribucion_esperada.tex`

---

## 2. PLANTEAMIENTO DEL PROBLEMA

### 2.1 Diagnóstico y descripción de la realidad

- **Lugar exacto del diagnóstico** (institución, comunidad, empresa): [DATO PENDIENTE]
- **Fecha(s) del diagnóstico de campo:** [DATO PENDIENTE] _(ej. "Marzo-Abril 2026")_
- **Técnica usada para diagnosticar:** [DATO PENDIENTE] _(ej. "Encuesta, entrevista, observación")_
- **Número de personas/unidades consultadas:** [DATO PENDIENTE] _(ej. "35 familias encuestadas")_
- **Hallazgo cuantitativo principal:** [DATO PENDIENTE] _(ej. "El 72% no tiene acceso a riego tecnificado")_
  - **Fuente:** [DATO PENDIENTE] _(ej. "Encuesta propia, Abril 2026")_
- **Segundo hallazgo relevante:** [DATO PENDIENTE]
  - **Fuente:** [DATO PENDIENTE]
- **Deficiencia o carencia más crítica detectada:** [DATO PENDIENTE]

### 2.2 Identificación del problema

- **Enunciado del problema central** (una oración clara): [DATO PENDIENTE]
- **¿A quiénes afecta directamente?** (cantidad y perfil): [DATO PENDIENTE] _(ej. "50 familias agricultoras de ingreso medio-bajo")_
- **¿Desde cuándo existe el problema?:** [DATO PENDIENTE] _(ej. "Al menos desde 2018, según registros municipales")_
- **Consecuencias si el problema no se resuelve:** [DATO PENDIENTE]
- **Causa raíz 1:** [DATO PENDIENTE]
- **Causa raíz 2:** [DATO PENDIENTE]

### 2.3 Formulación del problema

- **Pregunta de investigación principal:** [DATO PENDIENTE] _(ej. "¿De qué manera un sistema automatizado de riego solar reduce las pérdidas hídricas en cultivos de quinua en Rosaspata?")_
- **Pregunta específica 1:** [DATO PENDIENTE]
- **Pregunta específica 2:** [DATO PENDIENTE]

### 2.4 Objetivos

- **Objetivo general** (verbo en infinitivo + qué + para qué): [DATO PENDIENTE] _(ej. "Diseñar un sistema de riego automatizado solar para reducir pérdidas hídricas en 50 parcelas de quinua")_
- **Objetivo específico 1:** [DATO PENDIENTE]
- **Objetivo específico 2:** [DATO PENDIENTE]
- **Objetivo específico 3:** [DATO PENDIENTE]
- **Objetivo específico 4** (opcional): [DATO PENDIENTE]

### 2.5 Justificación

- **Justificación técnica** — ¿qué tecnología o conocimiento se aplica y por qué es adecuado?: [DATO PENDIENTE]
- **Justificación económica** — ¿qué ahorro, ingreso o reducción de costo genera?: [DATO PENDIENTE] _(ej. "Ahorro de Bs 1.200/mes por familia en agua")_
  - **Fuente del dato económico:** [DATO PENDIENTE]
- **Justificación social** — ¿qué beneficio humano o comunitario produce?: [DATO PENDIENTE]
- **Número de beneficiarios directos:** [DATO PENDIENTE]
- **Número de beneficiarios indirectos:** [DATO PENDIENTE]
- **¿El proyecto se vincula con algún ODS? ¿Cuál(es)?:** [DATO PENDIENTE] _(ej. "ODS 6 - Agua limpia y saneamiento")_

> **Nutre:** `capitulos/02_planteamiento_problema/main.tex` → `diagnostico.tex`, `identificacion_problema.tex`, `formulacion_problema.tex`, `objetivos.tex`, `justificacion.tex`

---

## 3. MARCO REFERENCIAL

### 3.1 Antecedentes del proyecto

1. **Antecedente 1**
   - Título: [DATO PENDIENTE]
   - Autor(es): [DATO PENDIENTE]
   - Año: [DATO PENDIENTE]
   - Institución / País: [DATO PENDIENTE]
   - Resultado o aporte clave: [DATO PENDIENTE]
   - Fuente: [DATO PENDIENTE]
2. **Antecedente 2**
   - Título: [DATO PENDIENTE]
   - Autor(es): [DATO PENDIENTE]
   - Año: [DATO PENDIENTE]
   - Institución / País: [DATO PENDIENTE]
   - Resultado o aporte clave: [DATO PENDIENTE]
   - Fuente: [DATO PENDIENTE]
3. **Antecedente 3**
   - Título: [DATO PENDIENTE]
   - Autor(es): [DATO PENDIENTE]
   - Año: [DATO PENDIENTE]
   - Institución / País: [DATO PENDIENTE]
   - Resultado o aporte clave: [DATO PENDIENTE]
   - Fuente: [DATO PENDIENTE]

### 3.2 Bases teóricas

- **Teoría o modelo directamente aplicado a la solución:** [DATO PENDIENTE]
  - **Autor y año:** [DATO PENDIENTE]
  - **Fuente bibliográfica completa:** [DATO PENDIENTE]
- **Segunda base teórica** (si aplica): [DATO PENDIENTE]
  - **Fuente:** [DATO PENDIENTE]
- **Disciplina(s) científica(s) o técnica(s) base del proyecto:** [DATO PENDIENTE] _(ej. "Electrónica de potencia, IoT, Agronomía")_
- **Principio técnico o ley física/química aplicada** (si corresponde): [DATO PENDIENTE] _(ej. "Ley de Ohm para dimensionamiento de circuitos")_
  - **Fuente:** [DATO PENDIENTE]

### 3.3 Marco conceptual y normativo

1. **Concepto 1:** [DATO PENDIENTE] _(ej. "Innovación tecnológica")_
   - Definición operativa: [DATO PENDIENTE]
   - Fuente: [DATO PENDIENTE]
2. **Concepto 2:** [DATO PENDIENTE] _(ej. "Arduino")_
   - Definición operativa: [DATO PENDIENTE]
   - Fuente: [DATO PENDIENTE]
3. **Concepto 3:** [DATO PENDIENTE]
   - Definición operativa: [DATO PENDIENTE]
   - Fuente: [DATO PENDIENTE]
4. **Concepto 4:** [DATO PENDIENTE]
   - Definición operativa: [DATO PENDIENTE]
   - Fuente: [DATO PENDIENTE]

- **Norma o ley boliviana aplicable:** [DATO PENDIENTE] _(ej. "Ley 164 de Telecomunicaciones, Art. 12")_
- **Norma técnica o estándar internacional aplicable:** [DATO PENDIENTE] _(ej. "ISO 9001:2015, NB 688")_
- **Reglamento institucional relevante:** [DATO PENDIENTE] _(ej. "RM 0912/2023 BTH")_

> **Nutre:** `capitulos/03_marco_referencial/main.tex` → `antecedentes.tex`, `bases_teoricas.tex`, `marco_conceptual.tex`

---

## 4. DESARROLLO DE LA INNOVACIÓN

### 4.1 Diseño del producto o servicio

> Corresponde a las subsecciones: Características, Utilidad y Calidad del producto o servicio.

- **Nombre del producto/servicio innovador:** [DATO PENDIENTE]
- **Tipo** (dispositivo físico, software, app, servicio, proceso): [DATO PENDIENTE]
- **Componentes o módulos principales:** [DATO PENDIENTE] _(ej. "1) Panel solar 100W, 2) Controlador Arduino Mega, 3) Bomba 12V, 4) Sensores de humedad")_
- **Dimensiones o especificaciones técnicas clave:** [DATO PENDIENTE] _(ej. "Caja IP65 de 30×20×15 cm, peso 2.5 kg")_
- **Material(es) principal(es) de fabricación:** [DATO PENDIENTE]
- **Funcionalidad principal** (qué hace paso a paso): [DATO PENDIENTE]
- **Utilidad / valor agregado para los beneficiarios:** [DATO PENDIENTE]
- **¿Qué lo diferencia de soluciones existentes?:** [DATO PENDIENTE]
- **Estándar de calidad que cumple o busca cumplir:** [DATO PENDIENTE] _(ej. "NB 688, pruebas de resistencia IP65")_
- **Criterios de control de calidad aplicados:** [DATO PENDIENTE] _(ej. "Pruebas de funcionamiento durante 72 h continuas")_

### 4.2 Planificación y cronograma

1. **Fase 1:** [DATO PENDIENTE] _(ej. "Investigación bibliográfica")_
   - Fecha inicio: [DATO PENDIENTE]
   - Fecha fin: [DATO PENDIENTE]
   - Responsable: [DATO PENDIENTE]
2. **Fase 2:** [DATO PENDIENTE] _(ej. "Diseño del prototipo")_
   - Fecha inicio: [DATO PENDIENTE]
   - Fecha fin: [DATO PENDIENTE]
   - Responsable: [DATO PENDIENTE]
3. **Fase 3:** [DATO PENDIENTE] _(ej. "Adquisición de materiales")_
   - Fecha inicio: [DATO PENDIENTE]
   - Fecha fin: [DATO PENDIENTE]
   - Responsable: [DATO PENDIENTE]
4. **Fase 4:** [DATO PENDIENTE] _(ej. "Ensamblaje y pruebas")_
   - Fecha inicio: [DATO PENDIENTE]
   - Fecha fin: [DATO PENDIENTE]
   - Responsable: [DATO PENDIENTE]
5. **Fase 5:** [DATO PENDIENTE] _(ej. "Implementación en campo")_
   - Fecha inicio: [DATO PENDIENTE]
   - Fecha fin: [DATO PENDIENTE]
   - Responsable: [DATO PENDIENTE]
6. **Fase 6:** [DATO PENDIENTE] _(ej. "Evaluación de resultados")_
   - Fecha inicio: [DATO PENDIENTE]
   - Fecha fin: [DATO PENDIENTE]
   - Responsable: [DATO PENDIENTE]
7. **Fase 7:** [DATO PENDIENTE] _(ej. "Redacción del informe final")_
   - Fecha inicio: [DATO PENDIENTE]
   - Fecha fin: [DATO PENDIENTE]
   - Responsable: [DATO PENDIENTE]

### 4.3 Recursos

#### Recursos humanos

1. **Persona 1:** [DATO PENDIENTE] _(ej. "Juan Pérez / Autor")_
   - Función: [DATO PENDIENTE]
   - Dedicación: [DATO PENDIENTE] horas/semana
2. **Persona 2:** [DATO PENDIENTE] _(ej. "Ing. María López / Tutor")_
   - Función: [DATO PENDIENTE]
   - Dedicación: [DATO PENDIENTE] horas/semana
3. **Persona 3:** [DATO PENDIENTE] _(ej. "Técnico electrónico externo")_
   - Función: [DATO PENDIENTE]
   - Dedicación: [DATO PENDIENTE] horas/semana

#### Recursos materiales

1. **Material 1:** [DATO PENDIENTE]
   - Cantidad: [DATO PENDIENTE]
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Proveedor / Origen: [DATO PENDIENTE]
2. **Material 2:** [DATO PENDIENTE]
   - Cantidad: [DATO PENDIENTE]
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Proveedor / Origen: [DATO PENDIENTE]
3. **Material 3:** [DATO PENDIENTE]
   - Cantidad: [DATO PENDIENTE]
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Proveedor / Origen: [DATO PENDIENTE]

#### Recursos financieros

- **Presupuesto total estimado (Bs):** [DATO PENDIENTE]
- **Fuente de financiamiento principal:** [DATO PENDIENTE] _(ej. "Recursos propios", "Fondo concursable UMSA", "Municipio de Achacachi")_
- **Monto financiado externamente (Bs):** [DATO PENDIENTE]
- **Monto financiado con recursos propios (Bs):** [DATO PENDIENTE]

### 4.4 Cálculo de costos

#### Costo de inversión (activos fijos, montaje)

1. **Ítem 1:** [DATO PENDIENTE]
   - Cantidad: [DATO PENDIENTE]
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Costo total (Bs): [DATO PENDIENTE]
2. **Ítem 2:** [DATO PENDIENTE]
   - Cantidad: [DATO PENDIENTE]
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Costo total (Bs): [DATO PENDIENTE]
- **Total inversión (Bs):** [DATO PENDIENTE]

#### Costo de operación mensual (fijos)

1. **Ítem 1:** [DATO PENDIENTE] _(ej. "Energía eléctrica")_
   - Costo mensual (Bs): [DATO PENDIENTE]
2. **Ítem 2:** [DATO PENDIENTE] _(ej. "Mantenimiento")_
   - Costo mensual (Bs): [DATO PENDIENTE]
- **Total fijos/mes (Bs):** [DATO PENDIENTE]

#### Costos variables (por unidad producida o ciclo)

1. **Ítem 1:** [DATO PENDIENTE] _(ej. "Insumos por lote")_
   - Costo por unidad/ciclo (Bs): [DATO PENDIENTE]
2. **Ítem 2:** [DATO PENDIENTE]
   - Costo por unidad/ciclo (Bs): [DATO PENDIENTE]
- **Total variable/unidad (Bs):** [DATO PENDIENTE]

#### Indicadores financieros

- **Precio de venta o valor del servicio por unidad (Bs):** [DATO PENDIENTE]
- **Punto de equilibrio estimado** (unidades o meses): [DATO PENDIENTE]
- **Retorno de inversión estimado** (meses): [DATO PENDIENTE]

> **Nutre:** `capitulos/04_desarrollo_innovacion/main.tex` → `diseno.tex`, `planificacion.tex`, `recursos.tex`, `calculo_costos.tex`; tablas referenciadas: `tablas/cronograma_ejemplo.tex`, `tablas/costos_ejemplo.tex`, `tablas/especificaciones_tecnicas_ejemplo.tex`

---

## 5. METODOLOGÍA

### 5.1 Tipo de investigación

- **Enfoque de investigación:** [DATO PENDIENTE] _(ej. "Cuantitativo", "Cualitativo", "Mixto")_
- **Tipo de investigación:** [DATO PENDIENTE] _(ej. "Aplicada-experimental", "Descriptiva-proyectiva")_
- **Alcance:** [DATO PENDIENTE] _(ej. "Exploratorio", "Descriptivo", "Correlacional", "Explicativo")_
- **Diseño metodológico:** [DATO PENDIENTE] _(ej. "Pre-experimental con pre-test y post-test")_
- **Justificación breve del tipo elegido:** [DATO PENDIENTE]
- **Autor de referencia metodológica:** [DATO PENDIENTE] _(ej. "Hernández Sampieri, 2014")_

### 5.2 Población y muestra

- **Población total del estudio:** [DATO PENDIENTE] _(ej. "120 familias del distrito 3 de Achacachi")_
  - **Fuente del dato poblacional:** [DATO PENDIENTE]
- **Tipo de muestreo:** [DATO PENDIENTE] _(ej. "No probabilístico por conveniencia", "Aleatorio simple")_
- **Tamaño de la muestra:** [DATO PENDIENTE]
- **Fórmula o criterio utilizado para determinar la muestra:** [DATO PENDIENTE]

### 5.3 Técnicas e instrumentos de recolección de datos

1. **Técnica 1:** [DATO PENDIENTE] _(ej. "Encuesta")_
   - Instrumento: [DATO PENDIENTE] _(ej. "Cuestionario de 15 preguntas cerradas")_
   - Objetivo: [DATO PENDIENTE]
   - Aplicada a: [DATO PENDIENTE]
   - Cantidad de aplicaciones: [DATO PENDIENTE]
2. **Técnica 2:** [DATO PENDIENTE] _(ej. "Observación directa")_
   - Instrumento: [DATO PENDIENTE] _(ej. "Ficha de observación")_
   - Objetivo: [DATO PENDIENTE]
   - Aplicada a: [DATO PENDIENTE]
   - Cantidad de aplicaciones: [DATO PENDIENTE]
3. **Técnica 3:** [DATO PENDIENTE] _(ej. "Medición de campo")_
   - Instrumento: [DATO PENDIENTE] _(ej. "Multímetro, higrómetro")_
   - Objetivo: [DATO PENDIENTE]
   - Aplicada a: [DATO PENDIENTE]
   - Cantidad de aplicaciones: [DATO PENDIENTE]
4. **Técnica 4:** [DATO PENDIENTE] _(ej. "Entrevista")_
   - Instrumento: [DATO PENDIENTE] _(ej. "Guía semiestructurada, 8 preguntas")_
   - Objetivo: [DATO PENDIENTE]
   - Aplicada a: [DATO PENDIENTE]
   - Cantidad de aplicaciones: [DATO PENDIENTE]

### 5.4 Procedimiento de análisis de datos

- **Software o herramienta de análisis utilizado:** [DATO PENDIENTE] _(ej. "Excel, SPSS v26, Python")_
- **Tipo de análisis aplicado:** [DATO PENDIENTE] _(ej. "Estadística descriptiva: media, moda, desviación estándar")_
- **Prueba estadística** (si aplica): [DATO PENDIENTE] _(ej. "t de Student para muestras pareadas")_

> **Nutre:** `capitulos/05_metodologia/main.tex` → `tipo_investigacion.tex`, `poblacion_muestra.tex`, `tecnicas_instrumentos.tex`, `analisis_datos.tex`

---

## 6. ESTRATEGIA DE MEJORA Y PROYECCIÓN

### 6.1 Plan de mejora continua

- **Mejora a corto plazo (0-6 meses):** [DATO PENDIENTE]
- **Mejora a mediano plazo (6-18 meses):** [DATO PENDIENTE]
- **Mejora a largo plazo (18+ meses):** [DATO PENDIENTE]
- **Indicador que medirá la mejora:** [DATO PENDIENTE] _(ej. "% de eficiencia hídrica", "tasa de fallas/mes")_
  - Valor actual (línea base): [DATO PENDIENTE]
  - Valor meta: [DATO PENDIENTE]

### 6.2 Proyección y escalamiento

- **¿A qué otros lugares o poblaciones podría expandirse?:** [DATO PENDIENTE]
- **Alianzas estratégicas identificadas** (instituciones, empresas, ONGs): [DATO PENDIENTE]
- **Nuevas funcionalidades técnicas previstas para versiones futuras:** [DATO PENDIENTE]
- **¿El proyecto tiene potencial de comercialización?** (Sí/No + argumento breve): [DATO PENDIENTE]
- **Mercado objetivo estimado** (tamaño, ubicación): [DATO PENDIENTE]

> **Nutre:** `capitulos/06_estrategia_mejora/main.tex` → `plan_mejora.tex`, `proyeccion_escalamiento.tex`; tablas referenciadas: `tablas/plan_mejora_ejemplo.tex`

---

## 7. RESULTADOS

### 7.1 Resultados obtenidos

1. **Resultado 1:** [DATO PENDIENTE] _(ej. "Reducción del consumo de agua")_
   - Dato cuantitativo o cualitativo: [DATO PENDIENTE] _(ej. "De 800 L/día a 320 L/día = –60%")_
   - Método de medición: [DATO PENDIENTE]
   - Fuente / Evidencia: [DATO PENDIENTE]
2. **Resultado 2:** [DATO PENDIENTE] _(ej. "Satisfacción de usuarios")_
   - Dato cuantitativo o cualitativo: [DATO PENDIENTE] _(ej. "85% satisfechos según encuesta post-uso")_
   - Método de medición: [DATO PENDIENTE]
   - Fuente / Evidencia: [DATO PENDIENTE]
3. **Resultado 3:** [DATO PENDIENTE]
   - Dato cuantitativo o cualitativo: [DATO PENDIENTE]
   - Método de medición: [DATO PENDIENTE]
   - Fuente / Evidencia: [DATO PENDIENTE]

### 7.2 Beneficios e impacto

- **Social:** [DATO PENDIENTE]
  - Dato de respaldo: [DATO PENDIENTE]
  - Fuente: [DATO PENDIENTE]
- **Tecnológico:** [DATO PENDIENTE]
  - Dato de respaldo: [DATO PENDIENTE]
  - Fuente: [DATO PENDIENTE]
- **Económico:** [DATO PENDIENTE] _(ej. "Ahorro mensual de Bs X")_
  - Dato de respaldo: [DATO PENDIENTE]
  - Fuente: [DATO PENDIENTE]
- **Ambiental:** [DATO PENDIENTE] _(ej. "Reducción de X kg de CO₂/mes")_
  - Dato de respaldo: [DATO PENDIENTE]
  - Fuente: [DATO PENDIENTE]

### 7.3 Comparación antes vs. después

1. **Indicador 1:** [DATO PENDIENTE]
   - Antes de la innovación: [DATO PENDIENTE]
   - Después de la innovación: [DATO PENDIENTE]
   - Variación (%): [DATO PENDIENTE]
2. **Indicador 2:** [DATO PENDIENTE]
   - Antes de la innovación: [DATO PENDIENTE]
   - Después de la innovación: [DATO PENDIENTE]
   - Variación (%): [DATO PENDIENTE]

> **Nutre:** `capitulos/07_resultados/main.tex` → `resultados_obtenidos.tex`, `beneficios_impacto.tex`, `comparacion_antes_despues.tex`; tablas referenciadas: `tablas/comparacion_antes_despues_ejemplo.tex`


---

## 8. PROYECTO DE VIDA

- **Carrera o profesión que el autor aspira seguir:** [DATO PENDIENTE]
- **Universidad o institución donde planea continuar estudios:** [DATO PENDIENTE]
- **¿Cómo se vincula este proyecto con sus metas profesionales?:** [DATO PENDIENTE]
- **Competencias técnicas adquiridas durante el proyecto:** [DATO PENDIENTE] _(ej. "Programación en C++, soldadura electrónica, gestión de proyectos")_
- **Competencias blandas desarrolladas:** [DATO PENDIENTE] _(ej. "Trabajo en equipo, comunicación oral, resiliencia")_
- **¿Planea emprender con este proyecto después del grado?** (Sí/No + detalle): [DATO PENDIENTE]
- **Compromiso con la comunidad — acción concreta futura:** [DATO PENDIENTE] _(ej. "Capacitar a 20 agricultores en el mantenimiento del sistema")_
- **Meta personal a 5 años relacionada con el proyecto:** [DATO PENDIENTE]

> **Nutre:** `capitulos/08_proyecto_vida/main.tex`

---

## 9. CONCLUSIONES Y RECOMENDACIONES

> Los datos de esta sección se derivan de las secciones anteriores. Complete después de tener los resultados.

### 9.1 Insumos para conclusiones

- **¿Se cumplió el objetivo general?** (Sí/Parcialmente/No + evidencia): [DATO PENDIENTE]
- **¿Se cumplió el objetivo específico 1?:** [DATO PENDIENTE]
- **¿Se cumplió el objetivo específico 2?:** [DATO PENDIENTE]
- **¿Se cumplió el objetivo específico 3?:** [DATO PENDIENTE]
- **¿Se cumplió el objetivo específico 4?:** [DATO PENDIENTE]
- **Hallazgo más importante del proyecto** (una frase factual): [DATO PENDIENTE]
- **¿La viabilidad financiera se confirmó?** (Sí/No + dato): [DATO PENDIENTE]
- **Principal limitación encontrada durante la ejecución:** [DATO PENDIENTE]

### 9.2 Insumos para recomendaciones

- **¿Qué debería monitorearse post-implementación?** (indicador + frecuencia): [DATO PENDIENTE]
- **¿A qué nueva población o contexto se recomienda ampliar las pruebas?:** [DATO PENDIENTE]
- **¿Qué fases de la estrategia de mejora se recomienda priorizar?:** [DATO PENDIENTE]
- **Recomendación técnica para futuros proyectos similares:** [DATO PENDIENTE]
- **Recomendación institucional** (qué debería hacer la unidad educativa o municipio): [DATO PENDIENTE]

> **Nutre:** `capitulos/09_conclusiones_recomendaciones/main.tex` → `conclusiones.tex`, `recomendaciones.tex`

---

## 10. Bibliografía (fuentes a incluir en `bibliografia/referencias.bib`)

1. **Referencia 1**
   - Tipo: [DATO PENDIENTE] _(ej. "Libro")_
   - Referencia completa: [DATO PENDIENTE]
   - Ya incluida en .bib: ☐
2. **Referencia 2**
   - Tipo: [DATO PENDIENTE] _(ej. "Artículo web")_
   - Referencia completa: [DATO PENDIENTE]
   - Ya incluida en .bib: ☐
3. **Referencia 3**
   - Tipo: [DATO PENDIENTE] _(ej. "Tesis")_
   - Referencia completa: [DATO PENDIENTE]
   - Ya incluida en .bib: ☐
4. **Referencia 4**
   - Tipo: [DATO PENDIENTE]
   - Referencia completa: [DATO PENDIENTE]
   - Ya incluida en .bib: ☐
5. **Referencia 5**
   - Tipo: [DATO PENDIENTE]
   - Referencia completa: [DATO PENDIENTE]
   - Ya incluida en .bib: ☐

> **Nutre:** `bibliografia/referencias.bib`

---

## 11. Anexos (material de soporte)

1. **Anexo 1:** [DATO PENDIENTE] _(ej. "Fotografías del prototipo ensamblado")_
   - Tipo: [DATO PENDIENTE] _(ej. "Foto")_
   - ¿Ya disponible?: ☐
2. **Anexo 2:** [DATO PENDIENTE] _(ej. "Encuesta aplicada — cuestionario completo")_
   - Tipo: [DATO PENDIENTE] _(ej. "Documento")_
   - ¿Ya disponible?: ☐
3. **Anexo 3:** [DATO PENDIENTE] _(ej. "Plano eléctrico del circuito")_
   - Tipo: [DATO PENDIENTE] _(ej. "Plano")_
   - ¿Ya disponible?: ☐
4. **Anexo 4:** [DATO PENDIENTE] _(ej. "Carta de autorización de la comunidad")_
   - Tipo: [DATO PENDIENTE] _(ej. "Certificado")_
   - ¿Ya disponible?: ☐

> **Nutre:** `anexos/index.tex` → `anexo_a_canvas.tex`, `anexo_b_fichas_tecnicas.tex`, `anexo_c_codigo_fuente.tex`
