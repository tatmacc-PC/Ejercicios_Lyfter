
from pathlib import Path

def validate_file(file_path):
    if not file_path.is_file():
        print(f"Error: no existe el archivo {file_path.name}.")
        return False

    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                return True

    print("Error: el archivo está vacío o solo contiene espacios.")
    return False


def remove_line_breaks(input_path, output_path):
    with input_path.open("r", encoding="utf-8") as input_file:
        text = input_file.read()

    words = text.split()
    result = " ".join(words)

    with output_path.open("w", encoding="utf-8") as output_file:
        output_file.write(result)


def main():
    print("================ EJERCICIO DE MANEJO DE ARCHIVOS ================")
    print("----------------------- Ejercicio #1 ---------------------------")
    print()

    folder_path = Path(__file__).resolve().parent
    input_path = folder_path / "Exerc#1.txt"
    output_path = folder_path / "Exerc#1.1.txt"

    try:
        if validate_file(input_path):
            remove_line_breaks(input_path, output_path)
            print(f"Archivo creado: {output_path.name}")

    except (OSError, UnicodeError) as error:
        print(f"No se pudo procesar el archivo: {error}")


if __name__ == "__main__":
    main()


