from json import loads
import os
import tkinter as tk
import random
import matplotlib.pyplot as plt

arquivos = os.listdir()
arquivos_txt = (arquivo for arquivo in arquivos if arquivo.endswith('.txt'))
ArquivoNaovazio = (arquivo for arquivo in arquivos_txt if os.stat(arquivo).st_size != 0)

quantidadePorcos = 0
for arquivo in ArquivoNaovazio:
    with open(arquivo, 'r') as f:
        por_disserializado = loads(f.read())
        quantidadePorcos += len(por_disserializado)

biogas = quantidadePorcos * 0.24
energia = biogas * 1.25
energia_gerada = random.randint(3000,6000)
energia_usada = random.randint(3000, 8000)
eficiencia_energia = round(energia_gerada/energia_usada * 100)


def BiogasEnergia():
    
    biogas_label['text'] = f'Produção de Biogás Esperada: {biogas}m³/dia'
    
    energia_label['text'] = f'Produção de Energia Esperada: {round(energia)}KWh/dia'
    
    energia_gerada_label['text'] = f'Energia Gerada: {energia_gerada}KWh/dia'

    diferenca = energia_gerada - energia
    if diferenca >= 0:
        diferenca_label['text'] = f'Sua produção de energia foi positiva!\n Você produziu {diferenca} acima do esperado.'
        eficiencia_energia_label['text'] = f'A eficiência da energia gerada foi de {eficiencia_energia}%'
    else:
        diferenca_label['text'] = f'Sua produção está abaixo do esperado.\n Você produziu {diferenca} abaixo do esperado.'
        eficiencia_energia_label['text'] = f'A eficiência da energia gerada foi de {eficiencia_energia}%'


def sair():
    root.destroy()

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

def grafico():
    infos = [energia, energia_usada, energia_gerada]
    nomes = ['Previsão de Geração', 'Energia Usada', 'Energia Gerada']
    indice = range(len(nomes))
    plt.figure("Gráfico de Barras - Comparações de Energia")
    plt.bar(indice, infos, color=['#64FA7C', '#C065FA', '#64FA7C'])
    plt.xlabel('')
    plt.ylabel('Energia em Kw/h')
    plt.title('Comparações de Energia')
    plt.xticks(indice, nomes)
    plt.show()
  

root = tk.Tk()
root.title('Biogás e Energia')
root.geometry('500x350')

frame1 = tk.Frame(root)
frame1.pack(side='top', pady=10)

label1 = tk.Label(frame1, text='Defina o tipo de produção de sua granja:')
label1.pack(side='left')

frame2 = tk.Frame(root)
frame2.pack(side='top', pady=10)

button1 = tk.Button(frame2, text='Ciclo Completo', command=ciclo_completo)
button1.pack(side='left')

button2 = tk.Button(frame2, text='Produtora de Leitão', command=produtora_leitao)
button2.pack(side='left')

button3 = tk.Button(frame2, text='Produção de terminados', command=producao_terminados)
button3.pack(side='left')


frame3 = tk.Frame(root)
frame3.pack(side='top', pady=10)

producaoDejetos_mes_label = tk.Label(frame3, text='')
producaoDejetos_mes_label.pack(side='top')

biogas_label = tk.Label(frame3, text='')
biogas_label.pack(side='top')

energia_label = tk.Label(frame3, text='')
energia_label.pack(side='top')

diferenca_label = tk.Label(frame3, text='')
diferenca_label.pack(side='top')

energia_gerada_label = tk.Label(frame3, text='')
energia_gerada_label.pack(side='top')

eficiencia_energia_label = tk.Label(frame3, text='')
eficiencia_energia_label.pack(side='top')

button4 = tk.Button(frame3, text='Gráfico de Comparações', command=grafico)
button4.pack(side='bottom', pady=15)

sair_button = tk.Button(root, text='Sair', command=sair, fg='red')
sair_button.pack(side='bottom', pady=5)

root.mainloop()
