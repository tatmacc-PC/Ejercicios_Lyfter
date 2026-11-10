print("============================== EJERCICIO DE FUNCIONES ================================")
print("-----------------------------------Ejercicio #6---------------------------------------")
print()

import time


# Ordenar palabras alfabéticamente
def sort_words(text):
    words = text.split("-")

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i].lower() > words[j].lower():
                words[i], words[j] = words[j], words[i]

    return "-".join(words)


# Pedir y validar el texto
while True:
    user_text = input(
        "Ingrese palabras separadas por guiones: "
    ).strip()

    if not user_text:
        print("Error: debe ingresar un texto.")
        continue

    if "," in user_text:
        print("Error: no se permiten comas.")
        continue

    if any(character.isspace() for character in user_text):
        print("Error: use guiones para separar las palabras, sin espacios.")
        continue

    has_numbers = False

    for character in user_text:
        if character.isnumeric():
            has_numbers = True
            break

    if has_numbers:
        print("Error: no se permiten números.")
        continue

    if any(not word for word in user_text.split("-")):
        print("Error: no deje palabras vacías entre los guiones.")
        continue

    break


sorted_words = sort_words(user_text)

print()
print(f"La cadena ingresada es: {user_text}")
print(f"Palabras ordenadas alfabéticamente: {sorted_words}")

time.sleep(2)