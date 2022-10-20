numeros = []

for i in range(1, 10):
   numeros.append(i ** 2 + i ** 3)
print(numeros)

print("*** Migrando a comprehesion ***")

numeros2 = [j ** 2 + j ** 3 for j in range(1, 10) if j % 2 == 0]

print(numeros2)


print("*** comprehesion con diccionarios***")

edades = {f"key-{i}": i for i in range(10, 20)}
print(edades)

lista = ["Pepe","Maria", None,"Luis", None]



