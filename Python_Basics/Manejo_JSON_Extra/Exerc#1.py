print("========================= EJERCICIO EXTRA DE MANEJO DE JSON ================================")
print("-----------------------------------Ejercicio #1---------------------------------------------")
print()

import json
from pathlib import Path


def load_pokemons(file_path):
    """Lee el archivo JSON y devuelve la lista de Pokémon."""
    with file_path.open("r", encoding="utf-8") as file:
        pokemons = json.load(file)

    if not isinstance(pokemons, list):
        raise ValueError("El archivo debe contener una lista de Pokémon.")

    return pokemons


def show_pokemons(pokemons):
    """Muestra toda la información de cada Pokémon."""
    if not pokemons:
        print("No hay Pokémon registrados.")
        return

    for pokemon in pokemons:
        print("\n--- Información del Pokémon ---")
        print(f"Nombre: {pokemon['name']}")
        print(f"Tipo: {pokemon['type']}")
        print(f"Nivel: {pokemon['level']}")
        print(f"Peso: {pokemon['weight_kg']} kg")

        shiny = "Sí" if pokemon["is_shiny"] else "No"
        print(f"Es shiny: {shiny}")

        held_item = pokemon["held_item"]
        if held_item is None:
            held_item = "Ninguno"

        print(f"Objeto equipado: {held_item}")

        print("\nHabilidades:")
        for skill in pokemon["skills"]:
            print(f"- {skill}")

        stats = pokemon["stats"]

        print("\nEstadísticas:")
        print(f"HP: {stats['hp']}")
        print(f"Ataque: {stats['attack']}")
        print(f"Defensa: {stats['defense']}")
        print(f"Ataque especial: {stats['sp_attack']}")
        print(f"Defensa especial: {stats['sp_defense']}")
        print(f"Velocidad: {stats['speed']}")
        print("-" * 40)


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

    show_pokemons(pokemons)


if __name__ == "__main__":
    main()