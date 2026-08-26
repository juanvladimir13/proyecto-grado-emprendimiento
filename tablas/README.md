# Directorio de Tablas (`tablas/`)

En este directorio se almacenan todas las tablas independientes del documento, facilitando su edición modular y reutilización en los capítulos.

---

## 📁 Archivos Disponibles

```text
tablas/
├── tabla_ejemplo.tex             # Estructura base de tabla formal con booktabs
├── estudio_mercado_ejemplo.tex   # Matriz de análisis de competidores y mercado
├── inversiones_ejemplo.tex       # Resumen de activos fijos y capital de operación
├── costos_produccion_ejemplo.tex # Estructura de costos variables y costos fijos
├── costos_ejemplo.tex            # Resumen de costos generales de innovación
├── cronograma_ejemplo.tex        # Planificación temporal de actividades por fases
└── README.md                     # Guía de uso (este archivo)
```

---

## 📌 ¿Cómo incluir una tabla en un capítulo?

Para incluir una tabla en cualquier sección o capítulo `.tex`, utiliza la instrucción `\input`:

```latex
\input{tablas/inversiones_ejemplo.tex}
```

---

## 📐 Estándar APA 7ma Edición para Tablas con `booktabs`

1. **Líneas horizontales:** Usar únicamente `\toprule`, `\midrule` y `\bottomrule`.
2. **Sin líneas verticales:** Las normas APA prohíben las líneas verticales en tablas (`|`).
3. **Alineación:**
   - Texto: alineado a la izquierda (`l`).
   - Números: alineados a la derecha (`r`).
   - Códigos o categorías breves: centrados (`c`).

### Plantilla Base:
```latex
\begin{table}[htbp]
    \centering
    \caption{Título descriptivo y conciso de la tabla.}
    \label{tab:clave_referencia}
    \begin{tabular}{lrr}
        \toprule
        \textbf{Concepto} & \textbf{Cantidad} & \textbf{Monto (Bs)} \\
        \midrule
        Ítem 1            & 10                & 150.00 \\
        Ítem 2            & 5                 & 80.00 \\
        \midrule
        \textbf{Total}    &                   & \textbf{230.00} \\
        \bottomrule
    \end{tabular}
\end{table}
```
