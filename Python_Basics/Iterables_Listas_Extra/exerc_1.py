import time

print("=================== EJERCICIO EXTRAS DE ITERABLES Y LISTAS ============================")
print("-------------------- Elimina números impares de una lista -----------------------------")
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

# Pedir y validar el número que desea buscar
while True:
    search_text = input("Ingrese el número que desea buscar: ").strip()

    nosign = search_text
    if nosign.startswith("-"):
        nosign = nosign[1:]

    if not nosign.isdecimal():
        print("\nError: no es un número entero válido. Intente de nuevo.\n")
    else:
        search_number = int(search_text)
        break

# Contar las apariciones del número
counter = 0

for number in lst_numbers:
    if number == search_number:
        counter += 1

print("Lista ingresada:", lst_numbers)
print("El número", search_number, "aparece", counter, "veces.")

time.sleep(5)