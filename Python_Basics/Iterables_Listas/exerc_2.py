import time

print("=============== EJERCICIO DE ITERABLES Y LISTAS =====================")
print("---------------- Impresión de string alreves -----------------------")
print()

string = input("Ingrese una frase: ")
print()
print("El texto de derecha a izquierda queda así: ", end="")

for position in range(len(string) -1, -1, -1):
    print(f"{string[position]}", end="")

print()
print(f"El texto de izquierda a derecha es, {string}")


time.sleep(5)