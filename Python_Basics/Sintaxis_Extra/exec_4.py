import time

print("===================================================== EJERCICIO EXTRA #4 ======================================")
print ("------------------------------------------------ Conversión de temperaturas ----------------------------------")
print()

celsius = float(input("Ingrese una temperatura en Celsius: "))
fahrenheit = float(0.0)
kelvin = float(0.0)
print()

while celsius < 1:
    celsius = float(input("La temperatura en Celius debe ser mayor a 0, por favor digitar nuevamente una cantidad en Celsius: "))
    print()

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print()
print(f"La temperatura en Celsius es {celsius}°C")
print(f"La temperatura en Fahrenheit es {fahrenheit}°F")
print(f"La temperatura en Kelvin es {kelvin}K")
print()

time.sleep(5)






