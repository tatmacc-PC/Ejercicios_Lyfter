print("======================== EJERCICIO EXTRA DE MANEJO DE CSVs ================================")
print("----------------------------------Ejercicio #2---------------------------------------------")
print()

import csv
from pathlib import Path


def read_videogames(file_path):
    """Read the CSV file and return a list of video games."""
    videogames = []

    with open(file_path, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        # Skip the first row because it contains the column headers.
        next(reader, None)

        for row in reader:
            # Skip empty rows or rows that do not contain four columns.
            if len(row) != 4:
                continue

            videogame = {
                "name": row[0].strip(),
                "genre": row[1].strip(),
                "developer": row[2].strip(),
                "rating": row[3].strip().upper()
            }

            videogames.append(videogame)

    return videogames


def request_rating():
    """Ask the user for an ESRB rating and reject empty input."""
    while True:
        rating = input(
            "Ingrese la clasificación ESRB que desea buscar "
            "(por ejemplo: E, E10+, T o M): "
        ).strip().upper()

        if rating:
            return rating

        print("Debe ingresar una clasificación.\n")


def filter_by_rating(videogames, rating):
    """Return the video games that match the requested rating."""
    matches = []

    for videogame in videogames:
        if videogame["rating"] == rating:
            matches.append(videogame)

    return matches


def show_videogames(videogames, rating):
    """Display the matching video games and the total count."""
    if not videogames:
        print(f"\nNo se encontraron videojuegos con clasificación {rating}.")
        return

    print(f"\nVideojuegos con clasificación ESRB {rating}:")
    print("-" * 40)

    for videogame in videogames:
        print(f"Nombre: {videogame['name']}")
        print(f"Género: {videogame['genre']}")
        print(f"Desarrollador: {videogame['developer']}")
        print(f"Clasificación: {videogame['rating']}")
        print("-" * 40)

    print(f"Total encontrados: {len(videogames)}")


def main():
    """Coordinate file reading, user input, filtering, and output."""
    # Build the CSV path using the folder where this Python file is saved.
    program_folder = Path(__file__).resolve().parent
    file_path = program_folder / "videogames.csv"

    try:
        videogames = read_videogames(file_path)

        if not videogames:
            print("El archivo no contiene videojuegos válidos.")
            return

        rating = request_rating()
        matches = filter_by_rating(videogames, rating)
        show_videogames(matches, rating)

    except FileNotFoundError:
        print(
            "No se encontró 'videogames.csv'. "
            "Asegúrese de que esté en la misma carpeta que el programa."
        )
    except UnicodeError:
        print("No se pudo leer el archivo. Guarde el CSV con codificación UTF-8.")
    except (OSError, csv.Error) as error:
        print(f"Ocurrió un error al leer el archivo: {error}")


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()