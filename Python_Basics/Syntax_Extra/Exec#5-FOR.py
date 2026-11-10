import time

print("================================================ EJERCICIO EXTRA #5 ======================================")
print ("---------------------------------------------- Tabla de Multiplicar ----------------------------------")
print()


number = int(input("Digite un número entre 1 y 10: "))
print()
counter = int(1)
result = int(0)

while number < 1:                       # Validad que el número digitado no sea igual a 0
    print()
    number = int(input("El número digitado debe estar dentro del rango entre 1 y 10, por favor vuelva  a digitar un número: "))
    print()

for counter in range(1,13):
    result = number * counter
    print(f"{number} x {counter} = {result}")

time.sleep(5)
  





