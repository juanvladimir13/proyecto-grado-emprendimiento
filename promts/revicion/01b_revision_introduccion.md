# Prompt: Revisión de la Introducción (Capítulo 1)

## Cuándo usar este prompt
Al finalizar la redacción del borrador del **Capítulo 1: Introducción** (`capitulos/01_introduccion/`).

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier revisión.
2. Obtén los datos del proyecto desde `estilos/configuracion.tex` (`\tituloproyecto`, `\especialidad`, `\modalidad`).
3. Lee directamente los archivos `.tex` indicados en la sección "Archivos a revisar".
4. Si necesitas contrastar con los objetivos o el diagnóstico, lee `capitulos/02_planteamiento_emprendimiento/diagnostico.tex` y `capitulos/02_planteamiento_emprendimiento/objetivos.tex`.
5. Consulta `docs/ficha-proyecto.md` (Sección 1) para verificar los datos de contexto.

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Sustituye los campos entre `[corchetes]` con los datos de tu proyecto.
3. Pega el contenido LaTeX de los archivos `.tex` correspondientes al final.

---

## Archivos a revisar

| Archivo | Contenido |
| :--- | :--- |
| `capitulos/01_introduccion/main.tex` | Ensamble del capítulo (`\chapter` y `\input` de las cuatro secciones) |
| `capitulos/01_introduccion/contexto_general.tex` | Contexto general del sector económico, dinámica comercial y ámbito geográfico |
| `capitulos/01_introduccion/oportunidad_negocio.tex` | Identificación fundamentada de la oportunidad de negocio y demanda insatisfecha |
| `capitulos/01_introduccion/propuesta_valor.tex` | Propuesta de valor, atributos de diferenciación y ventaja competitiva |
| `capitulos/01_introduccion/marco_teorico.tex` | Fundamentación teórica del modelo de negocio, marco conceptual y herramientas |

---

## PROMPT

Actúa como un **revisor académico y de planes de negocio BTH** en modalidad **Emprendimiento Productivo**. Evalúa el **Capítulo 1: Introducción** que te proporcionaré, verificando que presente un panorama fundamentado, coherente y comercialmente viable de la iniciativa productiva.

### Contexto del documento
- Modalidad: Emprendimiento Productivo (BTH Bolivia, RM 0912/2023, Anexo 1, inciso A)
- Especialidad técnica: [lee `\especialidad` de `estilos/configuracion.tex` o completa aquí]
- Título del proyecto: [lee `\tituloproyecto` de `estilos/configuracion.tex` o completa aquí]
- Secciones analizadas de `capitulos/01_introduccion/`:
  * `contexto_general.tex`: Caracterización del sector productivo o comercial, ámbito geográfico, dinámica económica local y datos cuantitativos con fuentes citadas.
  * `oportunidad_negocio.tex`: Necesidad insatisfecha identificada en el mercado objetivo, factores desatendidos por la competencia actual y origen de la iniciativa.
  * `propuesta_valor.tex`: Propuesta de valor concreta, atributos diferenciadores (calidad, innovación, precio, sostenibilidad) y ventaja competitiva.
  * `marco_teorico.tex`: Bases teóricas de modelos de negocio (Canvas, administración), marco conceptual (cadena productiva, costos, punto de equilibrio) y herramientas metodológicas.
- El texto incluye comandos LaTeX (`\section`, `\subsection`, `\label`, `\cite`, `\parencite`, `\textcite`) — consérvalos intactos.

### Qué debes evaluar
1. **Contextualización del rubro productivo:** ¿se describe el sector con datos cuantitativos verificables (INE, cámaras sectoriales, registros municipales) y fuentes debidamente citadas con APA 7?
2. **Claridad de la oportunidad de negocio:** ¿se demuestra con claridad la existencia de una brecha o demanda insatisfecha que hace oportuna la creación del negocio?
3. **Propuesta de valor diferenciadora:** ¿se definen con precisión los atributos que diferencian al producto o servicio de los competidores existentes?
4. **Rigor teórico-conceptual:** ¿el marco teórico conecta teorías reconocidas de modelos de negocio y define con claridad los conceptos económicos que se usarán en los capítulos posteriores?
5. **Hilo conductor hacia el Capítulo 2:** ¿la introducción prepara al lector para el diagnóstico de campo y los objetivos planteados en el Capítulo 2?
6. **Estilo y formato:** ¿emplea registro académico formal, tercera persona impersonal, sin afirmaciones publicitarias infundadas y con citas APA 7 correctas?

### Formato de salida esperado
```
## Diagnóstico general del Capítulo 1
[Evaluación global: solidez conceptual, fortalezas y debilidades]

## Evaluación sección por sección
### 1.1 Contexto general del emprendimiento
- Fortalezas:
- Aspectos a mejorar:

### 1.2 Identificación de la oportunidad de negocio
- Fortalezas:
- Aspectos a mejorar:

### 1.3 Propuesta de valor y diferenciación
- Fortalezas:
- Aspectos a mejorar:

### 1.4 Marco teórico y conceptual
- Fortalezas:
- Aspectos a mejorar:

## Propuestas de redacción mejorada (LaTeX)
```latex
% Fragmentos con corrección de estilo o complementación técnica
```
```
