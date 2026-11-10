import time

print("====================== EJERCICIO DICCIONARIO ================================")
print("--------------------------Ejercicio #3---------------------------------------")
print()

dictionary = {
    "name": "Tatiana",
    "age": 30,
    "city": "San José",
    "phone": "6061-1812"
}

# Mostrar los datos actuales
print("Datos actuales:")

for key in dictionary:
    print(f"{key}: {dictionary[key]}")

# Pedir las claves que desea eliminar
keys_text = input("\nIngrese las claves que desea eliminar separadas por comas: ")
keys_to_remove = keys_text.split(",")

# Eliminar las claves indicadas
for key in keys_to_remove:
    key = key.strip()

    if key in dictionary:
        del dictionary[key]
        print(f"Se eliminó la clave: {key}")
    else:
        print(f"La clave '{key}' no existe.")

# Mostrar los datos restantes
print("\nDatos restantes:")

for key in dictionary:
    print(f"{key}: {dictionary[key]}")

time.sleep(5)