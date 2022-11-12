print("Ejemplo 1")

def muestraNombre():
    print("Erick")

muestraNombre()

"""Parameters"""
print("Ejemplo 2")

def mostrarNombre(nombre):
    print(f"Tu nombre es: {nombre}")



mostrarNombre("Victor Robles")
mostrarNombre("Paquito")
mostrarNombre("Juanfran")

def mostrarTuNombre(nombre,edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tu nombre: ")
mostrarNombre(nombre)
mostrarTuNombre(nombre, 18)

"""ejemplo con funciones y parametros"""
