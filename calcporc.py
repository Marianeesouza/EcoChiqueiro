from json import loads
import os
import tkinter as tk
import random
import matplotlib.pyplot as plt
import customtkinter as ctk

#Lista os arquivos txt do diretório atual, e agrupa os que não estão vazios
arquivos = os.listdir()
arquivos_txt = (arquivo for arquivo in arquivos if arquivo.endswith('.txt'))
ArquivoNaovazio = (arquivo for arquivo in arquivos_txt if os.stat(arquivo).st_size != 0)

#Calcula a quantidade de porcos
quantidadePorcos = 0
for arquivo in ArquivoNaovazio:
    with open(arquivo, 'r') as f:
        por_disserializado = loads(f.read())
        quantidadePorcos += len(por_disserializado)

#Calcula a quantidade de biogás e energia
biogas = quantidadePorcos * 0.24
energia = biogas * 1.25

#Gera dados hipotéticos de energia gerada e usada
energia_gerada = random.randint(50,200)
energia_usada = random.randint(20, 250)
eficiencia_energia = round(energia_gerada/energia_usada * 100)


def BiogasEnergia(): #Função para mostrar os dados de biogás e energia na tela 
    
    biogas_label['text'] = f'Produção de Biogás Esperada: {biogas}m³/dia'
    
    energia_label['text'] = f'Produção de Energia Esperada: {round(energia)}KWh/dia'
    
    energia_gerada_label['text'] = f'Energia Gerada: {energia_gerada}KWh/dia'

    diferenca = energia_gerada - energia
    if diferenca >= 0: #Verifica se a energia gerada é maior que a esperada
        diferenca_label['text'] = f'Sua produção de energia foi positiva!\n Você produziu {diferenca} acima do esperado.'
        eficiencia_energia_label['text'] = f'A eficiência da energia gerada foi de {eficiencia_energia}%'
        if energia_gerada > energia_usada: #Verifica se a energia gerada é maior que a usada
            comparacao_label['text'] = f' Você está gerando mais energia do que consumindo!'
        else:
            comparacao_label['text'] = f'Cuidado! Você está consumindo mais energia que gerando.'
    else: #Caso a energia gerada seja menor que a esperada
        diferenca_label['text'] = f'Sua produção está abaixo do esperado.\n Você produziu {diferenca} abaixo do esperado.'
        eficiencia_energia_label['text'] = f'A eficiência da energia gerada foi de {eficiencia_energia}%'
        if energia_gerada > energia_usada: 
            comparacao_label['text'] = f' Você está gerando mais energia do que consumindo!'
        else:
            comparacao_label['text'] = f'Cuidado! Você está consumindo mais energia que gerando.'


def sair(): #Função para fechar o programa
    root.destroy()

#Funções para calcular a produção de dejetos de acordo com o tipo de produção
def ciclo_completo(): 
    producaoDejetos = 100 * quantidadePorcos
    producaoDejetos_mes_label['text'] = f'Produção de dejetos: {producaoDejetos * 30}L/mês'
    BiogasEnergia()

def produtora_leitao():
    producaoDejetos = 60 * quantidadePorcos 
    producaoDejetos_mes_label['text'] = f'Produção de dejetos: {producaoDejetos * 30} L/mês'
    BiogasEnergia()

def producao_terminados():
    producaoDejetos = 7.5 * quantidadePorcos
    producaoDejetos_mes_label['text'] = f'Produção de dejetos: {producaoDejetos * 30} L/mês'
    BiogasEnergia()

#Função para gerar o gráfico de comparações
def grafico():
    plt.style.use('dark_background')
    infos = [energia, energia_usada, energia_gerada]
    nomes = ['Previsão de Geração', 'Energia Usada', 'Energia Gerada']
    indice = range(len(nomes))
    plt.figure("Gráfico de Barras - Comparações de Energia")
    plt.bar(indice, infos, color=['#264b96', '#bf212f', '#27b376'])
    plt.xlabel('')
    plt.ylabel('Energia em Kw/h')
    plt.title('Comparações de Energia')
    plt.xticks(indice, nomes)
    plt.show()
  
#Interface gráfica
root = ctk.CTk()
root.title('Biogás e Energia')
root.geometry('500x350')

frame1 = ctk.CTkFrame(root)
frame1.pack(side='top', pady=10)

label1 = ctk.CTkLabel(frame1, text='Defina o tipo de produção de sua granja:')
label1.pack(side='left')

frame2 = ctk.CTkFrame(root)
frame2.pack(side='top', pady=10)

button1 = ctk.CTkButton(frame2, text='Ciclo Completo', command=ciclo_completo)
button1.pack(side='left')

button2 = ctk.CTkButton(frame2, text='Produtora de Leitão', command=produtora_leitao)
button2.pack(side='left')

button3 = ctk.CTkButton(frame2, text='Produção de terminados', command=producao_terminados)
button3.pack(side='left')


#Labels para mostrar os dados de biogás e energia
frame3 = ctk.CTkFrame(root)
frame3.pack(side='top', pady=10)

producaoDejetos_mes_label = tk.Label(frame3, text='', bg="#2B2B2B", fg="white")
producaoDejetos_mes_label.pack(side='top')

biogas_label = tk.Label(frame3, text='', bg="#2B2B2B", fg="white")
biogas_label.pack(side='top')

energia_label = tk.Label(frame3, text='', bg="#2B2B2B", fg="white")
energia_label.pack(side='top')

diferenca_label = tk.Label(frame3, text='', bg="#2B2B2B", fg="white")
diferenca_label.pack(side='top')

energia_gerada_label = tk.Label(frame3, text='', bg="#2B2B2B", fg="white")
energia_gerada_label.pack(side='top')

eficiencia_energia_label = tk.Label(frame3, text='', bg="#2B2B2B", fg="white")
eficiencia_energia_label.pack(side='top')

comparacao_label = tk.Label(frame3, text='', bg="#2B2B2B", fg="white")
comparacao_label.pack(side='top')

button4 = ctk.CTkButton(frame3, text='Gráfico de Comparações', command=grafico)
button4.pack(side='bottom', pady=15)

sair_button = ctk.CTkButton(root, text='Sair', command=sair, fg_color='red')
sair_button.pack(side='bottom', pady=5)

root.mainloop()