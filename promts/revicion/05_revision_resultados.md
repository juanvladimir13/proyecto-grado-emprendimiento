# Prompt: Revisión de Resultados de Validación Comercial (Capítulo 5)

## Cuándo usar este prompt
Al finalizar la redacción del borrador del **Capítulo 5: Resultados** (`capitulos/05_resultados/`).

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier revisión.
2. Obtén los datos del proyecto desde `estilos/configuracion.tex` (`\tituloproyecto`, `\especialidad`, `\modalidad`).
3. Lee directamente los archivos `.tex` indicados en la sección "Archivos a revisar".
4. Revisa la tabla de resultados piloto en `tablas/resultados_piloto_ejemplo.tex`.
5. Contrasta las cifras obtenidas con las metas proyectadas en el Cap. 4 (`capitulos/04_viabilidad_sostenibilidad/costo_produccion.tex`).
6. Consulta `docs/ficha-proyecto.md` (Sección 5).

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Sustituye los campos entre `[corchetes]` con los datos de tu proyecto.
3. Pega el contenido LaTeX de los archivos `.tex` y tablas correspondientes al final.

---

## Archivos a revisar

| Archivo | Contenido |
| :--- | :--- |
| `capitulos/05_resultados/main.tex` | Ensamble del capítulo (`\chapter` y `\input` de las secciones) |
| `capitulos/05_resultados/resultados_cuantitativos.tex` | Validación comercial, unidades producidas/vendidas, ingresos brutos y demanda real |
| `capitulos/05_resultados/resultados_cualitativos.tex` | Percepción del consumidor, atributos valorados y retroalimentación para mejora |
| `capitulos/05_resultados/indicadores_validados.tex` | Contraste de metas financieras proyectadas vs. resultados reales (`tablas/resultados_piloto_ejemplo.tex`) |
| `anexos/anexo_b_fichas_tecnicas.tex` | Evidencias documentales e instrumentos aplicados (cuestionarios, fichas de cata/degustación) |

---

## PROMPT

Actúa como un **evaluador de validación de proyectos productivos y mercado BTH**. Analiza el **Capítulo 5: Resultados** que te proporcionaré, verificando la autenticidad y solidez de los datos de prueba piloto, la evaluación cualitativa de los clientes y la contrastación empírica con las proyecciones del plan de negocio.

### Contexto del documento
- Modalidad: Emprendimiento Productivo (BTH Bolivia, RM 0912/2023, Anexo 1, inciso A)
- Especialidad técnica: [lee `\especialidad` de `estilos/configuracion.tex` o completa aquí]
- Título del proyecto: [lee `\tituloproyecto` de `estilos/configuracion.tex` o completa aquí]
- Archivos analizados: `resultados_cuantitativos.tex`, `resultados_cualitativos.tex`, `indicadores_validados.tex`.

### Qué debes evaluar

**1. Resultados cuantitativos y validación comercial**
- ¿Se describe con claridad cómo se ejecutó la prueba de campo o venta piloto (fechas, lugar, modalidad de colocación)?
- ¿Se reportan con exactitud las unidades fabricadas, unidades vendidas, precio unitario e ingresos brutos obtenidos en Bs.?
- ¿Se compara el comportamiento real de la demanda frente al volumen mínimo del punto de equilibrio del Cap. 4?

**2. Resultados cualitativos, percepción del cliente e instrumentos aplicados**
- ¿Se describen con precisión los instrumentos metodológicos aplicados durante la prueba piloto (cuestionarios de satisfacción escala Likert, fichas de cata/degustación, encuestas de retroalimentación)?
- ¿Se vincula o referencia el modelo de instrumento como evidencia documental en los Anexos (ej. `anexos/anexo_b_fichas_tecnicas.tex`)?
- ¿Se analizan las respuestas de los consumidores respecto a los atributos clave (calidad, sabor/funcionalidad, durabilidad, presentación, precio)?
- ¿Se presenta un nivel medible de satisfacción (porcentaje de aprobación o promedio en escala Likert)?
- ¿Se recoge retroalimentación constructiva que justifique mejoras operativas futuras?

**3. Indicadores de rentabilidad validados**
- ¿Se contrastan de forma transparente las metas proyectadas en el Cap. 4 con los resultados obtenidos en el piloto?
- ¿La tabla `tablas/resultados_piloto_ejemplo.tex` resume con claridad: unidades vendidas, ingresos totales, costo total incurrido y margen real obtenido?
- ¿La tabla cumple estrictamente con el formato APA 7 (`booktabs`, sin líneas verticales, nota con `\notatabla`)?

**4. Normas técnicas de formato (SI/ISO 80000-1)**
- Punto decimal obligatorio (`.`), sin comas decimales.
- Cifras formateadas correctamente según la convención del proyecto.

### Formato de salida esperado
```
## Diagnóstico general del Capítulo 5
[Evaluación global: validez empírica y solidez de los resultados presentados]

## Evaluación temática
- Resultados Cuantitativos y Ventas:
- Aceptación Cualitativa del Cliente e Instrumentos Aplicados (con respaldo en Anexos):
- Contraste con Metas Financieras (Proyectado vs Real):

## Auditoría de la Tabla de Resultados Piloto
- `tablas/resultados_piloto_ejemplo.tex`: [Evaluación APA 7 y exactitud de cifras]

## Propuesta de Mejoras en LaTeX
```latex
% Ajustes a párrafos descriptivos o indicadores
```
```
