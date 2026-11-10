
def validate_file(input_file):
    if not input_file.is_file():
        print("El archivo songs.txt no existe en la carpeta del programa.")
        return False

    with input_file.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                return True

    print("El archivo está vacío o solo contiene espacios.")
    return False

def sort_songs(input_file, output_file):
    with input_file.open("r", encoding="utf-8") as file:
        songs = []

        for line in file:
            song = line.strip()

            if song:
                songs.append(song)

    sorted_songs = sorted(songs, key=str.casefold)

    with output_file.open("w", encoding="utf-8") as file:
        for song in sorted_songs:
            file.write(song + "\n")

    print(f"Canciones guardadas en: {output_file}")


def main():
    print("===================== EJERCICIO DE MANEJO DE ARCHIVOS ================================")
    print("--------------------------------Ejercicio #1------------------------------------------")
    print()

    from pathlib import Path

    code_folder = Path(__file__).resolve().parent
    input_file = code_folder / "songs.txt"
    output_file = code_folder / "songs_sorted.txt"

    try:
        if validate_file(input_file):
            sort_songs(input_file, output_file)

    except UnicodeDecodeError:
        print("El archivo debe estar guardado con codificación UTF-8.")
    except OSError as error:
        print(f"No se pudo leer o guardar el archivo: {error}")

main()



