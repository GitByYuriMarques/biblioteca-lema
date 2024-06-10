import tkinter as tk  # Importa a biblioteca tkinter para criação da interface gráfica
from PIL import Image, ImageTk  # Importa a biblioteca PIL para manipulação de imagens
from tkinter import messagebox  # Importa a biblioteca messagebox para exibição de mensagens de diálogo
import os  # Importa a biblioteca os para interagir com o sistema operacional

# Lista fictícia de livros (substitua com a sua implementação real)
livros = ["Dom Quixote", "O Pequeno Príncipe", "1984", "Harry Potter", "A Revolução dos Bichos", "Cem Anos de Solidão"]

# Função para abrir a janela do sistema
def abrir_janela_sistema():
    global janela_sistema  # Declara a variável janela_sistema como global para ser acessível em outras funções
    janela_sistema = tk.Tk()  # Cria a janela principal
    janela_sistema.title("Biblioteca LEMA")  # Define o título da janela
    janela_sistema.configure(bg="#001f3f")  # Configura a cor de fundo da janela
    janela_sistema.state('zoomed')  # Define a janela para abrir em modo maximizado
    
    # Criação dos frames para as bordas da janela
    left_border_frame = tk.Frame(janela_sistema, width=5, bg="white")
    left_border_frame.pack(side="left", fill="y")
    
    right_border_frame = tk.Frame(janela_sistema, width=5, bg="white")
    right_border_frame.pack(side="right", fill="y")
    
    bottom_border_frame = tk.Frame(janela_sistema, height=5, bg="white")
    bottom_border_frame.pack(side="bottom", fill="x")
    
    top_border_frame = tk.Frame(janela_sistema, height=5, bg="white")
    top_border_frame.pack(side="top", fill="x")

    # Adicionando uma marca d'água no canto inferior direito da janela
    marca_dagua_label = tk.Label(janela_sistema, text="©️ Yuri Marques 2024", bg="#001f3f", fg="gray", font=("Arial", 8))
    marca_dagua_label.place(relx=0.99, rely=0.99, anchor='se')
    
    # Carregamento e exibição da imagem
    image = Image.open("Python/BibliotecaLEMA/logolemapng.png")  # Abre a imagem
    image = image.resize((250, 150))  # Redimensiona a imagem
    photo = ImageTk.PhotoImage(image)  # Converte a imagem para um formato compatível com tkinter
    image_label = tk.Label(janela_sistema, image=photo, bg="#001f3f")
    image_label.image = photo  # Armazena a referência da imagem para evitar coleta de lixo
    image_label.pack(pady=(90, 0))  # Adiciona a imagem à janela com um padding superior
    
    # Adicionando botões à janela
    adicionar_botoes(janela_sistema)

    # Adicionando campo de busca de livros
    search_frame = tk.Frame(janela_sistema, bg="#001f3f")
    search_frame.pack(pady=(70, 0))

    search_entry = tk.Entry(search_frame, font=("Arial", 10), fg="grey", width=30)
    search_entry.insert(0, "Buscar Livro")  # Insere o texto padrão no campo de busca
    search_entry.bind("<FocusIn>", lambda event: on_entry_click(event, search_entry))
    search_entry.bind("<FocusOut>", lambda event: on_focusout(event, search_entry))
    search_entry.bind("<KeyRelease>", lambda event: filtrar_livros(search_entry.get(), alfabeto_numeros, livros_listbox, inicio=False))
    search_entry.pack(side="left", padx=(0, 10))

    lupa_icon = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconelupa.png").subsample(1)
    search_button = tk.Label(search_frame, image=lupa_icon, bg="#001f3f", cursor="hand2")
    search_button.image = lupa_icon
    search_button.pack(side="left")
    search_button.bind("<Button-1>", lambda event: filtrar_livros(search_entry.get(), alfabeto_numeros, livros_listbox, inicio=False))

    # Adicionando alfabeto de A a Z e numerais de 0 a 9 como filtros
    filtro_frame = tk.Frame(janela_sistema, bg="#001f3f")
    filtro_frame.pack(pady=(10, 20))
    alfabeto_numeros = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for letra in alfabeto_numeros:
        filtro_button = tk.Label(filtro_frame, text=letra, font=("Arial", 10), bg="#001f3f", fg="white", cursor="hand2")
        filtro_button.pack(side="left", padx=(2, 2))
        filtro_button.bind("<Button-1>", lambda event, l=letra: filtrar_livros(l, alfabeto_numeros, livros_listbox, inicio=True))

    # Adicionando frame para exibição dos livros
    livros_frame = tk.Frame(janela_sistema, bg="#001f3f")
    livros_frame.pack(fill="both", expand=True)

    # Adicionando listbox para mostrar os livros
    global livros_listbox
    livros_listbox = tk.Listbox(livros_frame, bg="#001f3f", fg="white", font=("Arial", 10))
    livros_listbox.pack(side="left", fill="both", expand=True)

    # Adiciona os livros à listbox
    for livro in livros:
        livros_listbox.insert("end", livro)

# Função para adicionar os botões de logout
def adicionar_botoes(janela):
    logout_icon = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconedesligar.png").subsample(1)
    logout_button = tk.Label(janela, image=logout_icon, bd=0, bg="#001f3f", cursor="hand2")
    logout_button.image = logout_icon
    logout_button.place(relx=1.0, rely=0.0, x=-20, y=16, anchor='ne')
    logout_button.bind("<Button-1>", logout)

    settings_icon = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconeconfiguracoes.png").subsample(1)
    settings_button = tk.Label(janela, image=settings_icon, bd=0, bg="#001f3f", cursor="hand2")
    settings_button.image = settings_icon
    settings_button.place(relx=1.0, rely=0.0, x=-75, y=15, anchor='ne')

    home_icon = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconehome.png").subsample(1)
    home_button = tk.Label(janela, image=home_icon, bd=0, bg="#001f3f", cursor="hand2")
    home_button.image = home_icon
    home_button.place(relx=1.0, rely=0.0, x=-143, y=15, anchor='ne')
    home_button.bind("<Button-1>", abrir_pagina_principal)  # Vincula o botão Home/Início à função abrir_pagina_principal

# Função para abrir a página principal
def abrir_pagina_principal(event):
    os.system("python Python/BibliotecaLEMA/2_systempage.py")  # Executa o script da página principal

# Função para realizar o logout ao apertar o botão
def logout(event):
    if messagebox.askokcancel("Logout", "Tem certeza que deseja sair?"):  # Exibe uma mensagem de confirmação
        janela_sistema.destroy()  # Fecha a janela

# Função para filtrar os livros com base na letra ou palavra-chave digitada
def filtrar_livros(filtro, alfabeto_numeros, livros_listbox, inicio):
    global livros
    livros_listbox.delete(0, "end")  # Limpa a listbox antes de adicionar os livros filtrados
    if inicio:
        # Filtra livros que começam com a letra ou número
        for livro in livros:
            if livro.lower().startswith(filtro.lower()):
                livros_listbox.insert("end", livro)
    else:
        # Filtra livros que contêm a palavra-chave em qualquer parte do título
        for livro in livros:
            if filtro.lower() in livro.lower():
                livros_listbox.insert("end", livro)

# Função para lidar com o clique no campo de busca
def on_entry_click(event, entry):
    if entry.get() == "Buscar Livro":
        entry.delete(0, "end")  # Remove o texto padrão
        entry.insert(0, "")  # Insere um texto vazio
        entry.config(fg="black")  # Altera a cor do texto para preto

# Função para lidar com a saída do foco do campo de busca
def on_focusout(event, entry):
    if entry.get() == "":
        entry.insert(0, "Buscar Livro")  # Reinsere o texto padrão
        entry.config(fg="grey")  # Altera a cor do texto para cinza

# Seção principal para abrir a janela do sistema
if __name__ == "__main__":
    abrir_janela_sistema()  # Abre a janela do sistema
    janela_sistema.mainloop()  # Inicia o loop
