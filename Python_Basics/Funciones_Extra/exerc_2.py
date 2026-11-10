print("======================== EJERCICIO EXTRA DE FUNCIONES ================================")
print("--------------------------------Ejercicio #2-----------------------------------------")
print()

import time

def filter_words(words, n):
    filtered_words = []

    for word in words:
        if len(word) > n:
            filtered_words.append(word)

    return filtered_words


# Pedir y validar las palabras
while True:
    text = input("Ingrese palabras separadas por comas: ")
    parts = text.split(",")
    words = []
    is_valid = True

    for part in parts:
        word = part.strip()

        if not word.isalpha():
            is_valid = False
            break

        words.append(word)

    if not is_valid:
        print("Error: ingrese solo palabras separadas por comas.")
        print("No se permiten números, palabras vacías ni otros signos.")
        continue

    break


# Pedir y validar el número entero
while True:
    try:
        n = int(input("Ingrese un número entero: "))
        break

    except ValueError:
        print("Error: debe ingresar un número entero.")


result = filter_words(words, n)

print()
print(f"Palabras ingresadas: {words}")
print(f"Palabras con más de {n} letras: {result}")

time.sleep(2)