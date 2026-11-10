print("======================== EJERCICIO DE MANEJO DE CSVs ======================================")
print("----------------------------------Ejercicio #1---------------------------------------------")
print()

import csv
from pathlib import Path

def get_file_name():
    while True:
        file_name = input("Nombre del archivo (sin ruta): ").strip()

        if not file_name:
            print("El nombre no puede estar vacío.")
        elif "/" in file_name or "\\" in file_name:
            print("Ingrese solamente el nombre, sin carpetas.")
        else:
            if not file_name.lower().endswith(".csv"):
                file_name += ".csv"

            return file_name


def get_number_of_games():
    while True:
        try:
            number_of_games = int(
                input("¿Cuántos videojuegos desea ingresar? ")
            )

            if number_of_games > 0:
                return number_of_games

            print("Ingrese un número mayor que cero.")

        except ValueError:
            print("Debe ingresar un número entero.")


def get_game_information():
    name = input("Nombre: ").strip()
    genre = input("Género: ").strip()
    developer = input("Desarrollador: ").strip()
    esrb_rating = input("Clasificación ESRB: ").strip()

    return [name, genre, developer, esrb_rating]


def get_games(number_of_games):
    games = []

    for index in range(number_of_games):
        print(f"\nVideojuego {index + 1}")
        game = get_game_information()
        games.append(game)

    return games


def save_games(file_name, games):
    # Obtiene la carpeta donde está este archivo de Python.
    source_folder = Path(__file__).resolve().parent

    # Combina esa carpeta con el nombre del archivo CSV.
    file_path = source_folder / file_name

    with open(
        file_path, mode="w", newline="", encoding="utf-8-sig"
    ) as file:
        writer = csv.writer(file)

        writer.writerow([
            "Nombre",
            "Género",
            "Desarrollador",
            "Clasificación ESRB"
        ])

        writer.writerows(games)


def main():
    file_name = get_file_name()
    number_of_games = get_number_of_games()
    games = get_games(number_of_games)

    try:
        save_games(file_name, games)
        print(f"\nArchivo guardado correctamente: {file_name}")
    except OSError as error:
        print(f"\nNo se pudo guardar el archivo: {error}")


if __name__ == "__main__":
    main()