print("============================== EJERCICIO DE FUNCIONES ================================")
print("-----------------------------------Ejercicio #2.1---------------------------------------")
print()

import time

#Funcion para obtener datos del usuario
def get_data():
    name = input("Ingrese su nombre: ")
    return name

user_name = get_data() #funcion para obtener el nombre del usuario
# print(f'Hola {name}, bienvenido al programa de funciones.') -Error que da: NameError: name 'name' is not defined

print()
print(f"Hola {user_name}, bienvenido al programa de funciones.")
time.sleep(5) #pausa de 5 segundos antes de finalizar el programa

