print("============================== EJERCICIO DE FUNCIONES ================================")
print("-----------------------------------Ejercicio #5---------------------------------------")
print()

import time


#Funcion para contar letras mayúsculas y minúsculas
def count_letters(text):
    uppercase_count = 0
    lowercase_count = 0

    for character in text:
        if character.isupper():
            uppercase_count += 1
        elif character.islower():
            lowercase_count += 1
   
    return uppercase_count, lowercase_count

user_text = input("Ingrese una cadena de texto: ")

uppercase_count, lowercase_count = count_letters(user_text)

print()
print(f"La cadena ingresada es: {user_text}")
print(f"Número de letras mayúsculas: {uppercase_count}")
print(f"Número de letras minúsculas: {lowercase_count}")
time.sleep(2)
