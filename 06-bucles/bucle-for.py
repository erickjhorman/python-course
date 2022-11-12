contador = 0
resultado = 0
for contador in range(0,5):
    print("voy por el " + str(contador))
    resultado = resultado + contador

print(f"El resultado es: {resultado}")
#Ejemplo tabla de multiplicar
numero_usuario = int(input("¿De que numero quieres la tabla?"))
if numero_usuario < 1:
    numero_usuario =1

print(f"#### tabla de multiplicar del numero {numero_usuario} ####")

for numero_tabla in range(0,11):
    if numero_usuario == 45:
        print("No se puede mostrar numeros prohibidos")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("Tabla finaliza.")