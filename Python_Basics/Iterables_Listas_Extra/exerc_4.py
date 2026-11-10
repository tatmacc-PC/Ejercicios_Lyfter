import time

print("====================== EJERCICIO EXTRAS DE ITERABLES Y LISTAS ================================")
print("-- Obtiene el promedio de la lista y crea una lista nueva con los números mayores al promedi--")
print()

# Pedir y validar la lista
while True:
    text = input("Escribe números enteros separados por comas: ")
    parts = text.split(",")

    lst_numbers = []
    
    isvalid = True

    for part in parts:
        part = part.strip()

        # Quitar el signo negativo solo para validar
        nosign = part
        if nosign.startswith("-"):
            nosign = nosign[1:]

        if not nosign.isdecimal():
            print(
                "\nError:", repr(part),
                "no es un número entero válido. Intente de nuevo.\n"
            )
            isvalid = False
            break

        number = int(part)
        lst_numbers.append(number)

    if isvalid:
        break

# Sumar los valores de la lista uno por uno
total = 0

for number in lst_numbers:
    total = total + number

# Calcular el promedio
average = total / len(lst_numbers)

# Crear una lista con los valores mayores al promedio
average_major = []

for number in lst_numbers:
    if number > average:
        average_major.append(number)

print()
print("Lista ingresada:", lst_numbers)
print(f"Promedio: {average:.2f}")
print("Valores mayores al promedio:", average_major)

time.sleep(5)
