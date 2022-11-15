nombre = "Victor"

print(type(nombre)) # print the type of the variable

# detect variable type
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# clean spaces
frase = "    mi contenido   "
print(frase.split(frase))

# delete variables
year = 2022
print(year)
del year # del is used to delete variable

# check if strings is empty
texto = "  ff   "
if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido", len(texto))

# find characters
frase = "La vida es bella"
print(frase.find("vida"))

# Replace words in any string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# Lowercase & uppercase
print(nombre)
print(nombre.lower())
print(nombre.upper())