print("======================== EJERCICIO EXTRA DE FUNCIONES ================================")
print("--------------------------------Ejercicio #1-----------------------------------------")
print()

import time

def count_characters(text, character):
   count = 0

def count_characters(text, character):
    count = 0

    for letter in text:
        if letter == character:
            count += 1

    return count

#Pedir y validar el texto
while True:
    user_text = input("Ingrese un texto: ")


    if not user_text.strip():
        print("Error: el texto no puede estar vacío ni contener solo espacios.")
        continue

    break

#Pedir y validar el caracter
while True:
    user_character = input("Ingrese un solo caracter para buscar: ")

    if len(user_character) != 1:
        print("Error: debe ingresar un solo caracter.")
        continue

    break

result = count_characters(user_text, user_character)
print() 
print(f"El caracter '{user_character}' aparece {result} veces en el texto.")

time.sleep(2)