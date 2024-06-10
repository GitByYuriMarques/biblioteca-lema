import tkinter as tk
from tkinter import ttk
from systempage import PaginaPrincipal
from cadastrolivrospage import PaginaCadastroLivros
from emprestimolivrospage import PaginaEmprestimoLivros
from devolucaolivrospage import PaginaDevolucaoLivros
from atendimentopage import PaginaAtendimento
from acervopage import PaginaAcervo
from infograficopage import PaginaInfografico
from cadastrousuariospage import PaginaCadastroUsuarios
from relatoriospage import PaginaRelatorios

class BibliotecaLEMA(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema Biblioteca LEMA")
        self.geometry("800x600")

        self.frames = {}

        pages = (
            PaginaPrincipal,
            PaginaCadastroLivros,
            PaginaEmprestimoLivros,
            PaginaDevolucaoLivros,
            PaginaAtendimento,
            PaginaAcervo,
            PaginaInfografico,
            PaginaCadastroUsuarios,
            PaginaRelatorios,
        )

        for F in pages:
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PaginaPrincipal")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = BibliotecaLEMA()
    app.mainloop()
