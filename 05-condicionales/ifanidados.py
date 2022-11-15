""""
color = "rojo"
if color == "rojo":
    print("Enhorabuena")
    print("El color es Rojo")
else:
    print("El color No es Rojo")

nombre = input("¿Cual es tu nombre?:")
edad = input("Cual es tu fecha de nacimiento?: ")
print(type(edad))
print("Tipo de fecha de nacimiento en pantalla: " + edad)

if edad == "29-01-1993":
    print("Eres viejo" + nombre)
else:
    print("Eres Joven" + nombre)
"""
print("#######################If anidados ####################")
nombre = "Victor Robles"
ciudad = "Barcelona"
continente = "Oceania"
edad = 18
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")
    if continente != "Europa":
        print("El usuario no es Europeo")
    else:
        print(f"Es Europeo y de {ciudad}")
else:
    print(f"{nombre} No es mayor de edad")
