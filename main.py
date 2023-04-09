import tkinter as tk


# iniciando ....
if __name__ == "__main__":

    screen = tk.Tk()
    screen.title("Gerenciador de Tarefas")

    # Widget para entrada de tarefa
    task_entry = tk.Entry(screen, width=50)
    task_entry.pack(padx=10, pady=10)

    # Botão para adicionar tarefa
    add_button = tk.Button(screen, text="Adicionar Tarefa")
    add_button.pack(padx=10, pady=5)

    # Botão para remover tarefa
    remove_button = tk.Button(screen, text="Remover Tarefa")
    remove_button.pack(padx=10, pady=5)

    # Lista de tarefas
    task_list = tk.Listbox(screen, height=15, width=50)
    task_list.pack(padx=10, pady=10)

    screen.mainloop()

# falta colocar os comandos e fazer com que armazene as tarefas 