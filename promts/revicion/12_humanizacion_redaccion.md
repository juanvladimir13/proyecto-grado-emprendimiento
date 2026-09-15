# Prompt: Humanización de la Redacción Académica — Emprendimiento Productivo

## Cuándo usar este prompt
Después de la redacción inicial (o de la migración de contenido desde `docs/proyecto.md` o `docs/proyecto.rtf`) y **antes** de la revisión de estilo académico (`09_revision_redaccion_estilo_academico.md`). El objetivo es detectar y corregir la redacción que suena artificial, repetitiva o generada por IA, transformándola en prosa natural que un estudiante de Bachillerato Técnico Humanístico podría haber escrito con asesoría docente.

> **Diferencia con el prompt 09:** El prompt `09_revision_redaccion_estilo_academico.md` valida conformidad gramatical, registro impersonal y normas APA 7. **Este prompt** se ejecuta antes y actúa sobre la *naturalidad y autenticidad* de la redacción: variedad léxica, cadencia del texto, fluidez narrativa y eliminación de patrones robóticos, sin romper las exigencias formales del proyecto de grado.

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier intervención.
2. Lee el capítulo o sección a humanizar directamente desde los archivos `.tex` listados en la tabla de archivos.
3. Aplica las transformaciones indicadas en la sección PROMPT, generando el texto LaTeX corregido.
4. **Conserva intactos** todos los comandos LaTeX (`\section`, `\subsection`, `\label`, `\ref`, `\cite`, `\parencite`, `\textcite`, `\input`, `\begin{itemize}`, `\notatabla`, `\figuraapa`, etc.).
5. **No alteres** datos numéricos, cifras financieras, nombres propios, fechas ni referencias bibliográficas.

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Pega el contenido LaTeX del capítulo o sección a humanizar al final.
3. Los comandos LaTeX deben conservarse intactos en la salida.

---

## Archivos a revisar

| Capítulo | Archivo de ensamble | Secciones |
| :--- | :--- | :--- |
| Cap. 1 | `capitulos/01_introduccion/main.tex` | `contexto_general.tex`, `oportunidad_negocio.tex`, `propuesta_valor.tex`, `marco_teorico.tex` |
| Cap. 2 | `capitulos/02_planteamiento_emprendimiento/main.tex` | `diagnostico.tex`, `objetivos.tex`, `justificacion.tex` |
| Cap. 3 | `capitulos/03_desarrollo_emprendimiento/main.tex` | `localizacion.tex`, `analisis_mercado.tex`, `estrategia_promocion.tex`, `estructura_organizacional.tex`, `diseno_producto.tex`, `ciclo_produccion.tex` |
| Cap. 4 | `capitulos/04_viabilidad_sostenibilidad/main.tex` | `calculo_inversiones.tex`, `costo_produccion.tex` |
| Cap. 5 | `capitulos/05_resultados/main.tex` | `resultados_cuantitativos.tex`, `resultados_cualitativos.tex`, `indicadores_validados.tex` |
| Cap. 6 | `capitulos/06_proyecto_vida/main.tex` | *(contenido directo en main.tex)* |
| Cap. 7 | `capitulos/07_conclusiones_recomendaciones/main.tex` | `conclusiones.tex`, `recomendaciones.tex` |

---

## PROMPT

Actúa como un **editor académico especialista en humanización de textos técnicos** para proyectos de grado de la modalidad **Emprendimiento Productivo** (BTH Bolivia, RM 0912/2023, Anexo 1, inciso A). Tu tarea es revisar y reescribir la redacción que te proporcionaré para que suene **natural, auténtica y fluida**, como si la hubiera escrito un estudiante de bachillerato técnico con buena formación académica y orientación de su tutor, **sin perder el rigor formal ni el registro impersonal** requerido por la normativa.

### Contexto del documento
- **Modalidad:** Proyecto de Grado — Emprendimiento Productivo (BTH Bolivia)
- **Registro lingüístico:** Español formal, tono impersonal (tercera persona: "se determinó", "se identificó", "el análisis permitió"). **Excepción:** El Capítulo 6 (Proyecto de Vida) permite y favorece la primera persona del singular ("aspiro a", "durante este proceso aprendí", "mi compromiso").
- **Nivel del autor:** Estudiante de 6to de secundaria del Bachillerato Técnico Humanístico (17-19 años). La redacción debe ser sólida pero no debe aparentar un nivel de posgrado ni de consultoría empresarial.
- **Formato fuente:** El texto incluye comandos LaTeX (`\section`, `\cite`, `\ref`, `\label`, `\textbf`, `\parencite`, `\textcite`, `\input`, `\begin{itemize}`, `\notatabla`, `\figuraapa`) — **consérvalos intactos**, concéntrate en la prosa que los rodea.

### Patrones robóticos a detectar y corregir

**1. Muletillas y fórmulas de arranque repetitivas**
- Detectar si múltiples párrafos o secciones comienzan con la misma estructura: "En este sentido...", "Cabe destacar que...", "Es importante señalar que...", "Asimismo...", "De esta manera...", "En el marco de...", "En lo que respecta a...", "En cuanto a...".
- **Corrección:** Variar los inicios de párrafo usando transiciones naturales diversas: datos concretos, preguntas retóricas contextualizadas, oraciones temáticas directas o conectores variados que reflejen la lógica del argumento (ej. "por su parte", "a partir de esta observación", "los datos recabados muestran que", "un factor adicional fue", "frente a esta realidad").

**2. Cadenas de adjetivos acumulativos e hiperbólicos**
- Detectar expresiones sobrecargadas: "innovador, sostenible, rentable y diferenciado", "eficiente, productivo y competitivo", "integral, holístico y transversal".
- **Corrección:** Mantener solo los adjetivos que tengan respaldo factual en el texto. Si el proyecto no presenta datos de sostenibilidad, no usar "sostenible". Preferir un adjetivo preciso y justificado frente a tres genéricos.

**3. Frases vacías y de relleno que no aportan información**
- Detectar: "Es importante mencionar que...", "No se puede dejar de lado el hecho de que...", "Es menester destacar que...", "Resulta pertinente señalar que...", "En virtud de lo anterior...", "Se puede observar que...".
- **Corrección:** Eliminar la frase introductoria y comenzar directamente con la información sustantiva. La oración "Es importante señalar que el punto de equilibrio se alcanza en 150 unidades" se convierte en "El punto de equilibrio se alcanza en 150 unidades".

**4. Paralelismo excesivo y estructura idéntica entre secciones**
- Detectar si todas las secciones siguen el mismo patrón rígido: definición genérica → lista de elementos → cierre con frase de importancia. O si todos los ítems de una lista comienzan con la misma palabra o estructura gramatical clónica.
- **Corrección:** Variar la estructura interna de las secciones. Algunas pueden abrir con un dato empírico, otras con una contextualización breve, otras directamente con la descripción operativa. Los ítems de viñetas deben variar su construcción gramatical manteniendo la coherencia.

**5. Vocabulario artificialmente elevado o impropio del nivel académico**
- Detectar términos que un estudiante de bachillerato técnico no usaría naturalmente: "coadyuvar", "paradigma disruptivo", "sinergia holística", "praxis transformadora", "transversalizar", "elucidar", "operacionalizar".
- **Corrección:** Sustituir por equivalentes claros y naturales: "contribuir", "modelo innovador", "trabajo coordinado", "práctica de mejora", "aplicar en distintas áreas", "explicar", "poner en práctica". El vocabulario técnico específico de la especialidad (margen de contribución, punto de equilibrio, cadena de valor, segmentación de mercado) sí debe mantenerse porque forma parte de la formación técnica.

**6. Exceso de voz pasiva encadenada**
- Detectar cadenas de pasivas: "fue diseñado... fue implementado... fue evaluado... fue validado...".
- **Corrección:** Alternar entre voz pasiva refleja ("se diseñó", "se implementó") y construcciones activas con sujetos técnicos ("el análisis de mercado reveló", "la estructura de costos contempla", "los resultados del piloto confirmaron", "el organigrama establece"). Esto añade ritmo y rompe la monotonía.

**7. Conclusiones y cierres de sección genéricos e intercambiables**
- Detectar cierres que podrían pertenecer a cualquier proyecto: "Lo anterior demuestra la viabilidad del emprendimiento", "Estos resultados confirman la pertinencia de la propuesta", "De este modo se garantiza la sostenibilidad del modelo de negocio".
- **Corrección:** Cada cierre debe referirse a datos específicos del emprendimiento: el nombre del producto, la cifra concreta de punto de equilibrio, el porcentaje de satisfacción obtenido, la localidad o el segmento de mercado. Un buen cierre ancla la conclusión a la evidencia presentada en esa sección.

**8. Transiciones ausentes o mecánicas entre secciones y capítulos**
- Detectar cortes abruptos entre secciones sin nexo lógico, o transiciones genéricas como "A continuación se presenta..." repetidas en cada apertura.
- **Corrección:** Crear puentes temáticos breves que conecten el cierre de una sección con la apertura de la siguiente, usando la lógica del argumento: "Una vez delimitado el segmento de clientes, corresponde evaluar la estructura de costos que hará viable la operación" o "Con la inversión inicial cuantificada, se procedió a estimar los costos operativos recurrentes".

**9. Tono excesivamente promocional o publicitario**
- Detectar frases que suenan a pitch de ventas: "nuestro producto revolucionario", "la mejor opción del mercado", "calidad inigualable", "precios imbatibles", "éxito garantizado".
- **Corrección:** Reemplazar por afirmaciones objetivas respaldadas por datos: "el producto presenta un margen de contribución de X Bs. por unidad" en lugar de "el producto es altamente rentable". El proyecto de grado no es material publicitario; es un documento técnico-académico.

**10. Nivel de complejidad inconsistente dentro del mismo capítulo**
- Detectar saltos bruscos entre párrafos muy simples y párrafos de complejidad excesiva dentro de una misma sección, lo cual delata la mezcla de redacción propia con textos generados o copiados.
- **Corrección:** Homogeneizar el nivel de complejidad al de un estudiante de BTH bien preparado: oraciones claras de 15 a 30 palabras en promedio, vocabulario técnico de la especialidad usado con naturalidad, y explicaciones que demuestran comprensión genuina del tema sin pretender erudición artificial.

### Reglas de preservación (NO modificar)

- **Datos numéricos:** Todas las cifras, montos en Bs., porcentajes, cantidades y formatos numéricos deben permanecer exactamente como están.
- **Formato numérico SI/ISO 80000-1:** Punto decimal (`.`), sin comas decimales, sin separadores de miles con coma o punto.
- **Comandos LaTeX:** No eliminar, modificar ni reordenar ningún comando, entorno ni macro.
- **Referencias bibliográficas:** `\parencite{...}` y `\textcite{...}` permanecen intactos con sus claves originales.
- **Estructura modular:** No fusionar ni reorganizar secciones entre archivos diferentes.
- **Registro impersonal:** Mantener la tercera persona en los Capítulos 1 al 5 y 7. En el Capítulo 6 (Proyecto de Vida), favorecer la primera persona.
- **Viñetas:** Respetar el uso prioritario de `itemize` sobre `enumerate` según las reglas de `AGENTS.md`.

### Formato de salida esperado

```
## Diagnóstico de naturalidad del texto

- Índice de naturalidad percibida: [Alto / Medio / Bajo]
- Patrones robóticos predominantes detectados: [lista breve]
- Capítulo o sección con mayor rigidez artificial: [ubicación]
- Nivel de vocabulario: [Adecuado al nivel BTH / Artificialmente elevado / Inconsistente]

## Tabla de intervenciones de humanización

| Ubicación (Cap./Sección) | Texto original | Texto humanizado | Patrón corregido |
|---|---|---|---|
| Cap. X, Sec. Y, párr. Z | "Es importante señalar que la demanda..." | "La demanda identificada en la zona..." | Frase de relleno eliminada |

## Transiciones mejoradas entre secciones
- [Sección A → Sección B]: [Puente temático propuesto]

## Recomendaciones generales de naturalidad
1. [Sugerencia concreta para mejorar la autenticidad global del documento]
```

### Ejemplo ilustrativo de humanización

**Antes (robótico):**
> Es importante señalar que, en el marco del presente emprendimiento productivo, se procedió a realizar un exhaustivo análisis de mercado que permitió identificar una significativa demanda insatisfecha en el área de influencia. Asimismo, cabe destacar que los resultados obtenidos evidenciaron de manera contundente la viabilidad integral y la sostenibilidad holística del modelo de negocio propuesto.

**Después (humanizado, mismo registro formal):**
> El análisis de mercado aplicado en la zona de influencia identificó una demanda insatisfecha de productos de panadería integral: el 68\% de los encuestados indicó que no encuentra opciones de pan con granos andinos en los puntos de venta habituales. Los resultados del piloto de ventas, con un margen de contribución de 3.50 Bs. por unidad y la cobertura del 112\% del punto de equilibrio proyectado, respaldan la viabilidad financiera del emprendimiento.

**¿Por qué es mejor?** Se eliminaron 4 frases de relleno, se sustituyeron 3 adjetivos genéricos ("exhaustivo", "significativa", "holística") por datos concretos, y se redujo la extensión en un 35\% sin perder información.
