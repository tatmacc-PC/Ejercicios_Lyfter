print("======================== EJERCICIO EXTRA DE EXCEPCIONES =============================")
print("--------------------------------Ejercicio #1-----------------------------------------")
print()

import time

def get_name():
    while True:
        try:
            name = input("Ingrese su nombre: ").strip()

            if not name:
                raise ValueError("El nombre no puede estar vacío.")
            
            if any(char.isdigit() for char in name):
                raise ValueError("El nombre no puede contener números.")
            
            return name
        
        except ValueError as e:
            print(f"Error: {e}")

def get_age():
    while True:
        try:
            age = input("Ingrese su edad: ").strip()

            if not age:
                raise ValueError("La edad no puede estar vacía.")
            
            if not age.isdigit():
                raise ValueError("La edad debe ser un número entero.")
            
            return int(age)
        
        except ValueError as e:
            print(f"Error: {e}")

name = get_name()  
age = get_age()

print()
print(f"Hola {name}, tienes {age} años.")

time.sleep(2)