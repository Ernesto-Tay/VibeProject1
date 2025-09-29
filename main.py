import tkinter as tk
from tkinter import ttk, messagebox
root = tk.Tk()
root.title("Mi primera App en tkinter")
root.geometry("400x400")
root.resizable(False, False)

main = ttk.Frame(root, padding=15)
main.pack(side="top", fill="x")
def button1():
    top = tk.Toplevel(main)
    top.title("Nuevo")
    top.resizable(False, False)
    ttk.Label(top, text="Nombre").grid(row=0, column=0)
    entry1 = ttk.Entry(top)
    entry1.grid(row=0, column=1)
    def retornar():
        text1=entry1.get()
        ttk.Label(top, text=f"Tu nombre es: {text1}").grid(row=0, column=2)
    ttk.Button(top, text="Ingresar", command=retornar).grid(row=0, column=3)

def button2():
    pass

ttk.Button(main, text="Nuevo", command=button1).pack(side="left")
ttk.Button(main, text="Entrar", command = button2).pack(side="left")
ttk.Button(main, text="Salir", command=root.destroy).pack(side="right")
entry = ttk.Entry(main)


root.mainloop()