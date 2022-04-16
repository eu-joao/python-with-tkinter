from tkinter import *
from tkinter import ttk

import os

# Configurações da Janela
janela = Tk()
largura, altura = 360, 400
# pegando a resolução do sistema
largura_SO = janela.winfo_screenwidth()
altura_SO = janela.winfo_screenheight()
# posição da janela
posx = largura_SO // 2 - largura // 2
posy = altura_SO // 2 - altura // 2
janela.geometry(f'{largura}x{altura}+{posx}+{posy}')
janela.title('')
janela.resizable(False, False)
janela.configure(background='white')
janela.iconbitmap(r'03 - PC Tools\imagens\12.ico')

# imagens
img1 = PhotoImage(file=r'03 - PC Tools\imagens\1.png')
img2 = PhotoImage(file=r'03 - PC Tools\imagens\2.png')
img3 = PhotoImage(file=r'03 - PC Tools\imagens\3.png')
img4 = PhotoImage(file=r'03 - PC Tools\imagens\4.png')
img5 = PhotoImage(file=r'03 - PC Tools\imagens\5.png')
img6 = PhotoImage(file=r'03 - PC Tools\imagens\6.png')
img7 = PhotoImage(file=r'03 - PC Tools\imagens\7.png')
img8 = PhotoImage(file=r'03 - PC Tools\imagens\8.png')
img9 = PhotoImage(file=r'03 - PC Tools\imagens\9.png')
img10 = PhotoImage(file=r'03 - PC Tools\imagens\10.png')
img11 = PhotoImage(file=r'03 - PC Tools\imagens\11.png')

# título da janela
janela_titulo = Label(janela,
                      text='PC Tools',
                      image=img11,
                      font=('Tahoma', 35, 'bold'),
                      bg='white',
                      compound=LEFT,
                      fg='black')
janela_titulo.pack()

# estilo
estilo = ttk.Style()
estilo.configure('my.TButton',
                 font=('Arial', 10, 'bold'),
                 anchor=W,
                 width=18)

# Botões
bt1 = ttk.Button(janela,
                 text='Gerenciador de\ndispositivos',
                 image=img1,
                 compound=LEFT,
                 style='my.TButton',
                 command=lambda: os.system('devmgmt.msc'))

bt2 = ttk.Button(janela,
                 text='Propriedades do\nsistema',
                 image=img2,
                 compound=LEFT,
                 style='my.TButton',
                 command=lambda: os.system('sysdm.cpl'))

bt3 = ttk.Button(janela,
                 text='Desligar',
                 image=img3,
                 compound=LEFT,
                 style='my.TButton',
                 command=lambda: os.system('Shutdown.exe -s -t 00'))

bt4 = ttk.Button(janela,
                 text='Configurações de\nrede',
                 image=img4,
                 compound=LEFT,
                 style='my.TButton',
                 command=lambda: os.system('ncpa.cpl'))

bt5 = ttk.Button(janela,
                 text='Serviços do sistema',
                 image=img5,
                 compound=LEFT,
                 style='my.TButton',
                 command=lambda: os.system('services.msc'))

bt6 = ttk.Button(janela,
                 text='Gerenciador de\ntarefas',
                 image=img6,
                 compound=LEFT,
                 style='my.TButton',
                 command=lambda: os.system('Taskmgr'))

bt7 = ttk.Button(janela,
                 text='Reiniciar',
                 image=img7,
                 compound=LEFT,
                 style='my.TButton',
                 command=lambda: os.system('Shutdown.exe -r -t 00'))

bt8 = ttk.Button(janela,
                 text='Painel de controle',
                 image=img8,
                 compound=LEFT,
                 style='my.TButton',
                 command=lambda: os.system('control'))

bt9 = ttk.Button(janela,
                 text='Editor do registro',
                 image=img9,
                 compound=LEFT,
                 style='my.TButton',
                 command=lambda: os.system('regedit'))

bt10 = ttk.Button(janela,
                  text='Saúde da memória',
                  image=img10,
                  compound=LEFT,
                  style='my.TButton',
                  command=lambda: os.system('MdSched'))

# Posição dos botões
# Botões ímpares
bt1.place(relx=0.01, rely=0.27, relwidth=0.49, relheight=0.14)
bt3.place(relx=0.01, rely=0.41, relwidth=0.49, relheight=0.14)
bt5.place(relx=0.01, rely=0.55, relwidth=0.49, relheight=0.14)
bt7.place(relx=0.01, rely=0.69, relwidth=0.49, relheight=0.14)
bt9.place(relx=0.01, rely=0.83, relwidth=0.49, relheight=0.14)
# Botões pares
bt2.place(relx=0.5, rely=0.27, relwidth=0.49, relheight=0.14)
bt4.place(relx=0.5, rely=0.41, relwidth=0.49, relheight=0.14)
bt6.place(relx=0.5, rely=0.55, relwidth=0.49, relheight=0.14)
bt8.place(relx=0.5, rely=0.69, relwidth=0.49, relheight=0.14)
bt10.place(relx=0.5, rely=0.83, relwidth=0.49, relheight=0.14)

janela.mainloop()

