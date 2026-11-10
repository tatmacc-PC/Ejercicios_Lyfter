print("======================== EJERCICIO EXTRA DE EXCEPCIONES =============================")
print("--------------------------------Ejercicio #2-----------------------------------------")
print()

import time

def convert_to_integer(items):
    for item in items:
        item = item.strip()

        try:
            number = int(item)
            print(f'"{item}" convertido a {number}')
        except ValueError:
            print(f"No se pudo convertir el elemento: {item}")


print()
user_input = input("Ingrese los valores separados por comas: ")
values = user_input.split(",")

print()
print("Resultado:")
convert_to_integer(values)

time.sleep(2)