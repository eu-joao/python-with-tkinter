from tkinter import *
from tkinter import filedialog, messagebox

import os
import shutil

janela = Tk()
janela.title('Folder Organizer')

# dimensões da janela
largura, altura = 300, 200

# pegando a resolução do sistema
largura_so = janela.winfo_screenwidth()
altura_so = janela.winfo_screenheight()

# posição da janela
posx = largura_so // 2 - largura // 2
posy = altura_so // 2 - altura // 2

janela.resizable(False, False)
janela.geometry(f'{largura}x{altura}+{posx}+{posy}')
janela.iconbitmap('07 - Folder Organizer\Ícone\ícone.ico')
janela.configure(background='white')

# funções
caminho = ''


def selecionar_pasta():
    global caminho
    caminho = filedialog.askdirectory()
    msg2.configure(text=caminho, fg='green')

    if (len(caminho) == 0):
        messagebox.showerror('ERRO', 'Nenhuma pasta foi selecionada!')
        msg2.configure(text='Nenhuma pasta selecionada', fg='red')


def organizar():
    arquivos = os.listdir(caminho)

    for arquivo in arquivos:
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao[1:]
        if os.path.exists(os.path.join(caminho, extensao)):
            shutil.move(os.path.join(caminho, arquivo),
                        os.path.join(caminho, extensao, arquivo))
        else:
            os.makedirs(os.path.join(caminho, extensao))
            shutil.move(os.path.join(caminho, arquivo),
                        os.path.join(caminho, extensao, arquivo))
    messagebox.showinfo('AVISO', 'A pasta foi organizada com sucesso!')


msg1 = Label(janela,
             text='Selecione uma pasta para organizar:',
             bg='white',
             font=('Arial', 11, 'bold'),
             fg='black')
msg1.place(relx=0.07, rely=0.1, relwidth=0.85, relheight=0.1)

msg2 = Label(janela,
             text='Nenhuma pasta selecionada',
             bg='white',
             font=('Arial', 8, 'bold'),
             fg='red')
msg2.place(relx=0.14, rely=0.38, relwidth=0.7, relheight=0.1)

bt1 = Button(janela,
             text='SELECIONAR',
             bg='red',
             font=('Arial', 10, 'bold'),
             fg='white',
             command=selecionar_pasta,
             activeforeground='white',
             activebackground='red',
             relief='groove')
bt1.place(relx=0.1, rely=0.68, relwidth=0.8, relheight=0.12)

bt2 = Button(janela,
             text='ORGANIZAR',
             bg='blue',
             font=('Arial', 10, 'bold'),
             fg='white',
             command=organizar,
             activeforeground='white',
             activebackground='blue',
             relief='groove')
bt2.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.12)

janela.mainloop()
