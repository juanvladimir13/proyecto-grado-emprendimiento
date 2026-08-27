# Flujo de Revisión de Documentos de Proyecto de Grado

Este set de prompts está diseñado para revisar un proyecto de grado **por etapas**, en lugar de intentar evaluar todo el documento de una sola vez. Cada archivo es un prompt independiente que puedes pegar en una conversación con IA junto con el capítulo o sección correspondiente.

## Orden recomendado de uso

| # | Archivo | Qué revisa | Cuándo usarlo |
|---|---|---|---|
| 1 | `01_revision_estructura_general.md` | Índice, organización de capítulos, normas institucionales | Al iniciar, con el índice/esqueleto del documento |
| 2 | `02_revision_planteamiento_problema.md` | Cap. I: problema, objetivos, justificación, alcance | Al terminar el borrador del Cap. I |
| 3 | `03_revision_marco_teorico.md` | Cap. II: marco teórico, cobertura conceptual, citas | Al terminar el borrador del Cap. II |
| 4 | `04_revision_marco_metodologico.md` | Cap. III: metodología / ingeniería del proyecto | Al terminar el borrador del Cap. III |
| 5 | `05_revision_resultados.md` | Cap. IV: resultados, pruebas, evidencia | Al terminar el borrador del Cap. IV |
| 6 | `06_revision_conclusiones_recomendaciones.md` | Cap. V: conclusiones y recomendaciones | Al terminar el borrador del Cap. V |
| 7 | `07_revision_coherencia_sincronia_global.md` | Coherencia y sincronía entre TODOS los capítulos | Cuando ya tengas el documento completo (o casi) |
| 8 | `08_revision_redaccion_estilo_academico.md` | Redacción, gramática, registro académico | Después de cerrar el contenido, antes de pulir forma |
| 9 | `09_revision_citas_bibliografia.md` | Formato de citas, consistencia con bibliografía | En paralelo o después del punto 8 |
| 10 | `10_checklist_pre_entrega_final.md` | Checklist final integral antes de entregar | Última pasada, antes de imprimir/subir |

## Cómo usar cada prompt

1. Abre el archivo del prompt correspondiente a la etapa en la que estás.
2. Copia el contenido en tu conversación con la IA.
3. Completa los campos entre `[corchetes]` con la información de tu proyecto.
4. Pega el capítulo o sección a revisar donde se indica.
5. Guarda el informe de hallazgos que te devuelva la IA — te servirá como insumo para el prompt #7 (coherencia global), que revisa que las correcciones de cada capítulo no generen nuevas inconsistencias entre ellos.

## Nota sobre LaTeX

Todos los prompts incluyen una instrucción para que la IA conserve intactos los comandos LaTeX (`\section`, `\cite`, `\ref`, `\label`, etc.) y no los confunda con errores de redacción, dado que la documentación se trabaja en ese formato.

## Nota sobre proyectos técnicos/de sistemas

Si tu proyecto de grado es de desarrollo de software (como un sistema web), el prompt #4 (`04_revision_marco_metodologico.md`) incluye una variante para metodologías de desarrollo (Scrum, RUP, XP, cascada, etc.) en lugar de metodología de investigación pura — usa la que corresponda a tu enfoque.
