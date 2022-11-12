mi_texto = "Master"
mi_texto4 = "'Master'"
print(mi_texto4)
mi_texto2 = "en Python"
#mi_texto3 = "en "Pyhon" " #No valid
mi_texto3 = "en \"Pyhon\" " # valid
print("texto 3 ",mi_texto3)

texto_unido = mi_texto + mi_texto2
print(texto_unido)

texto_unido = mi_texto + "\n" + mi_texto2
print(texto_unido)

texto_unido = mi_texto + "\t" + mi_texto2
print(texto_unido)

texto_unido = mi_texto + "\r" + mi_texto2 #\r drop the words before \r
print(texto_unido)