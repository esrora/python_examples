'''
a = 1
while a < 10:
    print(f"Hola {a}")
    a = a + 1
    # a += 1
'''

jugando = True
while jugando:
    numero = int(input("Dime un número menor que 10: "))
    if numero < 10:
        jugando = False
        print("Muy bien")
    else:
        print(f"Muy mal el {numero} no es menor que 10")