print("============================== EJERCICIO DE MANEJO DE JSON ================================")
print("-----------------------------------Ejercicio #1---------------------------------------------")
print()

import json
from pathlib import Path


def load_pokemons(file_path):
    """Lee los Pokémon existentes o devuelve una lista vacía."""
    if not file_path.exists():
        print("El archivo no existe. Se creará al guardar.")
        return []

    with file_path.open("r", encoding="utf-8") as file:
        pokemons = json.load(file)

    if not isinstance(pokemons, list):
        raise ValueError("El archivo debe contener una lista de Pokémon.")

    return pokemons


def ask_integer(message, minimum=0, maximum=None):
    """Pide un número entero dentro del rango permitido."""
    while True:
        try:
            value = int(input(message))

            if value < minimum:
                print(f"Ingresa un número mayor o igual a {minimum}.")
            elif maximum is not None and value > maximum:
                print(f"Ingresa un número menor o igual a {maximum}.")
            else:
                return value

        except ValueError:
            print("Debes ingresar un número entero.")


def ask_positive_float(message):
    """Pide un número decimal mayor que cero."""
    while True:
        try:
            value = float(input(message).replace(",", "."))

            if 0 < value < float("inf"):
                return value

            print("Ingresa un número válido mayor que cero.")

        except ValueError:
            print("Debes ingresar un número, por ejemplo: 6.5.")


def ask_required_text(message):
    """Pide un texto que no esté vacío."""
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Este dato no puede estar vacío.")


def ask_shiny():
    """Convierte la respuesta del usuario en True o False."""
    while True:
        answer = input("¿Es shiny? (sí/no): ").strip().lower()

        if answer in ("sí", "si", "s"):
            return True

        if answer in ("no", "n"):
            return False

        print("Responde sí o no.")


def ask_pokemon():
    """Pide la información y construye el diccionario del Pokémon."""
    print("\n--- Agregar Pokémon ---")

    name = ask_required_text("Nombre: ")
    pokemon_type = ask_required_text("Tipo: ")
    level = ask_integer("Nivel (1 a 100): ", 1, 100)
    weight_kg = ask_positive_float("Peso en kilogramos: ")
    is_shiny = ask_shiny()

    held_item = input(
        "Objeto equipado (Enter si no tiene): "
    ).strip()

    # Si no escribe un objeto, se guardará como null en el JSON.
    if not held_item:
        held_item = None

    print("\nIngresa las habilidades separadas por comas.")

    while True:
        skills_text = input("Habilidades: ")

        skills = [
            skill.strip()
            for skill in skills_text.split(",")
            if skill.strip()
        ]

        if skills:
            break

        print("Debes ingresar al menos una habilidad.")

    print("\nIngresa las estadísticas:")

    stats = {
        "hp": ask_integer("HP: ", 1),
        "attack": ask_integer("Ataque: ", 1),
        "defense": ask_integer("Defensa: ", 1),
        "sp_attack": ask_integer("Ataque especial: ", 1),
        "sp_defense": ask_integer("Defensa especial: ", 1),
        "speed": ask_integer("Velocidad: ", 1)
    }

    return {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": stats
    }


def save_pokemons(file_path, pokemons):
    """Guarda la lista completa en el archivo JSON."""
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(
            pokemons,
            file,
            ensure_ascii=False,
            indent=4,
            allow_nan=False
        )


def main():
    # Carpeta desde la que se ejecuta el programa.
    file_path = Path.cwd() / "pokemones.json"

    print(f"Archivo utilizado: {file_path}")

    try:
        pokemons = load_pokemons(file_path)

    except (json.JSONDecodeError, ValueError) as error:
        print(f"No se pudo importar el archivo: {error}")
        print("Corrige el archivo antes de agregar Pokémon.")
        return

    except OSError as error:
        print(f"No se pudo leer el archivo: {error}")
        return

    print(f"Pokémon importados: {len(pokemons)}")

    quantity = ask_integer(
        "\n¿Cuántos Pokémon deseas ingresar?: ",
        minimum=1
    )

    for index in range(quantity):
        print(f"\n--- Pokémon {index + 1} de {quantity} ---")

        new_pokemon = ask_pokemon()
        pokemons.append(new_pokemon)

        # Guarda después de cada Pokémon ingresado.
        try:
            save_pokemons(file_path, pokemons)

        except OSError as error:
            print(f"No se pudo guardar el archivo: {error}")
            return

        print(f"¡{new_pokemon['name']} se guardó correctamente!")

    print(f"\nSe agregaron {quantity} Pokémon.")
    print(f"Total de Pokémon guardados: {len(pokemons)}")


if __name__ == "__main__":
    main()