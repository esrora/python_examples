palabra = input("Escribe una palabra: ")

for letra in palabra:
    if letra == "a":
        break
    print(letra)

palabra = input("Escribe otra palabra: ")

for letra in palabra:
    if letra == "a":
        continue
    print(letra)