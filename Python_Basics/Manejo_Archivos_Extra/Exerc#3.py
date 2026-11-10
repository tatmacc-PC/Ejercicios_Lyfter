print("================ EJERCICIO DE EXTRA MANEJO DE ARCHIVOS ================================")
print("---------------------------Ejercicio #3------------------------------------------")
print()

from pathlib import Path


def file_exists(file_path):
    return file_path.is_file()


def main():
    file_name = "Exerc#3.txt"
    output_name = "Exerc#3.1.txt"

    code_folder = Path(__file__).resolve().parent
    file_path = code_folder / file_name

    while not file_exists(file_path):
        print(f"No se encontró el archivo: {file_path}")

        user_path = input(
            "Ingrese la ubicación completa del archivo: "
        ).strip().strip('"')

        file_path = Path(user_path)

    output_path = file_path.parent / output_name

    try:
        with file_path.open(encoding="utf-8") as input_file:
            with output_path.open("w", encoding="utf-8") as output_file:
                for line in input_file:
                    output_file.write(line.upper())

        print(f"Archivo convertido a mayúsculas: {output_path}")

    except (OSError, UnicodeError) as error:
        print(f"No se pudo procesar el archivo: {error}")


if __name__ == "__main__":
    main()

