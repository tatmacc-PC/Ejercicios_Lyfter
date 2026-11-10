import time

print("====================== EJERCICIO EXTRAS DE ITERABLES Y LISTAS ================================")
print("---------------Muestra una lista con las palabras que contengan 4 letras----------------------")
print()

lstwords = []

# Pedir 5 palabras
while len(lstwords) < 5:
    word = input("Ingrese una palabra: ").strip()

    if not word.isalpha():
        print("Ingrese solo letras, sin espacios ni números.")
        continue

    lstwords.append(word)

# Crear una lista con palabras de más de 4 letras
lstnewwords = []

for word in lstwords:
    if len(word) > 4:
        lstnewwords.append(word)

print()
print("Lista ingresada:", lstwords)
print("Palabras con más de 4 letras:", lstnewwords)

time.sleep(5)