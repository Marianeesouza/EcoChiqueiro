import os
import json
import tkinter as tk
from tkinter import messagebox, scrolledtext
import customtkinter as ctk

# Lista global para armazenar nomes das baias
arquivo_sem_extensao = []

# Função para listar os arquivos .txt no diretório
def lista_de_arquivos():
    arquivos = os.listdir()
    arquivos_txt = [arquivo for arquivo in arquivos if arquivo.endswith('.txt')]
    arquivo_sem_extensao = [os.path.splitext(arquivo)[0] for arquivo in arquivos_txt]
    return arquivo_sem_extensao

# Função para adicionar informações de porcos em uma baia
def adicionar_porcos(nome_arquivo):
    ask = ctk.CTkInputDialog(text="Digite uma identificação para o animal: ", title="Identificação")
    identificacao = ask.get_input()
    if not identificacao:
        return  # Se não for fornecida uma identificação, sai da função
    
    try:
        with open(f'{nome_arquivo}.txt', 'r+') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                dados = {}  # Se o JSON estiver vazio ou inválido, inicializa com um dicionário vazio
    except FileNotFoundError:
        dados = {}

    if identificacao in dados: # Verifica se a identificação já existe e exibe uma mensagem de erro
        messagebox.showerror("Erro", f"Porco '{identificacao}' já existe!")
        return

    # Pede as informações do porco
    ask2 = ctk.CTkInputDialog(text="Digite a idade do seu animal: ", title="Idade")
    idade = float(ask2.get_input())

    ask3 = ctk.CTkInputDialog(text="Digite o sexo do seu animal: ", title="Sexo")
    sexo = ask3.get_input()

    ask4 = ctk.CTkInputDialog(text="Digite a raça do seu animal: ", title="Raça")
    raca = ask4.get_input()

    ask5 = ctk.CTkInputDialog(text="Digite o peso do seu animal(Kg): ", title="Peso")
    peso = float(ask5.get_input())

    ask6 = ctk.CTkInputDialog(text="Digite a quantidade de ração que o seu animal come por dia: ", title="Ração por Dia")
    racao_dia = float(ask6.get_input())
    
    vacina = []
    op = tk.messagebox.askyesno("Vacina", "O seu animal já tomou vacina?")
    
    if op: # Se o usuário responder sim, pede quantas vacinas o animal tomou e o nome de cada uma
        dialog = ctk.CTkInputDialog(text="Quantas vacinas o seu animal tomou?", title="Vacinas")
        ask = int(dialog.get_input())
        for _ in range(ask):
            vacina.append(ctk.CTkInputDialog(text = f"Diga o nome da vacina {_+1}:", title="Vacinas").get_input())

        # Cria um dicionário com as informações do porco 
    por = {'Idade': idade, 'Sexo': sexo, 'Raça': raca, 'Peso': peso, 'Ração por dia': racao_dia, 'Vacinas': vacina} 
    
    dados[identificacao] = por # Adiciona o porco ao dicionário de dados
    
    with open(f'{nome_arquivo}.txt', 'w') as f: # Salva os dados no arquivo
        json.dump(dados, f)
        
def listar_baias(baia_listbox, arquivo_sem_extensao): # Função para listar as baias existentes 
    baia_listbox.delete(0, ctk.END)
    for i, nome in enumerate(arquivo_sem_extensao, start=1):
        baia_listbox.insert(ctk.END, f'Baia {i}: {nome}')


# Função para remover uma baia
def remover_baia(nome_baia, baia_listbox, arquivo_sem_extensao): # Função para remover uma baia
    try: # Tenta remover o arquivo da baia 
        os.remove(f'{nome_baia}.txt')
        arquivo_sem_extensao.remove(nome_baia)
        baia_listbox.delete(ctk.ACTIVE)

        listar_baias(baia_listbox, arquivo_sem_extensao)
        messagebox.showinfo("Sucesso", f"Baia '{nome_baia}' removida com sucesso!") 

    except ValueError: # Se o nome da baia não estiver na lista de baias, exibe uma mensagem de erro
        messagebox.showerror("Erro", f"Baia '{nome_baia}' não encontrada!")
        
def remover_porco(nome_arquivo, identificacao): # Função para remover um porco
    try:
        with open(f'{nome_arquivo}.txt', 'r') as f: # Tenta abrir o arquivo da baia
            dados = json.load(f)
        if identificacao in dados: # Verifica se a identificação existe no arquivo
            del dados[identificacao]
            with open(f'{nome_arquivo}.txt', 'w') as f: # Salva os dados no arquivo
                json.dump(dados, f)
            messagebox.showinfo("Sucesso", f"Porco '{identificacao}' removido com sucesso!")
            listar_porcos_baia(nome_arquivo)  # Atualiza a lista de porcos na baia após a remoção
        else: # Se a identificação não existir, exibe uma mensagem de erro
            messagebox.showerror("Erro", f"Porco '{identificacao}' não encontrado!")
    except FileNotFoundError: # Se o arquivo da baia não existir, exibe uma mensagem de erro
        messagebox.showerror("Erro", "Arquivo da baia não encontrado!")
    except json.JSONDecodeError: # Se o arquivo da baia estiver vazio ou inválido, exibe uma mensagem de erro
        messagebox.showerror("Erro", "Erro ao carregar dados da baia!")

def listar_porcos_baia(nome_arquivo): # Função para listar os porcos de uma baia
    try: # Tenta abrir o arquivo da baia
        with open(f'{nome_arquivo}.txt', 'r') as f: 
            conteudo = f.read()
            if conteudo.strip() == "":
                return []  # Retorna uma lista vazia se o arquivo estiver vazio
            dados = json.loads(conteudo) # Carrega os dados do arquivo
            porcos = [] 
            for identificacao, porco in dados.items(): # Itera sobre os porcos da baia
                porcos.append(f"Identificação: {identificacao}, Idade: {porco['Idade']} anos, Sexo: {porco['Sexo']}")
            return porcos

    except FileNotFoundError:
        return [] # Retorna uma lista vazia se o arquivo não existir

def atualizar_porco(nome_arquivo, identificacao): # Função para atualizar os dados de um porco
    try: # Tenta abrir o arquivo da baia
        with open(f'{nome_arquivo}.txt', 'r') as f:
            dados = json.load(f) # Carrega os dados do arquivo

        if identificacao in dados: # Verifica se a identificação existe no arquivo
            ask = ctk.CTkInputDialog(text="O que você deseja atualizar?", title="Atualizar")
            op = ask.get_input().lower() # Pede ao usuário o que ele deseja atualizar

            # Verifica qual opção foi escolhida, pede ao usuário o novo valor e atualiza o arquivo
            if op == "idade": 
                ask = ctk.CTkInputDialog(text="Digite a nova idade do seu animal: ", title="Idade")
                idade = int(ask.get_input())
                dados[identificacao]['Idade'] = idade
                with open(f'{nome_arquivo}.txt', 'w') as f:
                    json.dump(dados, f)
                messagebox.showinfo("Sucesso", f"Porco '{identificacao}' atualizado com sucesso!")

            elif op == "peso":
                ask2 = ctk.CTkInputDialog(text="Digite o novo peso do seu animal: ", title="Peso")
                peso = int(ask2.get_input())
                dados[identificacao]['Peso'] = peso
                with open(f'{nome_arquivo}.txt', 'w') as f:
                    json.dump(dados, f)
                messagebox.showinfo("Sucesso", f"Porco '{identificacao}' atualizado com sucesso!")

            elif op == 'ração por dia':
                ask3 = ctk.CTkInputDialog(text="Digite a nova quantidade de ração que o seu animal come por dia: ", title="Ração por dia")
                racao_dia = int(ask3.get_input())
                dados[identificacao]['Ração por dia'] = racao_dia
                with open(f'{nome_arquivo}.txt', 'w') as f:
                    json.dump(dados, f)
                messagebox.showinfo("Sucesso", f"Porco '{identificacao}' atualizado com sucesso!")

            elif op == 'vacinas':
                ask4 = ctk.CTkInputDialog(text="Qual vacina deseja adicionar?", title="Vacina")
                vacina = ask4.get_input()
                dados[identificacao]['Vacinas'].append(vacina)
                with open(f'{nome_arquivo}.txt', 'w') as f:
                    json.dump(dados, f)
                messagebox.showinfo("Sucesso", f"Porco '{identificacao}' atualizado com sucesso!")

            else:
                messagebox.showerror("Erro", "Opção inválida!")

    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo da baia não encontrado!")

def infos_porco(nome_arquivo, identificacao): # Função para mostrar as informações de um porco
    try:
        with open(f'{nome_arquivo}.txt', 'r') as f:
            dados = json.load(f) # Carrega os dados do arquivo
        if identificacao in dados:
            vacinas = dados[identificacao]['Vacinas']
            vacinas = ', '.join(vacinas) # Transforma a lista de vacinas em uma string separada por vírgulas
            # Exibe as informações do porco em uma messagebox
            messagebox.showinfo("Informações", f"Idade: {dados[identificacao]['Idade']} anos\nSexo: {dados[identificacao]['Sexo']}\nRaça: {dados[identificacao]['Raça']}\nPeso: {dados[identificacao]['Peso']} Kg\nRação por dia: {dados[identificacao]['Ração por dia']} Kg\nVacinas: {vacinas}")
        else: # Se a identificação não existir, exibe uma mensagem de erro
            messagebox.showerror("Erro", f"Porco '{identificacao}' não encontrado!") 
    except FileNotFoundError: # Se o arquivo da baia não existir, exibe uma mensagem de erro
        messagebox.showerror("Erro", "Arquivo da baia não encontrado!")
    except json.JSONDecodeError: # Se o arquivo da baia estiver vazio ou inválido, exibe uma mensagem de erro
        messagebox.showerror("Erro", "Erro ao carregar dados da baia!")

def main(): # Função principal 
    root = ctk.CTk() # Cria a janela principal
    root.title("Gerenciamento de Porcos")
    root.geometry("1000x720")  # Definindo o tamanho da janela

    arquivo_sem_extensao = lista_de_arquivos() # Lista os arquivos .txt do diretório atual

    baia_listbox = tk.Listbox(root, font=("Helvetica", 14), bg="#2B2B2B", fg="white")

    listar_baias(baia_listbox, arquivo_sem_extensao)  # Aqui é onde você chama a função listar_baias

    def adicionar_baia(): # Função para adicionar uma baia
        ask = ctk.CTkInputDialog(text="Adicione o nome da baia:", title="Adicionar Baia")
        nome_baia = ask.get_input()
        if nome_baia:
            try:
                with open(f'{nome_baia}.txt', 'x'):
                    messagebox.showinfo("Sucesso", "Baia cadastrada com sucesso!")
                    arquivo_sem_extensao.append(nome_baia)
                    listar_baias(baia_listbox, arquivo_sem_extensao)  # Atualiza a lista de baias na interface
            except FileExistsError:
                messagebox.showerror("Erro", "Baia já cadastrada!")


    def baia_selecionada_event(event): # Função para quando uma baia for selecionada
        if baia_listbox.curselection(): # Verifica se alguma baia foi selecionada

            selected_index = baia_listbox.curselection()[0]
            nome_baia = arquivo_sem_extensao[selected_index]
            baia_label.configure(text=f"Baia selecionada: {nome_baia}")
            baia_frame.pack()
            #botão para chamada da função adicionar_porcos
            adicionar_porco_button.configure(command=lambda: adicionar_porcos(nome_baia)) 
            #botão para chamada da função infos_porco
            infos_porco_button.configure(command=lambda: infos_porco(nome_baia, identificacao_entry.get()))
            #botão para chamada da função remover_porco
            remover_porco_button.configure(command=lambda: remover_porco(nome_baia, identificacao_entry.get()))
            #botão para chamada da função atualizar_porco
            atualizar_porco_button.configure(command=lambda: atualizar_porco(nome_baia, identificacao_entry.get()))
            #botão para chamada da função remover_baia
            remover_baia_button.configure(command=lambda: remover_baia(nome_baia, baia_listbox, arquivo_sem_extensao))
         
            porcos_text.config(state=tk.DISABLED)  # Desabilita a caixa de texto dos porcos

            # Lista os porcos da baia selecionada
            porcos = listar_porcos_baia(nome_baia)
            porcos_text.config(state=ctk.NORMAL)
            porcos_text.delete(1.0, ctk.END)
            if porcos: # Se houver porcos na baia, exibe-os na caixa de texto
                porcos_text.insert(ctk.END, "\n".join(porcos))
            else: # Se não houver porcos na baia, exibe uma mensagem
                porcos_text.insert(ctk.END, "Não há porcos nesta baia.")
            porcos_text.config(state=ctk.DISABLED)

# Cria os widgets da baia
    baia_frame = ctk.CTkFrame(root)
    baia_label = ctk.CTkLabel(baia_frame, text="Baia selecionada:", font=("Helvetica", 16))
    adicionar_porco_button = ctk.CTkButton(baia_frame, text="Adicionar Porco", font=("Helvetica", 14))
    infos_porco_button = ctk.CTkButton(baia_frame, text="Visualizar Porco", font=("Helvetica", 14))
    remover_porco_button = ctk.CTkButton(baia_frame, text="Remover Porco", font=("Helvetica", 14))
    atualizar_porco_button = ctk.CTkButton(baia_frame, text="Atualizar Porco", font=("Helvetica", 14))
    identificacao_entry = ctk.CTkEntry(baia_frame, font=("Helvetica", 12))  # Campo de entrada para a identificação do porco a ser removido
    porcos_text = scrolledtext.ScrolledText(baia_frame, state=tk.DISABLED, height=10, width=60, font=("Helvetica", 12), bg="#2B2B2B", fg="white")  # Caixa de texto para listar porcos
    remover_baia_button = ctk.CTkButton(baia_frame, text="Remover Baia", font=("Helvetica", 14))
    remover_baia_button.pack()

# Posiciona os widgets da baia
    baia_label.pack(pady=5)
    adicionar_porco_button.pack(pady=5)
    identificacao_entry.pack(pady=5)  # Adicionar o campo de entrada de identificação
    remover_porco_button.pack(pady=5)
    atualizar_porco_button.pack(pady=5)
    infos_porco_button.pack(pady=5)
    porcos_text.pack(pady=5)

# Cria os botões da janela principal
    adicionar_baia_button = ctk.CTkButton(root, text="Adicionar Baia", command=adicionar_baia, font=("Helvetica", 14))
    sair_button = ctk.CTkButton(root, text="Sair", command=root.destroy, font=("Helvetica", 14), fg_color="red")

    baia_listbox.pack(pady=5)
 
    adicionar_baia_button.pack(pady=5)
    sair_button.pack(pady=5)

    baia_listbox.bind("<<ListboxSelect>>", baia_selecionada_event)

    root.mainloop()

if __name__ == "__main__":
    main()
