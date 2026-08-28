# Prompt: Revisión de Citas y Bibliografía (APA 7ma Edición / BibLaTeX)

## Cuándo usar este prompt
Al finalizar la redacción de los capítulos y tras registrar las fuentes en `bibliografia/referencias.bib`, para garantizar correspondencia biunívoca y formato APA 7ma Edición.

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de citas y bibliografía (Regla 5) antes de cualquier revisión.
2. Lee `bibliografia/referencias.bib` completo para analizar las entradas existentes.
3. Busca todas las ocurrencias de `\parencite` y `\textcite` en los archivos `.tex` de `capitulos/` (Capítulos 1 al 7) para mapear las citas en el texto.
4. Verifica la correspondencia biunívoca: toda cita en texto debe tener entrada en `.bib` y viceversa (sin referencias huérfanas).

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Pega las citas extraídas de los capítulos y el contenido de `referencias.bib` al final.

---

## Archivos a revisar

| Archivo | Contenido |
| :--- | :--- |
| `bibliografia/referencias.bib` | Base de datos BibLaTeX con todas las referencias del proyecto |
| `capitulos/01_introduccion/*.tex` a `capitulos/07_conclusiones_recomendaciones/*.tex` | Citas `\parencite{}` y `\textcite{}` en el cuerpo del documento |

---

## PROMPT

Actúa como un **experto en normalización bibliográfica y normas APA 7ma Edición** para documentos técnicos en LaTeX (`biblatex` con estilo `apa` y motor `biber`). Evalúa las citas dentro del texto y el archivo de referencias que te proporcionaré.

### Contexto del documento
- Modalidad: Proyecto de Grado BTH — Emprendimiento Productivo (RM 0912/2023)
- Motor bibliográfico: `biblatex` con `style=apa` y backend `biber`
- Archivo fuente de referencias: `bibliografia/referencias.bib`
- Comandos en texto:
  * Citas parentéticas: `\parencite{clave}` ➔ *(Apellido, Año)*
  * Citas narrativas: `\textcite{clave}` ➔ *Apellido (Año)*
  * Múltiples citas: `\parencite{clave1, clave2}`

### Qué debes evaluar
1. **Correspondencia biunívoca (100% sincronía)**:
   - ¿Toda cita presente en el texto (`\parencite`, `\textcite`) tiene su entrada correspondiente en `referencias.bib`?
   - ¿Toda entrada existente en `referencias.bib` está efectivamente citada en el cuerpo del documento (sin referencias huérfanas)?
2. **Campos obligatorios según tipo de fuente en APA 7**:
   - Libros (`@book`): autor, año, título (cursiva), editorial (ej. Kotler, Osterwalder).
   - Artículos de revista (`@article`): autor, año, título del artículo, nombre de la revista, volumen, número, páginas, DOI/URL.
   - Normas, leyes y reglamentos (`@misc` / `@legislation`): entidad emisora (Ministerio de Educación), año, título oficial (RM 0912/2023), URL o gaceta.
   - Informes técnicos o estadísticos (`@report` / `@online`): INE, cámaras sectoriales, fecha, título, URL.
3. **Calidad y pertinencia de las fuentes**:
   - ¿Se citan fuentes confiables de modelos de negocio, formulación de proyectos, costos y estudios sectoriales en lugar de páginas informales?
4. **Sintaxis BibLaTeX**:
   - Claves de citación descriptivas sin espacios ni caracteres especiales.
   - Llaves de protección de mayúsculas en nombres propios (`{Bolivia}`, `{Cochabamba}`).

### Formato de salida esperado
```
## Diagnóstico general de bibliografía
- Estado de correspondencia: [100% Sincronizado / Citas faltantes / Entradas huérfanas]
- Cumplimiento de normas APA 7: [Alto / Medio / Bajo]

## Matriz de Correspondencia Citas vs. Referencias
| Clave de citación | Citado en el texto | Presente en referencias.bib | Tipo de entrada | Observación |
|---|---|---|---|---|

## Entradas en .bib con errores de formato o campos faltantes
- [Clave]: [Campo faltante o error tipográfico]

## Propuesta de corrección para `bibliografia/referencias.bib`
```bibtex
% Entradas BibLaTeX corregidas o añadidas
```
```
