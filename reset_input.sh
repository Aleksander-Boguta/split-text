#!/bin/bash

# Ustawianie bieżącego katalogu na folder, w którym znajduje się skrypt
cd "$(dirname "$0")"

# Usuwanie całego folderu input
echo "Usuwam folder 'input/'..."
rm -rf input/

# Odtwarzanie struktury folderu input
echo "Odtwarzam strukturę folderu 'input/'..."
mkdir -p input/text_chunks
touch input/text.txt

# Wyświetlenie struktury folderu input
echo "Struktura folderu 'input/' wygląda następująco:"
ls -R input/

# Informacja o zakończeniu operacji
echo "Operacja zakończona."
