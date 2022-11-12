contador = 1
while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador +=1

print("--------------------------------------")
contador2 = 1
muestrame = str(0)
while contador2 <= 100:
   muestrame = muestrame +  ", " +  str(contador2)
   contador2 +=1
print(muestrame)

print("#### Ejempl tabla de multiplicar")
numero_usuario = int(input("¿De que numero quieres la tabla?"))
if numero_usuario < 1:
    numero_usuario = 1

print(f"## Tabla del {numero_usuario} ###")
contador2 = 1
while contador2 <= 10:
    print(f"{numero_usuario} * {contador2} = {numero_usuario * contador2}")
    contador2+=1
else:
    print("Tabla terminada.")



