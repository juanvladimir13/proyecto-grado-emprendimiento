#!/bin/bash

# ============================================================
# Script de Compilación y Limpieza para Proyecto de Grado BTH
# ============================================================

# Colores para salida en consola
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # Sin color

# Nombre del archivo principal sin extensión
MAIN="main"

function limpiar_auxiliares() {
    echo -e "${YELLOW}Limpiando archivos auxiliares temporales...${NC}"
    find . -type f \( \
        -name "*.aux" -o \
        -name "*.log" -o \
        -name "*.toc" -o \
        -name "*.lof" -o \
        -name "*.lot" -o \
        -name "*.out" -o \
        -name "*.bbl" -o \
        -name "*.blg" -o \
        -name "*.run.xml" -o \
        -name "*.bcf" -o \
        -name "*.synctex.gz" -o \
        -name "*.fdb_latexmk" -o \
        -name "*.fls" -o \
        -name "*.upa" -o \
        -name "*.upb" -o \
        -name "*.listing" -o \
        -name "*-blx.bib" \
    \) -delete
    echo -e "${GREEN}¡Limpieza completada!${NC}"
}

function compilar_rapido() {
    echo -e "${CYAN}=== Compilación Rápida (1 pasada pdflatex) ===${NC}"
    pdflatex -interaction=nonstopmode "$MAIN.tex" > /dev/null
    if [ -f "$MAIN.pdf" ]; then
        echo -e "${GREEN}¡Compilación rápida completada! Archivo '$MAIN.pdf' actualizado.${NC}"
    else
        echo -e "${RED}Error en la compilación. Revisa '$MAIN.log'.${NC}"
        exit 1
    fi
}

function compilar_pdf() {
    # Eliminar PDF anterior para comprobar si se genera de nuevo
    rm -f "$MAIN.pdf"

    echo -e "${BLUE}=== Iniciando Compilación LaTeX (Paso 1/4) ===${NC}"
    pdflatex -interaction=nonstopmode "$MAIN.tex" > /dev/null
    
    echo -e "${BLUE}=== Procesando Bibliografía con Biber (Paso 2/4) ===${NC}"
    biber "$MAIN" > /dev/null 2>&1
    
    echo -e "${BLUE}=== Enlazando referencias cruzadas (Paso 3/4) ===${NC}"
    pdflatex -interaction=nonstopmode "$MAIN.tex" > /dev/null
    
    echo -e "${BLUE}=== Generando PDF e índices finales (Paso 4/4) ===${NC}"
    pdflatex -interaction=nonstopmode "$MAIN.tex" > /dev/null
    
    # Comprobar si se generó el PDF
    if [ -f "$MAIN.pdf" ]; then
        echo -e "${GREEN}¡Compilación completada! Archivo '$MAIN.pdf' generado exitosamente.${NC}"
    else
        echo -e "${RED}Error: No se pudo generar el archivo '$MAIN.pdf'. Revisa los errores en '$MAIN.log'.${NC}"
        exit 1
    fi
}

# Evaluar parámetros
if [ "$1" == "--only-clean" ]; then
    limpiar_auxiliares
    exit 0
elif [ "$1" == "--clean" ]; then
    compilar_pdf
    limpiar_auxiliares
    exit 0
elif [ "$1" == "--fast" ]; then
    compilar_rapido
    exit 0
elif [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo -e "${CYAN}Uso del script de compilación:${NC}"
    echo -e "  ./compilar.sh              # Compila el PDF completo (4 pasos) y conserva temporales"
    echo -e "  ./compilar.sh --clean      # Compila el PDF completo y elimina temporales"
    echo -e "  ./compilar.sh --only-clean # Elimina temporales sin compilar"
    echo -e "  ./compilar.sh --fast       # Compilación rápida de 1 sola pasada (para redacción)"
    exit 0
elif [ -n "$1" ]; then
    echo -e "${RED}Parámetro desconocido: $1${NC}"
    echo -e "Ejecute './compilar.sh --help' para ver las opciones disponibles."
    exit 1
else
    compilar_pdf
    exit 0
fi
