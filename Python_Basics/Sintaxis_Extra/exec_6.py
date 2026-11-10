import time

print("===================================================== EJERCICIO EXTRA #6 ======================================")
print ("-------------------------------------------------------- Validar 30 ------------------------------------------")
print()

counter = int(1)
sum = int(0)

number  = int(input("Digite un número: "))
number1 = int(input("Digite un número: "))
number2 = int(input("Digite un número: "))

sum = number + number1 + number2

print()
print()
print(f"Los números digitados fueron: {number}, {number1}, {number2}")
print()

if number == 30 or number1 == 30 or number2 == 30:
    print(f"Está correcto, hay un 30 entre los números digitados ")
elif sum == 30:
    print("Está correcto, la suma de los números da 30")
else:
    print("Está inccorrecto ya que no hay ningún 30 entre los números o el resultado de sumarlos no da 30")


time.sleep(5)


