print("======================== EJERCICIO EXTRA DE MANEJO DE CSVs ================================")
print("----------------------------------Ejercicio #1---------------------------------------------")
print()

import csv
from pathlib import Path

def get_file_path():
    folder_path = Path(__file__).resolve().parent
    return folder_path / "videogames.csv"


def display_videogame(row):
    print(f"Nombre: {row[0]}")
    print(f"Género: {row[1]}")
    print(f"Desarrollador: {row[2]}")
    print(f"Clasificación: {row[3]}")
    print("-" * 40)


def read_videogames(file_path):
    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        # Quite esta línea si el archivo no tiene encabezados.
        next(reader, None)

        game_count = 0

        for line_number, row in enumerate(reader, start=2):
            # Omite filas vacías o que solo contienen espacios.
            if not row or all(not value.strip() for value in row):
                continue

            if len(row) != 4:
                print(
                    f"Registro {line_number} omitido: "
                    "debe contener exactamente 4 columnas."
                )
                continue

            row = [value.strip() for value in row]
            display_videogame(row)
            game_count += 1

        if game_count == 0:
            print("No se encontraron videojuegos válidos.")


def main():
    print("========== LISTA DE VIDEOJUEGOS ==========")
    print()

    file_path = get_file_path()

    try:
        read_videogames(file_path)
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo {file_path.name}.")
    except UnicodeDecodeError:
        print("Error: el archivo debe estar guardado con codificación UTF-8.")
    except csv.Error as error:
        print(f"Error al interpretar el archivo CSV: {error}")
    except OSError as error:
        print(f"Error al abrir o leer el archivo: {error}")


if __name__ == "__main__":
    main()
