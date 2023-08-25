import customtkinter as ctk
from tkinter import messagebox
import subprocess

def abrirCodeUm(): #Abre o código de gerenciamento de porcos
    try:
        subprocess.run(["python", "porccc.py"])
    except FileNotFoundError: #Caso o arquivo não seja encontrado, exibe uma mensagem de erro
        messagebox.showerror("Erro", "O arquivo do primeiro código não foi encontrado.")

def abrirCodeDois(): #Abre o código de cálculos de energia
    try:
        subprocess.run(["python", "calcporc.py"])
    except FileNotFoundError: #Caso o arquivo não seja encontrado, exibe uma mensagem de erro
        messagebox.showerror("Erro", "O arquivo do segundo código não foi encontrado.")

def sair(): #Fecha o programa
    root.destroy()

#Cria a janela principal
root = ctk.CTk()
root.title("Menu Principal")
root.geometry("720x480")

#Cria os widgets
label = ctk.CTkLabel(root, text="Selecione uma opção:", font=("Helvetica", 24))
label.pack(pady=20)

button1 = ctk.CTkButton(root, text="Gerenciamento de Porcos", command=abrirCodeUm, font=("Helvetica", 14))
button1.pack(pady=10)

button2 = ctk.CTkButton(root, text="Cálculos de Biogás", command=abrirCodeDois, font=("Helvetica", 14))
button2.pack(pady=10)

button_sair = ctk.CTkButton(root, text="Sair", command=sair, font=("Helvetica", 14), fg_color="red")
button_sair.pack(pady=10)

root.mainloop()
