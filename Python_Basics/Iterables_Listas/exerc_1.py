import time

print("=============== EJERCICIO DE ITERABLES Y LISTAS ==================")
print("------------------ Impresión de dos listas -----------------------")
print()

while True:
    first_list = input("Escribe la primera lista: ").split()
    second_list = input("Escribe la segunda lista: ").split()

    if len(first_list) == len(second_list):
        break

    print("Las listas deben tener el mismo tamaño. Inténtalo de nuevo.\n")

print()
print()

for i in range(len(first_list)):
    print(first_list[i], second_list[i], end = " ")

time.sleep(5)