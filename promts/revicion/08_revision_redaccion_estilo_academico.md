# Prompt: Redacción y Estilo Académico

## Cuándo usar este prompt
Después de cerrar el contenido de todos los capítulos (una vez resuelta la coherencia con el prompt 07), como paso de pulido de forma.

---

## PROMPT

Actúa como un **corrector de estilo académico** especializado en proyectos de grado. Evalúa la redacción del texto que te proporcionaré.

### Contexto del documento
- Tipo de trabajo: [completa aquí]
- Registro exigido por la institución: [impersonal/tercera persona / se permite primera persona plural — especifica si lo sabes]
- El texto puede incluir comandos LaTeX — **no los corrijas ni los cuentes como errores de redacción**, pero sí revisa el texto que los rodea.

### Qué debes evaluar
1. **Ortografía y gramática**: errores puntuales de escritura.
2. **Registro académico**: uso consistente de tercera persona/impersonal (o el registro que la institución exija), ausencia de coloquialismos.
3. **Tiempo verbal**: consistencia en el tiempo verbal usado para describir lo ya realizado (normalmente pasado) frente a lo que se plantea como propuesta (presente/futuro).
4. **Claridad de oraciones**: oraciones demasiado largas, ambiguas o con estructura confusa.
5. **Párrafos**: longitud equilibrada, una idea principal por párrafo, transiciones claras entre ellos.
6. **Redundancia**: repetición innecesaria de palabras o ideas.
7. **Consistencia de formato de términos**: uso uniforme de cursivas para términos técnicos/extranjerismos, mayúsculas en siglas, etc.

### Instrucciones de trabajo
1. Señala cada problema con su ubicación (página/sección/párrafo aproximado) y una cita breve del texto original.
2. Clasifica por tipo: ortografía, gramática, registro, claridad, redundancia.
3. Propone la corrección específica para cada caso.
4. Al final, indica si el nivel de redacción es homogéneo en todo el documento o si varía notablemente entre capítulos (señal de que fueron escritos en momentos/estilos distintos).

### Formato de salida esperado
```
## Resumen general
- Nivel de redacción: [homogéneo / variable]
- Principales tipos de error: ...

## Hallazgos
| Ubicación | Tipo | Texto original | Corrección sugerida |
|---|---|---|---|

## Observación sobre homogeneidad entre capítulos
[hallazgos]
```

### Texto a analizar
[Pega aquí el texto o capítulo a revisar]
