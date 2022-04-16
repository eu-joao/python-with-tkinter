from tkinter import *

import random

janela = Tk()
janela.title('Roll Dice')

# dimensões da janela
largura, altura = 500, 300

# pegando a resolução do sistema
largura_SO = janela.winfo_screenwidth()
altura_SO = janela.winfo_screenheight()

# posição da janela
posx = largura_SO // 2 - largura // 2
posy = altura_SO // 2 - altura // 2

janela.geometry(f'{largura}x{altura}+{posx}+{posy}')
janela.resizable(False, False)
janela.iconbitmap('05 - Roll Dice\Ícone\ícone.ico')


def rolar_dado():
    dados = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    area_dado.configure(text=f'{random.choice(dados)}{random.choice(dados)}')


area_dado = Label(text='', font=('times', 200))
area_dado.place(relx=0.1, rely=0.10, relwidth=0.8, relheight=0.6)

botao = Button(text='Jogar dados!',
               font=('times', 12, 'bold'),
               bg='black',
               fg='white',
               activebackground='black',
               activeforeground='white',
               command=rolar_dado)
botao.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.1)

janela.mainloop()

