from tkinter import *
from tkinter import ttk

# Configurações da Janela
janela = Tk()
largura, altura = 550, 300
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
janela.iconbitmap('01 - PyColor\Ícone\ícone.ico')

estilo = ttk.Style(janela)
estilo.theme_use('clam')


def copiar():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(entry_cor.get())
    clip.destroy()


def conversao(valor):
    R, G, B = s_red.get(), s_green.get(), s_blue.get()
    hexadecimal = "#%02x%02x%02x" % (R, G, B)
    l_cor.configure(background=hexadecimal)
    entry_cor.delete(0, END)
    entry_cor.insert(0, hexadecimal)


frame1 = LabelFrame(janela, text='PyColor',
                    background='white', font=('COMIC SANS MS', 15, 'bold'))
frame1.place(relx=0.01, rely=0, relheight=0.98, relwidth=0.98)

frame2 = LabelFrame(frame1, text='Visualização da cor', background='white',
                    font=('COMIC SANS MS', 12, 'bold'), foreground='black')
frame2.place(relx=0.01, rely=0, relheight=0.98, relwidth=0.5)

frame3 = LabelFrame(frame1, text='Código HEX', background='white',
                    font=('COMIC SANS MS', 10, 'bold'), foreground='black')
frame3.place(relx=0.52, rely=0.72, relheight=0.26, relwidth=0.47)

l_red = Label(frame1, text='RED', background='white',
              font=('COMIC SANS MS', 10, 'bold'), foreground='red')
l_red.place(relx=0.52, rely=0.01, relheight=0.09, relwidth=0.47)

l_green = Label(frame1, text='GREEN', background='white',
                font=('COMIC SANS MS', 10, 'bold'), foreground='green')
l_green.place(relx=0.52, rely=0.25, relheight=0.09, relwidth=0.47)

l_blue = Label(frame1, text='BLUE', background='white',
               font=('COMIC SANS MS', 10, 'bold'), foreground='blue')
l_blue.place(relx=0.52, rely=0.48, relheight=0.09, relwidth=0.47)

l_cor = Label(frame2, background='black')
l_cor.place(relx=0, rely=0, relheight=1, relwidth=1)

# Escalas
s_red = Scale(frame1, command=conversao, from_=0, to=255,
              background='white', foreground='red', orient=HORIZONTAL)
s_red.place(relx=0.52, rely=0.09, relheight=0.16, relwidth=0.47)

s_green = Scale(frame1, command=conversao, from_=0, to=255,
                background='white', foreground='green', orient=HORIZONTAL)
s_green.place(relx=0.52, rely=0.33, relheight=0.16, relwidth=0.47)

s_blue = Scale(frame1, command=conversao, from_=0, to=255,
               background='white', foreground='blue', orient=HORIZONTAL)
s_blue.place(relx=0.52, rely=0.56, relheight=0.16, relwidth=0.47)

# botão
bt_copiar = ttk.Button(frame3, text='Copiar', command=copiar)
bt_copiar.place(relx=0.7, rely=0.1, relwidth=0.25, relheight=0.7)

# entry
entry_cor = ttk.Entry(frame3, justify=CENTER)
entry_cor.insert(0, '#000000')
entry_cor.place(relx=0.05, rely=0.1, relwidth=0.63, relheight=0.7)

janela.mainloop()

