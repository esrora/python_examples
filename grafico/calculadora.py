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
numero1_etiq = tk.Label(
    ventana,
    text="Dime un número"
)
numero1_etiq.pack()
numero1_caja = tk.Entry(
    ventana,
    justify=tk.RIGHT
)
numero1_caja.pack()
numero2_etiq = tk.Label(
    ventana,
    text="Dime otro número"
)
numero2_etiq.pack()
numero2_caja = tk.Entry(
    ventana,
    justify=tk.RIGHT
)
numero2_caja.pack()

resultado = tk.Label(
    ventana,
    text="RESULTADO"
)
resultado.pack()

suma_boton = tk.Button(
    ventana,
    text="SUMA",
    command=suma
)
suma_boton.pack()
resta_boton = tk.Button(
    ventana,
    text="RESTA",
    command=resta
)
resta_boton.pack()
multi_boton = tk.Button(
    ventana,
    text="MULTI",
    command=multip
)
multi_boton.pack()
div_boton = tk.Button(
    ventana,
    text="DIVISIÓN",
    command=division
)
div_boton.pack()

ventana.mainloop()