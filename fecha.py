# Entrada: Pedir una fecha 15/03/2022
# Salida: Su fecha larga es 15 de Marzo de 2022
fecha = input("Dime una fecha (dd/mm/aaaa): ")

dia = int(fecha[0:2])
anio = int(fecha[6:10])
mes = int(fecha[3:5])-1

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

print(f"Su fecha larga es {dia} de {meses[mes]} de {anio}")