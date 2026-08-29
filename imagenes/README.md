# Directorio de Imágenes y Figuras (`imagenes/`)

En este directorio se almacenan todos los recursos gráficos del proyecto de grado (logotipos, diagramas de flujo, organigramas, esquemas de distribución, fotografías de prototipos y planos técnicos).

La ruta `imagenes/` está configurada automáticamente en el paquete `graphicx` dentro de `estilos/estilos.sty`, permitiendo invocar las imágenes directamente por su nombre de archivo (por ejemplo, `\includegraphics{ejemplo_figura.png}`) sin necesidad de anteponer la ruta de carpetas.

---

## 📐 Estándar APA 7ma Edición para Figuras e Imágenes

En la **7ma Edición de las Normas APA**, el formato de presentación de figuras se unificó con el de las tablas, estableciendo cuatro componentes esenciales en un orden estricto:

```text
┌─────────────────────────────────────────────────────────────┐
│ Figura X.Y                                                  │ <- 1. Número en Negrita (arriba)
│ Título breve y descriptivo en letra cursiva                 │ <- 2. Título en Cursiva (arriba)
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    [ ELEMENTO VISUAL ]                      │ <- 3. Imagen / Gráfico (centrado)
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ Nota. Explicación adicional, simbología y fuente.           │ <- 4. Nota al pie (abajo, alineada izq.)
└─────────────────────────────────────────────────────────────┘
```

### ⚠️ Diferencia Clave entre APA 6 y APA 7
* **Normas APA 6:** El número y título de la figura se colocaban debajo de la imagen.
* **Normas APA 7 (Vigente en este proyecto):** El número y título se colocan **OBLIGATORIAMENTE ARRIBA** de la imagen. La parte inferior queda reservada exclusivamente para la nota explicativa (`\notafigura`).

---

## 🚀 Formas de Agregar Imágenes en los Capítulos

La plantilla ofrece dos formas estandarizadas para incluir figuras: el **entorno clásico** (máximo control) y la **macro semántica** (más rápida y compacta).

### 📄 Opción 1: Entorno Estándar de LaTeX (Recomendada)
Ideal cuando se desea controlar individualmente el ancho, el centrado o incorporar ajustes específicos:

```latex
\begin{figure}[htbp]
    \caption{Diagrama de flujo del ciclo de transformación de la materia prima.}
    \label{fig:ciclo_produccion}
    \centering
    \includegraphics[width=0.85\textwidth]{ejemplo_figura.png}
    \notafigura{Elaboración propia a partir del estudio técnico de operaciones.}
\end{figure}
```

> **Importante sobre el orden:** 
> Observe que `\caption{...}` y `\label{...}` se colocan **antes** de `\includegraphics{...}`. La plantilla aplica automáticamente negrita al rótulo, salto de línea y cursiva al título según APA 7.

---

### ⚡ Opción 2: Macro Semántica Simplificada (`\figuraapa` / `\insertarfigura`)
Diseñada para insertar figuras en una sola instrucción sin repetir la estructura del entorno:

```latex
\figuraapa[width=0.80\textwidth]{ejemplo_figura.png}%
    {Diagrama de flujo del ciclo de transformación de la materia prima.}%
    {fig:ciclo_produccion}%
    {Elaboración propia a partir del estudio técnico de operaciones.}
```

**Sintaxis:**
`\figuraapa[opciones_ancho]{archivo}{Título}{etiqueta_label}{Nota_al_pie}`

* `[opciones_ancho]` *(Opcional)*: Define la escala (por defecto toma `\anchofigurapredeterminado`, es decir, `0.85\textwidth`).
* `{archivo}`: Nombre de la imagen en `imagenes/` (ej. `logotipo.png`).
* `{Título}`: Título descriptivo de la figura (se mostrará en cursiva automáticamente).
* `{etiqueta_label}`: Clave única para referencia cruzada (ej. `fig:logotipo`).
* `{Nota_al_pie}`: Contenido de la nota (se antecederá automáticamente con `Nota.` en cursiva). Si se deja `{}` vacío, no se imprimirá ninguna nota.

*(También disponible con el alias `\insertarfigura`).*

---

### 🧩 Opción 3: Subfiguras Comparativas (a y b)
Para comparar dos imágenes en paralelo (por ejemplo, antes vs. después, o prototipo inicial vs. final):

```latex
\begin{figure}[htbp]
    \caption{Comparación entre el prototipo preliminar y el diseño comercial final.}
    \label{fig:comparacion_prototipos}
    \centering
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{prototipo_a.png}
        \caption{Prototipo preliminar de laboratorio.}
        \label{subfig:prototipo_a}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{prototipo_b.png}
        \caption{Empaque biodegradable final.}
        \label{subfig:prototipo_b}
    \end{subfigure}
    \notafigura{Fotografías tomadas durante la fase de validación técnica.}
\end{figure}
```

---

### 📊 Opción 4: Gráficos y Diagramas Vectoriales Nativos (TikZ)
Para diagramas de bloques, flujos conceptuales o gráficos estadísticos generados directamente en LaTeX (sin archivo de imagen externo):

```latex
\begin{figure}[htbp]
    \caption{Esquema conceptual del modelo de operaciones del emprendimiento.}
    \label{fig:modelo_operaciones}
    \centering
    \begin{tikzpicture}
        \node[draw=primary, fill=lightgray, rounded corners, inner sep=6pt] (a) {Adquisición de Insumos};
        \node[draw=secondary, fill=lightgray, rounded corners, inner sep=6pt, right=1.5cm of a] (b) {Producción};
        \draw[->, thick, primary] (a) -- (b);
    \end{tikzpicture}
    \notagrafico{Elaboración propia con base en el diseño metodológico del proyecto.}
\end{figure}
```

---

## ✍️ Reglas de Redacción y Citación de Figuras

### 1. Referencia Cruzada en el Texto Principal
Toda figura debe mencionarse explícitamente en el cuerpo del texto antes de que el lector la visualice:
* Correcto: `Como se ilustra en la Figura~\ref{fig:ciclo_produccion}, el proceso inicia con...`
* Correcto: `El esquema organizativo propuesto (véase la Figura~\ref{fig:organigrama}) define...`
* Incorrecto: `En la figura de abajo podemos ver el resultado...` *(Nunca usar referencias espaciales como "arriba", "abajo" o "a continuación")*.

### 2. Estándar para la Nota al Pie (`\notafigura`)
La macro `\notafigura{...}` incluye de forma automática la palabra `Nota.` en cursiva. Se redacta según la procedencia del material:
* **Elaboración propia:**
  ```latex
  \notafigura{Elaboración propia con base en datos recolectados durante la prueba piloto.}
  ```
* **Fuente externa con adaptación (APA 7):**
  ```latex
  \notafigura{Adaptado de \textcite{senasag2024}.}
  ```
* **Reproducción textual / autoría externa (APA 7):**
  ```latex
  \notafigura{Tomado de \parencite[p.~45]{ine2022}.}
  ```

---

## ⚙️ Parámetros Centralizados en `estilos/configuracion.tex`

Puede ajustar los parámetros globales de las imágenes en `estilos/configuracion.tex`:

```latex
% Ancho predeterminado para figuras insertadas con \figuraapa
\newcommand{\anchofigurapredeterminado}{0.85\textwidth}

% Espaciado vertical entre la imagen y su nota al pie
\newcommand{\espacionotafigura}{4pt}
```

---

## 📷 Recomendaciones Técnicas de Calidad de Imagen

1. **Formatos recomendados:**
   - **Esquemas, gráficos, diagramas de bloques y logotipos:** `.png` o preferentemente vectoriales en `.pdf`.
   - **Fotografías y capturas de campo:** `.jpg` o `.png` con buena iluminación.
2. **Resolución mínima:** 300 DPI para asegurar nitidez absoluta en la impresión en papel o visualización en PDF.
3. **Tipografía dentro de la imagen:** Si crea diagramas en herramientas externas (draw.io, Figma, Canva, Illustrator), utilice tipografías sans-serif limpias (Arial, Helvetica, Roboto) de entre 8 pt y 14 pt para que sean legibles y armónicas con el cuerpo del documento.
