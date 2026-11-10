import time

print("====================== EJERCICIO DICCIONARIO ================================")
print("--------------------------Ejercicio #2---------------------------------------")
print()

# Pedir las claves
keys_text = input("Ingrese las claves separadas por comas: ")
keys = keys_text.split(",")

# Pedir los valores y validar el tamaño
while True:
    values_text = input("Ingrese los valores separados por comas: ")
    values = values_text.split(",")

    if len(keys) == len(values):
        break

    print("Error: ambas listas deben tener la misma cantidad de elementos.")

# Crear el diccionario
dictionary = {}

for index in range(len(keys)):
    key = keys[index].strip()
    value = values[index].strip()
    dictionary[key] = value

# Mostrar cada dato en una línea
print("\nDiccionario creado:")

for key in dictionary:
    print(f"{key}: {dictionary[key]}")

time.sleep(5)