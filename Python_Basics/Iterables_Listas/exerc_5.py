import time

print("=================== EJERCICIO DE ITERABLES Y LISTAS ============================")
print("---------------- Devuelve el número mayor de una lista -------------------------")
print()

counter = int(0)
largest = None
numbers = []

while counter < 10:
    number = int(input(f"Número {counter + 1} a ingresar: "))
    numbers.append(number)

    if largest is None or number > largest:
        largest = number

    counter = counter + 1

print()
print("Números ingresados: ", numbers)
print("El número mayor es:", largest)

time.sleep(5)