import time             # módulo de time
print("================================== Número mayor ==============================")
print("------------------------------------------------------------------------------")
print("")               # imprime una linea en blanco

mayor = int(0)
num1  = int(input("Ingrese el primero número: "))
num2  = int(input("Ingrese el segundo número: "))
num3  = int(input("Ingrese el tercer número:  "))
print("")              # imprime una línea en blanco

if num1 >= num2 and num1 >= num3:
    mayor = num1

elif num2 >= num1 and num2 >= num3:
    mayor = num2

else:
    mayor = num3

print(f"El número mayor es: {mayor}")
time.sleep(5)