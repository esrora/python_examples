# Imprimir
print("Hola mundo")
print("hola otra vez")

# Como preguntar al usuario
nombre = input("Dime tu nombre: ")
print("Hola " + nombre)
anyo = int(input(nombre + " ¿En que año naciste? "))
edad = 2022 - anyo
print("Ahhhh, " + nombre + " tienes " + str(edad) + " años")

# Condicionales
if edad < 18:
    print("No puedes usar esta aplicación")
else:
    print("que mayor que eres")

nota = int(input("¿Qúe nota has sacado en REDES? "))

if nota < 5:
    print("Suspenso")
elif nota < 6:
    print("Aprobado")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")

# Trabajar con números
numero = 3
numero2 = 5
# print(numero)