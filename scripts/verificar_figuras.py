#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
===============================================================================
Script de Verificación y Auditoría de Figuras e Imágenes (Normas APA 7ma Edición)
Proyecto de Grado BTH — Modalidad Emprendimiento Productivo
===============================================================================

Este script audita todos los entornos de figuras (`figure`, `\figuraapa`, `\insertarfigura`)
en `capitulos/**/*.tex`, `anexos/**/*.tex` y `preliminares/**/*.tex`, verificando:
1. Cumplimiento de APA 7ma Edición (ubicación de \caption ARRIBA de \includegraphics).
2. Presencia de etiquetas \label con prefijo estándar 'fig:'.
3. Centrado con \centering.
4. Existencia de los archivos de imagen en la carpeta `imagenes/`.
5. Presencia de notas explicativas o fuentes con \notafigura{...}.
"""

import sys
import os
import glob
import re

# Códigos ANSI para terminal
COLOR_RESET = "\033[0m"
COLOR_BOLD = "\033[1m"
COLOR_GREEN = "\033[0;32m"
COLOR_YELLOW = "\033[1;33m"
COLOR_RED = "\033[0;31m"
COLOR_CYAN = "\033[0;36m"
COLOR_GRAY = "\033[0;90m"

def obtener_ruta_base():
    """Retorna la ruta raíz del proyecto."""
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(ruta_script, ".."))

def auditar_figuras():
    ruta_raiz = obtener_ruta_base()
    dir_imagenes = os.path.join(ruta_raiz, "imagenes")
    
    archivos_tex = (
        glob.glob(os.path.join(ruta_raiz, "capitulos", "**", "*.tex"), recursive=True) +
        glob.glob(os.path.join(ruta_raiz, "anexos", "**", "*.tex"), recursive=True) +
        glob.glob(os.path.join(ruta_raiz, "preliminares", "**", "*.tex"), recursive=True) +
        [os.path.join(ruta_raiz, "main.tex")]
    )
    
    total_figuras = 0
    total_correctas = 0
    total_advertencias = 0
    total_errores = 0
    
    patron_fig_env = re.compile(r"\\begin\{figure\}(.*?)\\end\{figure\}", re.DOTALL)
    patron_figuraapa = re.compile(r"\\(?:figuraapa|insertarfigura|graficoapa|insertargrafico)(?:\[.*?\])?\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}\{([^}]*)\}")
    patron_caption = re.compile(r"\\caption\s*\{")
    patron_includegr = re.compile(r"\\includegraphics(?:\s*\[.*?\])?\s*\{([^}]+)\}")
    patron_label = re.compile(r"\\label\s*\{\s*fig:([^}]+)\s*\}")
    patron_nota = re.compile(r"\\(?:notafigura|notaimagen|notatabla|notagrafico)\s*\{")
    
    print(f"\n{COLOR_BOLD}{'='*60}{COLOR_RESET}")
    print(f"{COLOR_BOLD}  AUDITORÍA DE ESTILO DE FIGURAS E IMÁGENES (APA 7 / LaTeX)  {COLOR_RESET}")
    print(f"{COLOR_BOLD}{'='*60}{COLOR_RESET}\n")

    archivos_con_figuras = 0
    
    for ruta_archivo in archivos_tex:
        try:
            with open(ruta_archivo, "r", encoding="utf-8", errors="replace") as f:
                contenido = f.read()
        except Exception as e:
            continue
            
        rel_path = os.path.relpath(ruta_archivo, ruta_raiz)
        
        # 1. Auditar macros \figuraapa / \insertarfigura
        coincidencias_macro = patron_figuraapa.findall(contenido)
        for archivo_img, titulo, label_clave, nota in coincidencias_macro:
            total_figuras += 1
            advertencias = []
            errores = []
            
            # Verificar existencia de la imagen
            posibles_rutas = [
                os.path.join(dir_imagenes, archivo_img),
                os.path.join(dir_imagenes, archivo_img + ".png"),
                os.path.join(dir_imagenes, archivo_img + ".jpg"),
                os.path.join(dir_imagenes, archivo_img + ".pdf"),
                os.path.join(ruta_raiz, archivo_img)
            ]
            if not any(os.path.isfile(p) for p in posibles_rutas):
                errores.append(f"El archivo de imagen '{archivo_img}' no existe en '{dir_imagenes}'.")
                
            if not label_clave.startswith("fig:"):
                advertencias.append(f"La clave de referencia '{label_clave}' debería iniciar con el prefijo 'fig:'.")
                
            if not nota.strip():
                advertencias.append("La figura no incluye nota al pie (se recomienda indicar la fuente o 'Elaboración propia').")
                
            if errores:
                total_errores += 1
                print(f"{COLOR_RED}[ERROR CRÍTICO]{COLOR_RESET} {rel_path} (macro \\figuraapa -> {archivo_img})")
                for err in errores:
                    print(f"    {COLOR_RED}✗ {err}{COLOR_RESET}")
            elif advertencias:
                total_advertencias += 1
                print(f"{COLOR_YELLOW}[ADVERTENCIA]{COLOR_RESET} {rel_path} (macro \\figuraapa -> {archivo_img})")
                for adv in advertencias:
                    print(f"    {COLOR_YELLOW}▲ {adv}{COLOR_RESET}")
            else:
                total_correctas += 1
                print(f"{COLOR_GREEN}[CORRECTO]{COLOR_RESET} {rel_path} (macro \\figuraapa -> {archivo_img})")
        
        # 2. Auditar entornos \begin{figure}...\end{figure}
        coincidencias_env = patron_fig_env.findall(contenido)
        for bloque in coincidencias_env:
            total_figuras += 1
            advertencias = []
            errores = []
            
            idx_caption = bloque.find(r"\caption")
            idx_includegr = bloque.find(r"\includegraphics")
            
            if idx_caption == -1:
                errores.append("La figura no tiene definido un \\caption{...}.")
            elif idx_includegr != -1 and idx_caption > idx_includegr:
                errores.append("Violación APA 7: El \\caption debe colocarse ARRIBA de \\includegraphics (no abajo).")
                
            if r"\centering" not in bloque:
                advertencias.append("Se recomienda centrar el contenido visual con \\centering.")
                
            if not patron_label.search(bloque):
                advertencias.append("Falta etiqueta \\label{fig:...} para referenciar la figura en el texto.")
                
            if not patron_nota.search(bloque):
                advertencias.append("Se recomienda incluir \\notafigura{Fuente: ...} al pie de la figura.")
                
            archivos_inc = patron_includegr.findall(bloque)
            for archivo_img in archivos_inc:
                posibles_rutas = [
                    os.path.join(dir_imagenes, archivo_img),
                    os.path.join(dir_imagenes, archivo_img + ".png"),
                    os.path.join(dir_imagenes, archivo_img + ".jpg"),
                    os.path.join(dir_imagenes, archivo_img + ".pdf"),
                    os.path.join(ruta_raiz, archivo_img)
                ]
                if not any(os.path.isfile(p) for p in posibles_rutas):
                    errores.append(f"El archivo de imagen '{archivo_img}' no existe en '{dir_imagenes}'.")
            
            nombre_fig = archivos_inc[0] if archivos_inc else "figura"
            if errores:
                total_errores += 1
                print(f"{COLOR_RED}[ERROR CRÍTICO]{COLOR_RESET} {rel_path} (entorno figure -> {nombre_fig})")
                for err in errores:
                    print(f"    {COLOR_RED}✗ {err}{COLOR_RESET}")
            elif advertencias:
                total_advertencias += 1
                print(f"{COLOR_YELLOW}[ADVERTENCIA]{COLOR_RESET} {rel_path} (entorno figure -> {nombre_fig})")
                for adv in advertencias:
                    print(f"    {COLOR_YELLOW}▲ {adv}{COLOR_RESET}")
            else:
                total_correctas += 1
                print(f"{COLOR_GREEN}[CORRECTO]{COLOR_RESET} {rel_path} (entorno figure -> {nombre_fig})")

    # También auditar figuras en imagenes/figura_ejemplo.tex si existe
    ruta_ejemplo = os.path.join(dir_imagenes, "figura_ejemplo.tex")
    if os.path.isfile(ruta_ejemplo):
        print(f"{COLOR_CYAN}[PLANTILLA]{COLOR_RESET} imagenes/figura_ejemplo.tex disponible como referencia.")

    print(f"\n{COLOR_BOLD}{'-'*60}{COLOR_RESET}")
    print(f"Total de figuras analizadas: {total_figuras}")
    print(f"  {COLOR_GREEN}✓ Correctas según APA 7:     {total_correctas}{COLOR_RESET}")
    print(f"  {COLOR_YELLOW}▲ Con advertencias de ajuste: {total_advertencias}{COLOR_RESET}")
    print(f"  {COLOR_RED}✗ Con errores críticos:      {total_errores}{COLOR_RESET}")
    print(f"{COLOR_BOLD}{'-'*60}{COLOR_RESET}\n")

    if total_errores > 0:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(auditar_figuras())
