print("========================== EJERCICIO EXTRA DE MANEJO DE JSON ===============================")
print("-----------------------------------Ejercicio #3---------------------------------------------")
print()

import json
from pathlib import Path


def load_pokemons(file_path):
    """Lee el JSON y devuelve la lista de Pokémon."""
    with file_path.open("r", encoding="utf-8") as file:
        pokemons = json.load(file)

    if not isinstance(pokemons, list):
        raise ValueError("El archivo debe contener una lista de Pokémon.")

    return pokemons


def show_stats(pokemons):
    """Muestra las estadísticas principales de cada Pokémon."""
    if not pokemons:
        print("No hay Pokémon registrados.")
        return

    for pokemon in pokemons:
        stats = pokemon["stats"]

        print(f"Nombre: {pokemon['name']}")
        print(f"Ataque: {stats['attack']}")
        print(f"Defensa: {stats['defense']}")
        print(f"Velocidad: {stats['speed']}")
        print()


def main():
    # Busca el JSON en la misma carpeta del archivo Python.
    file_path = Path(__file__).resolve().parent / "pokemones.json"

    if not file_path.is_file():
        print(f"No se encontró el archivo: {file_path}")
        return

    try:
        pokemons = load_pokemons(file_path)

    except json.JSONDecodeError:
        print("El archivo no contiene un JSON válido.")
        return

    except ValueError as error:
        print(error)
        return

    except OSError as error:
        print(f"No se pudo leer el archivo: {error}")
        return

    show_stats(pokemons)


if __name__ == "__main__":
    main()