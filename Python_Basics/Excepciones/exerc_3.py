print("======================== EJERCICIO EXTRA DE FUNCIONES ================================")
print("--------------------------------Ejercicio #3-----------------------------------------")
print()

import time

def count_vowels(text):
    count = 0
    vowels = "aeiouáéíóúü"

    for character in text.lower():
        if character in vowels:
            count += 1

    return count


# Pedir y validar el texto
while True:
    user_text = input("Ingrese un texto: ").strip()

    if not user_text:
        print("Error: debe ingresar un texto.")
        continue

    is_valid = True

    for character in user_text:
        if not character.isalpha() and not character.isspace():
            is_valid = False
            break

    if not is_valid:
        print("Error: ingrese solo letras y espacios, sin números ni signos.")
        continue

    break


result = count_vowels(user_text)

print(f"El texto contiene {result} vocales.")


time.sleep(2)