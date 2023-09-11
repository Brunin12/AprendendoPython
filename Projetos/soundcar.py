import tkinter as tk
import sqlite3
import base64

def base_64(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

# Função para salvar as informações do cliente no banco de dados
def salvar_cliente(nome, email, senha, aparelho):
    # Conexão com o banco de dados
    conexao = sqlite3.connect('python_clientes.db')
    cursor = conexao.cursor()

    # Inserção dos dados na tabela clientes
    cursor.execute('INSERT INTO clientes VALUES (?, ?, ?, ?)', (nome, email, senha, aparelho))

    # Commit da transação
    conexao.commit()

    # Fechamento da conexão com o banco de dados
    conexao.close()

# Função para limpar os campos do formulário
def limpar_campos():
    nome_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    senha_entry.delete(0, tk.END)
    aparelho_entry.delete(0, tk.END)

# Função para coletar as informações do formulário e salvá-las no banco de dados
def salvar_formulario():
    nome = nome_entry.get()
    email = email_entry.get()
    senha = base_64(senha_entry.get())
    aparelho = aparelho_entry.get()

    salvar_cliente(nome, email, senha, aparelho)
    limpar_campos()

# Criação da janela principal
janela = tk.Tk()
janela.title('Cadastro de Clientes')

# Criação do formulário
tk.Label(janela, text='Nome:').grid(row=0, column=0)
nome_entry = tk.Entry(janela)
nome_entry.grid(row=0, column=1)

tk.Label(janela, text='E-mail:').grid(row=1, column=0)
email_entry = tk.Entry(janela)
email_entry.grid(row=1, column=1)

tk.Label(janela, text='Senha:').grid(row=2, column=0)
senha_entry = tk.Entry(janela, show='*')
senha_entry.grid(row=2, column=1)

tk.Label(janela, text='Aparelho:').grid(row=3, column=0)
aparelho_entry = tk.Entry(janela)
aparelho_entry.grid(row=3, column=1)

salvar_button = tk.Button(janela, text='Salvar', command=salvar_formulario)
salvar_button.grid(row=4, column=1)

# Iniciação do loop principal da janela
janela.mainloop()
