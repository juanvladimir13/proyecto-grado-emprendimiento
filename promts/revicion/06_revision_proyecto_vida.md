# Prompt: Revisión del Proyecto de Vida (Capítulo 6)

## Cuándo usar este prompt
Al finalizar la redacción del borrador del **Capítulo 6: Proyecto de Vida** (`capitulos/06_proyecto_vida/main.tex`).

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier revisión.
2. Obtén los datos del proyecto desde `estilos/configuracion.tex` (`\tituloproyecto`, `\especialidad`, `\autoruno`, `\autordos`, `\modalidad`).
3. Lee directamente `capitulos/06_proyecto_vida/main.tex` (archivo único con contenido directo).
4. Lee `capitulos/03_desarrollo_emprendimiento/estructura_organizacional.tex` y `capitulos/05_resultados/indicadores_validados.tex` para verificar que las competencias empresariales y aprendizajes coincidan con las actividades efectivamente desarrolladas.
5. Consulta `docs/ficha-proyecto.md` (Sección 6).

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Sustituye los campos entre `[corchetes]` con los datos de tu proyecto.
3. Pega el contenido LaTeX de `capitulos/06_proyecto_vida/main.tex` al final.

---

## Archivos a revisar

| Archivo | Contenido |
| :--- | :--- |
| `capitulos/06_proyecto_vida/main.tex` | Contenido completo del capítulo (aspiraciones, competencias empresariales y compromiso socioeconómico) |
| **Dato cruzado:** `capitulos/03_desarrollo_emprendimiento/` | Roles, procesos y organización desempeñados en el negocio |
| **Dato cruzado:** `capitulos/05_resultados/` | Resultados y lecciones aprendidas en la validación práctica |

---

## PROMPT

Actúa como un **evaluador pedagógico y formativo del Bachillerato Técnico Humanístico (BTH)**. Evalúa el **Capítulo 6: Proyecto de Vida** que te proporcionaré, verificando la madurez reflexiva del estudiante (o de ambos estudiantes si es en parejas), la articulación entre el emprendimiento productivo, su vocación profesional y su aspiración de independencia económica y retribución social.

### Contexto del documento
- Modalidad: Emprendimiento Productivo (BTH Bolivia, RM 0912/2023, Anexo 1, inciso A)
- Especialidad técnica: [lee `\especialidad` de `estilos/configuracion.tex` o completa aquí]
- Nombre(s) del/los estudiante(s): [lee `\autoruno` (y `\autordos` si aplica) de `estilos/configuracion.tex` o completa aquí]
- Contenido evaluado en `capitulos/06_proyecto_vida/main.tex`:
  * `\section{Aspiraciones académicas y profesionales}`: Continuidad de estudios en carreras universitarias o técnicas superiores afines y continuidad del negocio a mediano/largo plazo.
  * `\section{Competencias empresariales y socioemocionales adquiridas}`: Habilidades duras en costeo, administración, producción y ventas; sumadas a resiliencia, negociación, liderazgo y servicio al cliente.
  * `\section{Compromiso ético, independencia económica y proyección a futuro}`: El emprendimiento como fuente de autogestión, independencia económica, proyección a 5 años y compromiso social comunitario.

### Qué debes evaluar
1. **Articulación vocacional y formativa**: ¿las metas de educación superior guardan estrecha relación con el rubro del emprendimiento y la especialidad técnica cursada?
2. **Reflexión sobre competencias empresariales**: ¿se describen aprendizajes concretos en gestión de costos, negociación comercial, trato directo con clientes y resolución de contingencias operativas?
3. **Independencia económica y visión a futuro**: ¿se visualiza con claridad el potencial del emprendimiento como herramienta de autoempleo sostenible y crecimiento familiar/personal?
4. **Compromiso ético y responsabilidad social**: ¿se expresa una vocación clara de retribución, cuidado ambiental y beneficio para la comunidad local?
5. **Modalidad dual (en parejas, si aplica)**: si el proyecto cuenta con dos autores, ¿se integran armónicamente las perspectivas y metas de ambos estudiantes?
6. **Estilo y formato**: ¿mantiene un tono reflexivo pero formal y maduro, propio de un egresado de Técnico Medio BTH?

### Formato de salida esperado
```
## Diagnóstico del Proyecto de Vida
[Evaluación global de la introspección vocacional y visión empresarial]

## Análisis por áreas
| Área | Nivel de desarrollo | Observación formativa |
|---|---|---|
| Aspiraciones académicas y profesionales | [Alto / Medio / Inicial] | ... |
| Competencias empresariales y socioemocionales | [Alto / Medio / Inicial] | ... |
| Independencia económica y compromiso ético | [Alto / Medio / Inicial] | ... |

## Sugerencias para enriquecer la reflexión vocacional y empresarial
1. ...
```
