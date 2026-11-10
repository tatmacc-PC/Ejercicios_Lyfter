print("======================== EJERCICIO EXTRA DE MANEJO DE CSVs ================================")
print("----------------------------------Ejercicio #4---------------------------------------------")
print()

import csv
from pathlib import Path


def read_videogames(file_path):
    """Read the CSV file and return a list of video games."""
    videogames = []

    with file_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as file:
        reader = csv.reader(file)

        # Skip the column headers.
        next(reader, None)

        for row in reader:
            # Skip empty rows.
            if not row or all(not value.strip() for value in row):
                continue

            # Validate the number of columns.
            if len(row) != 4:
                raise ValueError(
                    f"La fila que termina en la línea {reader.line_num} "
                    "no contiene las cuatro columnas esperadas."
                )

            videogame = {
                "name": row[0].strip(),
                "genre": row[1].strip(),
                "developer": row[2].strip(),
                "rating": row[3].strip().upper()
            }

            videogames.append(videogame)

    return videogames


def request_developer():
    """Ask for a developer name and reject empty input."""
    while True:
        developer = input(
            "Ingrese el nombre del desarrollador "
            "(por ejemplo: Ubisoft): "
        ).strip()

        if developer:
            return developer

        print("Debe ingresar el nombre de un desarrollador.")


def show_videogames(videogames, developer):
    """Find and display video games from the requested developer."""
    matching_games = []

    for videogame in videogames:
        if videogame["developer"].casefold() == developer.casefold():
            matching_games.append(videogame)

    if not matching_games:
        print(
            f"No se encontraron videojuegos desarrollados por {developer}."
        )
        return

    # Use the developer name as written in the CSV.
    developer_name = matching_games[0]["developer"]
    print(f"\nVideojuegos desarrollados por {developer_name}:")

    # Display games in alphabetical order.
    for videogame in sorted(
        matching_games,
        key=lambda game: game["name"].casefold()
    ):
        print(
            f"- {videogame['name']} "
            f"(Clasificación: {videogame['rating']}, "
            f"Género: {videogame['genre']})"
        )


def main():
    # Search in the folder containing this Python file.
    current_folder = Path(__file__).resolve().parent
    file_path = current_folder / "videogames.csv"

    # Also accept the filename without an extension.
    if not file_path.is_file():
        file_path = current_folder / "videogames"

    if not file_path.is_file():
        print(
            "Error: no se encontró el archivo "
            "'videogames.csv' ni 'videogames'."
        )
        print(f"Carpeta revisada: {current_folder}")
        return

    try:
        videogames = read_videogames(file_path)

    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"No se pudo leer el archivo: {error}")
        return

    if not videogames:
        print("El archivo no contiene videojuegos.")
        return

    developer = request_developer()
    show_videogames(videogames, developer)


if __name__ == "__main__":
    main()