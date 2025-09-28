import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Mi primera App en tkinter")
root.geometry("400x400")
root.resizable(False, False)

main = ttk.Frame(root, padding="5")
main.grid(column=0, row=0)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.nombre = tk.StringVar(value="WEBOS")

ttk.Label(main, textvariable=root.nombre).grid(column=0, row=0, sticky="w")


root.mainloop()