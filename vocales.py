# Programa que cuenta las vocales

palabra = input("Dime un nombre: ")

numero_vocales = 0
for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        numero_vocales += 1
    
    #if letra in ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]:

print(f"Tu nombre {palabra} tiene {numero_vocales} vocales")