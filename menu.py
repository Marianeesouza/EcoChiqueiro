import tkinter as tk
from tkinter import messagebox
import subprocess

def abrirCodeUm():
    try:
        subprocess.run(["python", "porccc.py"])
    except FileNotFoundError:
        messagebox.showerror("Erro", "O arquivo do primeiro código não foi encontrado.")

def abrirCodeDois():
    try:
        subprocess.run(["python", "calcporc.py"])
    except FileNotFoundError:
        messagebox.showerror("Erro", "O arquivo do segundo código não foi encontrado.")

def sair():
    root.destroy()

root = tk.Tk()
root.title("Menu Principal")
root.geometry("720x480")

label = tk.Label(root, text="Selecione uma opção:", font=("Helvetica", 16))
label.pack(pady=20)

button1 = tk.Button(root, text="Gerenciamento de Porcos", command=abrirCodeUm, font=("Helvetica", 14))
button1.pack(pady=10)

button2 = tk.Button(root, text="Cálculos de Biogás", command=abrirCodeDois, font=("Helvetica", 14))
button2.pack(pady=10)

button_sair = tk.Button(root, text="Sair", command=sair, font=("Helvetica", 14), fg="red")
button_sair.pack(pady=20)

root.mainloop()
