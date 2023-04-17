import tkinter as tk
import os
from tkinter import messagebox as msb


# simplificar a chamada do arquivo
def arquivo_txt(comando):
   return open('Gerenciador-de-tarefas/tarefas.txt' , comando) 
        
   

def adiciona():
    # Obtém a tarefa digitada na entrada de texto
    tarefa = tarefa_entry.get()
    with arquivo_txt('a+') as lista :
        lista.write('\n' + tarefa) 
    
    # Adiciona a tarefa à lista de tarefas
    tarefa_list.insert(tk.END, tarefa)
    
    # Limpa o conteúdo da entrada de texto
    tarefa_entry.delete(0, tk.END)


def remove():
    # Obtém o índice do item selecionado na lista de tarefas
    seleciona_idx = tarefa_list.curselection()
    
    # ler o arquivo e o reescreve sem a linha apagada  
    with arquivo_txt('r') as arquivo :
        linhas = arquivo.readlines()
    with arquivo_txt('w') as arquivo :
        for i , id in enumerate(linhas , 1):
            if i != seleciona_idx[0] + 1 :
                arquivo.write(id)
    
    # Remove o item selecionado da lista de tarefas
    tarefa_list.delete(seleciona_idx)


def tarefa_feita():
    # Obtém o índice do item selecionado na lista de tarefas
    seleciona_idx = tarefa_list.curselection()
    
    # Obtém o texto do item selecionado
    seleciona_tarefa = tarefa_list.get(seleciona_idx)
    
    # Adiciona "feito" ao início do texto do item selecionado
    seleciona_tarefa = "feito - " + seleciona_tarefa
    
    # Atualiza o item selecionado na lista de tarefas
    tarefa_list.delete(seleciona_idx)
    tarefa_list.insert(seleciona_idx, seleciona_tarefa)
    
    with arquivo_txt('r') as arquivo :
        linhas = arquivo.readlines()
    with arquivo_txt('w') as arquivo :
        for i , id in enumerate(linhas , 1):
            if i != seleciona_idx[0] + 1:
                arquivo.write(id)
            else:
                arquivo.write(seleciona_tarefa)
                
    # Limpa a seleção na lista de tarefas
    tarefa_list.selection_clear(0, tk.END)


# iniciando ....
if __name__ == "__main__":
     # verifica se o arquivo existe , se não ele cria 
    try: 
        if os.path.exists('Gerenciador-de-tarefas/tarefas.txt'):
            with arquivo_txt('r') as arquivo:
                conteudos = arquivo.readlines()
                  
        else :
            with arquivo_txt('w') as arquivo :
                arquivo.write('== TAREFAS ==')
                conteudos = []
                
        screen = tk.Tk()
        # titulo 
        screen.title("Gerenciador de Tarefas")
        # define a cor de fundo
        screen.configure(bg="gray")
        # coloca o icone da janela
        # screen.iconbitmap("imagem.png") no meu tem que colocar todo o caminho então dixei assim 

        # Widget para entrada de tarefa
        tarefa_entry = tk.Entry(screen, width=50)
        tarefa_entry.pack(padx=10, pady=10)
        
        
        # Frame e para alinhar os botões horizontalmente
        frame = tk.Frame(screen)
        frame.configure(bg='gray')
        frame.pack()

        # Botão para adicionar tarefa
        add_button = tk.Button(frame, text="Adicionar Tarefa" , command=adiciona)
        add_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Botão para remover tarefa
        remove_button = tk.Button(frame, text="Remover Tarefa" , command=remove)
        remove_button.pack(side= tk.LEFT, padx=10, pady=5)

        # Botão para tarefa feita
        remove_button = tk.Button(screen, text="Tarefa Feita" , command=tarefa_feita)
        remove_button.pack(padx=10, pady=5)
        
        # Lista de tarefas
        tarefa_list = tk.Listbox(screen, height=15, width=50)
        for conteudo in conteudos :
            tarefa_list.insert(tk.END, conteudo)
            
        tarefa_list.pack(padx=10, pady=10)
        
        screen.mainloop()    
    
    # caso de erro ao ler o arquivo 
    except IOError as erro:
        msb.showerror('Erro ao abrir o arquivo !')    
        
   

