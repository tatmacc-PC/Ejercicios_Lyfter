print("============================== EJERCICIO DE FUNCIONES ================================")
print("-----------------------------------Ejercicio #1---------------------------------------")
print()

import time

#Funcion para mostrar los datos de nombre y edad
def display_data(name, age):
    print(f"Nombre: {name}")
    print(f"Edad: {age}")

#Funcion para mostrar los datos de ciudad y pais y pide los datos al usuario
def display_data1(city, country):
    name = input("Ingrese su nombre: ")
    age = input("Ingrese su edad: ")
    city = input("Ingrese su ciudad: ")
    country = input("Ingrese su país: ")
    print()
    
    display_data(name, age) #Llamada a la función display_data para mostrar nombre y edad

    print(f"Ciudad: {city}")
    print(f"País: {country}")


#Inicio del programa
display_data1("", "") #Llamada a la función display_data1 para mostrar ciudad y país y pedir los datos al usuario
time.sleep(5) #Pausa de 5 segundos antes de finalizar el programa
