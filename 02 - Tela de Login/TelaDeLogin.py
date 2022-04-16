from tkinter import *
from tkinter import ttk

# Estilos utilizados
COR_FRAME_1 = '#fafafa'
COR_FRAME_2 = 'darkblue'
FONTE_BOTOES_FRAME2 = ('Calibri', 12, 'bold')
FONTE_LABEL = ('Arial', 25, 'bold')
FONTE_LABEL2 = ('Arial', 12)

# configurações da janela
janela = Tk()
largura, altura = 706, 443
# pegando a resolução do sistema
largura_so = janela.winfo_screenwidth()
altura_so = janela.winfo_screenheight()
# posição da janela
posx = largura_so // 2 - largura // 2
posy = altura_so // 2 - altura // 2
# configurações finais da janela
janela.geometry(f'{largura}x{altura}+{posx}+{posy}')
janela.title('')
janela.resizable(False, False)
janela.iconbitmap(r'02 - Tela de Login\imagens\login.ico')

# frames da aplicação
frame1 = Frame(janela, background=COR_FRAME_1, relief=FLAT)
frame2 = Frame(janela, background=COR_FRAME_2, relief=FLAT)
# posições dos frames
frame1.place(relx=0, rely=0, relheight=1, relwidth=0.64)
frame2.place(relx=0.64, rely=0, relheight=1, relwidth=0.36)

# widgets do frame 1
cadeado = PhotoImage(file=r'02 - Tela de Login\imagens\cadeado.png')
mao = PhotoImage(file=r'02 - Tela de Login\imagens\mão_acenando.png')

boas_vindas = Label(frame1, font=FONTE_LABEL, text='Boas-vindas outra\nvez',
                    justify=LEFT, background=COR_FRAME_1)

conta = Label(frame1, font=FONTE_LABEL2, text='Entrar com sua conta',
              justify=LEFT, background=COR_FRAME_1)

mao_acenando = Label(frame1, text='',
                     background=COR_FRAME_1, image=mao)

entrar_conta = LabelFrame(frame1, text='E-mail/nome do(a) usuário(a)',
                          background=COR_FRAME_1)

senha = LabelFrame(frame1, text='Senha', background=COR_FRAME_1)

entry1 = Entry(entrar_conta, relief=FLAT)
entry2 = Entry(senha, show='*', relief=FLAT)

esqueci_a_senha = Label(frame1, background=COR_FRAME_1, foreground=COR_FRAME_2,
                        text='Esqueceu sua senha?', cursor='hand2')

botao_entrar = Button(frame1, image=cadeado, compound=LEFT, text='Entrar',
                      relief=FLAT, background=COR_FRAME_2, bd=3, foreground=COR_FRAME_1,
                      activeforeground=COR_FRAME_1, activebackground=COR_FRAME_2,
                      font=FONTE_BOTOES_FRAME2)

criar_conta = Label(frame1, background=COR_FRAME_1, foreground=COR_FRAME_2,
                    text='Criar sua conta', cursor='hand2', font=FONTE_LABEL2)

boas_vindas.place(relx=0.05, rely=0.1, relheight=0.2, relwidth=0.8)
conta.place(relx=0.1, rely=0.29, relheight=0.05, relwidth=0.4)
mao_acenando.place(relx=0.82, rely=0.15, relheight=0.1, relwidth=0.1)
entrar_conta.place(relx=0.13, rely=0.43, relheight=0.12, relwidth=0.72)
entry1.place(relx=0, rely=0, relheight=1, relwidth=1)
entry2.place(relx=0, rely=0, relheight=1, relwidth=1)
senha.place(relx=0.13, rely=0.57, relheight=0.12, relwidth=0.72)
esqueci_a_senha.place(relx=0.1, rely=0.7, relheight=0.05, relwidth=0.3)
botao_entrar.place(relx=0.13, rely=0.78, relheight=0.09, relwidth=0.2)
criar_conta.place(relx=0.35, rely=0.78, relheight=0.09, relwidth=0.3)

# widgets frame 2
estilo_botoes = ttk.Style()
estilo_botoes.configure('meu.TButton', anchor=NW,
                        font=FONTE_BOTOES_FRAME2)

img_facebook = PhotoImage(file=r'02 - Tela de Login\imagens\facebook.png')
img_google = PhotoImage(file=r'02 - Tela de Login\imagens\google.png')

botao_facebook = Button(frame2, image=img_facebook, compound=LEFT,
                        text=' com Facebook', anchor=NW, relief=FLAT,
                        background=COR_FRAME_2, bd=3, foreground=COR_FRAME_1,
                        activeforeground=COR_FRAME_1, activebackground=COR_FRAME_2,
                        font=FONTE_BOTOES_FRAME2, cursor='hand2')

botao_google = Button(frame2, image=img_google, compound=LEFT, text=' com Google',
                      anchor=NW, relief=FLAT, background=COR_FRAME_2, bd=3,
                      foreground=COR_FRAME_1, activeforeground=COR_FRAME_1,
                      activebackground=COR_FRAME_2, font=FONTE_BOTOES_FRAME2, cursor='hand2')
# posições
botao_facebook.place(relx=0.2, rely=0.4, relheight=0.1, relwidth=0.6)
botao_google.place(relx=0.2, rely=0.52, relheight=0.1, relwidth=0.6)

janela.mainloop()

