# Prompt: Coherencia y Sincronía Global (Los 7 Capítulos BTH)

## Cuándo usar este prompt
Cuando el borrador completo de los **7 capítulos** esté redactado, antes de proceder a la corrección de estilo y maquetación final. Es la auditoría integradora esencial del plan de emprendimiento productivo.

---

## Instrucciones de uso

### Para agentes de IA con acceso al repositorio
1. Lee `AGENTS.md` y sigue sus reglas de formato LaTeX antes de cualquier revisión.
2. Obtén los datos del proyecto desde `estilos/configuracion.tex` (`\tituloproyecto`, `\especialidad`, `\modalidad`).
3. Lee los 7 `main.tex` de cada capítulo y todas sus secciones `.tex` (ver tabla abajo).
4. Lee `bibliografia/referencias.bib` para verificar correspondencia de citas.
5. Consulta `docs/ficha-proyecto.md` como referencia cruzada de datos consolidados.

### Para uso manual (copiar y pegar)
1. Copia este prompt en la conversación con el asistente de IA.
2. Pega el contenido de los 7 capítulos al final.

---

## Archivos a revisar

| Capítulo | Archivo de ensamble | Secciones |
| :--- | :--- | :--- |
| Cap. 1 | `capitulos/01_introduccion/main.tex` | `contexto_general.tex`, `oportunidad_negocio.tex`, `propuesta_valor.tex`, `marco_teorico.tex` |
| Cap. 2 | `capitulos/02_planteamiento_emprendimiento/main.tex` | `diagnostico.tex`, `objetivos.tex`, `justificacion.tex` |
| Cap. 3 | `capitulos/03_desarrollo_emprendimiento/main.tex` | `localizacion.tex`, `analisis_mercado.tex`, `estrategia_promocion.tex`, `estructura_organizacional.tex`, `diseno_producto.tex`, `ciclo_produccion.tex` |
| Cap. 4 | `capitulos/04_viabilidad_sostenibilidad/main.tex` | `calculo_inversiones.tex`, `costo_produccion.tex` |
| Cap. 5 | `capitulos/05_resultados/main.tex` | `resultados_cuantitativos.tex`, `resultados_cualitativos.tex`, `indicadores_validados.tex` |
| Cap. 6 | `capitulos/06_proyecto_vida/main.tex` | *(contenido directo en main.tex)* |
| Cap. 7 | `capitulos/07_conclusiones_recomendaciones/main.tex` | `conclusiones.tex`, `recomendaciones.tex` |

---

## PROMPT

Actúa como un **auditor metodológico y financiero de proyectos de grado BTH**. Tu misión es evaluar los 7 capítulos del proyecto de grado en la modalidad de **Emprendimiento Productivo** para certificar su **coherencia argumental total**, **sincronía matemática/comercial** y **ausencia de contradicciones internas**.

### Contexto del documento
- Modalidad: Emprendimiento Productivo (BTH Bolivia, RM 0912/2023, Anexo 1, inciso A)
- Especialidad técnica: [lee `\especialidad` de `estilos/configuracion.tex` o completa aquí]
- Título del proyecto: [lee `\tituloproyecto` de `estilos/configuracion.tex` o completa aquí]
- Formato: comandos LaTeX (`\section`, `\ref`, `\cite`, `\input`) deben preservarse.

### Criterios de auditoría global

1. **Hilo conductor y sincronía (Oportunidad ➔ Objetivos ➔ Operaciones ➔ Finanzas ➔ Validación ➔ Conclusiones):**
   - ¿La oportunidad identificada en el Cap. 1 y el diagnóstico del Cap. 2 coinciden con la demanda y público objetivo analizados en el Cap. 3?
   - ¿Los productos o servicios diseñados en el Cap. 3 son exactamente los costea el Cap. 4 y valida el Cap. 5?
   - ¿Cada objetivo específico formulado en el Cap. 2 tiene su desarrollo operativo en el Cap. 3, su presupuesto en el Cap. 4, su verificación empírica en el Cap. 5 y su cierre formal en el Cap. 7?

2. **Consistencia numérica y financiera:**
   - ¿Los montos de inversión fija y capital de operación del Cap. 4 coinciden con las cifras mencionadas en la justificación económica (Cap. 2)?
   - ¿El precio de venta unitario determinado en el Cap. 4 es el mismo empleado en el estudio de mercado (Cap. 3) y en el registro de ventas piloto (Cap. 5)?
   - ¿El punto de equilibrio calculado en el Cap. 4 guarda proporción lógica con la capacidad instalada del proceso productivo (Cap. 3) y los resultados piloto (Cap. 5)?
   - ¿El formato numérico es rigurosamente homogéneo en todos los capítulos y tablas? (Uso obligatorio de punto `.` para decimales como `12.50` y ausencia de comas o puntos en millares, ej. `4500.00` o `25 000.00` según norma SI/ISO 80000-1).

3. **Consistencia institucional y de roles:**
   - ¿La denominación de la empresa, marca comercial y producto es idéntica en carátula, Cap. 1, 3, 4 y 6?
   - ¿Las funciones operativas asignadas en el manual de cargos (Cap. 3) coinciden con las competencias empresariales adquiridas descritas en el Proyecto de Vida (Cap. 6)?

4. **Formato y estilo:**
   - Prioridad obligatoria de viñetas (`\begin{itemize}`) sobre listas numeradas en objetivos, conclusiones y recomendaciones.
   - Citas normalizadas con BibLaTeX APA 7 (`\parencite`, `\textcite`).
   - Tablas en `booktabs` con `\notatabla{Fuente: ...}` y sin líneas verticales.

### Formato de salida esperado
```
## Diagnóstico Panorámico de Sincronía
[Evaluación global de coherencia entre los 7 capítulos]

## Matriz de Trazabilidad Integral
| Objetivo Específico (Cap. 2) | Sección Operativa (Cap. 3) | Registro Financiero (Cap. 4) | Validación Piloto (Cap. 5) | Conclusión (Cap. 7) | Estado |
|---|---|---|---|---|---|

## Inconsistencias Numéricas o Argumentales Detectadas
- [Capítulo X vs Capítulo Y]: [Contradicción detectada y propuesta de unificación]

## Ajustes Requeridos en Código LaTeX
```latex
% Fragmentos con las cifras o denominaciones unificadas
```
```
