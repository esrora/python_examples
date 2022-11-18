# Ejemplos de operaciones
num1 = 18
num2 = 5

suma = num1 + num2
print(f"La suma de {num1} y {num2} es {suma}")

resta = num2 - num1
print(f"La resta de {num2} y {num1} es {resta}")

multi = num1 * num2
print(f"La multiplicación de {num1} y {num2} es {multi}")

div = num1 / num2
print(f"La división de {num1} y {num2} es {div}")

resto = num1 % num2
print(f"La resto de la división de {num1} y {num2} es {resto}")

# Comparación o lógicos
# Igual ==
# Distinto !=
# Mayor que > 
# Menor que <
# Mayor igual que >=
# Menor igual que <=
# Y and
# O or
# No not
edad = int(input("¿Cuántos años tienes? "))
nota = int(input("¿Qué nota has sacado en el examen? "))

if (edad < 18) and (nota < 5):
    print("Muy mal vas a papá")
elif (edad >= 18) and (nota < 5):
    print("Pepino")
elif (edad < 18) and (nota >= 5):
    print("Le diré a papá que has aprobado")
else:
    print("Enhorabuena")














