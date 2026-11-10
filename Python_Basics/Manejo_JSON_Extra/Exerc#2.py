print("========================= EJERCICIO EXTRA DE MANEJO DE JSON ================================")
print("-----------------------------------Ejercicio #2---------------------------------------------")
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


def normalize_type(pokemon_type):
    """Convierte los tipos en español a su equivalente en inglés."""
    translations = {
        "agua": "water",
        "eléctrico": "electric",
        "electrico": "electric",
        "fuego": "fire",
        "planta": "grass",
        "hielo": "ice",
        "lucha": "fighting",
        "veneno": "poison",
        "tierra": "ground",
        "volador": "flying",
        "psíquico": "psychic",
        "psiquico": "psychic",
        "bicho": "bug",
        "roca": "rock",
        "fantasma": "ghost",
        "dragón": "dragon",
        "dragon": "dragon",
        "siniestro": "dark",
        "acero": "steel",
        "hada": "fairy",
        "normal": "normal"
    }

    pokemon_type = pokemon_type.strip().lower()

    return translations.get(pokemon_type, pokemon_type)


def search_by_type(pokemons):
    """Pide un tipo y muestra los Pokémon que coincidan."""
    while True:
        requested_type = input(
            "Ingrese el tipo de Pokémon que desea buscar "
            "(agua, eléctrico, fuego, etc.): "
        ).strip()

        if requested_type:
            break

        print("Debe ingresar un tipo de Pokémon.")

    requested_type = normalize_type(requested_type)
    matches = []

    for pokemon in pokemons:
        saved_type = normalize_type(pokemon["type"])

        if saved_type == requested_type:
            matches.append(pokemon["name"])

    if matches:
        print("\nLos Pokémon que existen de ese tipo son:")

        for name in matches:
            print(name)
    else:
        print("\nNo se encontraron Pokémon de ese tipo.")


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

    search_by_type(pokemons)


if __name__ == "__main__":
    main()