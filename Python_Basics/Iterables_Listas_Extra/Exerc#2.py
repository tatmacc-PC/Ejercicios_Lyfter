import time

print("====================== EJERCICIO EXTRAS DE ITERABLES Y LISTAS ================================")
print("------------------- Verifica si todos los números son positivos ------------------------------")
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

# Contar los números negativos o ceros
counter = 0

for number in lst_numbers:
    if number <= 0:
        counter += 1

print()
print("Lista ingresada:", lst_numbers)
print("Cantidad de números negativos o ceros:", counter)

time.sleep(5)