import time
print("Hola " + "Tatiana")        # string + string

#print("Edad: " + 48)             # string + int, da error ya que no se puede concatenar int y str
age = 48
print("Edad: " + str(age))        # forma correcta

#print(48 + " años")              # int + string, da error ya que no se puede concatenar int y str
print(str(age) + " años")         # forma correcta

print([1, 2] + [3, 4])            # list + list, correcto

#print("Hola" + ["Tatiana"])      # string + list, forma incorrecta porque son tipos diferentes
nombre = "Tatiana"
numeros = [1,2,3]
print(nombre + str(numeros))

print(10.5 + 5)                   # float + int = float, correcto

print(True + True)                # bool + bool = int, correcto

time.sleep(5)