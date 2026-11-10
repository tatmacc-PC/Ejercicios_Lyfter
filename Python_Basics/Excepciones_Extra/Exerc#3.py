print("======================== EJERCICIO EXTRA DE EXCEPCIONES =============================")
print("--------------------------------Ejercicio #3-----------------------------------------")
print()

import time

def sum_values(items):
    total = 0.0

    for item in items:
        try:
            number = float(item)
        except (ValueError, TypeError):
            print(f"Elemento inválido: {item}")
        else:
            total += number
            print(f"{number} sumado correctamente")

    print()
    print(f"Total de la suma: {total}")


print()
user_input = input("Ingrese los valores separados por comas: ")
my_list = user_input.split(",")

sum_values(my_list)

time.sleep(2)