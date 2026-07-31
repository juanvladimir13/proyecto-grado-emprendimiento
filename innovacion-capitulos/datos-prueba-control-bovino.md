# 📋 Ficha de Datos del Proyecto — Innovación Tecnológica (Datos de Prueba: Control Bovino)

> **Propósito:** Este archivo recopila los datos crudos (cifras, nombres, fechas, fuentes) que alimentan la redacción de cada capítulo del documento LaTeX de Innovación Tecnológica.
> No escriba prosa formal aquí; solo responda con datos concretos. Los valores marcados `[DATO PENDIENTE]` deben ser completados antes de redactar.

---

## Estructura del directorio `innovacion-capitulos/`

```text
innovacion-capitulos/
├── index.tex                                          # Ensamble de los 9 capítulos
├── datos-proyecto.md                                  # ← Este archivo (ficha de datos)
├── 01_introduccion/
│   └── main.tex                                       # Cap. 1 — INTRODUCCIÓN
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
│   └── tecnicas_instrumentos.tex                      #   └ Técnicas e instrumentos
├── 06_estrategia_mejora/
│   └── main.tex                                       # Cap. 6 — ESTRATEGIA DE MEJORA Y PROYECCIÓN
├── 07_resultados/
│   ├── main.tex                                       # Cap. 7 — RESULTADOS
│   └── beneficios_impacto.tex                         #   └ Beneficios e impacto
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

- **Nombre de la institución educativa:** Instituto Tecnológico BTH "El Sembrador"
- **Departamento / Provincia / Localidad:** Santa Cruz / Velasco / San Ignacio de Velasco
- **Programa o carrera:** Técnico Medio en Sistemas Informáticos y Electrónica
- **Título del proyecto de grado:** Sistema IoT de trazabilidad y monitoreo de salud bovina mediante collares GPS
- **Subtítulo o nombre comercial del producto/servicio:** BoviTrack Pro
- **Nombre(s) completo(s) del/los autor(es):** Carlos Mamani Quispe, Ana Rojas Silva
- **C.I. del autor principal:** 8546123 SC
- **Correo electrónico del autor:** carlos.mamani@email.com
- **Nombre completo del tutor/asesor:** Ing. Roberto Suárez
- **Grado académico y cargo del tutor:** Lic. en Ingeniería de Sistemas, Docente de Taller III
- **Ciudad y país de presentación:** San Ignacio de Velasco, Bolivia
- **Fecha de presentación (mes y año):** Diciembre 2026
- **Gestión académica:** Gestión 2026

### Páginas preliminares

- **Dedicatoria** — ¿A quién(es) se dedica y por qué en una frase?: A nuestras familias de ganaderos, por inspirarnos a mejorar su arduo trabajo diario mediante la tecnología.
- **Agradecimiento** — personas o instituciones a mencionar (nombre + relación): Al Ing. Roberto Suárez por su guía constante, y a la Asociación "El Torito" por permitir las pruebas de campo.
- **Resumen en castellano** — ¿cuál es el problema, qué se hizo y qué resultado se obtuvo? (3 frases factuales): La pérdida de ganado por extravío y enfermedades no detectadas afecta gravemente a pequeños productores. Se diseñó e implementó un collar IoT basado en ESP32 con GPS y sensor de temperatura para monitoreo remoto vía LoRa. Se logró reducir el tiempo de localización del ganado en un 85% y detectar picos febriles de forma temprana.
- **Resumen en lengua extranjera** (inglés, portugués u otro): Cattle loss due to wandering and undetected illnesses severely affects small-scale farmers. An IoT collar based on ESP32 with GPS and temperature sensors was designed and implemented for remote monitoring via LoRa. The system successfully reduced cattle location time by 85% and enabled early detection of fever spikes.
- **Resumen en lengua originaria** (aymara, quechua u otra): Wakakuna chinkasqanmanta unqusqanmanta pisilla qullqiyuq uywaqkunata llakichin. Uq IoT wallqa ESP32 GPS nisqawan, ruphay tupuyuqwan ruwasqa karqan, LoRa nisqawan karumanta qhawanapaq. Kay sistemaqa 85% pachapi wakakuna tarinapaq pisiyachirqa, chaymanta unquy qallariyninta ñawpaqmanta yacharqa.
- **Palabras clave** (mínimo 3, máximo 6): Internet de las Cosas, Ganadería de Precisión, Trazabilidad, LoRa, ESP32, Sanidad Animal

> **Nutre:** `estilos/configuracion.tex`, `preliminares/caratula.tex`, `preliminares/dedicatoria.tex`, `preliminares/agradecimiento.tex`, `preliminares/resumen.tex`

---

## 1. INTRODUCCIÓN

### 1.1 Contexto general

- **Sector o área de aplicación del proyecto:** Agropecuario / Ganadería de Precisión
- **Ámbito geográfico donde se implementa:** Municipio de San Ignacio de Velasco, Santa Cruz
- **Población o grupo social al que se dirige:** Asociación de Pequeños Ganaderos "El Torito" (30 familias productoras)
- **Situación actual del sector en Bolivia — cifra o dato relevante:** El 60% de los pequeños ganaderos reporta pérdidas económicas por abigeato, extravío y falta de monitoreo sanitario oportuno.
  - **Fuente:** CAO (Cámara Agropecuaria del Oriente), Reporte Anual 2024

### 1.2 Motivación y pertinencia

- **¿Qué evento, experiencia o necesidad personal originó la idea?:** La pérdida de 5 cabezas de ganado de la familia de los autores en 2025 debido a una enfermedad no detectada a tiempo en pastoreo extensivo.
- **¿Por qué esta solución es relevante ahora?** (política pública, tendencia, normativa): Existe una creciente demanda de certificación de trazabilidad cárnica exigida por el SENASAG para exportación y mercado interno formal.
  - **Fuente o referencia de la pertinencia:** Resolución Administrativa SENASAG 045/2023 sobre trazabilidad bovina.

### 1.3 Contribución esperada

- **¿Qué tipo de solución se propone?** (producto físico, app, sistema, servicio): Dispositivo de hardware (collar IoT) y una plataforma web de monitoreo (dashboard).
- **¿Qué mejora concreta genera respecto a la situación actual?:** Automatiza la ubicación del ganado en áreas extensas sin cobertura celular celular y emite alertas de salud tempranas.
- **¿La innovación es incremental (mejora algo existente) o disruptiva (algo nuevo)?:** Incremental (democratiza el uso de collares de alto costo adaptándolos con tecnología LoRa de bajo costo para pequeños productores).

> **Nutre:** `innovacion-capitulos/01_introduccion/main.tex`

---

## 2. PLANTEAMIENTO DEL PROBLEMA

### 2.1 Diagnóstico y descripción de la realidad

- **Lugar exacto del diagnóstico** (institución, comunidad, empresa): Estancias afiliadas a la Asociación "El Torito", San Ignacio de Velasco.
- **Fecha(s) del diagnóstico de campo:** Febrero-Marzo 2026
- **Técnica usada para diagnosticar:** Encuestas a productores y observación directa en potreros.
- **Número de personas/unidades consultadas:** 25 productores ganaderos encuestados.
- **Hallazgo cuantitativo principal:** El 80% de los productores invierte más de 12 horas semanales buscando ganado disperso en el monte.
  - **Fuente:** Encuesta de campo propia, Marzo 2026.
- **Segundo hallazgo relevante:** El 45% ha sufrido muertes de terneros por fiebre aftosa o rabia detectada demasiado tarde.
  - **Fuente:** Registros sanitarios de la asociación, Gestión 2025.
- **Deficiencia o carencia más crítica detectada:** Ausencia total de sistemas de monitoreo remoto asequibles para estancias sin cobertura de red móvil.

### 2.2 Identificación del problema

- **Enunciado del problema central** (una oración clara): Alto índice de pérdida de tiempo, dinero y ganado debido al control manual ineficiente de ubicación y salud del rebaño en zonas de pastoreo extensivo.
- **¿A quiénes afecta directamente?** (cantidad y perfil): A pequeños y medianos ganaderos con rebaños de 20 a 100 cabezas.
- **¿Desde cuándo existe el problema?:** Es un problema histórico, pero agravado recientemente por la falta de mano de obra en el campo.
- **Consecuencias si el problema no se resuelve:** Reducción del margen de ganancia, propagación de brotes infecciosos a toda la manada y abandono de la actividad ganadera.
- **Causa raíz 1:** Grandes extensiones de terreno con vegetación tupida que dificultan el avistamiento.
- **Causa raíz 2:** Alto costo de los sistemas satelitales comerciales (inviables para pequeños productores).

### 2.3 Formulación del problema

- **Pregunta de investigación principal:** ¿De qué manera la implementación de un sistema IoT basado en tecnología LoRa permite optimizar la trazabilidad y el monitoreo sanitario de ganado bovino en San Ignacio de Velasco?
- **Pregunta específica 1:** ¿Cuáles son los parámetros técnicos requeridos para lograr comunicación a larga distancia sin red celular?
- **Pregunta específica 2:** ¿Cómo procesar los datos de temperatura superficial para generar alertas sanitarias confiables?

### 2.4 Objetivos

- **Objetivo general** (verbo en infinitivo + qué + para qué): Desarrollar un sistema de trazabilidad y monitoreo IoT basado en redes LoRaWAN para reducir pérdidas por extravío y enfermedades en ganado bovino de pastoreo extensivo.
- **Objetivo específico 1:** Diseñar y ensamblar un prototipo de collar electrónico con módulo GPS y sensor de temperatura corporal.
- **Objetivo específico 2:** Configurar una red Gateway LoRa para la recepción de datos en zonas sin cobertura GSM.
- **Objetivo específico 3:** Desarrollar un dashboard web para la visualización en tiempo real de la ubicación y alertas de salud.
- **Objetivo específico 4** (opcional): Validar el funcionamiento del sistema en un entorno real con 5 cabezas de ganado durante 15 días.

### 2.5 Justificación

- **Justificación técnica** — ¿qué tecnología o conocimiento se aplica y por qué es adecuado?: Uso de LoRaWAN, ideal para enviar pequeños paquetes de datos (GPS y temperatura) a larga distancia (hasta 15km) con ultra bajo consumo de batería.
- **Justificación económica** — ¿qué ahorro, ingreso o reducción de costo genera?: Ahorro estimado de 3.000 Bs mensuales por estancia al evitar extravíos y reducir el gasto de combustible en motocicletas de búsqueda.
  - **Fuente del dato económico:** Estimación de costos operativos, Asociación "El Torito".
- **Justificación social** — ¿qué beneficio humano o comunitario produce?: Mejora la calidad de vida del productor al reducir el estrés y la carga física de patrullaje diario.
- **Número de beneficiarios directos:** 30 familias ganaderas.
- **Número de beneficiarios indirectos:** Proveedores de insumos, carnicerías locales, consumidores finales (mejor calidad de carne).
- **¿El proyecto se vincula con algún ODS? ¿Cuál(es)?:** ODS 2 - Hambre cero (promoviendo la agricultura sostenible) y ODS 9 - Industria, innovación e infraestructura.

> **Nutre:** `innovacion-capitulos/02_planteamiento_problema/main.tex` → `diagnostico.tex`, `identificacion_problema.tex`, `formulacion_problema.tex`, `objetivos.tex`, `justificacion.tex`

---

## 3. MARCO REFERENCIAL

### 3.1 Antecedentes del proyecto

1. **Antecedente 1**
   - Título: Sistema de monitoreo de ganado basado en redes WSN
   - Autor(es): López, J. y Fernández, R.
   - Año: 2022
   - Institución / País: Universidad Tecnológica Nacional, Argentina
   - Resultado o aporte clave: Demostró que el uso de acelerómetros mejora la detección de celo en las vacas.
   - Fuente: Repositorio UTN
2. **Antecedente 2**
   - Título: Uso de LoRa para trazabilidad agrícola en el altiplano
   - Autor(es): Mamani, P.
   - Año: 2023
   - Institución / País: UMSA, Bolivia
   - Resultado o aporte clave: Validó el alcance de módulos LoRa SX1278 logrando 8 km en línea de vista.
   - Fuente: Biblioteca Central UMSA
3. **Antecedente 3**
   - Título: CowTracking: App móvil para gestión ganadera
   - Autor(es): Silva, T.
   - Año: 2021
   - Institución / País: SENA, Colombia
   - Resultado o aporte clave: Interfaz gráfica orientada a usuarios no técnicos, clave para la adopción tecnológica rural.
   - Fuente: Revista Tecnológica del SENA

### 3.2 Bases teóricas

- **Teoría o modelo directamente aplicado a la solución:** Arquitectura de Internet de las Cosas (IoT) de 3 capas (Percepción, Red, Aplicación).
  - **Autor y año:** Burhan et al., 2018.
  - **Fuente bibliográfica completa:** IEEE Internet of Things Journal.
- **Segunda base teórica** (si aplica): Teoría de la propagación de ondas de radiofrecuencia.
  - **Fuente:** Rappaport, 2015. Wireless Communications.
- **Disciplina(s) científica(s) o técnica(s) base del proyecto:** Electrónica de telecomunicaciones, Desarrollo de Software Web, Veterinaria Básica.
- **Principio técnico o ley física/química aplicada** (si corresponde): Efecto Doppler (para el cálculo de posición del GPS).
  - **Fuente:** Manual técnico de posicionamiento global (GPS), Hofmann-Wellenhof, 2012.

### 3.3 Marco conceptual y normativo

1. **Concepto 1:** Trazabilidad
   - Definición operativa: Capacidad para seguir el historial, aplicación o localización del ganado desde su nacimiento hasta la comercialización.
   - Fuente: Organización Mundial de Sanidad Animal (OMSA)
2. **Concepto 2:** LoRa (Long Range)
   - Definición operativa: Tecnología de comunicación inalámbrica orientada a radioenlaces de larga distancia y bajo consumo de energía.
   - Fuente: LoRa Alliance
3. **Concepto 3:** Gateway IoT
   - Definición operativa: Enrutador que actúa como puente entre la red de sensores LoRa y el servidor central en internet.
   - Fuente: Cisco IoT Concepts
4. **Concepto 4:** Termistor (Sensor NTC)
   - Definición operativa: Componente resistivo cuyo valor varía inversamente con la temperatura.
   - Fuente: Boylestad, Electrónica Básica.

- **Norma o ley boliviana aplicable:** Ley 300 Marco de la Madre Tierra (Art. 35 sobre producción agropecuaria sustentable).
- **Norma técnica o estándar internacional aplicable:** Estándar de comunicación LoRaWAN 1.0.3 y certificación IP67 para gabinetes exteriores.
- **Reglamento institucional relevante:** Reglamento PRONAT (Programa Nacional de Trazabilidad Bovina) del SENASAG.

> **Nutre:** `innovacion-capitulos/03_marco_referencial/main.tex` → `antecedentes.tex`, `bases_teoricas.tex`, `marco_conceptual.tex`

---

## 4. DESARROLLO DE LA INNOVACIÓN

### 4.1 Diseño del producto o servicio

> Corresponde a las subsecciones: Características, Utilidad y Calidad del producto o servicio.

- **Nombre del producto/servicio innovador:** BoviTrack Pro Collar
- **Tipo** (dispositivo físico, software, app, servicio, proceso): Dispositivo Físico (Hardware) acoplado a un Dashboard Web (Software).
- **Componentes o módulos principales:** 1) Microcontrolador ESP32 LoRa (SX1276), 2) Módulo GPS Neo-6M, 3) Sensor de temperatura DS18B20 sumergible, 4) Batería Li-Po 18650 3400mAh, 5) Panel solar de 5V 1W.
- **Dimensiones o especificaciones técnicas clave:** Caja estanca de impresión 3D PETG (10x6x4 cm), peso total de 300 gramos, sujeta a correa de nylon reforzado.
- **Material(es) principal(es) de fabricación:** Filamento PETG (resistente a rayos UV), acero inoxidable (para remaches).
- **Funcionalidad principal** (qué hace paso a paso): El collar lee el GPS y la temperatura cada 30 minutos; envía la trama vía LoRa al Gateway de la estancia; el Gateway lo sube por WiFi/3G a una base de datos en la nube; el dashboard muestra la ubicación en un mapa y genera alertas rojas si la temperatura supera los 39.5°C.
- **Utilidad / valor agregado para los beneficiarios:** Permite un monitoreo 24/7 sin esfuerzo físico, previniendo robos nocturnos mediante geocercas virtuales.
- **¿Qué lo diferencia de soluciones existentes?:** Funciona sin necesitar chip de telefonía celular móvil (SIM) en el collar, logrando costo cero mensual de conexión por animal.
- **Estándar de calidad que cumple o busca cumplir:** Resistencia al polvo y agua IP67 (soporta lluvias intensas y barro).
- **Criterios de control de calidad aplicados:** Prueba de inmersión en agua por 1 hora; prueba de caída desde 2 metros; validación de precisión del GPS contrastado contra smartphone.

### 4.2 Planificación y cronograma

1. **Fase 1:** Investigación de tecnologías inalámbricas y protocolos IoT
   - Fecha inicio: 10/04/2026
   - Fecha fin: 25/04/2026
   - Responsable: Carlos Mamani
2. **Fase 2:** Diseño de la placa de circuito y modelado 3D del case
   - Fecha inicio: 26/04/2026
   - Fecha fin: 15/05/2026
   - Responsable: Ana Rojas
3. **Fase 3:** Adquisición de componentes electrónicos
   - Fecha inicio: 16/05/2026
   - Fecha fin: 30/05/2026
   - Responsable: Carlos Mamani
4. **Fase 4:** Ensamblaje, soldadura y programación de firmware (C++)
   - Fecha inicio: 01/06/2026
   - Fecha fin: 30/06/2026
   - Responsable: Carlos y Ana
5. **Fase 5:** Desarrollo del Dashboard Web (React.js y Node.js)
   - Fecha inicio: 01/07/2026
   - Fecha fin: 30/07/2026
   - Responsable: Ana Rojas
6. **Fase 6:** Implementación y pruebas de campo en estancias reales
   - Fecha inicio: 05/08/2026
   - Fecha fin: 20/08/2026
   - Responsable: Equipo completo
7. **Fase 7:** Evaluación de resultados y redacción del informe final
   - Fecha inicio: 21/08/2026
   - Fecha fin: 30/09/2026
   - Responsable: Equipo completo

### 4.3 Recursos

#### Recursos humanos

1. **Persona 1:** Carlos Mamani / Estudiante Autor
   - Función: Diseño de hardware, soldadura y pruebas de campo.
   - Dedicación: 15 horas/semana
2. **Persona 2:** Ana Rojas / Estudiante Autora
   - Función: Modelado 3D, desarrollo backend web y bases de datos.
   - Dedicación: 15 horas/semana
3. **Persona 3:** Ing. Roberto Suárez / Tutor Académico
   - Función: Revisión técnica, depuración de código y guía metodológica.
   - Dedicación: 4 horas/semana

#### Recursos materiales

1. **Material 1:** Placa Heltec LoRa 32 V3 (ESP32)
   - Cantidad: 3 unidades
   - Costo unitario (Bs): 150
   - Proveedor / Origen: Tienda de Electrónica "RoboTech" / China
2. **Material 2:** Módulo GPS Ublox Neo-6M con antena
   - Cantidad: 3 unidades
   - Costo unitario (Bs): 60
   - Proveedor / Origen: "Mundo Arduino" Santa Cruz
3. **Material 3:** Filamento PETG 1Kg
   - Cantidad: 1 rollo
   - Costo unitario (Bs): 180
   - Proveedor / Origen: Importadora 3DPrint Bolivia

#### Recursos financieros

- **Presupuesto total estimado (Bs):** 1.850
- **Fuente de financiamiento principal:** Recursos propios (Aportes personales de los estudiantes).
- **Monto financiado externamente (Bs):** 0
- **Monto financiado con recursos propios (Bs):** 1.850

### 4.4 Cálculo de costos

#### Costo de inversión (activos fijos, montaje)

1. **Ítem 1:** Computadora para programación y diseño
   - Cantidad: 1
   - Costo unitario (Bs): 3.500 (Ya se poseía, costo hundido)
   - Costo total (Bs): 0
2. **Ítem 2:** Cautín, estaño y herramientas manuales
   - Cantidad: 1 kit
   - Costo unitario (Bs): 250
   - Costo total (Bs): 250
- **Total inversión (Bs):** 250

#### Costo de operación mensual (fijos)

1. **Ítem 1:** Suscripción Hosting y Base de datos en la nube (AWS)
   - Costo mensual (Bs): 35
2. **Ítem 2:** Plan de datos móviles (chip) para el Gateway
   - Costo mensual (Bs): 50
- **Total fijos/mes (Bs):** 85

#### Costos variables (por unidad producida o ciclo)

1. **Ítem 1:** Componentes electrónicos del collar (Micro, GPS, batería)
   - Costo por unidad/ciclo (Bs): 280
2. **Ítem 2:** Carcasa impresa en 3D (costo por gr de filamento y energía)
   - Costo por unidad/ciclo (Bs): 45
3. **Ítem 3:** Correas de nylon y herrajes
   - Costo por unidad/ciclo (Bs): 25
- **Total variable/unidad (Bs):** 350

#### Indicadores financieros

- **Precio de venta o valor del servicio por unidad (Bs):** 550 Bs (incluye instalación)
- **Punto de equilibrio estimado** (unidades o meses): Venta de 2 collares cubre fijos del mes.
- **Retorno de inversión estimado** (meses): 3 meses si se comercializa localmente.

> **Nutre:** `innovacion-capitulos/04_desarrollo_innovacion/main.tex` → `diseno.tex`, `planificacion.tex`, `recursos.tex`, `calculo_costos.tex`; tablas referenciadas: `tablas/cronograma_ejemplo.tex`, `tablas/costos_ejemplo.tex`

---

## 5. METODOLOGÍA

### 5.1 Tipo de investigación

- **Enfoque de investigación:** Mixto (Cuantitativo para métricas de señal/temperatura, Cualitativo para percepción del usuario).
- **Tipo de investigación:** Aplicada-experimental
- **Alcance:** Explicativo y correlacional (relaciona la temperatura con el estado de salud).
- **Diseño metodológico:** Pre-experimental con pre-test (registro manual) y post-test (registro automatizado).
- **Justificación breve del tipo elegido:** El proyecto busca resolver un problema concreto del entorno laboral (aplicada) diseñando y probando un prototipo físico real bajo condiciones variables (experimental).
- **Autor de referencia metodológica:** Hernández Sampieri, 2014.

### 5.2 Población y muestra

- **Población total del estudio:** 1.200 cabezas de ganado de la Asociación "El Torito"
  - **Fuente del dato poblacional:** Registro Asociación 2025.
- **Tipo de muestreo:** No probabilístico por conveniencia (se eligieron animales dóciles del mismo hato).
- **Tamaño de la muestra:** 5 cabezas de ganado vacuno (raza Nelore).
- **Fórmula o criterio utilizado para determinar la muestra:** Presupuesto disponible para construir 5 prototipos funcionales para validación piloto.

### 5.3 Técnicas e instrumentos de recolección de datos

1. **Técnica 1:** Observación experimental de campo
   - Instrumento: Bitácora de pruebas electrónicas (Loggings de RSSI/SNR de señal LoRa)
   - Objetivo: Validar la distancia máxima de conexión.
   - Aplicada a: Nodos en potreros
   - Cantidad de aplicaciones: 30 registros en diferentes puntos del terreno.
2. **Técnica 2:** Medición instrumental
   - Instrumento: Termómetro clínico veterinario (patrón de control)
   - Objetivo: Contrastar el margen de error del sensor DS18B20.
   - Aplicada a: Las 5 vacas de muestra.
   - Cantidad de aplicaciones: 10 mediciones comparativas (2 por animal).
3. **Técnica 3:** Encuesta
   - Instrumento: Cuestionario de Usabilidad SUS (System Usability Scale)
   - Objetivo: Evaluar si el sistema web es fácil de entender para el ganadero.
   - Aplicada a: Productores dueños de los predios.
   - Cantidad de aplicaciones: 5 personas encuestadas post-prueba.

### 5.4 Procedimiento de análisis de datos

- **Software o herramienta de análisis utilizado:** Microsoft Excel, Python (pandas para series de tiempo).
- **Tipo de análisis aplicado:** Estadística descriptiva: cálculo de medias de error de temperatura y porcentaje de pérdida de paquetes de red.
- **Prueba estadística** (si aplica): Cálculo de Coeficiente de correlación de Pearson (entre temperatura corporal y temperatura ambiental para descartar falsos positivos).

> **Nutre:** `innovacion-capitulos/05_metodologia/main.tex` → `tipo_investigacion.tex`, `tecnicas_instrumentos.tex`

---

## 6. ESTRATEGIA DE MEJORA Y PROYECCIÓN

### 6.1 Plan de mejora continua

- **Mejora a corto plazo (0-6 meses):** Optimizar el algoritmo de "deep sleep" del ESP32 para extender la batería de 1 semana a 1 mes sin panel solar.
- **Mejora a mediano plazo (6-18 meses):** Incorporar un sensor de movimiento (acelerómetro MPU6050) para detectar patrones de cojera o ataque de depredadores.
- **Mejora a largo plazo (18+ meses):** Migrar el servidor local a AWS IoT Core para manejar datos de miles de animales simultáneamente.
- **Indicador que medirá la mejora:** Consumo de corriente en miliamperios (mA) en modo reposo.
  - Valor actual (línea base): 15 mA
  - Valor meta: 2 mA

### 6.2 Proyección y escalamiento

- **¿A qué otros lugares o poblaciones podría expandirse?:** A ganaderos de la zona del Beni, donde la geografía plana favorece aún más el alcance de las antenas LoRa.
- **Alianzas estratégicas identificadas** (instituciones, empresas, ONGs): FEGASACRUZ (Federación de Ganaderos de Santa Cruz), SENASAG.
- **Nuevas funcionalidades técnicas previstas para versiones futuras:** Sistema de identificación visual con código QR impreso en el collar para lectura rápida con celular en corral.
- **¿El proyecto tiene potencial de comercialización?** (Sí/No + argumento breve): Sí. El precio de 550 Bs ($80) es un 60% más barato que los collares satelitales importados comerciales ($200).
- **Mercado objetivo estimado** (tamaño, ubicación): Más de 5.000 medianos ganaderos en la Chiquitanía y regiones adyacentes.

> **Nutre:** `innovacion-capitulos/06_estrategia_mejora/main.tex`

---

## 7. RESULTADOS

### 7.1 Resultados obtenidos

1. **Resultado 1:** Transmisión de datos sin internet móvil
   - Dato cuantitativo o cualitativo: Se logró comunicación estable (0% pérdida de paquetes) a 4.5 km de distancia con línea de vista parcial en el monte.
   - Método de medición: Logging en el Gateway central evaluando la fuerza de señal (RSSI promedio -105 dBm).
   - Fuente / Evidencia: Capturas de pantalla de consola del servidor LoRa (Anexo B).
2. **Resultado 2:** Precisión del monitoreo térmico
   - Dato cuantitativo o cualitativo: El sensor registró temperaturas con un margen de error máximo de ±0.3°C comparado con el termómetro de mercurio veterinario.
   - Método de medición: Prueba pareada in-vivo (sensor de collar vs. toma rectal).
   - Fuente / Evidencia: Tabla de registros tabulados en Excel.
3. **Resultado 3:** Detección de anomalías en campo
   - Dato cuantitativo o cualitativo: El sistema disparó exitosamente 1 alerta de "posible celo / estrés térmico" al detectar un pico de 39.8°C en el animal V-02.
   - Método de medición: Disparo automático de Webhook desde la plataforma hacia el Telegram del usuario.
   - Fuente / Evidencia: Captura de pantalla de notificación en celular (Anexo C).

### 7.2 Beneficios e impacto

- **Social:** Los trabajadores del campo reducen su estrés laboral y exposición a accidentes al no tener que patrullar montes densos buscando ganado perdido.
  - Dato de respaldo: 5/5 trabajadores encuestados reportaron sentirse "más tranquilos" con el sistema.
  - Fuente: Cuestionario cualitativo post-implementación.
- **Tecnológico:** Democratiza el uso de IoT (Internet de las Cosas) en áreas rurales históricamente marginadas por las operadoras de telecomunicación.
  - Dato de respaldo: 1ra implementación exitosa de red LoRa en la comunidad.
  - Fuente: Registro de proyectos de la Asociación.
- **Económico:** Ahorro directo en combustible y prevención de pérdidas de capital por mortalidad o robo (una vaca promedio cuesta $400 USD).
  - Dato de respaldo: Reducción del uso de gasolina en 15 litros semanales.
  - Fuente: Control de gastos de la Estancia piloto.
- **Ambiental:** Disminuye la emisión de gases CO2 al reducir el patrullaje motorizado rutinario.
  - Dato de respaldo: Ahorro de 60 litros de gasolina al mes = reducción de aprox. 140 kg de CO2.
  - Fuente: Calculadora de huella de carbono EPA.

### 7.3 Comparación antes vs. después

1. **Indicador 1:** Tiempo de localización de un animal disperso.
   - Antes de la innovación: 3 a 5 horas promedio.
   - Después de la innovación: 2 minutos (consulta en Dashboard).
   - Variación (%): Reducción del > 95% del tiempo.
2. **Indicador 2:** Detección de fiebre.
   - Antes de la innovación: Tardía, solo cuando el animal presentaba decaimiento visible (24-48 h).
   - Después de la innovación: Inmediata (reporte automatizado cada hora).
   - Variación (%): Mejora en tiempo de reacción del 100%.

> **Nutre:** `innovacion-capitulos/07_resultados/main.tex` → `beneficios_impacto.tex`

---

## 8. PROYECTO DE VIDA

- **Carrera o profesión que el autor aspira seguir:** Ingeniería Mecatrónica o Ingeniería de Telecomunicaciones.
- **Universidad o institución donde planea continuar estudios:** Universidad Autónoma Gabriel René Moreno (UAGRM) o UCB Santa Cruz.
- **¿Cómo se vincula este proyecto con sus metas profesionales?:** Afianza la base práctica en electrónica y programación de microcontroladores que será requerida en los primeros semestres universitarios.
- **Competencias técnicas adquiridas durante el proyecto:** Programación en C++ orientado a hardware, diseño de placas PCB, manejo de redes LoRaWAN, y diseño UI en React.
- **Competencias blandas desarrolladas:** Resiliencia ante fallos técnicos, comunicación asertiva con usuarios rurales, trabajo colaborativo en GitHub.
- **¿Planea emprender con este proyecto después del grado?** (Sí/No + detalle): Sí, se planea patentar el diseño del case y buscar fondos de incubadoras (startups) agropecuarias.
- **Compromiso con la comunidad — acción concreta futura:** Realizar un taller gratuito sobre "Agricultura Digital" para los hijos de los asociados de "El Torito".
- **Meta personal a 5 años relacionada con el proyecto:** Consolidar una empresa proveedora de soluciones Agrotech (Tecnología Agrícola) líder en la región de la Chiquitanía.

> **Nutre:** `innovacion-capitulos/08_proyecto_vida/main.tex`

---

## 9. CONCLUSIONES Y RECOMENDACIONES

> Los datos de esta sección se derivan de las secciones anteriores. Complete después de tener los resultados.

### 9.1 Insumos para conclusiones

- **¿Se cumplió el objetivo general?** (Sí/Parcialmente/No + evidencia): Sí. Se desarrolló e implementó el sistema BoviTrack reduciendo el tiempo de búsqueda y reportando parámetros térmicos con éxito en la granja piloto.
- **¿Se cumplió el objetivo específico 1?:** Sí, el collar fue ensamblado en caja IP67.
- **¿Se cumplió el objetivo específico 2?:** Sí, el Gateway LoRa cubrió 4.5 km de radio efectivo.
- **¿Se cumplió el objetivo específico 3?:** Sí, el Dashboard permitió visualizar a los 5 animales en tiempo real.
- **¿Se cumplió el objetivo específico 4?:** Sí, la prueba de 15 días demostró estabilidad estructural y energética.
- **Hallazgo más importante del proyecto** (una frase factual): La tecnología LoRa es altamente resistente a la interferencia por follaje espeso en zonas de pastoreo tropical.
- **¿La viabilidad financiera se confirmó?** (Sí/No + dato): Sí, el costo de producción (350 Bs) frente a la valoración del mercado (550 Bs) deja un margen bruto del 36%, sostenible a escala.
- **Principal limitación encontrada durante la ejecución:** La falta de impresoras 3D industriales obligó a imprimir los cases de manera muy lenta caseramente.

### 9.2 Insumos para recomendaciones

- **¿Qué debería monitorearse post-implementación?** (indicador + frecuencia): La degradación de las baterías Li-Po sometidas al sol (revisión semestral).
- **¿A qué nueva población o contexto se recomienda ampliar las pruebas?:** Ganado bufalino en áreas pantanosas (para estresar el estándar de impermeabilidad IP67 al máximo).
- **¿Qué fases de la estrategia de mejora se recomienda priorizar?:** La inclusión del acelerómetro para la detección temprana de cojeras o celo dinámico.
- **Recomendación técnica para futuros proyectos similares:** Utilizar antenas LoRa direccionales de alta ganancia en el Gateway central para duplicar la cobertura sin cambiar los collares.
- **Recomendación institucional** (qué debería hacer la unidad educativa o municipio): El municipio debería instalar una antena Gateway pública (torre municipal) que brinde cobertura LoRa gratuita a todo el municipio para incentivar a estudiantes a crear sensores.

> **Nutre:** `innovacion-capitulos/09_conclusiones_recomendaciones/main.tex` → `conclusiones.tex`, `recomendaciones.tex`

---

## 10. Bibliografía (fuentes a incluir en `bibliografia/referencias.bib`)

1. **Referencia 1**
   - Tipo: Artículo Científico
   - Referencia completa: Burhan, M., Rehman, R. A., Khan, B., & Kim, B. S. (2018). IoT elements, layered architectures and security issues: A comprehensive survey. *Sensors*, 18(9), 2796.
   - Ya incluida en .bib: ☐
2. **Referencia 2**
   - Tipo: Libro
   - Referencia completa: Hofmann-Wellenhof, B., Lichtenegger, H., & Collins, J. (2012). *Global positioning system: theory and practice*. Springer Science & Business Media.
   - Ya incluida en .bib: ☐
3. **Referencia 3**
   - Tipo: Especificación Técnica
   - Referencia completa: LoRa Alliance. (2020). *LoRaWAN 1.0.4 Specification*. Technical Document.
   - Ya incluida en .bib: ☐
4. **Referencia 4**
   - Tipo: Manual Oficial
   - Referencia completa: SENASAG Bolivia. (2023). *Manual de Procedimientos del Programa Nacional de Trazabilidad (PRONAT)*. Ministerio de Desarrollo Rural y Tierras.
   - Ya incluida en .bib: ☐
5. **Referencia 5**
   - Tipo: Datasheet Componente
   - Referencia completa: Espressif Systems. (2022). *ESP32 Series Datasheet*. Recuperado de https://www.espressif.com
   - Ya incluida en .bib: ☐

> **Nutre:** `bibliografia/referencias.bib`

---

## 11. Anexos (material de soporte)

1. **Anexo A:** Diagrama esquemático de conexiones electrónicas (PCB)
   - Tipo: Plano / Esquema
   - ¿Ya disponible?: ☐
2. **Anexo B:** Capturas de consola demostrando la recepción de paquetes LoRa (RSSI)
   - Tipo: Captura de pantalla
   - ¿Ya disponible?: ☐
3. **Anexo C:** Fotografías del prototipo ensamblado colocado en el ganado (Prueba de campo)
   - Tipo: Fotografía
   - ¿Ya disponible?: ☐
4. **Anexo D:** Código fuente principal del microcontrolador (Fragmento lectura GPS)
   - Tipo: Código C++
   - ¿Ya disponible?: ☐

> **Nutre:** `anexos/anexo_a.tex`
