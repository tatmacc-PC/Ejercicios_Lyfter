print("============================== EJERCICIO DE FUNCIONES ================================")
print("-----------------------------------Ejercicio #2.2---------------------------------------")
print()

import time

#vVariable global
name = "Juan"

#Funcion para cambiar el nombre
def change_name():
    global name #Se declara la variable como global para poder modificarla dentro de la funcion

    print(f"El nombre actual es:  {name}" ) #Muestra el nombre actual
    print()
    name = input("Ingrese el nuevo nombre: ") #Solicita el nuevo nombre
    print(f"Valor de la variable name cambiado a: {name}") #Muestra el nuevo nombre

change_name() #Llamada a la funcion para cambiar el nombre

print()
print(f"Valor fuera de la funcion: {name}") #Muestra el nombre actual
time.sleep(2) #Pausa de 2 segundos


