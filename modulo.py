import os

def borrar():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

borrar()
print("Hola")
nombre = input("Dime tu nombre: ")

borrar()
edad = int(input(f"{nombre}, dime tu edad: "))