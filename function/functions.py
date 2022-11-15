print("Ejemplo 1")

"""
def muestraNombre():
    print("Erick")


muestraNombre()
"""
"""Parameters"""
"""
print("Ejemplo 2")


def mostrarNombre(nombre):
    print(f"Tu nombre es: {nombre}")


mostrarNombre("Victor Robles")
mostrarNombre("Paquito")
mostrarNombre("Juanfran")


def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")


nombre = input("Introduce tu nombre: ")
mostrarNombre(nombre)
mostrarTuNombre(nombre, 18)

"""
"""ejemplo con funciones y parametros"""


def table(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} * {contador} = {operacion}")

    print("\n")


table(3)

for numero_table in range(1, 11):
    table(numero_table)

print("Ejemplo 4")


# Parametros opcionales
def getEmpleado(nombre, dni=None):
    print("Empleado")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")


getEmpleado("Victor Robles")


# Ejemplo 5

def calculadora(numero1, numero2, basicas=False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return cadena


print(calculadora(5, 5, True))


# Ejemplo 7
def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto


def getApellidos(apellidos):
    texto = f"El nombre es: {apellidos }"
    return texto


def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto


print(devuelveTodo("Erick", "Romero Jojoa"))


#Ejemplo 7
dime_el_year = lambda year: f"El año es {year * 50}"

print(dime_el_year(2034))