# Prompt: Revisión de Viabilidad y Sostenibilidad Financiera (Capítulo 4)

## Cuándo usar este prompt
Al finalizar la redacción del borrador del **Capítulo 4: Viabilidad y Sostenibilidad** (`capitulos/04_viabilidad_sostenibilidad/`).

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier revisión.
2. Obtén los datos del proyecto desde `estilos/configuracion.tex` (`\tituloproyecto`, `\especialidad`, `\modalidad`).
3. Lee directamente los archivos `.tex` indicados en la sección "Archivos a revisar".
4. Revisa las tablas financieras asociadas en `tablas/`:
   - `inversiones_ejemplo.tex`
   - `costos_produccion_ejemplo.tex`
   - `indicadores_financieros_ejemplo.tex`
5. Consulta `docs/ficha-proyecto.md` (Sección 4) para contrastar cifras de inversión, costos y precios.

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Sustituye los campos entre `[corchetes]` con los datos de tu proyecto.
3. Pega el contenido LaTeX de los archivos `.tex` y tablas correspondientes al final.

---

## Archivos a revisar

| Archivo | Contenido |
| :--- | :--- |
| `capitulos/04_viabilidad_sostenibilidad/main.tex` | Ensamble del capítulo (`\chapter` y `\input` de las secciones) |
| `capitulos/04_viabilidad_sostenibilidad/calculo_inversiones.tex` | Capital de inversión fija, activos diferidos y capital de operación (`tablas/inversiones_ejemplo.tex`) |
| `capitulos/04_viabilidad_sostenibilidad/costo_produccion.tex` | Costos variables, fijos, indicadores de rentabilidad y punto de equilibrio (`tablas/costos_produccion_ejemplo.tex`, `tablas/indicadores_financieros_ejemplo.tex`) |

---

## PROMPT

Actúa como un **auditor financiero y evaluador de proyectos de inversión productiva BTH**. Analiza con rigor el **Capítulo 4: Viabilidad y Sostenibilidad** que te proporcionaré, verificando la exactitud de los cálculos numéricos, la coherencia de costos y precios, y la solvencia económica del emprendimiento.

### Contexto del documento
- Modalidad: Emprendimiento Productivo (BTH Bolivia, RM 0912/2023, Anexo 1, inciso A)
- Especialidad técnica: [lee `\especialidad` de `estilos/configuracion.tex` o completa aquí]
- Título del proyecto: [lee `\tituloproyecto` de `estilos/configuracion.tex` o completa aquí]
- Moneda oficial: Bolivianos (Bs.)

### Qué debes evaluar

**1. Presupuesto de inversiones**
- Capital de inversión fija: ¿se desglosan adecuadamente maquinaria, herramientas, mobiliario y activos diferidos?
- Capital de operación: ¿cubre razonablemente los costos operativos iniciales (1 a 3 meses de materia prima y mano de obra)?
- Inversión total: ¿la suma matemática entre inversión fija y capital de operación es exacta y coincide con la tabla `tablas/inversiones_ejemplo.tex`?

**2. Estructura de costos de producción**
- Costos variables: ¿incluyen insumos directos, envases, rotulado y mano de obra directa proporcional al volumen?
- Costos fijos: ¿contemplan alquiler, servicios básicos, depreciaciones y sueldos administrativos?
- Costo total unitario: ¿el cálculo del costo unitario es coherente con la capacidad estimada del Cap. 3?
- Tabla de costos: ¿la tabla `tablas/costos_produccion_ejemplo.tex` cumple estrictamente con APA 7?

**3. Precio de venta, punto de equilibrio y rentabilidad**
- Precio de venta sugerido: ¿contempla un margen de ganancia razonable (ej. 25% a 35%) y resulta competitivo frente al mercado analizado en el Cap. 3?
- Margen de contribución unitario: $MC = P_{venta} - CV_{unitario}$. ¿Es positivo y matemáticamente exacto?
- Punto de equilibrio: $PE_{unidades} = CF / MC$. ¿El volumen resultante en unidades y en bolivianos es realista frente a la demanda y capacidad de producción?
- Retorno de inversión: ¿se calcula un tiempo estimado de recuperación coherente?
- Tabla de indicadores: ¿la tabla `tablas/indicadores_financieros_ejemplo.tex` presenta estos valores con precisión?

**4. Normas técnicas de formato (SI/ISO 80000-1 y APA 7)**
- **Punto decimal obligatorio (`.`):** PROHIBIDO el uso de comas decimales (ej. verificar que se use `12.50` y no `12,50`).
- **Separador de miles:** Sin comas ni puntos (cifras de 4 dígitos juntas: `4500.00`; de 5 o más dígitos continuas o con espacio: `25 000.00`).
- Tablas con `booktabs`, encabezados claros, notas con `\notatabla{Fuente: ...}` y sin líneas verticales.

### Formato de salida esperado
```
## Diagnóstico general del Capítulo 4
[Evaluación global de viabilidad financiera y consistencia de costos]

## Auditoría Numérica y Financiera
| Concepto | Valor Reportado (Bs.) | Valor Recalculado (Bs.) | Estado |
|---|---|---|---|
| Inversión fija total | | | |
| Capital de operación | | | |
| Inversión total requerida | | | |
| Costo variable unitario | | | |
| Costos fijos mensuales | | | |
| Precio de venta unitario | | | |
| Margen de contribución | | | |
| Punto de equilibrio (unidades) | | | |
| Punto de equilibrio (Bs.) | | | |

## Observaciones de Formato y Estilo
- Formato numérico SI/ISO 80000-1: [Conformidad]
- Auditoría de tablas APA 7: [Conformidad]

## Correcciones y Ajustes LaTeX Sugeridos
```latex
% Ajustes a tablas o párrafos financieros
```
```
