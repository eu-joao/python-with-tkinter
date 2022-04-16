from tkinter import *

import random

janela = Tk()
janela.title('Gerador de Senhas')
# dimensões da janela
largura, altura = 400, 650
# pegando a resolução do sistema
largura_so = janela.winfo_screenwidth()
altura_so = janela.winfo_screenheight()
# posição da janela
posx = largura_so // 2 - largura // 2
posy = altura_so // 2 - altura // 2
janela.resizable(False, False)
janela.geometry(f'{largura}x{altura}+{posx}+{posy}')
janela.iconbitmap('06 - Gerador de Senhas\imagens\key.ico')
janela.configure(background='white')


def senha():
    minusculo = 'abcdefghijklmnopqrstuvwxyz'
    maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'
    simbolos = '!@#$%&*()-+.,;?{[}]^><:'

    qtd = int(tam.get())
    tudo = senha = ''

    if (Check1.get()):
        tudo += maiusculo
    if (Check2.get()):
        tudo += minusculo
    if (Check3.get()):
        tudo += numeros
    if (Check4.get()):
        tudo += simbolos

    senha = ''.join(random.sample(tudo, qtd))

    mostrar_senha.configure(text=senha)


def copiar():
    janela.clipboard_clear()
    janela.clipboard_append(str(senha))


# carregando a logo
logo = PhotoImage(file='06 - Gerador de Senhas\imagens\logo.png')
img = Label(janela, image=logo, bg='white')
img.pack()

op = Label(text='OPÇÕES',
           font=('Arial', 12, 'bold'),
           fg='white',
           bg='black',
           relief='solid',
           width=38)

txt1 = Label(janela,
             text='Tamanho da senha:',
             bg='white',
             fg='black',
             font=('Arial', 12, 'bold'))

tam = Spinbox(janela,
              from_=1,
              to=20,
              bg='white',
              fg='black',
              font=('Arial', 12))

txt2 = Label(janela,
             text='Incluir:',
             bg='white',
             fg='black',
             font=('Arial', 12, 'bold'))

Check1 = BooleanVar()
Check2 = BooleanVar()
Check3 = BooleanVar()
Check4 = BooleanVar()

b1 = Checkbutton(janela,
                 text='Letras Maiúsculas',
                 variable=Check1,
                 bg='white',
                 fg='black',
                 activebackground='white',
                 anchor=NW,
                 font=('Arial', 12))

b2 = Checkbutton(janela,
                 text='Letras Minúsculas',
                 variable=Check2,
                 bg='white',
                 fg='black',
                 activebackground='white',
                 anchor=NW,
                 font=('Arial', 12))

b3 = Checkbutton(janela,
                 text='Números',
                 variable=Check3,
                 bg='white',
                 fg='black',
                 activebackground='white',
                 anchor=NW,
                 font=('Arial', 12))

b4 = Checkbutton(janela,
                 text='Caracteres Especiais',
                 variable=Check4,
                 bg='white',
                 fg='black',
                 activebackground='white',
                 anchor=NW,
                 font=('Arial', 12))

b5 = Button(janela,
            text='Gerar senha',
            bg='white',
            fg='red',
            font=('Arial', 12, 'bold'),
            background='red',
            foreground='white',
            activebackground='red',
            activeforeground='white',
            command=senha)

b6 = Button(janela,
            text='Copiar',
            bg='white',
            fg='red',
            font=('Arial', 12, 'bold'),
            background='blue',
            foreground='white',
            activebackground='blue',
            activeforeground='white',
            command=copiar)

mostrar_senha = Label(text='',
                      font=('Arial', 15),
                      fg='black',
                      bg='#DCDCDC',
                      relief='solid',
                      width=38,
                      bd=3)
# posições dos elementos
op.pack()
txt1.place(relx=0.01, rely=0.38, relwidth=0.4, relheight=0.04)
tam.place(relx=0.42, rely=0.38, relwidth=0.15, relheight=0.04)
txt2.place(relx=0.02, rely=0.45, relwidth=0.15, relheight=0.04)
b1.place(relx=0.1, rely=0.5, relwidth=0.45, relheight=0.05)
b2.place(relx=0.1, rely=0.56, relwidth=0.45, relheight=0.05)
b3.place(relx=0.1, rely=0.62, relwidth=0.45, relheight=0.05)
b4.place(relx=0.1, rely=0.68, relwidth=0.45, relheight=0.05)
b5.place(relx=0.02, rely=0.75, relwidth=0.48, relheight=0.05)
b6.place(relx=0.5, rely=0.75, relwidth=0.48, relheight=0.05)
mostrar_senha.place(relx=0.02, rely=0.81, relwidth=0.96, relheight=0.17)

janela.mainloop()
