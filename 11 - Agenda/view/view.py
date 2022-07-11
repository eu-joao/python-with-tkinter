from tkinter import *
from tkinter import ttk


class Interface(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        estilo = ttk.Style(self)
        estilo.theme_use('clam')

        # Título do programa
        self.frame1 = Frame(self, background="#FFDAB9", height=50, width=500)
        self.frame1.place(relx=0, rely=0)

        self.titulo = Label(self.frame1, text="Agenda de contatos",
                            font=("Tahoma", 23, "bold"), foreground="black",
                            background="#FFDAB9")
        self.titulo.place(relx=0.19, rely=0)

        # campos para preenchimento
        self.frame2 = Frame(self, background="#FFEFD5", height=150, width=500, 
                            highlightbackground="#f2c691", highlightcolor="#f2c691", 
                            highlightthickness=2)
        self.frame2.place(relx=0, rely=0.1)

        self.nomeLabel = Label(self.frame2, text="Nome",
                            font=("Arial", 12), foreground="black",
                            background="#FFEFD5")
        self.nomeLabel.place(relx=0.01, rely=0.1)

        self.nomeEntry = ttk.Entry(self.frame2, width=30)
        self.nomeEntry.place(relx=0.19, rely=0.1)

        self.sobrenomeLabel = Label(self.frame2, text="Sobrenome",
                            font=("Arial", 12), foreground="black",
                            background="#FFEFD5")
        self.sobrenomeLabel.place(relx=0.01, rely=0.3)

        self.sobrenomeEntry = ttk.Entry(self.frame2, width=30)
        self.sobrenomeEntry.place(relx=0.19, rely=0.3)

        self.numeroLabel = Label(self.frame2, text="Número",
                            font=("Arial", 12), foreground="black",
                            background="#FFEFD5")
        self.numeroLabel.place(relx=0.01, rely=0.5)

        self.numeroEntry = ttk.Entry(self.frame2, width=30)
        self.numeroEntry.place(relx=0.19, rely=0.5)

        self.emailLabel = Label(self.frame2, text="E-mail",
                            font=("Arial", 12), foreground="black",
                            background="#FFEFD5")
        self.emailLabel.place(relx=0.01, rely=0.7)

        self.emailEntry = ttk.Entry(self.frame2, width=30)
        self.emailEntry.place(relx=0.19, rely=0.7)

        self.bt_salvar = Button(self.frame2, text="SALVAR", command=self.salvar, background="#FFFACD",
                                 activebackground="#FFFACD", foreground="black",
                                 font=("arial", 10), activeforeground="black")
        self.bt_salvar.place(relx=0.58, rely=0.12, relheight=0.23, relwidth=0.19)

        self.bt_alterar = Button(self.frame2, text="ALTERAR",command=self.atualizar, background="#FFF0F5",
                                 activebackground="#FFF0F5", foreground="black",
                                 font=("arial", 10), activeforeground="black")
        self.bt_alterar.place(relx=0.58, rely=0.36, relheight=0.23, relwidth=0.19)

        self.bt_buscar = Button(self.frame2, text="BUSCAR", command=self.buscar, background="#E6E6FA",
                                 activebackground="#E6E6FA", foreground="black",
                                 font=("arial", 10), activeforeground="black")
        self.bt_buscar.place(relx=0.78, rely=0.12, relheight=0.23, relwidth=0.19)

        self.bt_excluir = Button(self.frame2, text="EXCLUIR", 
                                 command=self.excluir, background="#FFDAB9",
                                 activebackground="#FFDAB9", foreground="black",
                                 font=("arial", 10), activeforeground="black")
        self.bt_excluir.place(relx=0.78, rely=0.36, relheight=0.23, relwidth=0.19)

        self.labelParametro = Label(self.frame2, background="#FFEFD5", text="Buscar por:", font=("Arial", 9))
        self.parametro = ttk.Combobox(self.frame2, values=["nome", "sobrenome", "numero", "email"], width=16)

        self.labelParametro.place(relx=0.58, rely=0.7)
        self.parametro.place(relx=0.73, rely=0.7)

        self.tv = ttk.Treeview(self, height=3, column=("col1", "col2", "col3", "col4", "col5"), selectmode=EXTENDED)
        self.tv.heading('#0', text='')
        self.tv.heading('#1', text='ID')
        self.tv.heading('#2', text='Nome')
        self.tv.heading('#3', text='Sobrenome')
        self.tv.heading('#4', text='Número')
        self.tv.heading('#5', text='E-mail')

        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('#1', anchor=CENTER, minwidth=20, width=20, stretch=NO)
        self.tv.column('#2', anchor=CENTER, minwidth=110, width=110,stretch=NO)
        self.tv.column('#3', anchor=CENTER, minwidth=110, width=110,stretch=NO)
        self.tv.column('#4', anchor=CENTER, minwidth=92, width=92, stretch=NO)
        self.tv.column('#5', anchor=CENTER, minwidth=150, width=150,stretch=NO)

        # add scrollbar Y
        scrollbary = ttk.Scrollbar(self, orient=VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=scrollbary.set)
        scrollbary.place(relx=0.97, rely=0.43, relheight=0.54, relwidth=0.03)

        # add scrollbar X
        scrollbarx = ttk.Scrollbar(self, orient=HORIZONTAL, command=self.tv.xview)
        self.tv.configure(xscroll=scrollbarx.set)
        scrollbarx.place(relx=0, rely=0.97, relheight=0.03, relwidth=0.97)

        self.tv.bind("<Double-1>", self.OnDoubleClick)
        self.tv.place(relx=0, rely=0.43, relheight=0.54, relwidth=0.97)

    def OnDoubleClick(self, event):
        self.tv.selection()

        for n in self.tv.selection():
            col1, col2, col3, col4, col5 = self.tv.item(n, 'values')
            self.nomeEntry.insert(END, col2)
            self.sobrenomeEntry.insert(END, col3)
            self.numeroEntry.insert(END, col4)
            self.emailEntry.insert(END, col5)

    def set_controller(self, controller):
        self.controller = controller
    
    def salvar(self):
        if self.controller:
            self.controller.adicionar_contato()
    
    def atualizar(self):
        if self.controller:
            self.controller.atualizar_contato()
    def buscar(self):
        if self.controller:
            self.controller.buscar_contato()

    def excluir(self):
        if self.controller:
            self.controller.excluir_contato()
    