print("================ EJERCICIO DE EXTRA MANEJO DE ARCHIVOS ================================")
print("---------------------------Ejercicio #4------------------------------------------")
print()

from pathlib import Path


def get_text():
    return input("Ingrese una línea de texto: ")


def append_text(file_path, text):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text + "\n")


def main():
    folder_path = Path(__file__).resolve().parent
    file_path = folder_path / "Ejerc#4.txt"

    text = get_text()
    append_text(file_path, text)

    print("El texto se agrega al final del archivo sin borrar lo anterior")


if __name__ == "__main__":
    main()

