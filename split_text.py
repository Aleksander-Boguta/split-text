import os
import sys

def split_text(text, max_length=3900):
    words = text.split()
    current_chunk = ""
    chunks = []

    for word in words:
        if len(current_chunk) + len(word) + 1 > max_length:
            chunks.append(current_chunk.strip())
            current_chunk = word
        else:
            current_chunk += " " + word

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Plik nie został znaleziony. Sprawdź ścieżkę i spróbuj ponownie.")
        return ""

def save_chunks(chunks, output_folder):
    for i, chunk in enumerate(chunks):
        file_name = f"chunk_{i + 1}.txt"
        file_path = os.path.join(output_folder, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(chunk)
        print(f"Zapisano: {file_path}")

def main():
    if len(sys.argv) < 2:
        print("Użycie: python split_text.py <ścieżka_do_pliku> [maksymalna_długość_pakietu]")
        sys.exit(1)

    file_path = sys.argv[1]
    max_length = int(sys.argv[2]) if len(sys.argv) > 2 else 3900

    input_text = read_file(file_path)
    if not input_text:
        return

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_folder = os.path.join(os.path.dirname(file_path), base_name)

    os.makedirs(output_folder, exist_ok=True)

    packets = split_text(input_text, max_length)

    save_chunks(packets, output_folder)

    print(f"Wszystkie pakiety zapisano w folderze: {output_folder}")

if __name__ == "__main__":
    main()
