import time                           # módulo time
import random                         # módulo random, que genera numeros aleatorios

print("====================== Número Secreto =================== ")
print("----------------------------------------------------------")
print("")           # imprime una linea en blanco

random_number = random.randint(1,10)        # genera el número secreto
number = int(input("Digite un número entre 1 y 10 para adivinar el número secreto: "))      # variable que el usuario digita para adivinar el número secreto

while random_number != number:
    print("")       #   imprime una línea en blanco
    print("Número incorrecto. Intente nuevamente")
    number = int(input("Ingrese otro número entre 1 y 10: "))


print("")           # imprime una línea en blanco
print(f"FELICIDADES! Adivinaste el número secreto, el cual es: {random_number}")   
time.sleep(5) 
