# Prompt: Revisión de Conclusiones y Recomendaciones (Capítulo 7)

## Cuándo usar este prompt
Al finalizar el borrador del **Capítulo 7: Conclusiones y Recomendaciones** (`capitulos/07_conclusiones_recomendaciones/`).

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier revisión.
2. Obtén los datos del proyecto desde `estilos/configuracion.tex` (`\tituloproyecto`, `\especialidad`, `\modalidad`).
3. Lee directamente los archivos `.tex` indicados en la sección "Archivos a revisar".
4. Lee `capitulos/02_planteamiento_emprendimiento/objetivos.tex` para verificar el cierre puntual de cada objetivo específico.
5. Lee `capitulos/04_viabilidad_sostenibilidad/costo_produccion.tex` y `capitulos/05_resultados/indicadores_validados.tex` para verificar que las conclusiones financieras y comerciales se sustenten en evidencia.
6. Consulta `docs/ficha-proyecto.md` (Sección 7).

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Sustituye los campos entre `[corchetes]` con los datos de tu proyecto.
3. Pega el contenido LaTeX del capítulo, los objetivos del Cap. 2 y los resultados del Cap. 5 al final.

---

## Archivos a revisar

| Archivo | Contenido |
| :--- | :--- |
| `capitulos/07_conclusiones_recomendaciones/main.tex` | Ensamble del capítulo (`\chapter` y sub-archivos) |
| `capitulos/07_conclusiones_recomendaciones/conclusiones.tex` | Conclusiones directas del cumplimiento de objetivos específicos |
| `capitulos/07_conclusiones_recomendaciones/recomendaciones.tex` | Recomendaciones operativas, comerciales y de gestión |
| **Dato cruzado:** `capitulos/02_planteamiento_emprendimiento/objetivos.tex` | Objetivos específicos a cerrar |
| **Dato cruzado:** `capitulos/04_viabilidad_sostenibilidad/costo_produccion.tex` | Rentabilidad y punto de equilibrio calculados |
| **Dato cruzado:** `capitulos/05_resultados/indicadores_validados.tex` | Evidencia empírica de validación comercial |

---

## PROMPT

Actúa como un **revisor de comités de titulación BTH** en la modalidad **Emprendimiento Productivo**. Evalúa el **Capítulo 7: Conclusiones y Recomendaciones** que te proporcionaré, verificando que cierre de forma rigurosa, comercialmente verificable y técnica todo lo planteado a lo largo del plan de negocio.

### Contexto del documento
- Modalidad: Emprendimiento Productivo (BTH Bolivia, RM 0912/2023, Anexo 1, inciso A)
- Especialidad técnica: [lee `\especialidad` de `estilos/configuracion.tex` o completa aquí]
- Título del proyecto: [lee `\tituloproyecto` de `estilos/configuracion.tex` o completa aquí]
- Objetivos específicos a cerrar: [lee `capitulos/02_planteamiento_emprendimiento/objetivos.tex` o pega aquí]
- Resumen de resultados clave: [lee `capitulos/05_resultados/` o pega aquí]

### Qué debes evaluar
1. **Cierre directo de objetivos específicos**: ¿existe una conclusión explícita, clara y medible por cada objetivo específico formulado en el Capítulo 2 (estudio de mercado, diseño operativo/organizacional y viabilidad financiera)?
2. **Conclusiones fundamentadas en resultados**: ¿todas las conclusiones derivan directamente de las evidencias del Capítulo 5 y del análisis financiero del Capítulo 4 (sin introducir afirmaciones infundadas)?
3. **Validación de la propuesta de valor y del negocio**: ¿las conclusiones dejan establecido que el emprendimiento es comercialmente viable, técnicamente factible y económicamente sostenible?
4. **Recomendaciones estratégicas y aplicadas**: ¿son sugerencias concretas orientadas a la expansión comercial, canales digitales, optimización de costos, formalización tributaria/sanitaria y reinversión de utilidades?
5. **Estructura en viñetas (`itemize`)**: ¿se utiliza obligatoriamente el entorno `itemize` para la presentación de conclusiones y recomendaciones, evitando enumeraciones con números?
6. **Tono y registro**: ¿mantiene redacción formal en tercera persona impersonal y evita incorporar citas bibliográficas nuevas en este capítulo final?

### Formato de salida esperado
```
## Diagnóstico general del Capítulo 7
[Evaluación global: rigor del cierre y pertinencia de recomendaciones]

## Matriz de Coherencia: Objetivos vs. Conclusiones
| Objetivo Específico (Cap. 2) | Conclusión Correspondiente (Cap. 7) | Estado de Cierre |
|---|---|---|
| 1. Estudio de mercado y demanda | ... | [Cerrado / Parcial / No abordado] |
| 2. Organización y ciclo operativo | ... | [Cerrado / Parcial / No abordado] |
| 3. Viabilidad financiera y costos | ... | [Cerrado / Parcial / No abordado] |

## Evaluación de Recomendaciones
- Viabilidad operativa:
- Estrategia comercial y de crecimiento:
- Control de costos y reinversión:

## Propuesta de Redacción Optimizada (LaTeX)
```latex
% Fragmentos con conclusiones y recomendaciones ajustadas
```
```
