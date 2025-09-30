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

    #Labels (columna 1)
    ttk.Label(top, text="Nombre").grid(row=0, column=0)
    ttk.Label(top, text="Género").grid(row=1, column=0)
    ttk.Label(top, text="Tipo").grid(row=2, column=0)
    default_var = tk.StringVar(value="Escribe aquí...")
    admin_var = tk.StringVar(value="User")
    admin_code_var = tk.StringVar(value="Ingrese el código...")

    #Entries (columna 2)
    entry1 = ttk.Entry(top, textvariable=default_var)
    entry1.grid(row=0, column=1)

    genre = ["Masculino", "Femenino"]
    selection = ttk.Combobox(top, values=genre, state="readonly")
    selection.grid(row=1, column=1)
    selection.current(0)

    type = ["User", "Admin"]
    selection2 = ttk.Combobox(top, values=type, textvariable=admin_var, state="readonly")
    selection2.grid(row=2, column=1)
    selection2.current(0)

    admin_confirm = False
    admin_frame = ttk.Frame(top)
    admin_frame.grid(row=3, column=1)
    admin_frame.columnconfigure(1, weight=1)
    admin_label = ttk.Label(admin_frame, text="Código admin")
    admin_entry = ttk.Entry(admin_frame, textvariable=admin_code_var)


    def role_switch(*args):
        role = admin_var.get()
        if role.lower() == "admin":
            admin_confirm = True
            if not admin_label.winfo_ismapped():
                admin_label.grid(row=0, column=0)
                admin_entry.grid(row=0, column=1)
        else:
            admin_frame.grid_forget()
            admin_entry.grid_forget()

    admin_var.trace_add("write", role_switch)
    role_switch()

    def retornar():
        text1=entry1.get()
    ttk.Button(top, text="Ingresar", command=retornar).grid(row=0, column=3)

def button2():
    pass

ttk.Button(main, text="Nuevo", command=button1).pack(side="left")
ttk.Button(main, text="Entrar", command = button2).pack(side="left")
ttk.Button(main, text="Salir", command=root.destroy).pack(side="right")
entry = ttk.Entry(main)


root.mainloop()