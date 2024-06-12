import tkinter as tk  # Importando o módulo tkinter para criar interfaces gráficas
from PIL import Image, ImageTk  # Importando os módulos Image e ImageTk do Pillow para trabalhar com imagens
from tkinter import messagebox  # Adicionando esta linha para importar messagebox separadamente

# Executando a função de abrir a janela do sistema baseado no login da página principal
def abrir_janela_sistema():
    global janela_sistema  # Declarando a janela_sistema como uma variável global para ser acessível em outras funções
    janela_sistema = tk.Tk()  # Criando uma nova janela
    janela_sistema.title("Biblioteca LEMA")  # Título da janela
    janela_sistema.configure(bg="#001f3f")  # Cor de fundo da janela
    janela_sistema.state('zoomed')  # Faz abrir a janela de forma maximizada
    
    #-------------------\\-------------------
    # Criando frames para a borda esquerda da janela
    left_border_frame = tk.Frame(janela_sistema, width=5, bg="white")
    left_border_frame.pack(side="left", fill="y")
    
    # Criando frames para a borda direita da janela
    right_border_frame = tk.Frame(janela_sistema, width=5, bg="white")
    right_border_frame.pack(side="right", fill="y")
    
    # Criando frames para a borda inferior da janela
    bottom_border_frame = tk.Frame(janela_sistema, height=5, bg="white")
    bottom_border_frame.pack(side="bottom", fill="x")
    
    # Criando frames para a borda superior da janela
    top_border_frame = tk.Frame(janela_sistema, height=5, bg="white")
    top_border_frame.pack(side="top", fill="x")

    # Adicionando uma marca d'água no canto inferior direito da janela
    marca_dagua_label = tk.Label(janela_sistema, text="©️ Yuri Marques 2024", bg="#001f3f", fg="gray", font=("Arial", 8))
    marca_dagua_label.place(relx=0.99, rely=0.99, anchor='se')
    
    #-------------------\\-------------------
    # Carregando a imagem
    image = Image.open("Python/BibliotecaLEMA/logolemapng.png")

    # Redimensionando a imagem para ALTURAxLARGURA pixels
    image = image.resize((250, 150))

    # Convertendo a imagem para um formato compatível com o tkinter
    photo = ImageTk.PhotoImage(image)

    # Exibindo a imagem centralizada abaixo do texto
    image_label = tk.Label(janela_sistema, image=photo, bg="#001f3f")
    image_label.image = photo  # Mantenha uma referência à imagem para evitar que seja coletada pelo garbage collector
    image_label.pack(pady=(90, 0)) # onde 0 é o espaço ACIMA da imagem e 10 é o espaço ABAIXO da imagem
    
    #-------------------\\-------------------
    # Adicionando os campos de cadastro de usuário
    adicionar_campos_cadastro(janela_sistema)
    
    #-------------------\\-------------------
    # Adicionando botões LOGOUT e CONFIGURAÇÕES à janela
    adicionar_botoes(janela_sistema)

#-------------------\\-------------------
# Função para realizar o logout ao apertar o botão
def logout(janela):
    if messagebox.askokcancel("Logout", "Tem certeza que deseja sair?"):
        janela.destroy()  # Fecha o sistema quando o usuário confirma o logout

#-------------------\\-------------------
# Função para ir até a página de configurações ao apertar o botão
def abrir_pagina_configuracoes():
    print("Abrir página de configurações")  # Vamos modificar depois quando criar a página de configurações, por enquanto, só irá imprimir uma mensagem

#-------------------\\-------------------
def adicionar_botoes(janela):
    # Função para adicionar o botão de logout à janela
    logout_icon = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconedesligar.png").subsample(1)  # Imagem do botão de logout
    logout_button = tk.Button(janela, image=logout_icon, command=lambda: logout(janela_sistema), bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")  # Criando o botão de logout
    logout_button.image = logout_icon  # Definindo a imagem do botão
    logout_button.place(relx=1.0, rely=0.0, x=-20, y=16, anchor='ne')  # Posicionando o botão no topo superior direito

    # Função para adicionar o botão de configurações à janela
    settings_icon = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconeconfiguracoes.png").subsample(1)  # Imagem do botão de configurações
    settings_button = tk.Button(janela, image=settings_icon, command=abrir_pagina_configuracoes, bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")  # Criando o botão de configurações
    settings_button.image = settings_icon  # Definindo a imagem do botão
    settings_button.place(relx=1.0, rely=0.0, x=-75, y=15, anchor='ne')  # Posicionando o botão ao lado do botão de logout
    
    # Função para adicionar o botão de início à janela
    home_icon = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconehome.png").subsample(1)  # Imagem do botão de início
    home_button = tk.Button(janela, image=home_icon, command=abrir_pagina_configuracoes, bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")  # Criando o botão de início
    home_button.image = home_icon  # Definindo a imagem do botão
    home_button.place(relx=1.0, rely=0.0, x=-143, y=15, anchor='ne')  # Posicionando o botão ao lado do botão de logout

#-------------------\\-------------------
# Função para adicionar campos de cadastro de usuário à janela
def adicionar_campos_cadastro(janela):
    frame_cadastro = tk.Frame(janela, bg="#001f3f")
    frame_cadastro.pack(pady=(90, 0))
    
    # Título do box
    title_label = tk.Label(frame_cadastro, text="Cadastro de Usuários", font=("Arial", 14, "bold"), fg="white", bg="#001f3f")
    title_label.pack(pady=(10, 20))

    # Subframe para os campos de cadastro
    subframe_cadastro = tk.Frame(frame_cadastro, bg="#001f3f")
    subframe_cadastro.pack(padx=20, pady=10)

    # Labels e entries
    labels_texts = ["Nome:", "RG:", "Matrícula:", "Curso:", "E-mail:", "Telefone:"]
    labels_entries = []

    for i, text in enumerate(labels_texts):
        label = tk.Label(subframe_cadastro, text=text, font=("Arial", 11), fg="white", bg="#001f3f", anchor='w') #Configura os títulos dos campos
        entry = tk.Entry(subframe_cadastro, font=("Arial", 11), width=40) #Configura o box de preenchimento
        labels_entries.append((label, entry))
        label.grid(row=(i//2)*2, column=i%2, sticky='w', padx=(10, 10), pady=(5, 0))
        entry.grid(row=(i//2)*2+1, column=i%2, pady=(0, 5), padx=(10, 10))
    
    # Adicionando botão de submissão
    submit_button = tk.Button(frame_cadastro, text="Cadastrar", font=("Arial", 10), bg="white", fg="#001f3f", command=submit_cadastro)
    submit_button.pack(pady=(20, 10))

#-------------------\\-------------------
# Função de submissão de cadastro (exemplo simples)
def submit_cadastro():
    messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")

#-------------------\\-------------------
if __name__ == "__main__":
    abrir_janela_sistema()  # Chamando a função para abrir a janela do sistema quando o código é executado
    janela_sistema.mainloop()  # Adicionando o loop principal do tkinter
