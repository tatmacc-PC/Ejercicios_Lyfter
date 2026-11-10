import time

print("===================================================== EJERCICIO EXTRA #3 ======================================")
print ("----------------------------------------------------- Suma de dígitos ----------------------------------------")
print()

counter = int(1)
sum = int(0)
number = int(input("Digite un número: "))

while number < 1:                   # Valida que el número digitado no sea 0
    print()
    number = int(input("Número digitado debe ser mayor a 0, por favor vuelva a digitar un número: "))
    print()

while counter <= number:           # Suma cada uno de los d¢gitos del número digitado
    sum = sum + counter
    counter = counter + 1

print(f"La suma desde 1 hasta {number} es {sum}")
time.sleep(5)


