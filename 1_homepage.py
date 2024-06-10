import tkinter as tk # Importando o módulo tkinter para criar interfaces gráficas
from PIL import Image, ImageTk
import importlib.util

def redimensionar_imagem(image_path, new_width, new_height):
    """
    Redimensiona uma imagem para as novas dimensões especificadas.
    
    Args:
        image_path (str): O caminho para o arquivo da imagem.
        new_width (int): A largura desejada da imagem redimensionada.
        new_height (int): A altura desejada da imagem redimensionada.
    
    Returns:
        ImageTk.PhotoImage: A imagem redimensionada. 
    """

    # ^ Comentário especial chamado "docstring" usado normalmente em Python pra documentar funções, métodos, classes ou módulos. 
    # Recomendado o uso como boas práticas em Python pois, pode ser útil para quem estiver usando ou mantendo o código no futuro. 
    # Neste caso, essa docstring, está documentando a função 'redimensionar_imagem', onde ele descreve o propósito da função, 
    # além de fornecer informações sobre os argumentos que ela recebe, bem como sobre o que retorna.
    #-------------------\\-------------------



    # Abrindo a imagem usando a biblioteca PIL
    image = Image.open(image_path)
    
    # Redimensionando a imagem
    resized_image = image.resize((new_width, new_height), Image.BILINEAR)
    
    # Convertendo a imagem para um formato compatível com o tkinter
    photo_image = ImageTk.PhotoImage(resized_image)
    
    return photo_image

#-------------------\\-------------------
#Função realizar_login criada APÓS todo o layout da homepage
#Está função precisa ser revisada pois, no atual momento, estamos pré determinando o login e senha diretamente no código,
#precisará ser implementado um banco de dados onde permita o usuário criar o próprio login e senha.
#Feito desta maneira somente para testar a usabilidade e integração entre as páginas.


# Função para realizar o login
def realizar_login():
    # Obtendo o nome de usuário e senha digitados pelo usuário
    username = login_entry.get()
    password = senha_entry.get()

    # Verificando se o nome de usuário e senha estão corretos
    if username == "lema" and password == "1234":
        # Se estiverem corretos, abrir a segunda página
        abrir_segunda_pagina()
        # Fechando a janela de login
        root.withdraw()
    else:
        # Se estiverem incorretos, exibir uma mensagem de erro abaixo do botão Entrar
        mensagem_erro.config(text="Nome de usuário ou senha incorretos. Tente novamente.")

# Função para abrir a segunda página
def abrir_segunda_pagina():
    try:
        # Especificando o caminho exato para o arquivo 2_systempage.py (página principal do sistema)
        caminho_arquivo = "Python/BibliotecaLEMA/2_systempage.py"

        # Importando o arquivo 2_systempage.py 
        spec = importlib.util.spec_from_file_location("2_systempage", caminho_arquivo)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Chamando a função para abrir a segunda página
        module.abrir_janela_sistema()
    except FileNotFoundError:
        print("Arquivo 2_systempage.py não encontrado.")




#-------------------\\-------------------
# Criação da janela principal
root = tk.Tk()
root.title("Biblioteca LEMA")  

# Definição do tamanho da janela e centralização da mesma na tela do usuário
largura_janela = 500
altura_janela = 650
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
posicao_x = (largura_tela - largura_janela) // 2
posicao_y = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
root.resizable(False, False)  # Impede que a janela seja redimensionada (maximizada)

# Defina o fundo azul marinho para a janela
root.configure(bg="#001f3f") 

# Criação do frame para a borda esquerda
left_border_frame = tk.Frame(root, width=5, bg="white")
left_border_frame.pack(side="left", fill="y")

# Criação do frame para a borda direita
right_border_frame = tk.Frame(root, width=5, bg="white")
right_border_frame.pack(side="right", fill="y")

# Criação do frame para a borda inferior
bottom_border_frame = tk.Frame(root, height=5, bg="white")
bottom_border_frame.pack(side="bottom", fill="x")

# Criação do frame para a borda superior
top_border_frame = tk.Frame(root, height=5, bg="white")
top_border_frame.pack(side="top", fill="x")

#-------------------\\-------------------
# Redimensionando a imagem da Biblioteca LEMA
resized_image = redimensionar_imagem("Python/BibliotecaLEMA/logolemapng.png", 200, 125)

# Criação do Canvas para exibir a imagem acima do formulário de login
canvas_width = resized_image.width()  # Largura do Canvas
canvas_height = resized_image.height()  # Altura do Canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="#001f3f", highlightthickness=0)
canvas.pack(pady=(165, 0))  # Adiciona espaço entre o Canvas e o próximo elemento (X, Y onde X é parte superior e Y é parte inferior)

# Adição da imagem ao Canvas
canvas.create_image(canvas_width // 2, canvas_height // 2, image=resized_image)

#-------------------\\-------------------
# Criação do formulário de login
login_frame = tk.Frame(root, bg="white", bd=5, relief="ridge")
login_frame.pack(pady=20)  # Adiciona espaço entre o formulário e o próximo elemento

# Adição dos campos de login e senha
tk.Label(login_frame, text="Usuário:", bg="white").grid(row=0, column=0, padx=1, pady=5)
tk.Label(login_frame, text="Senha:", bg="white").grid(row=1, column=0, padx=1, pady=5)

# Adição dos campos de entrada para login e senha
login_entry = tk.Entry(login_frame)
login_entry.grid(row=0, column=1, padx=10, pady=5)  # Ajusta o preenchimento e o tamanho do campo de entrada

senha_entry = tk.Entry(login_frame, show="*")
senha_entry.grid(row=1, column=1, padx=10, pady=5)  # Ajusta o preenchimento e o tamanho do campo de entrada

#-------------------\\-------------------
# Criação do botão de login
login_button = tk.Button(root, text="Entrar", bg="#eead2d", fg="black", font=("Arial", 10), bd=3, padx=5, pady=2, command=realizar_login, cursor="hand2") 
login_button.pack(pady=(0, 5))  # Adiciona espaço abaixo do botão de login

#-------------------\\-------------------
# Rótulo para exibir mensagens de erro
mensagem_erro = tk.Label(root, text="", fg="white", bg = "#001f3f")
mensagem_erro.pack()

#-------------------\\-------------------
# Adição da marca d'água no canto inferior direito
marca_dagua_label = tk.Label(root, text="©️ Yuri Marques 2024", bg="#001f3f", fg="gray", font=("Arial", 8))
marca_dagua_label.place(relx=0.98, rely=0.99, anchor='se')

#-------------------\\-------------------
# Execução do loop principal da aplicação 
root.mainloop()
