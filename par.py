# Ejemplo par impar

numero = int(input("Dime un número: "))

resto = numero % 2

if resto == 0:
    print(f"El {numero} es par")
else:
    print(f"El {numero} es impar")