# Define list
peliculas = ["Batman", "Spiderman"]

cantantes = list(('2pac', 'Drake', ' Jene'))  # List is inmutable now

years = list(range(2020, 2050))

various_list = ["V", 1, False, 4, 4]

# index in list
print(peliculas[1])
print(peliculas[-2])  # travers the list from the end

print(cantantes[0:2])
print(cantantes[1:])  # get a sublist from index 1

# assign new value to an index
peliculas[1] = "Gran torino"

# Add new value to list
cantantes.append("Kase O")

for cantante in cantantes:
    print(cantante)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1} . {pelicula}")

nueva_pelicula = ""
"""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)


print("\n ******* Listado peliculas*******")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1} . {pelicula}")
"""

# multidimensional list
contactos = [
    [
        'Anotonio',
        'antonio@antonio.com'
    ],
    [
        'luis',
        'Luis@luis.com'
    ],
    [
        'erick',
        'erick@luis.com'
    ]
]

print(contactos[1][1])
"""
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print(elemento)
"""

contador = 0
contador1 = 0
for contador in range(contador, len(contactos)):
    for contador1 in range(contador1, len(contactos[contador])):
        print("Contactos " + contactos[contador][contador1])
        contador1 = contador1 + 1


    contador = contador + 1
