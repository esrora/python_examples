import tkinter as tk
# Creo ventana
ventana = tk.Tk()
# Cambiar título ventana
ventana.title("Mi primera aplicación")
# Cambiar tamaño ventana
ventana.geometry("500x900")
# Restringir cambio de tamaño
ventana.resizable(width=True,height=True)

ventana.minsize(width=300, height=300)
ventana.maxsize(width=1000, height=1000)

ventana.configure(background="lightgreen")

ventana.mainloop()