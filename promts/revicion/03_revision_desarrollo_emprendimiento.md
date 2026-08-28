# Prompt: Revisión del Desarrollo del Emprendimiento Productivo (Capítulo 3)

## Cuándo usar este prompt
Al finalizar la redacción del borrador del **Capítulo 3: Desarrollo del Emprendimiento Productivo** (`capitulos/03_desarrollo_emprendimiento/`).

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier revisión.
2. Obtén los datos del proyecto desde `estilos/configuracion.tex` (`\tituloproyecto`, `\especialidad`, `\modalidad`).
3. Lee directamente los archivos `.tex` indicados en la sección "Archivos a revisar".
4. Revisa las tablas asociadas en `tablas/` (`estudio_mercado_ejemplo.tex`, `estructura_organizacional_ejemplo.tex`).
5. Consulta `docs/ficha-proyecto.md` (Sección 3) para contrastar los datos operativos y de mercado.

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Sustituye los campos entre `[corchetes]` con los datos de tu proyecto.
3. Pega el contenido LaTeX de los archivos `.tex` y tablas correspondientes al final.

---

## Archivos a revisar

| Archivo | Contenido |
| :--- | :--- |
| `capitulos/03_desarrollo_emprendimiento/main.tex` | Ensamble del capítulo (`\chapter` y `\input` de las secciones) |
| `capitulos/03_desarrollo_emprendimiento/localizacion.tex` | Macrolocalización y microlocalización del emprendimiento |
| `capitulos/03_desarrollo_emprendimiento/analisis_mercado.tex` | Oferta, demanda, público objetivo, competencia y ventaja competitiva (`tablas/estudio_mercado_ejemplo.tex`) |
| `capitulos/03_desarrollo_emprendimiento/estrategia_promocion.tex` | Canales de distribución, logística de entrega, fijación de precios y promoción comercial |
| `capitulos/03_desarrollo_emprendimiento/estructura_organizacional.tex` | Forma jurídica, organigrama y manual de funciones (`tablas/estructura_organizacional_ejemplo.tex`) |
| `capitulos/03_desarrollo_emprendimiento/diseno_producto.tex` | Características técnicas, formulación, empaque, presentación y marca comercial |
| `capitulos/03_desarrollo_emprendimiento/ciclo_produccion.tex` | Etapas del proceso productivo, capacidad instalada y equipamiento principal (opcional) |

---

## PROMPT

Actúa como un **evaluador de planes de negocio y operaciones productivas BTH**. Analiza exhaustivamente el **Capítulo 3: Desarrollo del Emprendimiento Productivo** que te proporcionaré, verificando la factibilidad comercial, la precisión operativa y la coherencia del diseño del bien o servicio.

### Contexto del documento
- Modalidad: Emprendimiento Productivo (BTH Bolivia, RM 0912/2023, Anexo 1, inciso A)
- Especialidad técnica: [lee `\especialidad` de `estilos/configuracion.tex` o completa aquí]
- Título del proyecto: [lee `\tituloproyecto` de `estilos/configuracion.tex` o completa aquí]
- Archivos analizados: `localizacion.tex`, `analisis_mercado.tex`, `estrategia_promocion.tex`, `estructura_organizacional.tex`, `diseno_producto.tex`, `ciclo_produccion.tex`.

### Qué debes evaluar

**1. Localización (Macro y Micro)**
- ¿Se justifica la macrolocalización con datos de accesibilidad vial y conectividad departamental/municipal?
- ¿La microlocalización detalla la dirección o zona exacta y argumenta la cercanía estratégica a materias primas y clientes?

**2. Análisis del mercado y ventaja competitiva**
- Oferta y Demanda: ¿se identifica claramente a la competencia y se cuantifica la demanda estimada?
- Público objetivo: ¿está segmentado adecuadamente (edad, nivel socioeconómico, hábitos de compra)?
- Ventaja competitiva: ¿se define con claridad por qué el cliente preferirá esta propuesta?
- Tabla de mercado: ¿la tabla `tablas/estudio_mercado_ejemplo.tex` cumple normas APA 7 (`booktabs`, sin líneas verticales, nota con `\notatabla`)?

**3. Estrategia comercial y distribución**
- Canales de distribución: ¿se detalla la logística desde el taller o unidad productiva hasta el cliente final?
- Promoción: ¿las estrategias publicitarias (redes sociales, ferias, degustaciones) son realistas y de bajo costo para un emprendimiento escolar/técnico?

**4. Organización y recursos humanos**
- Forma jurídica: ¿se especifica la naturaleza legal del negocio (empresa unipersonal, asociación)?
- Organigrama y cargos: ¿las funciones asignadas en la tabla `tablas/estructura_organizacional_ejemplo.tex` cubren las áreas indispensables (administración, producción, ventas)?

**5. Producto, marca y proceso productivo**
- Especificaciones del producto: ¿se detallan dimensiones, insumos, formulación o características funcionales?
- Empaque y presentación: ¿se describe el rotulado, marca y criterios ambientales del empaque?
- Ciclo de producción: ¿se describen las etapas secuenciales con controles de calidad y capacidad estimada por ciclo?

**6. Estilo y formato**
- Convención numérica SI/ISO 80000-1 (punto decimal, cifras de 4 dígitos juntas: 1000, 3500; 5 dígitos con espacio: 25 000.00).
- Prioridad de viñetas (`itemize`) en listados descriptivos.

### Formato de salida esperado
```
## Diagnóstico general del Capítulo 3
[Evaluación global: consistencia comercial, técnica y operativa]

## Evaluación temática
- Localización (Macro/Micro):
- Estudio de Mercado y Competencia:
- Estrategia Comercial y Canales:
- Estructura Organizacional:
- Diseño de Producto y Presentación:
- Proceso Productivo y Capacidad:

## Auditoría de Tablas APA 7
- `tablas/estudio_mercado_ejemplo.tex`: [Conformidad con booktabs y notas]
- `tablas/estructura_organizacional_ejemplo.tex`: [Conformidad con booktabs y notas]

## Mejoras sugeridas de redacción (LaTeX)
```latex
% Propuestas de ajuste técnico o enriquecimiento de secciones
```
```
