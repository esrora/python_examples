import os
from random import randint

def borrar():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

borrar()

numero = randint(1,100)
limite = 10
jugando = True

while jugando:
    num = int(input("Dime un número del 1 al 100: "))

    if num == numero:
        print("Eres el amo")
        jugando = False
    elif num < numero:
        print("Te has quedado corto")
        limite = limite - 1
    else:
        print("Te has pasado")
        limite = limite -1
    
    if limite == 0:
        print("Se han agotado los intentos")
        jugando = False