from tkinter import *

class Funcionalidades:
    def __init__(self, interface, banco):
        self.interface = interface
        self.banco = banco
        self.banco.criar_tabela()
        self.atualizar(self.banco.READ())

    def limpar_campos(self):
        self.interface.nomeEntry.delete(0, END)
        self.interface.sobrenomeEntry.delete(0, END)
        self.interface.numeroEntry.delete(0, END)
        self.interface.emailEntry.delete(0, END)
    
    def atualizar(self, lista):
        self.interface.tv.delete(*self.interface.tv.get_children())
        
        self.interface.tv.tag_configure("gray", background="#CCCCCC")
        self.interface.tv.tag_configure("white", background="#FFF")

        cor = ["gray", "white"]
        i = 2
    
        for v in lista:
            i=0 if i>1 else 1
            self.interface.tv.insert("", END, values=v, tags=(cor[i],))
            i += 1
        self.banco.desconectar()

    def adicionar_contato(self):
        self.banco.CREATE(self.interface.nomeEntry.get(), self.interface.sobrenomeEntry.get(), self.interface.numeroEntry.get(), self.interface.emailEntry.get())
        self.atualizar(self.banco.READ())
        self.limpar_campos()
    
    def atualizar_contato(self):
        self.banco.UPDATE(self.interface.tv.item(self.interface.tv.focus()), self.interface.nomeEntry.get(), self.interface.sobrenomeEntry.get(), self.interface.numeroEntry.get(), self.interface.emailEntry.get())
        self.atualizar(self.banco.READ())
        self.limpar_campos()
    
    def excluir_contato(self):
        self.banco.DELETE(self.interface.tv.item(self.interface.tv.focus()))
        self.atualizar(self.banco.READ())
    
    def buscar_contato(self):
        idx = self.interface.parametro.current()
        k = v = ""

        if idx == 0:
            v= self.interface.nomeEntry.get()
            k = self.interface.parametro.get()
        elif idx == 1:
            v= self.interface.sobrenomeEntry.get()
            k = self.interface.parametro.get()
        elif idx == 2:
            v= self.interface.numeroEntry.get()
            k = self.interface.parametro.get()
        elif idx == 3:
            v= self.interface.emailEntry.get()
            k = self.interface.parametro.get()
        
        self.atualizar(self.banco.SEARCH(k, v))

        self.limpar_campos()
        self.banco.desconectar()
