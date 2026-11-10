import time

print("=================== EJERCICIO DE ITERABLES Y LISTAS ============================")
print("----------------- Elimina números impares de una lista -------------------------")
print()

while True:
    text = input("Escribe números enteros separados por comas: ")
    parts = text.split(",")

    even_numbers = []
    isvalid = True

    for part in parts:
        part = part.strip()

        # Validar: quitar un "-" al inicio y revisar que queden solo dígitos
        nosign = part
        if nosign.startswith("-"):
            nosign = nosign[1:]

        if not nosign.isdigit():
            print("Error:", repr(part), "no es un número entero válido. Intenta de nuevo. \n")
            isvalid = False
            break

        number = int(part)
        if number % 2 == 0:
            even_numbers.append(number)

    if isvalid:
        break

print("Lista sin impares:", even_numbers)

time.sleep(5)