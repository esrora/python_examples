import tkinter as tk

def suma():
    numero1 = int(numero1_caja.get())
    numero2 = int(numero2_caja.get())
    calculo = numero1 + numero2
    resultado.config(text=calculo)

def resta():
    numero1 = int(numero1_caja.get())
    numero2 = int(numero2_caja.get())
    calculo = numero1 - numero2
    resultado.config(text=calculo)

def multip():
    numero1 = int(numero1_caja.get())
    numero2 = int(numero2_caja.get())
    calculo = numero1 * numero2
    resultado.config(text=calculo)

def division():
    numero1 = int(numero1_caja.get())
    numero2 = int(numero2_caja.get())
    if numero2 == 0:
        calculo = "ERROR"
    else:
        calculo = numero1 / numero2
    resultado.config(text=calculo)

ventana = tk.Tk()

espacio1 = tk.Frame(ventana)
espacio1.grid(row=0,column=0)
espacio2 = tk.Frame(ventana)
espacio2.grid(row=1,column=0)
espacio3 = tk.Frame(ventana)
espacio3.grid(row=2,column=0)

numero1_etiq = tk.Label(
    espacio1,
    text="Dime un número"
)
numero1_etiq.grid(row=0,column=0)
numero1_caja = tk.Entry(
    espacio1,
    justify=tk.RIGHT
)
numero1_caja.grid(row=0,column=1)
numero2_etiq = tk.Label(
    espacio1,
    text="Dime otro número"
)
numero2_etiq.grid(row=1, column=0)
numero2_caja = tk.Entry(
    espacio1,
    justify=tk.RIGHT
)
numero2_caja.grid(row=1, column=1)

resultado = tk.Label(
    espacio2,
    text="RESULTADO"
)
resultado.grid(row=0,column=0)

suma_boton = tk.Button(
    espacio3,
    text="SUMA",
    command=suma
)
suma_boton.grid(row=0,column=0)
resta_boton = tk.Button(
    espacio3,
    text="RESTA",
    command=resta
)
resta_boton.grid(row=0,column=1)
multi_boton = tk.Button(
    espacio3,
    text="MULTI",
    command=multip
)
multi_boton.grid(row=0,column=2)
div_boton = tk.Button(
    espacio3,
    text="DIVISIÓN",
    command=division
)
div_boton.grid(row=0,column=3)

ventana.mainloop()