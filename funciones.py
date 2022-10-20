#Como es la sintaxis de una funcion

#def va a indicar que esto es una funcion
#nombre_function 
#(parametros):

def saludar_alumnos(nombre, apellido = "Perez"):
    print(f"Bienvenido {nombre} {apellido} al bootcamp de backend")

#Esta funcion tiene la instriccion de elevar un numero al cubo
def calcularCubo(n):
   return n ** 3

saludar_alumnos("Jose","Julca")
saludar_alumnos(apellido="Julca",nombre="Javier")

numero = calcularCubo(10)
numero2 = calcularCubo(2)
print(numero)
print(numero2)

def esPar(n):
    if n % 2 == 0:
        return "Es par"
    else:
        return "Es Impar"


print("**** Usando Return ****")
valor1= esPar(10)
print(valor1)
valor2= esPar(13)
print(valor2)


def calcular_primer_puesto(nombre="Alumno",edad="16", nota1=10, nota2=11, nota3=13):
    return f"El alumno {nombre} con edad {edad} tiene en promedio {(nota1 + nota2 + nota3) / 3}"