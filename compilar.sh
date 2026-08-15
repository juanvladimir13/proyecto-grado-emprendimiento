#!/bin/bash

# Colores para salida en consola
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # Sin color

# Nombre del archivo principal sin extensión
MAIN="main"

function limpiar_auxiliares() {
    echo -e "${YELLOW}Limpiando archivos auxiliares temporales...${NC}"
    rm -f *.aux *.log *.toc *.lof *.lot *.out *.bbl *.blg *.run.xml *.bcf *.synctex.gz
    rm -f emprendimiento-capitulos/**/*.aux innovacion-capitulos/**/*.aux preliminares/**/*.aux anexos/**/*.aux estilos/**/*.aux portada/**/*.aux docs/**/*.aux
    echo -e "${GREEN}¡Limpieza completada!${NC}"
}

function compilar_pdf() {
    # Eliminar PDF anterior para comprobar si se genera de nuevo
    rm -f "$MAIN.pdf"

    echo -e "${BLUE}=== Iniciando Compilación LaTeX (Paso 1/4) ===${NC}"
    pdflatex -interaction=nonstopmode "$MAIN.tex" > /dev/null
    
    echo -e "${BLUE}=== Procesando Bibliografía (Paso 2/4) ===${NC}"
    # Ejecutar biber (motor APA 7 / biblatex)
    biber "$MAIN" > /dev/null 2>&1
    
    echo -e "${BLUE}=== Enlazando referencias (Paso 3/4) ===${NC}"
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
elif [ -n "$1" ]; then
    echo -e "${RED}Parámetro desconocido: $1${NC}"
    echo -e "Uso:"
    echo -e "  ./compilar.sh          # Compila el PDF y conserva archivos auxiliares"
    echo -e "  ./compilar.sh --clean  # Compila el PDF y borra archivos auxiliares"
    echo -e "  ./compilar.sh --only-clean # Solo borra archivos auxiliares sin compilar"
    exit 1
else
    compilar_pdf
    exit 0
fi
