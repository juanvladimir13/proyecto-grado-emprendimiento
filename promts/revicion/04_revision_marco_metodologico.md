# Prompt: Revisión del Marco Metodológico / Ingeniería del Proyecto (Capítulo III)

## Cuándo usar este prompt
Al terminar el borrador del capítulo de metodología (o de diseño/ingeniería del proyecto, en el caso de proyectos técnicos).

---

## PROMPT

Actúa como un **revisor metodológico** de proyectos de grado. Evalúa el capítulo de metodología que te proporcionaré, verificando que sea coherente con los objetivos planteados y ejecutable de forma verificable.

### Contexto del documento
- Tipo de proyecto: [investigación aplicada / desarrollo de software / ingeniería — especifica]
- Objetivos específicos del proyecto: [pega aquí los objetivos del Cap. I]
- El texto puede incluir comandos LaTeX — consérvalos intactos.

> **Nota:** si tu proyecto es de desarrollo de software, evalúa esta sección como **metodología de desarrollo** (ej. Scrum, RUP, XP, cascada) en lugar de metodología de investigación clásica (enfoque, tipo, diseño, población/muestra). Indica cuál aplica antes de comenzar el análisis.

### Qué debes evaluar (proyectos de investigación clásica)
1. **Enfoque y tipo de investigación**: ¿están correctamente justificados según el problema y los objetivos?
2. **Población/muestra**: ¿está bien definida y es coherente con el alcance del Cap. I?
3. **Instrumentos y técnicas de recolección**: ¿son adecuados para responder cada objetivo específico?
4. **Procedimiento**: ¿las fases descritas son suficientes para reproducir el trabajo?

### Qué debes evaluar (proyectos de desarrollo de software/técnicos)
1. **Metodología de desarrollo elegida**: ¿está justificada (por qué esa y no otra)?
2. **Fases/etapas**: ¿cubren todo el ciclo necesario (análisis, diseño, implementación, pruebas)?
3. **Herramientas y tecnologías**: ¿están claramente listadas y justificadas?
4. **Requerimientos**: ¿los requerimientos funcionales/no funcionales se derivan claramente de los objetivos y del problema?

### En ambos casos
- **Alineación objetivo → método**: cada objetivo específico debe tener una fase o técnica metodológica que lo aborde explícitamente.
- **Viabilidad**: ¿el método descrito es realista dentro del alcance y tiempo definidos en el Cap. I?

### Instrucciones de trabajo
1. Construye una tabla que relacione cada objetivo específico con la parte de la metodología que lo atiende.
2. Señala objetivos sin método asociado, o partes de la metodología sin objetivo que las justifique.
3. Evalúa si el nivel de detalle permite reproducir o auditar el trabajo.

### Formato de salida esperado
```
## Enfoque metodológico identificado
[clásico / desarrollo de software / mixto]

## Tabla de alineación objetivo–método
| Objetivo específico | Fase/técnica que lo atiende | ¿Suficiente? | Observación |
|---|---|---|---|

## Vacíos o sobredimensionamientos
- ...

## Recomendaciones priorizadas
1. ...
```

### Capítulo a analizar
[Pega aquí el Capítulo III completo]
