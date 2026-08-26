# 📋 Ficha de Datos del Proyecto — Emprendimiento Productivo

> **Propósito:** Este archivo recopila los datos crudos (cifras, nombres, fechas, fuentes) que alimentan la redacción de cada capítulo del documento LaTeX de Emprendimiento Productivo.
> No escriba prosa formal aquí; solo responda con datos concretos. Los valores marcados `[DATO PENDIENTE]` deben ser completados antes de redactar.

---

## Estructura del directorio `emprendimiento-capitulos/`

```text
emprendimiento-capitulos/
├── index.tex                                          # Ensamble de los 7 capítulos
├── datos-proyecto.md                                  # Ficha en blanco para recopilación de datos
├── datos-prueba-desayunos.md                          # ← Este archivo (datos de prueba)
├── 01_introduccion/
│   ├── main.tex                                       # Cap. 1 — INTRODUCCIÓN (ensamble)
│   ├── contexto_general.tex                           #   └ 1.1 Contexto general del sector
│   ├── oportunidad_negocio.tex                        #   └ 1.2 Identificación de la oportunidad de negocio
│   ├── propuesta_valor.tex                            #   └ 1.3 Propuesta de valor y diferenciación
│   └── marco_teorico.tex                              #   └ 1.4 Marco teórico y conceptual
├── 02_planteamiento_emprendimiento/
│   ├── main.tex                                       # Cap. 2 — PLANTEAMIENTO DEL EMPRENDIMIENTO (ensamble)
│   ├── diagnostico.tex                                #   └ 2.1 Diagnóstico del contexto productivo
│   ├── objetivos.tex                                  #   └ 2.2 Objetivos (general, específicos, misión, visión)
│   └── justificacion.tex                              #   └ 2.3 Justificación (económica, social, técnica)
├── 03_desarrollo_emprendimiento/
│   ├── main.tex                                       # Cap. 3 — DESARROLLO DEL EMPRENDIMIENTO (ensamble)
│   ├── localizacion.tex                               #   └ 3.1 Localización (macro y micro)
│   ├── analisis_mercado.tex                           #   └ 3.2 Análisis de mercado (oferta, demanda, ventaja)
│   ├── estrategia_promocion.tex                       #   └ 3.3 Estrategia de promoción y distribución
│   ├── estructura_organizacional.tex                  #   └ 3.4 Estructura organizacional (forma jurídica y cargos)
│   ├── diseno_producto.tex                            #   └ 3.5 Diseño del producto/servicio (atributos y empaque)
│   └── ciclo_produccion.tex                           #   └ 3.6 Ciclo de producción o servicio
├── 04_viabilidad_sostenibilidad/
│   ├── main.tex                                       # Cap. 4 — VIABILIDAD Y SOSTENIBILIDAD (ensamble)
│   ├── calculo_inversiones.tex                        #   └ 4.1 Inversiones (activos fijos y capital de operación)
│   └── costo_produccion.tex                           #   └ 4.2 Costos de producción e indicadores financieros
├── 05_resultados/
│   ├── main.tex                                       # Cap. 5 — RESULTADOS (ensamble)
│   ├── resultados_cuantitativos.tex                   #   └ 5.1 Resultados cuantitativos y ventas piloto
│   ├── resultados_cualitativos.tex                    #   └ 5.2 Aceptación y percepción de calidad
│   └── indicadores_validados.tex                      #   └ 5.3 Indicadores de rentabilidad validados
├── 06_proyecto_vida/
│   └── main.tex                                       # Cap. 6 — PROYECTO DE VIDA (metas, competencias, ética)
└── 07_conclusiones_recomendaciones/
    ├── main.tex                                       # Cap. 7 — CONCLUSIONES Y RECOMENDACIONES (ensamble)
    ├── conclusiones.tex                               #   └ Conclusiones
    └── recomendaciones.tex                            #   └ Recomendaciones
```

---

## 0. Datos Generales e Institucionales

> Estos datos alimentan `estilos/configuracion.tex`, la carátula y las páginas preliminares.

- **Nombre de la institución educativa:** Unidad Educativa "San José"
- **Departamento / Provincia / Localidad:** Cochabamba / Cercado / Cochabamba
- **Programa o carrera:** Programa de Emprendimiento Productivo y Gastronomía
- **Título del proyecto de grado:** Creación de una empresa de desayunos especiales sorpresa a domicilio
- **Subtítulo o nombre comercial del emprendimiento:** "Amanecer Feliz - Desayunos Sorpresa"
- **Nombre(s) completo(s) del/los emprendedor(es):** María Elena Rojas Pinto
- **C.I. del emprendedor principal:** 7891234 Cba.
- **Correo electrónico del emprendedor:** maria.rojas.amanecer@gmail.com
- **Nombre completo del tutor/asesor:** Lic. Carlos Pérez Morales
- **Grado académico y cargo del tutor:** Licenciado en Administración de Empresas, Docente Asesor
- **Ciudad y país de presentación:** Cochabamba, Bolivia
- **Fecha de presentación (mes y año):** Noviembre 2026
- **Gestión académica:** Gestión 2026

### Páginas preliminares

- **Dedicatoria** — ¿A quién(es) se dedica y por qué en una frase?: A mis padres, por su apoyo incondicional en cada paso de mi formación.
- **Agradecimiento** — personas o instituciones a mencionar (nombre + relación): A la Unidad Educativa "San José" y a mis docentes por las herramientas brindadas.
- **Resumen en castellano** — ¿cuál es el negocio, qué se hizo y qué resultado se obtuvo? (3 frases factuales): Se desarrolló un plan de negocios para una empresa de desayunos sorpresa a domicilio en Cochabamba. Se evaluó la viabilidad técnica y económica, determinando una alta demanda en fechas festivas. El proyecto demostró ser rentable con un retorno de inversión en el primer año.
- **Resumen en lengua extranjera** (inglés, portugués u otro): A business plan was developed for a surprise breakfast delivery company in Cochabamba. Technical and economic feasibility were evaluated, showing high demand during holidays. The project proved profitable with a return on investment within the first year.
- **Resumen en lengua originaria** (aymara, quechua u otra): Sumaq paqariy mikhuna rurayta qallarirqayku Quchapampa llaqtapi, runakunaman kusiyta apanapaq.
- **Palabras clave** (mínimo 3, máximo 6): Desayunos sorpresa, emprendimiento, gastronomía, delivery, regalos.

> **Nutre:** `estilos/configuracion.tex`, `preliminares/caratula.tex`, `preliminares/dedicatoria.tex`, `preliminares/agradecimiento.tex`, `preliminares/resumen.tex`

---

## 1. INTRODUCCIÓN

### 1.1 Contexto general del emprendimiento

- **Sector productivo o de servicio:** Servicios y Alimentos
- **Rubro específico:** Servicio de catering y regalos personalizados (Desayunos sorpresa)
- **Ámbito geográfico del mercado:** Zona Norte y Centro de Cochabamba, radio de 10 km
- **Situación actual del rubro en la zona — cifra o dato relevante:** El envío de regalos a domicilio ha crecido un 40% en los últimos dos años en la ciudad.
  - **Fuente:** Observatorio Económico Local, Enero 2026

### 1.2 Oportunidad de negocio

- **¿Qué necesidad insatisfecha del mercado se detectó?:** Falta de opciones de regalos matutinos saludables, personalizados y con entrega puntual.
- **¿Qué evento, experiencia o necesidad personal originó la idea de negocio?:** La dificultad de encontrar un regalo original y de calidad para el Día de la Madre desde el extranjero.
- **¿Por qué este emprendimiento es relevante ahora?:** Por el estilo de vida ajetreado que impide a las personas preparar sorpresas elaboradas para sus seres queridos.
  - **Fuente o referencia de la pertinencia:** Tendencias de consumo de conveniencia post-pandemia.

### 1.3 Propuesta de valor

- **¿Qué producto o servicio se ofrece?:** Desayunos gourmet empacados en cajas decorativas con temáticas personalizadas, entregados a domicilio.
- **¿Qué lo diferencia de lo que ya existe en el mercado?:** Uso de ingredientes orgánicos locales y la posibilidad de personalizar completamente el mensaje y la temática (tazas, globos, fotos).
- **Alcance empresarial planteado** (local, regional, departamental): Local (Cochabamba Cercado)

### 1.4 Marco teórico

- **Disciplina(s) o área(s) de conocimiento base del emprendimiento:** Gastronomía, Marketing, Logística
- **Teoría o modelo empresarial de referencia:** Modelo Canvas de Osterwalder, 2010
  - **Fuente bibliográfica:** Osterwalder, A. & Pigneur, Y. (2010). Generación de modelos de negocio.
- **Segunda teoría o concepto complementario:** Teoría del Comportamiento del Consumidor
  - **Fuente bibliográfica:** Kotler, P. (2012). Dirección de Marketing.

1. **Concepto 1:** Desayuno Sorpresa
   - Definición breve: Servicio que combina alimentos matutinos y detalles de regalo entregados a domicilio.
   - Fuente: Revista Emprender (2023)
2. **Concepto 2:** Marketing Emocional
   - Definición breve: Estrategias diseñadas para apelar a las emociones y sentimientos de los consumidores.
   - Fuente: Kotler (2012)
3. **Concepto 3:** Logística de Última Milla
   - Definición breve: El paso final del proceso de entrega desde un centro de distribución o local hasta el usuario final.
   - Fuente: Supply Chain Management Review (2024)
4. **Concepto 4:** Costeo Basado en Actividades (ABC)
   - Definición breve: Método de asignación de costos que identifica actividades en una organización y asigna el costo de cada actividad a los productos.
   - Fuente: Horngren (2010)

> **Nutre:** `emprendimiento-capitulos/01_introduccion/main.tex` → `contexto_general.tex`, `oportunidad_negocio.tex`, `propuesta_valor.tex`, `marco_teorico.tex`

---

## 2. PLANTEAMIENTO DEL EMPRENDIMIENTO PRODUCTIVO

### 2.1 Diagnóstico del contexto productivo

- **Lugar exacto del diagnóstico** (barrio, comunidad, zona comercial): Redes sociales y sondeo presencial en Plaza de las Banderas
- **Fecha(s) del diagnóstico de campo:** Febrero-Marzo 2026
- **Técnica usada para diagnosticar:** Encuesta online y entrevistas cortas
- **Número de personas consultadas:** 120 personas
- **Brecha de oferta detectada** (dato cuantitativo): El 75% de los encuestados ha tenido problemas con la impuntualidad en servicios de entrega de regalos.
  - **Fuente:** Encuesta propia, Marzo 2026
- **Segundo hallazgo relevante:** El 60% prefiere opciones saludables (jugos naturales, sándwiches integrales) sobre opciones altas en azúcar.
  - **Fuente:** Encuesta propia, Marzo 2026
- **Necesidad no atendida más crítica:** Entregas puntuales antes de las 7:00 am con productos frescos.

### 2.2 Objetivos del emprendimiento productivo

- **Objetivo general** (verbo en infinitivo + qué + para qué): Establecer una microempresa de desayunos sorpresa personalizados a domicilio en la ciudad de Cochabamba para ofrecer una alternativa innovadora y de calidad en regalos matutinos.
- **Objetivo específico 1:** Diseñar menús variados (saludables, tradicionales, infantiles) que se adapten a diferentes gustos y presupuestos.
- **Objetivo específico 2:** Implementar un sistema de logística eficiente que garantice entregas puntuales entre las 6:30 am y 9:00 am.
- **Objetivo específico 3:** Desarrollar una estrategia de marketing digital enfocada en redes sociales para captar clientes en fechas especiales y cumpleaños.
- **Objetivo específico 4** (opcional): Evaluar la viabilidad económica y financiera del proyecto durante el primer año de operaciones.
- **Misión del emprendimiento** (opcional): Entregar momentos de felicidad y conexión a través de desayunos sorpresa elaborados con amor y calidad.
- **Visión del emprendimiento** (opcional): Ser la empresa líder en Cochabamba en regalos y desayunos sorpresa, reconocida por su puntualidad y creatividad.

### 2.3 Justificación

- **Justificación económica** — ¿qué empleo, ingreso o dinamización económica genera?: Genera 2 empleos directos (cocina y logística) y fomenta la compra a proveedores locales de frutas y panadería.
  - **Fuente:** Plan de Negocios "Amanecer Feliz"
- **Justificación social** — ¿qué beneficio humano o comunitario produce?: Fortalece los vínculos afectivos entre familiares y amigos, promoviendo el bienestar emocional.
- **Justificación técnica** — ¿qué conocimiento o tecnología se aplica?: Aplicación de técnicas de conservación de alimentos y uso de plataformas digitales para gestión de pedidos.
- **Número de beneficiarios directos** (clientes): Estimado 50 clientes al mes inicialmente.
- **Número de beneficiarios indirectos** (proveedores, familias de empleados): 3 proveedores locales y familias de 2 empleados.
- **Aprovechamiento de recursos locales mencionado:** Uso de frutas de temporada del Valle Alto y productos lácteos locales.

> **Nutre:** `emprendimiento-capitulos/02_planteamiento_emprendimiento/main.tex` → `diagnostico.tex`, `objetivos.tex`, `justificacion.tex`

---

## 3. DESARROLLO DEL EMPRENDIMIENTO PRODUCTIVO

### 3.1 Localización del emprendimiento

- **Macrolocalización** (departamento, provincia, municipio): Cochabamba, Provincia Cercado, Municipio de Cochabamba
- **Microlocalización** (dirección exacta o zona): Zona Norte, Av. América y Santa Cruz
- **Argumento de cercanía a insumos:** Acceso rápido a mercados de abastecimiento mayorista para frutas y empaques.
- **Argumento de cercanía a clientes:** Ubicación central para optimizar rutas de entrega hacia zonas de alta demanda (Zona Norte y Centro).
- **Costo de alquiler o propiedad del local (Bs/mes):** 1.500 Bs (Cocina taller/coworking)
  - **Fuente:** Cotización Inmobiliaria, Febrero 2026

### 3.2 Análisis de mercado

#### Oferta (competidores)

1. **Competidor 1**
   - Nombre: Sorpresas Cbba
   - Ubicación: Zona Centro
   - Producto/servicio que ofrece: Desayunos tradicionales y arreglos florales
   - Precio referencial (Bs): 150 Bs
   - Fortaleza: Marca conocida, muchos seguidores en Facebook
   - Debilidad: Poca innovación en los menús, quejas por demoras
2. **Competidor 2**
   - Nombre: Regalos Express
   - Ubicación: Zona Sur
   - Producto/servicio que ofrece: Cajas de chocolates y desayunos básicos
   - Precio referencial (Bs): 120 Bs
   - Fortaleza: Precios bajos
   - Debilidad: Baja calidad en los empaques, productos no frescos
3. **Competidor 3**
   - Nombre: Desayunos Fit & Love
   - Ubicación: Zona Norte
   - Producto/servicio que ofrece: Desayunos saludables y veganos
   - Precio referencial (Bs): 180 Bs
   - Fortaleza: Nicho de mercado específico, productos de alta calidad
   - Debilidad: Precios elevados, catálogo limitado

#### Demanda

- **Volumen estimado de consumo** (unidades/mes o Bs/mes en la zona): Mercado potencial de 500 desayunos/mes en fechas ordinarias, triplicándose en fechas especiales.
- **Frecuencia de compra del cliente típico:** 1 a 2 veces al año (cumpleaños, aniversarios).
- **Patrón de compra detectado:** Pedidos realizados con 2 a 3 días de anticipación; picos de entrega los fines de semana.
  - **Fuente del dato de demanda:** Análisis de tendencias de búsqueda en Google Trends y encuestas.

#### Público objetivo (cliente y/o usuario)

- **Segmento demográfico:** Personas de 18 a 45 años.
- **Segmento geográfico:** Residentes de Cochabamba o personas en el extranjero con familiares en la ciudad.
- **Segmento socioeconómico:** Clase media y media-alta (Ingreso familiar > 4.000 Bs/mes).
- **Necesidad principal del cliente:** Sorprender a un ser querido con un regalo útil, estético y puntual.

#### Entorno y competencia

- **Factor político/legal relevante:** Normativas de inocuidad alimentaria (SENASAG).
- **Factor económico relevante:** Estabilidad en el precio de insumos básicos (lácteos, panadería).
  - **Fuente:** INE, Reporte de Inflación 2025
- **Factor social/cultural relevante:** Alta valoración cultural de la comida y la celebración de fechas festivas (Día de la Madre, de la Amistad).
  - **Fuente:** Estudio de Consumo Cultural Cbba 2025
- **Barreras de entrada al mercado:** Bajas barreras de inversión, pero alta exigencia en calidad logística.

#### Ventaja competitiva

- **Propuesta de valor única** (una frase): Desayunos sorpresa gourmet, altamente personalizados y con garantía de entrega puntual.
- **Diferenciador principal vs. competencia:** Garantía de puntualidad (devolución del 20% si hay demora mayor a 15 min) y empaques eco-amigables.
- **Segundo diferenciador:** Opción de incluir fotos impresas y mensajes grabados en audio mediante código QR.

### 3.3 Estrategia de promoción y distribución

- **Canales de distribución:** Venta online directa mediante WhatsApp y catálogo en Instagram.
- **Estrategia de precio:** Precio de penetración premium: desde 130 Bs hasta 250 Bs dependiendo del menú y la personalización.
- **Estrategia de marketing/publicidad:** Campañas en Instagram/TikTok Ads, influencers locales para unboxing, programa de referidos.
- **Presupuesto estimado de marketing (Bs/mes):** 500 Bs (Pauta digital y muestras).

### 3.4 Estructura organizacional

- **Forma jurídica del emprendimiento:** Empresa Unipersonal
- **Número total de empleados previstos:** 3 (incluyendo al emprendedor)

1. **Cargo 1:** Gerente/Administrador (Emprendedor)
   - Función principal: Gestión de pedidos, compras, marketing y atención al cliente.
   - Sueldo/remuneración (Bs/mes): 2.500 Bs
2. **Cargo 2:** Encargado de Producción (Medio tiempo)
   - Función principal: Preparación de alimentos y ensamblado de las cajas sorpresa.
   - Sueldo/remuneración (Bs/mes): 1.200 Bs
3. **Cargo 3:** Repartidor / Logística (Por pedido)
   - Función principal: Entrega de los desayunos en las rutas asignadas.
   - Sueldo/remuneración (Bs/mes): Pago por entrega (Aprox. 1.000 Bs/mes)

### 3.5 Diseño de producto o servicio

- **Nombre comercial del producto/servicio:** "Caja Amanecer Clásica"
- **Características técnicas** (tamaño, peso, ingredientes, materiales): Caja de madera MDF (30x20x10 cm), taza personalizada, sándwich de jamón y queso, jugo natural 300ml, postre (cupcake), tarjeta y globo.
- **Empaque / presentación:** Empaque premium con cinta de satín, papel seda interior y tarjeta de presentación.
- **Marca registrada** (si aplica): En trámite ante SENAPI.
- **Diferenciadores de calidad:** Jugos prensados en frío, panadería artesanal del día.

### 3.6 Ciclo de producción o servicio (opcional)

- **Etapas del proceso productivo** (listar en orden): 1) Recepción de pedido (T-48h) → 2) Compra de insumos frescos (T-24h) → 3) Personalización de taza/tarjeta (T-12h) → 4) Preparación de alimentos (Día D, 5:00 am) → 5) Ensamblado y decoración (Día D, 6:00 am) → 6) Ruta de entrega (Día D, 7:00 am) → 7) Confirmación al comprador.
- **Tiempo total del ciclo** (de inicio a producto terminado): 48 horas (preparación logística), 2 horas (ensamblado físico).
- **Capacidad de producción por ciclo:** Hasta 15 desayunos por mañana.
- **Equipo o maquinaria principal utilizada:** Licuadora semi-industrial, sandwichera/parrilla, impresora a color para fotos/tarjetas.

> **Nutre:** `emprendimiento-capitulos/03_desarrollo_emprendimiento/main.tex` → `localizacion.tex`, `analisis_mercado.tex`, `estrategia_promocion.tex`, `estructura_organizacional.tex`, `diseno_producto.tex`, `ciclo_produccion.tex`; tablas referenciadas: `tablas/estudio_mercado_ejemplo.tex`, `tablas/estructura_organizacional_ejemplo.tex`

---

## 4. VIABILIDAD Y SOSTENIBILIDAD

### 4.1 Cálculo de inversiones

#### Capital de inversión (activos fijos, infraestructura, montaje)

1. **Ítem 1:** Equipamiento de cocina (Licuadora, sandwichera, utensilios)
   - Cantidad: 1 set
   - Costo unitario (Bs): 1.500 Bs
   - Costo total (Bs): 1.500 Bs
2. **Ítem 2:** Equipamiento de oficina (Laptop, impresora a color)
   - Cantidad: 1 set
   - Costo unitario (Bs): 4.000 Bs
   - Costo total (Bs): 4.000 Bs
3. **Ítem 3:** Insumos de montaje (Cajas MDF, tazas en blanco, cintas, globos)
   - Cantidad: Lote inicial 50 un.
   - Costo unitario (Bs): 30 Bs
   - Costo total (Bs): 1.500 Bs
4. **Ítem 4:** Trámites de formalización (Fundaempresa, NIT, etc.)
   - Cantidad: 1
   - Costo unitario (Bs): 500 Bs
   - Costo total (Bs): 500 Bs
- **Total capital de inversión (Bs):** 7.500 Bs

#### Capital de operación (primeros meses antes de percibir ingresos continuos)

1. **Ítem 1:** Compra de alimentos (mes 1 y 2)
   - Meses cubiertos: 2
   - Costo total (Bs): 2.000 Bs
2. **Ítem 2:** Alquiler de taller
   - Meses cubiertos: 2
   - Costo total (Bs): 3.000 Bs
3. **Ítem 3:** Presupuesto de publicidad digital
   - Meses cubiertos: 2
   - Costo total (Bs): 1.000 Bs
4. **Ítem 4:** Reserva para imprevistos logísticos
   - Meses cubiertos: 2
   - Costo total (Bs): 1.000 Bs
- **Total capital de operación (Bs):** 7.000 Bs

#### Resumen de inversión

- **Inversión total (inversión + operación) (Bs):** 14.500 Bs
- **Fuente de financiamiento principal:** Ahorros personales y aporte familiar.
- **Monto financiado externamente (Bs):** 0 Bs
- **Monto financiado con recursos propios (Bs):** 14.500 Bs

### 4.2 Costo de producción

#### Costos variables (por unidad o lote producido - ej. 1 Desayuno)

1. **Insumo 1:** Alimentos (sándwich, jugo, postre)
   - Cantidad por lote: 1 set
   - Costo unitario (Bs): 35 Bs
   - Costo por lote (Bs): 35 Bs
2. **Insumo 2:** Empaque y decoración (Caja, tarjeta, globo)
   - Cantidad por lote: 1 set
   - Costo unitario (Bs): 20 Bs
   - Costo por lote (Bs): 20 Bs
3. **Insumo 3:** Personalización (Taza sublimada / foto)
   - Cantidad por lote: 1 un
   - Costo unitario (Bs): 15 Bs
   - Costo por lote (Bs): 15 Bs
4. **Insumo 4:** Costo de envío (Pago a repartidor)
   - Cantidad por lote: 1
   - Costo unitario (Bs): 15 Bs
   - Costo por lote (Bs): 15 Bs
- **Total costo variable/lote (Bs):** 85 Bs
- **Costo variable por unidad (Bs):** 85 Bs
- **Unidades por lote:** 1 (por desayuno)

#### Costos fijos (mensuales, independientes del volumen)

1. **Ítem 1:** Alquiler del local (taller)
   - Costo mensual (Bs): 1.500 Bs
2. **Ítem 2:** Servicios básicos (luz, agua, internet)
   - Costo mensual (Bs): 350 Bs
3. **Ítem 3:** Sueldos (Gerente y Ayudante)
   - Costo mensual (Bs): 3.700 Bs
4. **Ítem 4:** Publicidad y mantenimiento de redes
   - Costo mensual (Bs): 500 Bs
- **Total costos fijos/mes (Bs):** 6.050 Bs

#### Indicadores financieros

- **Precio de venta por unidad (Bs):** 160 Bs
- **Margen de ganancia por unidad** (Bs y %): 75 Bs (46.8% sobre el precio de venta)
- **Punto de equilibrio** (unidades/mes): 81 unidades (6.050 / 75)
- **Ingreso mensual proyectado (Bs):** 16.000 Bs (Venta de 100 desayunos/mes)
- **Utilidad neta mensual proyectada (Bs):** 1.450 Bs (100 desayunos: Ingreso 16000 - C.Var 8500 - C.Fijos 6050)
- **Retorno de inversión estimado** (meses): 10 meses

> **Nutre:** `emprendimiento-capitulos/04_viabilidad_sostenibilidad/main.tex` → `calculo_inversiones.tex`, `costo_produccion.tex`; tablas referenciadas: `tablas/inversiones_ejemplo.tex`, `tablas/costos_produccion_ejemplo.tex`, `tablas/indicadores_financieros_ejemplo.tex`

---

## 5. RESULTADOS

### 5.1 Resultados cuantitativos

1. **Resultado 1:** Ventas en etapa de lanzamiento
   - Dato obtenido: 45 desayunos vendidos en el primer mes de operaciones, 120 en el mes del Día de la Madre.
   - Método de medición: Registro de ventas e ingresos diarios.
   - Fuente / Evidencia: Libro de ventas.
2. **Resultado 2:** Margen de ganancia real
   - Dato obtenido: Margen de 45%, ligeramente menor al 46.8% proyectado por un incremento temporal en el precio de frutas.
   - Método de medición: Análisis de costos reales post-producción.
   - Fuente / Evidencia: Flujo de caja del primer trimestre.
3. **Resultado 3:** Eficiencia en entregas (Puntualidad)
   - Dato obtenido: 95% de las entregas realizadas dentro de la ventana de 15 minutos prometida.
   - Método de medición: Tracking de horarios de entrega por GPS.
   - Fuente / Evidencia: Reporte de logística.

### 5.2 Resultados cualitativos

1. **Aspecto 1:** Satisfacción del cliente final y del comprador
   - Resultado: 98% de calificaciones positivas (5 estrellas) en la página de Facebook e Instagram.
   - Fuente / Evidencia: Reseñas en redes sociales.
2. **Aspecto 2:** Posicionamiento de marca
   - Resultado: Reconocimiento de "Amanecer Feliz" por la estética de sus cajas y la inclusión del audio QR.
   - Fuente / Evidencia: Comentarios cualitativos de usuarios.

### 5.3 Indicadores de rentabilidad validados

1. **Indicador 1:** Margen de ganancia unitario
   - Valor proyectado: 75 Bs
   - Valor real/validado: 72 Bs
   - Variación: -4%
2. **Indicador 2:** Punto de equilibrio (1er semestre)
   - Valor proyectado: 81 unidades/mes
   - Valor real/validado: Se alcanzó un promedio de 85 unidades/mes.
   - Variación: +5% (superó el punto de equilibrio)

> **Nutre:** `emprendimiento-capitulos/05_resultados/main.tex` → `resultados_cuantitativos.tex`, `resultados_cualitativos.tex`, `indicadores_validados.tex`; tablas referenciadas: `tablas/resultados_piloto_ejemplo.tex`

---

## 6. PROYECTO DE VIDA

- **Carrera o profesión que el emprendedor aspira seguir:** Ingeniería Comercial o Gastronomía.
- **Universidad o institución donde planea continuar estudios:** Universidad Mayor de San Simón (UMSS) o Instituto Técnico de Gastronomía.
- **¿Cómo se vincula este emprendimiento con sus metas profesionales?:** Proporciona experiencia práctica en gestión de negocios, marketing digital y atención al cliente, áreas clave para la Ingeniería Comercial.
- **¿Planea continuar con la empresa después del grado?** (Sí/No + detalle): Sí, se planea mantener la operación durante los estudios universitarios contratando un asistente adicional.
- **Competencias empresariales adquiridas durante el proyecto:** Gestión de costos logísticos, manejo de redes sociales comerciales, negociación con proveedores mayoristas.
- **Competencias blandas desarrolladas:** Liderazgo, resolución de problemas bajo presión (horarios matutinos), y empatía comercial.
- **Compromiso ético con la comunidad — acción concreta futura:** Utilizar exclusivamente envases biodegradables y donar los excedentes de insumos perecederos a un hogar de niños los fines de semana.
- **Rol del emprendimiento como vehículo de independencia económica:** Generar ingresos suficientes para cubrir el 100% de los gastos universitarios futuros.
- **Meta personal a 5 años relacionada con la empresa:** Abrir un local físico estilo "Café y Regalos" y expandir el servicio a eventos corporativos (coffee breaks).

> **Nutre:** `emprendimiento-capitulos/06_proyecto_vida/main.tex`

---

## 7. CONCLUSIONES Y RECOMENDACIONES

> Los datos de esta sección se derivan de las secciones anteriores. Complete después de tener los resultados.

### 7.1 Insumos para conclusiones

- **¿Se cumplió el objetivo general?** (Sí/Parcialmente/No + evidencia): Sí, se estableció la microempresa y se lograron ventas sostenidas que superaron el punto de equilibrio en fechas clave.
- **¿Se cumplió el objetivo específico 1?:** Sí, se diseñaron 4 menús estándar que tuvieron buena rotación (Clásico, Fit, Dulce, Infantil).
- **¿Se cumplió el objetivo específico 2?:** Sí, la logística externalizada por pedido permitió un 95% de éxito en puntualidad.
- **¿Se cumplió el objetivo específico 3?:** Sí, el marketing en redes sociales logró captar el 90% de los clientes actuales, demostrando su efectividad.
- **¿El análisis de mercado confirmó la demanda insatisfecha?** (Sí/No + dato): Sí, la alta demanda por el valor agregado de la personalización (audio QR) demostró que el mercado buscaba opciones más originales.
- **¿La evaluación financiera demostró rentabilidad?** (Sí/No + dato): Sí, el negocio proyecta recuperar la inversión en 10 meses con una utilidad neta promedio mensual de 1.450 Bs inicial.
- **¿El modelo productivo es replicable?** (Sí/No + argumento): Sí, los procesos estandarizados de compras y ensamblado permiten replicar el modelo en otras zonas geográficas.
- **Principal limitación encontrada durante la ejecución:** La dependencia de terceros (repartidores independientes) para garantizar la puntualidad extrema en días de lluvia o tráfico inusual.

### 7.2 Insumos para recomendaciones

- **Recomendación sobre comercialización** (canales digitales, alianzas): Implementar un catálogo automatizado vía WhatsApp Business y realizar alianzas con floristerías para ofrecer combos cruzados.
- **Recomendación sobre monitoreo financiero** (qué indicador, con qué frecuencia): Monitorear semanalmente el precio de las frutas de temporada para ajustar los costos variables y no afectar el margen de ganancia.
- **Recomendación sobre reinversión de utilidades:** Destinar el 30% de las utilidades iniciales a la compra de una impresora 3D pequeña para crear souvenirs personalizados únicos.
- **Recomendación sobre capacitación del personal:** Capacitar al personal de logística en servicio al cliente, ya que son el único contacto físico de la marca con el agasajado.
- **Recomendación institucional** (qué debería hacer la unidad educativa o municipio): Que el municipio promueva ferias específicas de emprendimientos juveniles para visibilizar marcas nuevas sin costo de stand.

> **Nutre:** `emprendimiento-capitulos/07_conclusiones_recomendaciones/main.tex` → `conclusiones.tex`, `recomendaciones.tex`

---

## 8. Bibliografía (fuentes a incluir en `bibliografia/referencias.bib`)

1. **Referencia 1**
   - Tipo: Libro
   - Referencia completa: Osterwalder, A. y Pigneur, Y. (2010). Generación de modelos de negocio. Deusto.
   - Ya incluida en .bib: ☐
2. **Referencia 2**
   - Tipo: Libro
   - Referencia completa: Kotler, P. y Keller, K. (2012). Dirección de Marketing (14a ed.). Pearson Educación.
   - Ya incluida en .bib: ☐
3. **Referencia 3**
   - Tipo: Artículo web
   - Referencia completa: Revista Emprender. (2023). El auge de los negocios de regalos a domicilio post-pandemia. Recuperado de https://ejemplo.com/articulo
   - Ya incluida en .bib: ☐
4. **Referencia 4**
   - Tipo: Informe Institucional
   - Referencia completa: Instituto Nacional de Estadística (INE). (2025). Índice de Precios al Consumidor y Canasta Familiar.
   - Ya incluida en .bib: ☐
5. **Referencia 5**
   - Tipo: Artículo web
   - Referencia completa: Supply Chain Management Review. (2024). Estrategias de última milla para pequeñas empresas. Recuperado de https://ejemplo.com/logistica
   - Ya incluida en .bib: ☐

> **Nutre:** `bibliografia/referencias.bib`

---

## 9. Anexos (material de soporte)

1. **Anexo 1:** Fotografías del producto (Caja Amanecer Clásica)
   - Tipo: Foto
   - ¿Ya disponible?: ☐
2. **Anexo 2:** Resultados gráficos de la encuesta de mercado
   - Tipo: Gráficos
   - ¿Ya disponible?: ☐
3. **Anexo 3:** Organigrama de la empresa "Amanecer Feliz"
   - Tipo: Diagrama
   - ¿Ya disponible?: ☐
4. **Anexo 4:** Flujograma de recepción de pedido y producción
   - Tipo: Diagrama
   - ¿Ya disponible?: ☐
5. **Anexo 5:** Diseño de tarjeta y código QR de ejemplo
   - Tipo: Documento/Imagen
   - ¿Ya disponible?: ☐

> **Nutre:** `anexos/anexo_a.tex`
