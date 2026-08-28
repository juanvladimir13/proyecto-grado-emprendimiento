# Prompt: Revisión de Conclusiones y Recomendaciones (Capítulo V)

## Cuándo usar este prompt
Al terminar el borrador del capítulo final del proyecto.

---

## PROMPT

Actúa como un **revisor de proyectos de grado**. Evalúa el capítulo de conclusiones y recomendaciones que te proporcionaré, verificando que cierre de forma coherente todo lo planteado en el documento.

### Contexto del documento
- Objetivos específicos del proyecto: [pega aquí los objetivos del Cap. I]
- Resumen de resultados clave: [pega aquí un resumen del Cap. IV, o el capítulo completo]
- El texto puede incluir comandos LaTeX — consérvalos intactos.

### Qué debes evaluar
1. **Cierre de objetivos**: ¿existe una conclusión explícita por cada objetivo específico? ¿la conclusión se deriva directamente de un resultado presentado en el Cap. IV (y no de una idea nueva no discutida antes)?
2. **Conclusiones "huérfanas"**: ¿hay conclusiones que no corresponden a ningún objetivo ni resultado previo?
3. **Coherencia con el problema inicial**: ¿las conclusiones responden efectivamente al problema planteado en el Cap. I?
4. **Recomendaciones**: ¿son concretas y accionables (no genéricas)? ¿se derivan de limitaciones o hallazgos reales del proyecto, y no de temas nunca mencionados antes?
5. **Tono**: ¿se evita introducir información, datos o citas nuevas en este capítulo (las conclusiones no deben "descubrir" nada nuevo)?

### Instrucciones de trabajo
1. Construye una tabla objetivo → conclusión correspondiente → ¿cerrado? (sí/no).
2. Señala conclusiones sin objetivo asociado.
3. Evalúa si cada recomendación tiene una base clara en el desarrollo del proyecto.

### Formato de salida esperado
```
## Tabla de cierre de objetivos
| Objetivo específico | Conclusión asociada | ¿Cerrado? | Observación |
|---|---|---|---|

## Conclusiones huérfanas
- ...

## Evaluación de recomendaciones
| Recomendación | ¿Basada en un hallazgo real? | Observación |
|---|---|---|

## Recomendaciones priorizadas (para el autor)
1. ...
```

### Capítulo a analizar
[Pega aquí el Capítulo V completo]
