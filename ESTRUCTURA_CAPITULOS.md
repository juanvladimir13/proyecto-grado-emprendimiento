# 📖 Estructura Detallada de los Capítulos — Emprendimiento Productivo

Este documento describe a detalle el contenido, propósito y archivos fuente de cada uno de los **7 capítulos** de la modalidad de **Emprendimiento Productivo** en este proyecto LaTeX, en estricto cumplimiento del Reglamento de Graduación del Bachillerato Técnico Humanístico (BTH, RM 0912/2023) en Bolivia (ver Anexo 1, inciso A de la RM 0912/2023).

Todos los archivos fuente de los capítulos se encuentran en el directorio `capitulos/` y se ensamblan modularmente a través de `capitulos/index.tex`.

---

## 🚀 Estructura de los 7 Capítulos (`capitulos/`)

### Capítulo 1: Introducción (`capitulos/01_introduccion/`)
* **Archivo de ensamble:** `capitulos/01_introduccion/main.tex`
* **Propósito:** Contextualizar el sector productivo o comercial, identificar la oportunidad detectada en el mercado, definir la propuesta de valor y fundamentar teóricamente el modelo de negocio.
* **Archivos y Contenido:**
  * `contexto_general.tex`: Caracterización del sector económico, ámbito geográfico, dinámica productiva y antecedentes que sustentan la actividad.
  * `oportunidad_negocio.tex`: Descripción fundamentada de la necesidad o demanda insatisfecha identificada en el mercado objetivo.
  * `propuesta_valor.tex`: Propuesta de valor diferencial, ventajas competitivas y factores de innovación frente a las alternativas del entorno.
  * `marco_teorico.tex`: Fundamentación teórica y conceptual (bases teóricas del modelo de negocio, marco conceptual de costos/cadena de valor y fundamentos técnicos aplicados).

### Capítulo 2: Planteamiento del Emprendimiento Productivo (`capitulos/02_planteamiento_emprendimiento/`)
* **Archivo de ensamble:** `capitulos/02_planteamiento_emprendimiento/main.tex`
* **Propósito:** Diagnosticar la realidad del contexto de mercado, definir los objetivos estratégicos y justificar la pertinencia del negocio.
* **Archivos y Contenido:**
  * `diagnostico.tex`: Diagnóstico del contexto productivo, análisis de brechas de oferta y necesidades no atendidas con respaldo de instrumentos de recolección.
  * `objetivos.tex`: Objetivos del emprendimiento productivo:
    - Objetivo general
    - Objetivos específicos (estudio de mercado, diseño organizacional/procesos, estructura de costos y precios)
    - Misión institucional (opcional)
    - Visión empresarial (opcional)
  * `justificacion.tex`: Justificación económica, social y técnica (generación de autoempleo, aprovechamiento de recursos locales y beneficio comunitario).

### Capítulo 3: Desarrollo del Emprendimiento Productivo (`capitulos/03_desarrollo_emprendimiento/`)
* **Archivo de ensamble:** `capitulos/03_desarrollo_emprendimiento/main.tex`
* **Propósito:** Planificar de forma integral las dimensiones de mercado, localización, organización, mercadotecnia, especificaciones del producto y proceso operativo.
* **Archivos y Contenido:**
  * `localizacion.tex`: Macrolocalización (departamento, provincia, accesibilidad vial) y Microlocalización (dirección o zona de emplazamiento, cercanía a clientes e insumos).
  * `analisis_mercado.tex`: Análisis de la oferta, demanda estimada, caracterización del público objetivo (segmentación demográfica/geográfica), entorno competitivo y ventaja competitiva (`tablas/estudio_mercado_ejemplo.tex`).
  * `estrategia_promocion.tex`: Canales de distribución, logística de entrega, política de precios y estrategias de promoción comercial (redes sociales, ferias, material impreso).
  * `estructura_organizacional.tex`: Forma jurídica (empresa unipersonal o asociativa), organigrama funcional y manual de funciones/cargos (`tablas/estructura_organizacional_ejemplo.tex`).
  * `diseno_producto.tex`: Características, atributos técnicos y formulación del bien o servicio; empaque, rotulado, presentación y marca comercial.
  * `ciclo_produccion.tex` *(opcional)*: Etapas del flujo de procesos operativos (desde insumos hasta producto terminado), controles de calidad, capacidad instalada y equipamiento principal.

### Capítulo 4: Viabilidad y Sostenibilidad (`capitulos/04_viabilidad_sostenibilidad/`)
* **Archivo de ensamble:** `capitulos/04_viabilidad_sostenibilidad/main.tex`
* **Propósito:** Demostrar la factibilidad económica, el requerimiento de capital, la estructura de costos y los indicadores de rentabilidad del emprendimiento.
* **Archivos y Contenido:**
  * `calculo_inversiones.tex`: Desglose del capital de inversión (activos fijos, maquinaria, herramientas, gastos preoperativos) y capital de operación inicial (`tablas/inversiones_ejemplo.tex`).
  * `costo_produccion.tex`:
    - Costos variables (materia prima directa, insumos, envases, mano de obra directa)
    - Costos fijos (alquileres, servicios, depreciaciones, sueldos administrativos) (`tablas/costos_produccion_ejemplo.tex`)
    - Indicadores de rentabilidad, margen de contribución unitario, precio de venta sugerido y punto de equilibrio operativo (`tablas/indicadores_financieros_ejemplo.tex`).

### Capítulo 5: Resultados (`capitulos/05_resultados/`)
* **Archivo de ensamble:** `capitulos/05_resultados/main.tex`
* **Propósito:** Presentar los hallazgos de las pruebas de validación comercial, ventas iniciales o pilotos de campo.
* **Archivos y Contenido:**
  * `resultados_cuantitativos.tex`: Volumen de producción colocado, ventas efectivas en bolivianos, costos incurridos y comportamiento real de la demanda frente a lo proyectado.
  * `resultados_cualitativos.tex`: Percepción del cliente, nivel de satisfacción con los atributos de valor (calidad, sabor, presentación, servicio) y retroalimentación para mejora continua.
  * `indicadores_validados.tex`: Contraste empírico de las metas financieras proyectadas vs. resultados reales de prueba piloto (`tablas/resultados_piloto_ejemplo.tex`).

### Capítulo 6: Proyecto de Vida (`capitulos/06_proyecto_vida/`)
* **Archivo de ensamble:** `capitulos/06_proyecto_vida/main.tex`
* **Propósito:** Articular el emprendimiento productivo con el plan de vida vocacional, profesional y económico del estudiante.
* **Contenido Principal (en `main.tex`):**
  * `\section{Aspiraciones académicas y profesionales}`: Metas de formación en educación superior técnica o universitaria vinculadas al rubro del negocio y continuidad del emprendimiento.
  * `\section{Competencias empresariales y socioemocionales adquiridas}`: Habilidades técnicas en costeo, comercialización, negociación, administración, sumadas a resiliencia, liderazgo y servicio.
  * `\section{Compromiso ético, independencia económica y proyección a futuro}`: Rol del negocio como fuente de autoempleo e independencia económica, proyección a 5 años y responsabilidad comunitaria.

### Capítulo 7: Conclusiones y Recomendaciones (`capitulos/07_conclusiones_recomendaciones/`)
* **Archivo de ensamble:** `capitulos/07_conclusiones_recomendaciones/main.tex`
* **Propósito:** Sintetizar los logros alcanzados respecto a los objetivos planteados y orientar las futuras etapas operativas.
* **Archivos y Contenido:**
  * `conclusiones.tex`: Síntesis del cumplimiento de los objetivos específicos (estudio de mercado, viabilidad financiera, validación de producto y modelo de negocio). Formato en viñetas (`itemize`).
  * `recomendaciones.tex`: Sugerencias estratégicas para la consolidación comercial, control de costos, ampliación de mercado y reinversión de utilidades. Formato en viñetas (`itemize`).
