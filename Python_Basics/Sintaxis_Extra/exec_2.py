import time
print("=========================================== EJERCICIO EXTRA #2 ==============================")
print("----------------------------- Calcuola el tiempo resto para llegar a 10 minutos -------------")
print()

seconds = int(input("Ingrese el tiempo en segundos "))
print()
seconds_left = int(0)
minutes_secs = 10 * 60              # 10 minutos en segundos

while seconds <= 0:               # Valida que los segundos sean mayor a 0
    print("Los segundos digitados deben ser mayor 0 ")
    seconds = int(input("Ingrese el tiempo en segundos "))
    print()

if seconds < minutes_secs:
    seconds_left = minutes_secs - seconds
    print(f"Faltan {seconds_left} segundos para 10 minutos")
elif seconds > minutes_secs:
    print("El tiempo digitado es mayor a 10 minutos")
else:
    print("El tiempo es igual a 10 minutos")

time.sleep(5)



