print("========================== EJERCICIO EXTRA DE MANEJO DE JSON ===============================")
print("-----------------------------------Ejercicio #4---------------------------------------------")
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


def show_average_levels(pokemons):
    """Agrupa los Pokémon por tipo y calcula su promedio de nivel."""
    if not pokemons:
        print("No hay Pokémon registrados.")
        return

    groups = {}

    for pokemon in pokemons:
        pokemon_type = pokemon["type"].strip().lower()
        level = pokemon["level"]

        # Crea un grupo cuando el tipo aparece por primera vez.
        if pokemon_type not in groups:
            groups[pokemon_type] = {
                "total_levels": 0,
                "count": 0
            }

        # Acumula los niveles y cuenta los Pokémon de ese tipo.
        groups[pokemon_type]["total_levels"] += level
        groups[pokemon_type]["count"] += 1

    print("\n--- Promedio de nivel por tipo ---")

    for pokemon_type, data in groups.items():
        average = data["total_levels"] / data["count"]

        print(
            f"Tipo: {pokemon_type.capitalize()} → "
            f"Promedio de nivel: {average:.1f}"
        )


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

    show_average_levels(pokemons)


if __name__ == "__main__":
    main()