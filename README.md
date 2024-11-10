# Split-Text

Split-Text to narzędzie do podziału dużych plików tekstowych (.txt lub .md) na mniejsze fragmenty (chunk). Powstał na potrzeby dokładnego przetwarzania dużych plików tekstowych przez ChatGPT
```
split-text
├── README.md
├── reset_input.sh
├── split_text.py
└── input/
    ├── text.txt
	└── text_chunks
```
Pliki:
•	reset_input.sh: Skrypt Bash resetujący folder input/.
•	split_text.py: Główny program do podziału plików tekstowych na pakiety.
•	input/: Folder, w którym znajdują się pliki wejściowe i gdzie zapisywane są wyniki.

Instalacja:

1.	Klonuj repozytorium:

```bash
git clone https://github.com/your-username/split-text.git
```

Uruchamianie programu

1. Podział pliku tekstowego na pakiety

Umieść plik tekstowy (.txt lub .md) w folderze input/ (np. input/text.txt). Następnie uruchom program:

python split_text.py input/text.txt

Opcjonalnie: Podaj maksymalną długość pakietu

Jeśli chcesz zmienić domyślną długość pakietu (3900 znaków), dodaj odpowiedni argument:

python split_text.py input/text.txt 2000

Wyniki zostaną zapisane w folderze input/text_chunks/.

2. Resetowanie folderu input/

Aby usunąć zawartość folderu input/ i odtworzyć jego strukturę, uruchom skrypt:

./reset_input.sh

Wynik działania skryptu

Usuwam folder 'input/'...
Odtwarzam strukturę folderu 'input/'...
Struktura folderu 'input/' wygląda następująco:
input/:
text.txt
text_chunks/

input/text_chunks/:

Operacja zakończona.

Gałąź Docker

Wszystkie związane z Docker pliki i instrukcje są dostępne na pobocznej gałęzi docker. Aby przełączyć się na tę gałąź, wykonaj:

git checkout docker

Na gałęzi docker znajdziesz Dockerfile oraz instrukcje do uruchamiania programu w kontenerze.
