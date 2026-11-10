print("============================== EJERCICIO DE FUNCIONES ================================")
print("-----------------------------------Ejercicio #4---------------------------------------")
print()

import time

def reverse_string(string):
    return string[::-1]

# Pedir al usuario que ingrese una cadena de texto
text = input("Ingrese una cadena de texto: ")

# Invertir la cadena y guardar el resultado en una variable
reversed_text = reverse_string(text)

# Mostrar el resultado
print()
print(f"La cadena ingresada es: {text}")
print(f"La cadena invertida es: {reversed_text}")
time.sleep(2)