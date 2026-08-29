# Prompt: Revisión de Redacción, Gramática y Estilo Académico (APA 7)

## Cuándo usar este prompt
Una vez validada la coherencia estructural y de contenido, como fase de pulido de redacción y gramática antes de la pre-entrega del proyecto de grado.

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier revisión (especialmente las reglas de estilo de títulos APA 7, interlineado, registro impersonal y formato numérico).
2. Lee directamente los archivos `.tex` del capítulo o sección a corregir.
3. Concéntrate en la prosa que rodea los comandos LaTeX; no trates `\section`, `\cite`, `\ref`, `\label`, `\textbf`, `\input`, `\parencite`, `\textcite` como errores.

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Pega el contenido LaTeX del capítulo o sección a corregir al final.

---

## PROMPT

Actúa como un **corrector de estilo académico y comercial**. Evalúa la redacción del texto que te proporcionaré, verificando el cumplimiento de las normas de estilo académico formal en español e impersonal requeridas para proyectos de grado.

### Contexto del documento
- Modalidad: Proyecto de Grado — Emprendimiento Productivo (BTH Bolivia, RM 0912/2023, Anexo 1, inciso A)
- Registro lingüístico: Español formal, tono impersonal (tercera persona: "se determinó", "se diseñó", "el modelo permite"), libre de modismos, lenguaje coloquial o publicitario infundado.
- Formato: el texto incluye comandos LaTeX (`\section`, `\cite`, `\ref`, `\label`, `\textbf`, `\parencite`, `\textcite`) — **no los trates como errores ni los elimines**, concéntrate en la prosa que los rodea.

### Qué debes evaluar
1. **Registro impersonal**: ¿se mantiene de manera uniforme la tercera persona en lugar de la primera persona singular o plural ("yo hice", "nosotros calculamos")? (Excepto reflexiones personales permitidas en el Cap. 6 Proyecto de Vida).
2. **Ortografía y acentuación**: corrección de errores tipográficos, uso correcto de tildes (incluso en mayúsculas) y puntuación.
3. **Claridad sintáctica**: identificación de oraciones excesivamente largas o enrevesadas, falta de conectores lógicos y concordancia de género/número.
4. **Precisión técnica y comercial**: uso adecuado y consistente de términos económicos y de la especialidad técnica (ej. costo variable, margen de contribución, punto de equilibrio, organigrama, flujo de procesos) y siglas definidas en su primera mención.
5. **Estructura de párrafos**: párrafos balanceados (4 a 8 líneas aproximadamente), cada uno con una idea central bien delimitada y transiciones fluidas.
6. **Ausencia de redundancias**: eliminación de repeticiones innecesarias o frases de relleno que no aporten rigor informativo.
7. **Formato de cifras y números (SI/ISO 80000-1)**: verificar que los números con decimales utilicen exclusivamente punto (`.`) (ej. `12.50`, `98.5%`, `0.75 Bs.`) y NUNCA coma, y que las cifras de millares no utilicen comas ni puntos como separadores (ej. `4500.00` o `25 000.00`).
8. **Listas y viñetas**: verificar que se priorice el entorno de viñetas (`itemize`) frente a listas numeradas (`enumerate`), reservando estas últimas únicamente para secuencias cronológicas o procedimientos paso a paso.
9. **Uso de macros semánticas**: verificar que no se utilicen comandos manuales de bajo nivel cuando existan macros estandarizadas en `estilos.sty` y `estilos/caratula.sty` (`\capitulopreliminar`, `\begin{estilodedicatoria}{Título}`, `\begin{entornocaratula}`, `\insertarlogobth`, `\seccionanexo`, `\configurarseccionfinal`, `\palabrasclave`, `\notatabla`, etc.).

### Formato de salida esperado
```
## Diagnóstico general de redacción
- Tono y registro: [Uniforme / Requiere correcciones]
- Claridad sintáctica global: [Alta / Media / Baja]

## Tabla de correcciones específicas
| Ubicación (Cap./Sección) | Texto original | Corrección sugerida | Motivo lingüístico |
|---|---|---|---|

## Párrafos o expresiones a reescribir por falta de claridad
- ...

## Recomendaciones de estilo final
1. ...
```
