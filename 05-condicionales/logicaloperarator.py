edad_minima = 18
edad_maxima = 65
edad_oficial = 17

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")
pais = "Mexico"
if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana!!")
else:
    print(f"{pais} no es un pais de habla hispana: ")

pais = "Alemania"
if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana!!")
else:
    print(f"{pais} SI es un pais de habla hispana: ")

pais = "USA"
if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana!!")
else:
    print(f"{pais} SI es un pais de habla hispana: ")
