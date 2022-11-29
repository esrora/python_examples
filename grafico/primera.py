import tkinter as tk

# Funciones
def saludo():
    print("Hola")
    resultado.config(text="hola")


# Creo ventana
ventana = tk.Tk()
# Cambiar título ventana
ventana.title("Mi primera aplicación")
# Cambiar tamaño ventana
ventana.geometry("500x600")
# Restringir cambio de tamaño
ventana.resizable(width=True,height=True)
# Tamaño mínimo y máximo
ventana.minsize(width=300, height=300)
ventana.maxsize(width=1000, height=1000)
# Color de fondo
ventana.configure(background="lightgreen")
# Etiquetas
titulo = tk.Label(ventana,
    text="TÍTULO DE LA APLICACIÓN",
    background="darkblue",
    foreground="white",
    font=("Times", 25, "bold"),
    padx=15, pady=15,
    border=10,
    relief=tk.SUNKEN
)
# tk.GROOVE tk.RAISED
titulo.pack()

# Botón
boton = tk.Button(ventana,
    text="Pulsa aquí",
    foreground="green",
    font=("arial", 30),
    padx=10, pady=10,
    command=saludo
)
boton.pack()
salir = tk.Button(ventana,
    text="Salir",
    command=ventana.quit
)
salir.pack()
resultado = tk.Label(ventana,
    text="Mensaje"
)
resultado.pack()

ventana.mainloop()