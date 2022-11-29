import tkinter as tk
import random

def aleatorio():
    numero = random.randint(1,10)
    resultado.config(text=numero)

ventana = tk.Tk()

resultado = tk.Label(
    ventana,
    text="Pulsa el botón",
    font=("Courier", 20, "bold")
)
resultado.pack()

boton = tk.Button(
    ventana,
    text="GENERAR",
    command=aleatorio
)
boton.pack()
ventana.mainloop()