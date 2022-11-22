import os
# import random
from random import randint

def borrar():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

borrar()
# numero = random.randint(1,10)
numero = randint(1,10)
jugando = True
while jugando:
    num = int(input("Dime un número del 1 al 10: "))

    if num == numero:
        print("Eres el amo")
        jugando = False
    elif num < numero:
        print("Te has quedado corto")
    else:
        print("Te has pasado")