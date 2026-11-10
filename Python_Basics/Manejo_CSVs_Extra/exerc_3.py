print("======================== EJERCICIO EXTRA DE MANEJO DE CSVs ================================")
print("----------------------------------Ejercicio #3---------------------------------------------")
print()

import csv
from pathlib import Path


def count_genres(file_path):
    """Read the CSV file and count video games by genre."""
    genre_counts = {}

    with file_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as file:
        reader = csv.reader(file)

        # Skip the row containing the column headers.
        next(reader, None)

        for row in reader:
            # Skip empty rows.
            if not row or all(not value.strip() for value in row):
                continue

            # Each video game must contain four columns.
            if len(row) != 4:
                raise ValueError(
                    f"La fila que termina en la línea {reader.line_num} "
                    "no contiene las cuatro columnas esperadas."
                )

            # Remove extra spaces and normalize capitalization.
            genre = row[1].strip().capitalize()

            if not genre:
                genre = "Sin género"

            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts


def main():
    # Get the directory from which the program was executed.
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
        genre_counts = count_genres(file_path)

    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"No se pudo leer el archivo: {error}")
        return

    if not genre_counts:
        print("El archivo no contiene videojuegos.")
        return

    print("Géneros encontrados:")

    # Display genres in alphabetical order.
    for genre, count in sorted(genre_counts.items()):
        print(f"{genre}: {count}")


if __name__ == "__main__":
    main()