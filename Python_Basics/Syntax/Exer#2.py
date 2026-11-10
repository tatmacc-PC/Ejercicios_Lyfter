import time

print("=============== EJERCICIO #1 =================")
print("----------------------------------------------")
print("")

name = input("Ingrese tu nombre: ")
lastname = input("Ingrese tu primer apellido: ")
age = int(input("Ingrese tu edad: "))

if age <= 2:
    category = "Bebé"

elif age <= 11:
    category = "Niño"

elif age <= 13:
    category = "Preadolescente"

elif age <= 17:
    category = "Adolescente"

elif age <= 25:
    category = "Joven Adulto"

elif age <= 64:
    category = "Adulto"

else:
    category = "Adulto Mayor"


print("")       # Ingresa una línea en blanco
print(f"{name} {lastname}, tienes  {age} a₧os")
print(f"Tu categoría es:  {category}")
time.sleep(5)   # Pausa de 5 segundos para que muestre el resultado

