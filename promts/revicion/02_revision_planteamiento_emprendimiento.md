# Prompt: Revisión del Planteamiento del Emprendimiento Productivo (Capítulo 2)

## Cuándo usar este prompt
Al finalizar la redacción del borrador del **Capítulo 2: Planteamiento del Emprendimiento Productivo** (`capitulos/02_planteamiento_emprendimiento/`).

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier revisión.
2. Obtén los datos del proyecto desde `estilos/configuracion.tex` (`\tituloproyecto`, `\especialidad`, `\modalidad`).
3. Lee directamente los archivos `.tex` indicados en la sección "Archivos a revisar".
4. Consulta `docs/ficha-proyecto.md` (Sección 2) para contrastar los datos de diagnóstico y formulación de objetivos.
5. Verifica la alineación con `capitulos/01_introduccion/oportunidad_negocio.tex`.

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Sustituye los campos entre `[corchetes]` con los datos de tu proyecto.
3. Pega el contenido LaTeX de los archivos `.tex` correspondientes al final.

---

## Archivos a revisar

| Archivo | Contenido |
| :--- | :--- |
| `capitulos/02_planteamiento_emprendimiento/main.tex` | Ensamble del capítulo (`\chapter` y `\input` de las secciones) |
| `capitulos/02_planteamiento_emprendimiento/diagnostico.tex` | Diagnóstico del contexto productivo, instrumentos aplicados y brechas de mercado |
| `capitulos/02_planteamiento_emprendimiento/objetivos.tex` | Objetivo general, objetivos específicos (en `itemize`), misión y visión empresarial |
| `capitulos/02_planteamiento_emprendimiento/justificacion.tex` | Justificación económica, social y técnica del emprendimiento |

---

## PROMPT

Actúa como un **tutor y evaluador metodológico de proyectos de grado BTH** en la modalidad **Emprendimiento Productivo**. Evalúa el **Capítulo 2: Planteamiento del Emprendimiento Productivo** que te proporcionaré, verificando la solidez del diagnóstico, la coherencia de los objetivos y la pertinencia de las justificaciones.

### Contexto del documento
- Modalidad: Emprendimiento Productivo (BTH Bolivia, RM 0912/2023, Anexo 1, inciso A)
- Especialidad técnica: [lee `\especialidad` de `estilos/configuracion.tex` o completa aquí]
- Título del proyecto: [lee `\tituloproyecto` de `estilos/configuracion.tex` o completa aquí]
- Archivos analizados de `capitulos/02_planteamiento_emprendimiento/`:
  * `diagnostico.tex`: Diagnóstico de la realidad productiva y de consumo local apoyado en datos de campo, tamaño muestral e instrumentos de recolección (encuestas, entrevistas, observación directa).
  * `objetivos.tex`:
    - Objetivo general: verbo en infinitivo, medible, delimitado al emprendimiento productivo.
    - Objetivos específicos: lista en viñetas (`itemize`), secuenciales y operativos (estudio de mercado, diseño técnico/organizacional, evaluación financiera/precios).
    - Misión y Visión (opcionales pero recomendadas): coherentes con la especialidad técnica.
  * `justificacion.tex`: Argumentación del impacto económico (generación de ingresos y empleo), social (beneficio directo a la comunidad) y técnico (aplicación de saberes de la especialidad).

### Qué debes evaluar
1. **Rigor del diagnóstico productivo y representatividad muestral:**
   - ¿Se describe el estado real del mercado con base en evidencias o instrumentos aplicados directamente en la zona de influencia?
   - ¿Se especifica el **tamaño de la muestra o grupo focal** (número concreto de personas o negocios consultados) y el criterio de selección aplicado?
   - ¿Se identifican con precisión las brechas de oferta o insatisfacción que justifican la propuesta productiva?
2. **Formulación del objetivo general:** ¿inicia con verbo en infinitivo (establecer, implementar, producir, etc.), define con precisión qué se va a emprender, para quién y en qué contexto?
3. **Calidad de los objetivos específicos:**
   - ¿Están formateados obligatoriamente con `\begin{itemize}` en lugar de enumeraciones numeradas?
   - ¿Cubren las tres etapas fundamentales: mercado/demanda, diseño organizativo/productivo y viabilidad financiera/precios?
   - ¿Son alcanzables dentro del alcance de un proyecto de grado Técnico Medio?
4. **Misión y Visión empresarial:** ¿reflejan la identidad productiva y los valores de la especialidad técnica?
5. **Completitud de la justificación:** ¿desarrolla claramente la triple perspectiva económica, social y técnica con datos concretos del entorno local?
6. **Normativa de formato:** ¿respeta la convención de punto decimal (SI/ISO 80000-1) y registro impersonal académico?

### Formato de salida esperado
```
## Diagnóstico general del Capítulo 2
[Evaluación global: alineación diagnóstica, objetivos y justificación]

## Evaluación de Objetivos
- Objetivo General: [Veredicto y sugerencia de redacción precisa]
- Objetivos Específicos:
  * [Objetivo 1]: [Observación metodológica]
  * [Objetivo 2]: [Observación metodológica]
  * [Objetivo 3]: [Observación metodológica]
- Misión y Visión: [Pertinencia con el rubro comercial]

## Evaluación del Diagnóstico y Justificación
- Diagnóstico y representatividad muestral: [Fortalezas, muestra diagnosticada, instrumentos aplicados y datos faltantes]
- Justificación económica/social/técnica: [Grado de sustento cuantitativo y social]

## Propuesta de texto LaTeX optimizado
```latex
% Fragmentos de objetivos y justificación mejorados
```
```
