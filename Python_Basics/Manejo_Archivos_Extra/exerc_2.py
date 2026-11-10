print("================ EJERCICIO DE EXTRA MANEJO DE ARCHIVOS ================================")
print("---------------------------Ejercicio #2------------------------------------------")
print()

from pathlib import Path

def file_exists(file_path):
    return file_path.is_file()


def file_is_empty(content):
    return not content.strip()


def count_words(content):
    return len(content.split())


def main():
    file_name = "Exerc#2.txt"
    code_folder = Path(__file__).resolve().parent
    file_path = code_folder / file_name

    while not file_exists(file_path):
        print(f"No se encontró el archivo: {file_path}")

        user_path = input(
            "Ingrese la ubicación completa del archivo: "
        ).strip().strip('"')

        file_path = Path(user_path)

    try:
        content = file_path.read_text(encoding="utf-8")

        if file_is_empty(content):
            print("El archivo está vacío.")
            return

        total_words = count_words(content)
        print(f"Este archivo contiene {total_words} palabras")

    except (OSError, UnicodeError) as error:
        print(f"No se pudo leer el archivo: {error}")


if __name__ == "__main__":
    main()

