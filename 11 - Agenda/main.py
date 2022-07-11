from tkinter import *

from model.model import BancoDeDados
from view.view import Interface
from controller.controller import Funcionalidades

class Agenda(Tk):
    def __init__(self):
        super().__init__()
        # configurações da janela
        largura, altura = 500, 450
        # pegando a resolução do sistema
        largura_so = self.winfo_screenwidth()
        altura_so = self.winfo_screenheight()
        # posição da janela
        posx = largura_so // 2 - largura // 2
        posy = altura_so // 2 - altura // 2
        self.geometry(f"{largura}x{altura}+{posx}+{posy}")
        self.title("")
        self.iconbitmap(r"img\icone.ico")
        self.resizable(FALSE, FALSE)
        
        model = BancoDeDados()
        view = Interface(self)
        view.place(relx=0, rely=0, relheight=1, relwidth=1)
        controller = Funcionalidades(view, model)

        view.set_controller(controller)


if __name__ == "__main__":
    agenda = Agenda()
    agenda.mainloop()
