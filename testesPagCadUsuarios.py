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
    # Adicionando botões LOGOUT e CONFIGURAÇÕES à janela
    adicionar_botoes(janela_sistema)

    # Adicionando botões com ícones abaixo do campo de busca
    buttons_frame = tk.Frame(janela_sistema, bg="#001f3f")
    buttons_frame.pack(pady=(100, 0))

    # Botão cadastro de livro e legenda
    frame1 = tk.Frame(buttons_frame, bg="#001f3f")
    frame1.pack(side="left", padx=60)
    icon1 = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconecadastrolivros.png").subsample(1)
    button1 = tk.Button(frame1, image=icon1, command=lambda: print("Botão 1 clicado"), bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")
    button1.image = icon1
    button1.pack()
    label1 = tk.Label(frame1, text="Cadastro de livro", font=("Arial", 10), fg="white", bg="#001f3f")
    label1.pack()

    # Botão emprestimo de livro e legenda
    frame2 = tk.Frame(buttons_frame, bg="#001f3f")
    frame2.pack(side="left", padx=60)
    icon2 = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconeemprestimo.png").subsample(1)
    button2 = tk.Button(frame2, image=icon2, command=lambda: print("Botão 2 clicado"), bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")
    button2.image = icon2
    button2.pack()
    label2 = tk.Label(frame2, text="Empréstimo de livro", font=("Arial", 10), fg="white", bg="#001f3f")
    label2.pack()

    # Botão devolucao de livro e legenda
    frame3 = tk.Frame(buttons_frame, bg="#001f3f")
    frame3.pack(side="left", padx=60)
    icon3 = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconedevolucao.png").subsample(1)
    button3 = tk.Button(frame3, image=icon3, command=lambda: print("Botão 3 clicado"), bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")
    button3.image = icon3
    button3.pack()
    label3 = tk.Label(frame3, text="Devolução de livro", font=("Arial", 10), fg="white", bg="#001f3f")
    label3.pack()

    # Botão atendimento e legenda
    frame4 = tk.Frame(buttons_frame, bg="#001f3f")
    frame4.pack(side="left", padx=60)
    icon4 = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconeatendimento.png").subsample(1)
    button4 = tk.Button(frame4, image=icon4, command=lambda: print("Botão 4 clicado"), bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")
    button4.image = icon4
    button4.pack()
    label4 = tk.Label(frame4, text="Atendimento", font=("Arial", 10), fg="white", bg="#001f3f")
    label4.pack()

    # Frame para os botões da fileira de baixo
    buttons_frame_below = tk.Frame(janela_sistema, bg="#001f3f")
    buttons_frame_below.pack(pady=(100, 0))

    # Botão biblioteca e legenda
    frame5 = tk.Frame(buttons_frame_below, bg="#001f3f")
    frame5.pack(side="left", padx=60)
    icon5 = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconebiblioteca.png").subsample(1)
    button5 = tk.Button(frame5, image=icon5, command=abrir_janela_acervo, bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")
    button5.image = icon5
    button5.pack()
    label5 = tk.Label(frame5, text="Acervo de livros", font=("Arial", 10), fg="white", bg="#001f3f")
    label5.pack()

    # Botão infográfico e legenda
    frame6 = tk.Frame(buttons_frame_below, bg="#001f3f")
    frame6.pack(side="left", padx=60)
    icon6 = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconeinfografico.png").subsample(1)
    button6 = tk.Button(frame6, image=icon6, command=lambda: print("Botão 6 clicado"), bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")
    button6.image = icon6
    button6.pack()
    label6 = tk.Label(frame6, text="Infográfico bibliotecário", font=("Arial", 10), fg="white", bg="#001f3f")
    label6.pack()

    # Botão cadastros e legenda
    frame7 = tk.Frame(buttons_frame_below, bg="#001f3f")
    frame7.pack(side="left", padx=60)
    icon7 = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconecadastros.png").subsample(1)
    button7 = tk.Button(frame7, image=icon7, command=abrir_janela_cadastro_usuarios, bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")
    button7.image = icon7
    button7.pack()
    label7 = tk.Label(frame7, text="Cadastros de usuários", font=("Arial", 10), fg="white", bg="#001f3f")
    label7.pack()

    # Botão relatórios e legenda
    frame8 = tk.Frame(buttons_frame_below, bg="#001f3f")
    frame8.pack(side="left", padx=60)
    icon8 = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconerelatorios.png").subsample(1)
    button8 = tk.Button(frame8, image=icon8, command=lambda: print("Botão 8 clicado"), bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")
    button8.image = icon8
    button8.pack()
    label8 = tk.Label(frame8, text="Relatórios", font=("Arial", 10), fg="white", bg="#001f3f")
    label8.pack()

    # Botão do usuário e legenda
    frame9 = tk.Frame(buttons_frame_below, bg="#001f3f")
    frame9.pack(side="left", padx=60)
    icon9 = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconeusuario.png").subsample(1)
    button9 = tk.Button(frame9, image=icon9, command=lambda: print("Botão 9 clicado"), bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")
    button9.image = icon9
    button9.pack()
    label9 = tk.Label(frame9, text="Usuário", font=("Arial", 10), fg="white", bg="#001f3f")
    label9.pack()

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

    # Função para adicionar o botão de configurações à janela
    settings_icon = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconehome.png").subsample(1)  # Imagem do botão de início
    settings_button = tk.Button(janela, image=settings_icon, command=abrir_pagina_configuracoes, bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")  # Criando o botão de início
    settings_button.image = settings_icon  # Definindo a imagem do botão
    settings_button.place(relx=1.0, rely=0.0, x=-143, y=15, anchor='ne')  # Posicionando o botão ao lado do botão de logout

    # subsample()= reduz a imagem, quanto maior o número, menor a imagem em relação ao tamanho original   
    # relx= Posiciona o botão na extrema direita
    # rely= Posiciona o botão no topo
    # x= Ajusta a posição para esquerda
    # y= Ajusta a posição para baixo
    # anchor= 'ne' usa o canto superior direito do botão como ponto de ancoragem

#-------------------\\-------------------
# Função para abrir a janela de acervo
def abrir_janela_acervo():
    global janela_acervo  # Declarando a janela_acervo como uma variável global para ser acessível em outras funções
    janela_sistema.withdraw()  # Esconde a janela principal
    janela_acervo = tk.Toplevel()  # Cria uma nova janela
    janela_acervo.title("Acervo de Livros")  # Título da janela de acervo
    janela_acervo.configure(bg="#001f3f")  # Cor de fundo da janela
    janela_acervo.state('zoomed')  # Faz abrir a janela de forma maximizada

    # Adicionando uma marca d'água no canto inferior direito da janela
    marca_dagua_label = tk.Label(janela_acervo, text="©️ Yuri Marques 2024", bg="#001f3f", fg="gray", font=("Arial", 8))
    marca_dagua_label.place(relx=0.99, rely=0.99, anchor='se')
    
    # Exemplo de conteúdo na janela de acervo
    label = tk.Label(janela_acervo, text="Bem-vindo ao Acervo de Livros!", font=("Arial", 12), fg="white", bg="#001f3f")
    label.pack(pady=(20, 0))  # onde 0 é o espaço ACIMA do texto e 10 é o espaço ABAIXO do texto

    # Botão Home para voltar à janela principal
    settings_icon = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconehome.png").subsample(1)  # Imagem do botão de início
    settings_button = tk.Button(janela_acervo, image=settings_icon, command=voltar_janela_principal, bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")  # Criando o botão de início
    settings_button.image = settings_icon  # Definindo a imagem do botão
    settings_button.place(relx=1.0, rely=0.0, x=-143, y=15, anchor='ne')  # Posicionando o botão ao lado do botão de logout

#-------------------\\-------------------
def voltar_janela_principal():
    janela_acervo.withdraw()  # Esconde a janela de acervo
    janela_sistema.deiconify()  # Mostra a janela principal

#-------------------\\-------------------
# Função para abrir a janela de cadastro de usuários
def abrir_janela_cadastro_usuarios():
    global janela_cadastro_usuarios  # Declarando a janela_cadastro_usuarios como uma variável global para ser acessível em outras funções
    janela_sistema.withdraw()  # Esconde a janela principal
    janela_cadastro_usuarios = tk.Toplevel()  # Cria uma nova janela
    janela_cadastro_usuarios.title("Cadastro de Usuários")  # Título da janela de cadastro de usuários
    janela_cadastro_usuarios.configure(bg="#001f3f")  # Cor de fundo da janela
    janela_cadastro_usuarios.state('zoomed')  # Faz abrir a janela de forma maximizada

    # Adicionando uma marca d'água no canto inferior direito da janela
    marca_dagua_label = tk.Label(janela_cadastro_usuarios, text="©️ Yuri Marques 2024", bg="#001f3f", fg="gray", font=("Arial", 8))
    marca_dagua_label.place(relx=0.99, rely=0.99, anchor='se')

    # Título da página de cadastro
    label = tk.Label(janela_cadastro_usuarios, text="Cadastro de Usuários", font=("Arial", 20), fg="white", bg="#001f3f")
    label.pack(pady=(20, 20))

    # Frame para conter os campos de cadastro
    frame_cadastro = tk.Frame(janela_cadastro_usuarios, bg="#001f3f")
    frame_cadastro.pack(pady=20)

    # Campos de entrada para o cadastro de usuários
    labels = ["Nome Completo", "Data de Nascimento", "CPF", "Email", "Telefone", "Endereço"]
    entries = []

    for label_text in labels:
        label = tk.Label(frame_cadastro, text=label_text, font=("Arial", 12), fg="white", bg="#001f3f")
        label.pack(anchor="w")
        entry = tk.Entry(frame_cadastro, width=40)
        entry.pack(pady=5)
        entries.append(entry)

    # Botão para salvar o cadastro
    button_salvar = tk.Button(frame_cadastro, text="Salvar", font=("Arial", 12), bg="white", fg="#001f3f", command=lambda: salvar_cadastro(entries))
    button_salvar.pack(pady=20)

    # Botão Home para voltar à janela principal
    settings_icon = tk.PhotoImage(file="Python/BibliotecaLEMA/icones/iconehome.png").subsample(1)  # Imagem do botão de início
    settings_button = tk.Button(janela_cadastro_usuarios, image=settings_icon, command=voltar_janela_principal, bd=0, bg="#001f3f", activebackground="#001f3f", cursor="hand2")  # Criando o botão de início
    settings_button.image = settings_icon  # Definindo a imagem do botão
    settings_button.place(relx=1.0, rely=0.0, x=-143, y=15, anchor='ne')  # Posicionando o botão ao lado do botão de logout

#-------------------\\-------------------
# Função para salvar o cadastro de usuários (simulada)
def salvar_cadastro(entries):
    dados = {entry.get() for entry in entries}  # Obtendo os valores de todos os campos
    print("Dados salvos:", dados)  # Imprimindo os dados no console (simulação)
    messagebox.showinfo("Cadastro", "Cadastro salvo com sucesso!")  # Exibindo uma mensagem de sucesso

#-------------------\\-------------------
if __name__ == "__main__":
    abrir_janela_sistema()  # Chamando a função para abrir a janela do sistema quando o código é executado
    janela_sistema.mainloop()  # Adicionando o loop principal do tkinter
