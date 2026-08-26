# 📋 Ficha de Datos del Proyecto — Emprendimiento Productivo

> **Propósito:** Este archivo recopila los datos crudos (cifras, nombres, fechas, fuentes) que alimentan la redacción de cada capítulo del documento LaTeX de Emprendimiento Productivo.
> No escriba prosa formal aquí; solo responda con datos concretos. Los valores marcados `[DATO PENDIENTE]` deben ser completados antes de redactar.

---

## Estructura del directorio `emprendimiento-capitulos/`

```text
emprendimiento-capitulos/
├── index.tex                                          # Ensamble de los 7 capítulos
├── datos-proyecto.md                                  # ← Este archivo (ficha de datos)
├── 01_introduccion/
│   ├── main.tex                                       # Cap. 1 — INTRODUCCIÓN (ensamble)
│   ├── contexto_oportunidad.tex                       #   └ Contexto general y oportunidad
│   ├── propuesta_valor.tex                            #   └ Propuesta de valor
│   └── marco_teorico.tex                              #   └ Marco teórico (fundamentos y gráficos)
├── 02_planteamiento_emprendimiento/
│   ├── main.tex                                       # Cap. 2 — PLANTEAMIENTO DEL EMPRENDIMIENTO PRODUCTIVO
│   ├── diagnostico.tex                                #   └ Diagnóstico del contexto productivo
│   ├── objetivos.tex                                  #   └ Objetivos (general, específicos, misión, visión)
│   └── justificacion.tex                              #   └ Justificación
├── 03_desarrollo_emprendimiento/
│   ├── main.tex                                       # Cap. 3 — DESARROLLO DEL EMPRENDIMIENTO PRODUCTIVO
│   ├── localizacion.tex                               #   └ Localización del emprendimiento
│   ├── analisis_mercado.tex                           #   └ Análisis del mercado (oferta, demanda, ventaja)
│   ├── estrategia_promocion.tex                       #   └ Estrategia de promoción y distribución
│   ├── estructura_organizacional.tex                  #   └ Estructura organizacional
│   ├── diseno_producto.tex                            #   └ Diseño de producto o servicio
│   └── ciclo_produccion.tex                           #   └ Ciclo de producción o servicio (opcional)
├── 04_viabilidad_sostenibilidad/
│   ├── main.tex                                       # Cap. 4 — VIABILIDAD Y SOSTENIBILIDAD
│   ├── calculo_inversiones.tex                        #   └ Cálculo de inversiones (capital inversión + operación)
│   └── costo_produccion.tex                           #   └ Costo de producción (variables + fijos)
├── 05_resultados/
│   └── main.tex                                       # Cap. 5 — RESULTADOS
├── 06_proyecto_vida/
│   └── main.tex                                       # Cap. 6 — PROYECTO DE VIDA
└── 07_conclusiones_recomendaciones/
    ├── main.tex                                       # Cap. 7 — CONCLUSIONES Y RECOMENDACIONES
    ├── conclusiones.tex                               #   └ Conclusiones
    └── recomendaciones.tex                            #   └ Recomendaciones
```

---

## 0. Datos Generales e Institucionales

> Estos datos alimentan `estilos/configuracion.tex`, la carátula y las páginas preliminares.

- **Nombre de la institución educativa:** [DATO PENDIENTE]
- **Departamento / Provincia / Localidad:** [DATO PENDIENTE]
- **Programa o carrera:** [DATO PENDIENTE] _(ej. "Programa de Emprendimiento Productivo")_
- **Título del proyecto de grado:** [DATO PENDIENTE]
- **Subtítulo o nombre comercial del emprendimiento:** [DATO PENDIENTE] _(ej. "Panadería Artesanal 'El Trigal'")_
- **Nombre(s) completo(s) del/los emprendedor(es):** [DATO PENDIENTE]
- **C.I. del emprendedor principal:** [DATO PENDIENTE]
- **Correo electrónico del emprendedor:** [DATO PENDIENTE]
- **Nombre completo del tutor/asesor:** [DATO PENDIENTE]
- **Grado académico y cargo del tutor:** [DATO PENDIENTE] _(ej. "Lic. en Administración, Asesor Empresarial")_
- **Ciudad y país de presentación:** [DATO PENDIENTE] _(ej. "Cochabamba, Bolivia")_
- **Fecha de presentación (mes y año):** [DATO PENDIENTE] _(ej. "Diciembre 2026")_
- **Gestión académica:** [DATO PENDIENTE] _(ej. "Gestión 2026")_

### Páginas preliminares

- **Dedicatoria** — ¿A quién(es) se dedica y por qué en una frase?: [DATO PENDIENTE]
- **Agradecimiento** — personas o instituciones a mencionar (nombre + relación): [DATO PENDIENTE]
- **Resumen en castellano** — ¿cuál es el negocio, qué se hizo y qué resultado se obtuvo? (3 frases factuales): [DATO PENDIENTE]
- **Resumen en lengua extranjera** (inglés, portugués u otro): [DATO PENDIENTE]
- **Resumen en lengua originaria** (aymara, quechua u otra): [DATO PENDIENTE]
- **Palabras clave** (mínimo 3, máximo 6): [DATO PENDIENTE]

> **Nutre:** `estilos/configuracion.tex`, `preliminares/caratula.tex`, `preliminares/dedicatoria.tex`, `preliminares/agradecimiento.tex`, `preliminares/resumen.tex`

---

## 1. INTRODUCCIÓN

### 1.1 Contexto general del emprendimiento

- **Sector productivo o de servicio:** [DATO PENDIENTE] _(ej. "Alimentos", "Textil", "Turismo", "Tecnología")_
- **Rubro específico:** [DATO PENDIENTE] _(ej. "Panadería artesanal", "Confección de polleras", "Servicio de catering")_
- **Ámbito geográfico del mercado:** [DATO PENDIENTE] _(ej. "Zona Sur de Cochabamba, radio de 5 km")_
- **Situación actual del rubro en la zona — cifra o dato relevante:** [DATO PENDIENTE] _(ej. "Existen 3 panaderías en un radio de 2 km, ninguna ofrece producto integral")_
  - **Fuente:** [DATO PENDIENTE] _(ej. "Observación directa, Marzo 2026")_

### 1.2 Oportunidad de negocio

- **¿Qué necesidad insatisfecha del mercado se detectó?:** [DATO PENDIENTE]
- **¿Qué evento, experiencia o necesidad personal originó la idea de negocio?:** [DATO PENDIENTE]
- **¿Por qué este emprendimiento es relevante ahora?:** [DATO PENDIENTE]
  - **Fuente o referencia de la pertinencia:** [DATO PENDIENTE] _(ej. "Plan municipal, tendencia de mercado, normativa")_

### 1.3 Propuesta de valor

- **¿Qué producto o servicio se ofrece?:** [DATO PENDIENTE]
- **¿Qué lo diferencia de lo que ya existe en el mercado?:** [DATO PENDIENTE] _(ej. "Pan integral con granos andinos, sin conservantes")_
- **Alcance empresarial planteado** (local, regional, departamental): [DATO PENDIENTE]

### 1.4 Marco teórico

- **Disciplina(s) o área(s) de conocimiento base del emprendimiento:** [DATO PENDIENTE] _(ej. "Administración de empresas, Tecnología de alimentos")_
- **Teoría o modelo empresarial de referencia:** [DATO PENDIENTE] _(ej. "Modelo Canvas de Osterwalder, 2010")_
  - **Fuente bibliográfica:** [DATO PENDIENTE]
- **Segunda teoría o concepto complementario:** [DATO PENDIENTE]
  - **Fuente bibliográfica:** [DATO PENDIENTE]

1. **Concepto 1:** [DATO PENDIENTE] _(ej. "Emprendimiento productivo")_
   - Definición breve: [DATO PENDIENTE]
   - Fuente: [DATO PENDIENTE]
2. **Concepto 2:** [DATO PENDIENTE] _(ej. "Cadena de valor")_
   - Definición breve: [DATO PENDIENTE]
   - Fuente: [DATO PENDIENTE]
3. **Concepto 3:** [DATO PENDIENTE] _(ej. "Punto de equilibrio")_
   - Definición breve: [DATO PENDIENTE]
   - Fuente: [DATO PENDIENTE]
4. **Concepto 4:** [DATO PENDIENTE]
   - Definición breve: [DATO PENDIENTE]
   - Fuente: [DATO PENDIENTE]

> **Nutre:** `emprendimiento-capitulos/01_introduccion/main.tex`, `emprendimiento-capitulos/01_introduccion/marco_teorico.tex`

---

## 2. PLANTEAMIENTO DEL EMPRENDIMIENTO PRODUCTIVO

### 2.1 Diagnóstico del contexto productivo

- **Lugar exacto del diagnóstico** (barrio, comunidad, zona comercial): [DATO PENDIENTE]
- **Fecha(s) del diagnóstico de campo:** [DATO PENDIENTE] _(ej. "Marzo-Abril 2026")_
- **Técnica usada para diagnosticar:** [DATO PENDIENTE] _(ej. "Encuesta, entrevista, observación")_
- **Número de personas consultadas:** [DATO PENDIENTE] _(ej. "80 personas encuestadas en la feria dominical")_
- **Brecha de oferta detectada** (dato cuantitativo): [DATO PENDIENTE] _(ej. "El 65% de encuestados compraría pan integral si estuviera disponible")_
  - **Fuente:** [DATO PENDIENTE] _(ej. "Encuesta propia, Abril 2026")_
- **Segundo hallazgo relevante:** [DATO PENDIENTE]
  - **Fuente:** [DATO PENDIENTE]
- **Necesidad no atendida más crítica:** [DATO PENDIENTE]

### 2.2 Objetivos del emprendimiento productivo

- **Objetivo general** (verbo en infinitivo + qué + para qué): [DATO PENDIENTE] _(ej. "Establecer una panadería artesanal para la producción y comercialización de pan integral con granos andinos en la Zona Sur de Cochabamba")_
- **Objetivo específico 1:** [DATO PENDIENTE] _(ej. "Realizar el estudio de mercado para identificar la demanda insatisfecha")_
- **Objetivo específico 2:** [DATO PENDIENTE] _(ej. "Diseñar la estructura organizacional y los procesos operativos")_
- **Objetivo específico 3:** [DATO PENDIENTE] _(ej. "Determinar los costos de inversión y precios de venta garantizando rentabilidad")_
- **Objetivo específico 4** (opcional): [DATO PENDIENTE]
- **Misión del emprendimiento** (opcional): [DATO PENDIENTE]
- **Visión del emprendimiento** (opcional): [DATO PENDIENTE]

### 2.3 Justificación

- **Justificación económica** — ¿qué empleo, ingreso o dinamización económica genera?: [DATO PENDIENTE] _(ej. "Genera 3 empleos directos y compra insumos a 5 productores locales de quinua")_
  - **Fuente:** [DATO PENDIENTE]
- **Justificación social** — ¿qué beneficio humano o comunitario produce?: [DATO PENDIENTE] _(ej. "Ofrece alimento nutritivo a precio accesible para familias de ingreso medio-bajo")_
- **Justificación técnica** — ¿qué conocimiento o tecnología se aplica?: [DATO PENDIENTE]
- **Número de beneficiarios directos** (clientes): [DATO PENDIENTE]
- **Número de beneficiarios indirectos** (proveedores, familias de empleados): [DATO PENDIENTE]
- **Aprovechamiento de recursos locales mencionado:** [DATO PENDIENTE] _(ej. "Quinua y amaranto de productores del municipio de Sipe Sipe")_

> **Nutre:** `emprendimiento-capitulos/02_planteamiento_emprendimiento/main.tex` (secciones: diagnóstico, objetivos, justificación)

---

## 3. DESARROLLO DEL EMPRENDIMIENTO PRODUCTIVO

### 3.1 Localización del emprendimiento

- **Macrolocalización** (departamento, provincia, municipio): [DATO PENDIENTE]
- **Microlocalización** (dirección exacta o zona): [DATO PENDIENTE] _(ej. "Av. Blanco Galindo Km 4, local 12-B")_
- **Argumento de cercanía a insumos:** [DATO PENDIENTE] _(ej. "A 15 min del mercado mayorista La Cancha")_
- **Argumento de cercanía a clientes:** [DATO PENDIENTE] _(ej. "Zona residencial con 2.000 familias en radio de 1 km")_
- **Costo de alquiler o propiedad del local (Bs/mes):** [DATO PENDIENTE]
  - **Fuente:** [DATO PENDIENTE]

### 3.2 Análisis de mercado

#### Oferta (competidores)

1. **Competidor 1**
   - Nombre: [DATO PENDIENTE]
   - Ubicación: [DATO PENDIENTE]
   - Producto/servicio que ofrece: [DATO PENDIENTE]
   - Precio referencial (Bs): [DATO PENDIENTE]
   - Fortaleza: [DATO PENDIENTE]
   - Debilidad: [DATO PENDIENTE]
2. **Competidor 2**
   - Nombre: [DATO PENDIENTE]
   - Ubicación: [DATO PENDIENTE]
   - Producto/servicio que ofrece: [DATO PENDIENTE]
   - Precio referencial (Bs): [DATO PENDIENTE]
   - Fortaleza: [DATO PENDIENTE]
   - Debilidad: [DATO PENDIENTE]
3. **Competidor 3**
   - Nombre: [DATO PENDIENTE]
   - Ubicación: [DATO PENDIENTE]
   - Producto/servicio que ofrece: [DATO PENDIENTE]
   - Precio referencial (Bs): [DATO PENDIENTE]
   - Fortaleza: [DATO PENDIENTE]
   - Debilidad: [DATO PENDIENTE]

#### Demanda

- **Volumen estimado de consumo** (unidades/mes o Bs/mes en la zona): [DATO PENDIENTE]
- **Frecuencia de compra del cliente típico:** [DATO PENDIENTE] _(ej. "Diaria", "3 veces por semana")_
- **Patrón de compra detectado:** [DATO PENDIENTE] _(ej. "Mayor demanda de 6:00 a 8:00 y de 17:00 a 19:00")_
  - **Fuente del dato de demanda:** [DATO PENDIENTE]

#### Público objetivo (cliente y/o usuario)

- **Segmento demográfico:** [DATO PENDIENTE] _(ej. "Mujeres de 25-50 años, amas de casa")_
- **Segmento geográfico:** [DATO PENDIENTE] _(ej. "Residentes de la Zona Sur, radio de 1 km")_
- **Segmento socioeconómico:** [DATO PENDIENTE] _(ej. "Ingreso medio, Bs 3.000-6.000/mes por hogar")_
- **Necesidad principal del cliente:** [DATO PENDIENTE]

#### Entorno y competencia

- **Factor político/legal relevante:** [DATO PENDIENTE] _(ej. "Ley 453 de Derechos del Consumidor exige etiquetado nutricional")_
- **Factor económico relevante:** [DATO PENDIENTE] _(ej. "Inflación de harina del 8% en el último año")_
  - **Fuente:** [DATO PENDIENTE]
- **Factor social/cultural relevante:** [DATO PENDIENTE] _(ej. "Tendencia creciente de consumo saludable en la zona")_
  - **Fuente:** [DATO PENDIENTE]
- **Barreras de entrada al mercado:** [DATO PENDIENTE] _(ej. "Inversión inicial moderada, registro SENASAG obligatorio")_

#### Ventaja competitiva

- **Propuesta de valor única** (una frase): [DATO PENDIENTE] _(ej. "Único pan integral con quinua real en la zona, horneado diariamente sin conservantes")_
- **Diferenciador principal vs. competencia:** [DATO PENDIENTE]
- **Segundo diferenciador:** [DATO PENDIENTE]

### 3.3 Estrategia de promoción y distribución

- **Canales de distribución:** [DATO PENDIENTE] _(ej. "Venta directa en local, pedidos por WhatsApp, ferias dominicales")_
- **Estrategia de precio:** [DATO PENDIENTE] _(ej. "Precio competitivo: Bs 2 por unidad vs. Bs 1.50 del pan convencional")_
- **Estrategia de marketing/publicidad:** [DATO PENDIENTE] _(ej. "Página de Facebook, degustaciones en ferias, volantes en el barrio")_
- **Presupuesto estimado de marketing (Bs/mes):** [DATO PENDIENTE]

### 3.4 Estructura organizacional

- **Forma jurídica del emprendimiento:** [DATO PENDIENTE] _(ej. "Empresa unipersonal", "Sociedad colectiva")_
- **Número total de empleados previstos:** [DATO PENDIENTE]

1. **Cargo 1:** [DATO PENDIENTE] _(ej. "Gerente/Emprendedor")_
   - Función principal: [DATO PENDIENTE]
   - Sueldo/remuneración (Bs/mes): [DATO PENDIENTE]
2. **Cargo 2:** [DATO PENDIENTE] _(ej. "Panadero")_
   - Función principal: [DATO PENDIENTE]
   - Sueldo/remuneración (Bs/mes): [DATO PENDIENTE]
3. **Cargo 3:** [DATO PENDIENTE] _(ej. "Vendedor")_
   - Función principal: [DATO PENDIENTE]
   - Sueldo/remuneración (Bs/mes): [DATO PENDIENTE]

### 3.5 Diseño de producto o servicio

- **Nombre comercial del producto/servicio:** [DATO PENDIENTE]
- **Características técnicas** (tamaño, peso, ingredientes, materiales): [DATO PENDIENTE] _(ej. "Pan integral de 80g con 15% quinua, 10% amaranto")_
- **Empaque / presentación:** [DATO PENDIENTE] _(ej. "Bolsa de papel kraft con logo, unidad y paquete de 6")_
- **Marca registrada** (si aplica): [DATO PENDIENTE]
- **Diferenciadores de calidad:** [DATO PENDIENTE] _(ej. "Sin conservantes, horneado diario, insumos orgánicos certificados")_

### 3.6 Ciclo de producción o servicio (opcional)

- **Etapas del proceso productivo** (listar en orden): [DATO PENDIENTE] _(ej. "1) Recepción de insumos → 2) Pesado y mezcla → 3) Amasado → 4) Fermentación → 5) Horneado → 6) Enfriado → 7) Empacado → 8) Venta")_
- **Tiempo total del ciclo** (de inicio a producto terminado): [DATO PENDIENTE] _(ej. "4 horas por lote")_
- **Capacidad de producción por ciclo:** [DATO PENDIENTE] _(ej. "200 unidades por lote, 2 lotes/día")_
- **Equipo o maquinaria principal utilizada:** [DATO PENDIENTE] _(ej. "Horno industrial de 10 bandejas, amasadora de 25 kg")_

> **Nutre:** `emprendimiento-capitulos/03_desarrollo_emprendimiento/main.tex` (secciones: localización, análisis de mercado, estrategia de promoción, estructura organizacional, diseño de producto, ciclo de producción); tablas referenciadas: `tablas/estudio_mercado_ejemplo.tex`

---

## 4. VIABILIDAD Y SOSTENIBILIDAD

### 4.1 Cálculo de inversiones

#### Capital de inversión (activos fijos, infraestructura, montaje)

1. **Ítem 1:** [DATO PENDIENTE] _(ej. "Horno industrial")_
   - Cantidad: [DATO PENDIENTE]
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Costo total (Bs): [DATO PENDIENTE]
2. **Ítem 2:** [DATO PENDIENTE] _(ej. "Amasadora")_
   - Cantidad: [DATO PENDIENTE]
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Costo total (Bs): [DATO PENDIENTE]
3. **Ítem 3:** [DATO PENDIENTE] _(ej. "Vitrinas de exhibición")_
   - Cantidad: [DATO PENDIENTE]
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Costo total (Bs): [DATO PENDIENTE]
4. **Ítem 4:** [DATO PENDIENTE] _(ej. "Adecuación del local")_
   - Cantidad: [DATO PENDIENTE]
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Costo total (Bs): [DATO PENDIENTE]
- **Total capital de inversión (Bs):** [DATO PENDIENTE]

#### Capital de operación (primeros meses antes de percibir ingresos continuos)

1. **Ítem 1:** [DATO PENDIENTE] _(ej. "Materia prima inicial")_
   - Meses cubiertos: [DATO PENDIENTE]
   - Costo total (Bs): [DATO PENDIENTE]
2. **Ítem 2:** [DATO PENDIENTE] _(ej. "Sueldos primer mes")_
   - Meses cubiertos: [DATO PENDIENTE]
   - Costo total (Bs): [DATO PENDIENTE]
3. **Ítem 3:** [DATO PENDIENTE] _(ej. "Alquiler primer mes")_
   - Meses cubiertos: [DATO PENDIENTE]
   - Costo total (Bs): [DATO PENDIENTE]
4. **Ítem 4:** [DATO PENDIENTE] _(ej. "Servicios básicos")_
   - Meses cubiertos: [DATO PENDIENTE]
   - Costo total (Bs): [DATO PENDIENTE]
- **Total capital de operación (Bs):** [DATO PENDIENTE]

#### Resumen de inversión

- **Inversión total (inversión + operación) (Bs):** [DATO PENDIENTE]
- **Fuente de financiamiento principal:** [DATO PENDIENTE] _(ej. "Ahorro familiar Bs 8.000 + préstamo BancoSol Bs 12.000")_
- **Monto financiado externamente (Bs):** [DATO PENDIENTE]
- **Monto financiado con recursos propios (Bs):** [DATO PENDIENTE]

### 4.2 Costo de producción

#### Costos variables (por unidad o lote producido)

1. **Insumo 1:** [DATO PENDIENTE] _(ej. "Harina integral")_
   - Cantidad por lote: [DATO PENDIENTE] _(ej. "10 kg")_
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Costo por lote (Bs): [DATO PENDIENTE]
2. **Insumo 2:** [DATO PENDIENTE] _(ej. "Quinua")_
   - Cantidad por lote: [DATO PENDIENTE]
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Costo por lote (Bs): [DATO PENDIENTE]
3. **Insumo 3:** [DATO PENDIENTE] _(ej. "Envases")_
   - Cantidad por lote: [DATO PENDIENTE]
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Costo por lote (Bs): [DATO PENDIENTE]
4. **Insumo 4:** [DATO PENDIENTE] _(ej. "Mano de obra directa")_
   - Cantidad por lote: [DATO PENDIENTE]
   - Costo unitario (Bs): [DATO PENDIENTE]
   - Costo por lote (Bs): [DATO PENDIENTE]
- **Total costo variable/lote (Bs):** [DATO PENDIENTE]
- **Costo variable por unidad (Bs):** [DATO PENDIENTE]
- **Unidades por lote:** [DATO PENDIENTE]

#### Costos fijos (mensuales, independientes del volumen)

1. **Ítem 1:** [DATO PENDIENTE] _(ej. "Alquiler del local")_
   - Costo mensual (Bs): [DATO PENDIENTE]
2. **Ítem 2:** [DATO PENDIENTE] _(ej. "Servicios básicos: luz, agua, gas")_
   - Costo mensual (Bs): [DATO PENDIENTE]
3. **Ítem 3:** [DATO PENDIENTE] _(ej. "Sueldos administrativos")_
   - Costo mensual (Bs): [DATO PENDIENTE]
4. **Ítem 4:** [DATO PENDIENTE] _(ej. "Depreciación de equipos")_
   - Costo mensual (Bs): [DATO PENDIENTE]
- **Total costos fijos/mes (Bs):** [DATO PENDIENTE]

#### Indicadores financieros

- **Precio de venta por unidad (Bs):** [DATO PENDIENTE]
- **Margen de ganancia por unidad** (Bs y %): [DATO PENDIENTE] _(ej. "Bs 0.80 = 40%")_
- **Punto de equilibrio** (unidades/mes): [DATO PENDIENTE]
- **Ingreso mensual proyectado (Bs):** [DATO PENDIENTE]
- **Utilidad neta mensual proyectada (Bs):** [DATO PENDIENTE]
- **Retorno de inversión estimado** (meses): [DATO PENDIENTE]

> **Nutre:** `emprendimiento-capitulos/04_viabilidad_sostenibilidad/main.tex` (secciones: cálculo de inversiones, costo de producción); tablas referenciadas: `tablas/inversiones_ejemplo.tex`, `tablas/costos_produccion_ejemplo.tex`

---

## 5. RESULTADOS

### 5.1 Resultados cuantitativos

1. **Resultado 1:** [DATO PENDIENTE] _(ej. "Ventas en prueba piloto")_
   - Dato obtenido: [DATO PENDIENTE] _(ej. "320 unidades vendidas en 5 días de feria")_
   - Método de medición: [DATO PENDIENTE]
   - Fuente / Evidencia: [DATO PENDIENTE]
2. **Resultado 2:** [DATO PENDIENTE] _(ej. "Margen de ganancia real")_
   - Dato obtenido: [DATO PENDIENTE] _(ej. "38% por unidad, cercano al 40% proyectado")_
   - Método de medición: [DATO PENDIENTE]
   - Fuente / Evidencia: [DATO PENDIENTE]
3. **Resultado 3:** [DATO PENDIENTE] _(ej. "Punto de equilibrio alcanzado")_
   - Dato obtenido: [DATO PENDIENTE]
   - Método de medición: [DATO PENDIENTE]
   - Fuente / Evidencia: [DATO PENDIENTE]

### 5.2 Resultados cualitativos

1. **Aspecto 1:** [DATO PENDIENTE] _(ej. "Aceptación del producto")_
   - Resultado: [DATO PENDIENTE] _(ej. "90% de compradores repetiría la compra según encuesta post-venta")_
   - Fuente / Evidencia: [DATO PENDIENTE]
2. **Aspecto 2:** [DATO PENDIENTE] _(ej. "Percepción de calidad")_
   - Resultado: [DATO PENDIENTE]
   - Fuente / Evidencia: [DATO PENDIENTE]

### 5.3 Indicadores de rentabilidad validados

1. **Indicador 1:** [DATO PENDIENTE] _(ej. "Margen de ganancia")_
   - Valor proyectado: [DATO PENDIENTE]
   - Valor real/validado: [DATO PENDIENTE]
   - Variación: [DATO PENDIENTE]
2. **Indicador 2:** [DATO PENDIENTE] _(ej. "Punto de equilibrio")_
   - Valor proyectado: [DATO PENDIENTE]
   - Valor real/validado: [DATO PENDIENTE]
   - Variación: [DATO PENDIENTE]

> **Nutre:** `emprendimiento-capitulos/05_resultados/main.tex`

---

## 6. PROYECTO DE VIDA

- **Carrera o profesión que el emprendedor aspira seguir:** [DATO PENDIENTE]
- **Universidad o institución donde planea continuar estudios:** [DATO PENDIENTE]
- **¿Cómo se vincula este emprendimiento con sus metas profesionales?:** [DATO PENDIENTE]
- **¿Planea continuar con la empresa después del grado?** (Sí/No + detalle): [DATO PENDIENTE]
- **Competencias empresariales adquiridas durante el proyecto:** [DATO PENDIENTE] _(ej. "Gestión de costos, negociación con proveedores, atención al cliente")_
- **Competencias blandas desarrolladas:** [DATO PENDIENTE] _(ej. "Resiliencia, liderazgo, comunicación comercial")_
- **Compromiso ético con la comunidad — acción concreta futura:** [DATO PENDIENTE] _(ej. "Donar 5% de producción semanal a comedor comunitario")_
- **Rol del emprendimiento como vehículo de independencia económica:** [DATO PENDIENTE]
- **Meta personal a 5 años relacionada con la empresa:** [DATO PENDIENTE] _(ej. "Abrir segunda sucursal y formalizar con SENASAG")_

> **Nutre:** `emprendimiento-capitulos/06_proyecto_vida/main.tex`

---

## 7. CONCLUSIONES Y RECOMENDACIONES

> Los datos de esta sección se derivan de las secciones anteriores. Complete después de tener los resultados.

### 7.1 Insumos para conclusiones

- **¿Se cumplió el objetivo general?** (Sí/Parcialmente/No + evidencia): [DATO PENDIENTE]
- **¿Se cumplió el objetivo específico 1?:** [DATO PENDIENTE]
- **¿Se cumplió el objetivo específico 2?:** [DATO PENDIENTE]
- **¿Se cumplió el objetivo específico 3?:** [DATO PENDIENTE]
- **¿El análisis de mercado confirmó la demanda insatisfecha?** (Sí/No + dato): [DATO PENDIENTE]
- **¿La evaluación financiera demostró rentabilidad?** (Sí/No + dato): [DATO PENDIENTE]
- **¿El modelo productivo es replicable?** (Sí/No + argumento): [DATO PENDIENTE]
- **Principal limitación encontrada durante la ejecución:** [DATO PENDIENTE]

### 7.2 Insumos para recomendaciones

- **Recomendación sobre comercialización** (canales digitales, alianzas): [DATO PENDIENTE]
- **Recomendación sobre monitoreo financiero** (qué indicador, con qué frecuencia): [DATO PENDIENTE] _(ej. "Revisar margen de contribución cada mes y variación de precios de materia prima")_
- **Recomendación sobre reinversión de utilidades:** [DATO PENDIENTE] _(ej. "Destinar 20% de utilidades a innovación de producto")_
- **Recomendación sobre capacitación del personal:** [DATO PENDIENTE]
- **Recomendación institucional** (qué debería hacer la unidad educativa o municipio): [DATO PENDIENTE]

> **Nutre:** `emprendimiento-capitulos/07_conclusiones_recomendaciones/main.tex` (secciones: conclusiones, recomendaciones)

---

## 8. Bibliografía (fuentes a incluir en `bibliografia/referencias.bib`)

1. **Referencia 1**
   - Tipo: [DATO PENDIENTE] _(ej. "Libro")_
   - Referencia completa: [DATO PENDIENTE]
   - Ya incluida en .bib: ☐
2. **Referencia 2**
   - Tipo: [DATO PENDIENTE] _(ej. "Artículo web")_
   - Referencia completa: [DATO PENDIENTE]
   - Ya incluida en .bib: ☐
3. **Referencia 3**
   - Tipo: [DATO PENDIENTE] _(ej. "Plan municipal")_
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

## 9. Anexos (material de soporte)

1. **Anexo 1:** [DATO PENDIENTE] _(ej. "Fotografías del producto terminado y del local")_
   - Tipo: [DATO PENDIENTE] _(ej. "Foto")_
   - ¿Ya disponible?: ☐
2. **Anexo 2:** [DATO PENDIENTE] _(ej. "Encuesta de mercado — cuestionario completo")_
   - Tipo: [DATO PENDIENTE] _(ej. "Documento")_
   - ¿Ya disponible?: ☐
3. **Anexo 3:** [DATO PENDIENTE] _(ej. "Organigrama del emprendimiento")_
   - Tipo: [DATO PENDIENTE] _(ej. "Diagrama")_
   - ¿Ya disponible?: ☐
4. **Anexo 4:** [DATO PENDIENTE] _(ej. "Flujograma del proceso productivo")_
   - Tipo: [DATO PENDIENTE] _(ej. "Diagrama")_
   - ¿Ya disponible?: ☐
5. **Anexo 5:** [DATO PENDIENTE] _(ej. "Cotizaciones de proveedores de maquinaria")_
   - Tipo: [DATO PENDIENTE] _(ej. "Documento")_
   - ¿Ya disponible?: ☐

> **Nutre:** `anexos/anexo_a.tex`
