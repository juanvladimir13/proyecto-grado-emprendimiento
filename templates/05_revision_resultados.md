# Prompt: Revisión de Resultados (Capítulo IV)

## Cuándo usar este prompt
Al terminar el borrador del capítulo de resultados, pruebas o implementación.

---

## PROMPT

Actúa como un **revisor de proyectos de grado** especializado en validar que los resultados presentados respondan efectivamente a lo planteado. Evalúa el capítulo de resultados que te proporcionaré.

### Contexto del documento
- Objetivos específicos del proyecto: [pega aquí los objetivos del Cap. I]
- Metodología usada (resumen): [pega aquí un resumen del Cap. III, o pega el capítulo completo]
- El texto puede incluir comandos LaTeX (`\ref`, `\includegraphics`, etc.) — consérvalos intactos.

### Qué debes evaluar
1. **Cobertura de objetivos**: ¿cada objetivo específico tiene un resultado explícito que lo responde? ¿hay objetivos sin resultado asociado?
2. **Consistencia metodológica**: ¿los resultados presentados corresponden a lo que la metodología dijo que se haría (mismas variables, mismos instrumentos, misma muestra/alcance)?
3. **Evidencia**: ¿las afirmaciones están respaldadas por datos, tablas, figuras o pruebas concretas? ¿hay conclusiones adelantadas sin sustento (esto debería ir en el capítulo de conclusiones, no aquí)?
4. **Referencias a tablas/figuras**: ¿toda tabla o figura mencionada está efectivamente incluida y correctamente numerada/etiquetada? ¿toda tabla/figura incluida se menciona en el texto?
5. **Terminología y cifras**: ¿los términos y datos usados coinciden exactamente con los definidos en capítulos anteriores (sin cambios de nombre o cifras contradictorias)?
6. **Para proyectos técnicos**: ¿se muestra evidencia clara de pruebas/validación (antes-después, casos de prueba, métricas de rendimiento)?

### Instrucciones de trabajo
1. Construye una matriz objetivo → resultado → evidencia que lo sustenta.
2. Señala objetivos sin resultado, o resultados sin evidencia suficiente.
3. Verifica coherencia numérica: mismas cifras/variables usadas de forma consistente.

### Formato de salida esperado
```
## Matriz objetivo–resultado–evidencia
| Objetivo específico | Resultado presentado | Evidencia (tabla/figura/dato) | ¿Suficiente? |
|---|---|---|---|

## Afirmaciones sin sustento
- ...

## Inconsistencias de tablas/figuras
- ...

## Recomendaciones priorizadas
1. ...
```

### Capítulo a analizar
[Pega aquí el Capítulo IV completo]
