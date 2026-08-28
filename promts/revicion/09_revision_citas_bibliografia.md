# Prompt: Citas y Bibliografía

## Cuándo usar este prompt
En paralelo o después de la revisión de redacción (prompt 08), antes de la pasada final de checklist.

---

## PROMPT

Actúa como un **revisor de normas de citación académica**. Evalúa las citas y la bibliografía del documento que te proporcionaré.

### Contexto del documento
- Norma de citación exigida: [APA 7 / IEEE / Vancouver / otra — especifica]
- El texto puede incluir comandos LaTeX (`\cite{}`, `\bibliography{}`, archivos `.bib`) — trátalos como el mecanismo de citación válido, no como error.

### Qué debes evaluar
1. **Formato de citas en el texto**: ¿siguen consistentemente la norma indicada (autor-fecha, numérica, etc.)?
2. **Correspondencia cita↔referencia**: ¿todo autor/fuente citado en el texto aparece en la lista de referencias? ¿toda referencia listada se cita al menos una vez en el texto?
3. **Formato de la lista de referencias**: ¿cada entrada sigue el formato completo exigido (autor, año, título, fuente, etc.)?
4. **Actualidad de fuentes**: ¿qué proporción de fuentes es de los últimos 5-10 años? ¿hay dependencia excesiva de fuentes muy antiguas o de baja calidad (blogs no especializados, Wikipedia como fuente primaria, etc.)?
5. **Uso de citas textuales vs. paráfrasis**: ¿se abusa de la cita textual en lugar de la paráfrasis y el análisis propio?
6. **Autocitación de fuentes secundarias**: ¿se cita a un autor citado por otro (cita de cita) sin acceder a la fuente original, sin indicarlo correctamente?

### Instrucciones de trabajo
1. Si te proporciono el texto y la bibliografía, cruza ambas listas y señala discrepancias.
2. Calcula (aproximado) el porcentaje de fuentes por antigüedad.
3. Señala citas con formato inconsistente respecto a la norma indicada.

### Formato de salida esperado
```
## Discrepancias cita–referencia
### Citadas en el texto pero ausentes en bibliografía
- ...
### En bibliografía pero nunca citadas
- ...

## Consistencia de formato
[hallazgos]

## Actualidad de fuentes
- % últimos 5 años: ...
- % más de 10 años: ...

## Recomendaciones priorizadas
1. ...
```

### Material a analizar
[Pega aquí el texto con las citas, y/o la lista de referencias/bibliografía]
