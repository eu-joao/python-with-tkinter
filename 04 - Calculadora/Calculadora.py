from tkinter import *

# ========================== Configurações da Janela ===========================
janela = Tk()
largura, altura = 331, 507
# pegando a resolução do sistema
largura_so = janela.winfo_screenwidth()
altura_so = janela.winfo_screenheight()
# posição da janela
posx = largura_so // 2 - largura // 2
posy = altura_so // 2 - altura // 2
janela.geometry(f'{largura}x{altura}+{posx}+{posy}')
janela.title('Calculadora Simples')
janela.resizable(False, False)
janela.configure(background='black')
janela.iconbitmap('04 - Calculadora\Ícone\ícone.ico')
# ========================= Definindo variáveis importantes ====================
expressao_atual = resultado = ''
expressao_total = StringVar()
erro = False
# ========================= Definindo as operações =============================


def incrementa(valor):
    global expressao_atual, expressao_total, erro

    if erro:
        expressao_atual = ''
        expressao_total.set('')
        erro = False
    else:
        expressao_atual += valor
        expressao_total.set(expressao_atual)


def calcular():
    global expressao_atual, expressao_total, resultado, erro

    try:
        # substituindo os caracteres de divisão e multiplicação
        expressao_atual = expressao_atual.replace(
            '\u00F7', '/').replace('\u00D7', '*')
        resultado = eval(expressao_atual)

        # formatando o resultado da expressão
        if (int(resultado) == resultado):
            resultado = str(int(resultado))
        else:
            resultado = str(float(f'{resultado:.2f}'))

        expressao_total.set(resultado)
        expressao_atual = resultado

    except:
        expressao_total.set('ERRO')
        erro = True


def limpar():
    global expressao_atual, expressao_total

    expressao_atual = ' '
    expressao_total.set(expressao_atual)


def raiz_quadrada():
    global expressao_atual, expressao_total, resultado

    resultado = str(eval(f'{expressao_atual} ** 0.5'))
    if len(resultado) > 9:
        resultado = f'{float(resultado):.2f}'

    expressao_atual = str(resultado)
    expressao_total.set(resultado)


# ============================= Criação dos Frames =============================
frame1 = Frame(janela, background='black')
frame2 = Frame(janela, background='black')
frame1.place(relx=0, rely=0, relwidth=1, relheight=0.3)
frame2.place(relx=0, rely=0.3, relwidth=1, relheight=1)
# ============================= Definindo a Entry  =============================
entry_expressao = Label(frame1,
                        font=('Arial', 50, 'bold'),
                        foreground='white',
                        background='black',
                        anchor=E,
                        relief=FLAT,
                        textvariable=expressao_total)
entry_expressao.place(relx=0, rely=0, relheight=1, relwidth=1)
# ============================= Criação dos Botões =============================
botao_limpar = Button(frame2,
                      text='C',
                      background='black',
                      foreground='white',
                      activebackground='black',
                      activeforeground='white',
                      font=('Arial', 20, 'bold'),
                      relief=GROOVE,
                      bd=4,
                      command=lambda: limpar())

botao_raiz = Button(frame2,
                    text='\u221ax',
                    background='black',
                    foreground='white',
                    activebackground='black',
                    activeforeground='white',
                    font=('Arial', 20, 'bold'),
                    relief=GROOVE,
                    bd=4,
                    command=lambda: raiz_quadrada())

botao_dividir = Button(frame2,
                       text='\u00F7',
                       background='black',
                       foreground='white',
                       activebackground='black',
                       activeforeground='white',
                       font=('Arial', 20, 'bold'),
                       relief=GROOVE,
                       bd=4,
                       command=lambda: incrementa('\u00F7'))

botao_vezes = Button(frame2,
                     text='\u00D7',
                     background='black',
                     foreground='white',
                     activebackground='black',
                     activeforeground='white',
                     font=('Arial', 20, 'bold'),
                     relief=GROOVE,
                     bd=4,
                     command=lambda: incrementa('\u00D7'))

botao_7 = Button(frame2,
                 text='7',
                 background='black',
                 foreground='white',
                 activebackground='black',
                 activeforeground='white',
                 font=('Arial', 20, 'bold'),
                 relief=GROOVE,
                 bd=4,
                 command=lambda: incrementa('7'))

botao_8 = Button(frame2,
                 text='8',
                 background='black',
                 foreground='white',
                 activebackground='black',
                 activeforeground='white',
                 font=('Arial', 20, 'bold'),
                 relief=GROOVE,
                 bd=4,
                 command=lambda: incrementa('8'))

botao_9 = Button(frame2,
                 text='9',
                 background='black',
                 foreground='white',
                 activebackground='black',
                 activeforeground='white',
                 font=('Arial', 20, 'bold'),
                 relief=GROOVE,
                 bd=4,
                 command=lambda: incrementa('9'))

botao_menos = Button(frame2,
                     text='-',
                     background='black',
                     foreground='white',
                     activebackground='black',
                     activeforeground='white',
                     font=('Arial', 20, 'bold'),
                     relief=GROOVE,
                     bd=4,
                     command=lambda: incrementa('-'))

botao_4 = Button(frame2,
                 text='4',
                 background='black',
                 foreground='white',
                 activebackground='black',
                 activeforeground='white',
                 font=('Arial', 20, 'bold'),
                 relief=GROOVE,
                 bd=4,
                 command=lambda: incrementa('4'))

botao_5 = Button(frame2,
                 text='5',
                 background='black',
                 foreground='white',
                 activebackground='black',
                 activeforeground='white',
                 font=('Arial', 20, 'bold'),
                 relief=GROOVE,
                 bd=4,
                 command=lambda: incrementa('5'))

botao_6 = Button(frame2,
                 text='6',
                 background='black',
                 foreground='white',
                 activebackground='black',
                 activeforeground='white',
                 font=('Arial', 20, 'bold'),
                 relief=GROOVE,
                 bd=4,
                 command=lambda: incrementa('6'))

botao_mais = Button(frame2,
                    text='+',
                    background='black',
                    foreground='white',
                    activebackground='black',
                    activeforeground='white',
                    font=('Arial', 20, 'bold'),
                    relief=GROOVE,
                    bd=4,
                    command=lambda: incrementa('+'))

botao_1 = Button(frame2,
                 text='1',
                 background='black',
                 foreground='white',
                 activebackground='black',
                 activeforeground='white',
                 font=('Arial', 20, 'bold'),
                 relief=GROOVE,
                 bd=4,
                 command=lambda: incrementa('1'))

botao_2 = Button(frame2,
                 text='2',
                 background='black',
                 foreground='white',
                 activebackground='black',
                 activeforeground='white',
                 font=('Arial', 20, 'bold'),
                 relief=GROOVE,
                 bd=4,
                 command=lambda: incrementa('2'))

botao_3 = Button(frame2,
                 text='3',
                 background='black',
                 foreground='white',
                 activebackground='black',
                 activeforeground='white',
                 font=('Arial', 20, 'bold'),
                 relief=GROOVE,
                 bd=4,
                 command=lambda: incrementa('3'))

botao_igual = Button(frame2,
                     text='=',
                     background='black',
                     foreground='white',
                     activebackground='black',
                     activeforeground='white',
                     font=('Arial', 20, 'bold'),
                     relief=GROOVE,
                     bd=4,
                     command=lambda: calcular())

botao_0 = Button(frame2,
                 text='0',
                 background='black',
                 foreground='white',
                 activebackground='black',
                 activeforeground='white',
                 font=('Arial', 20, 'bold'),
                 relief=GROOVE,
                 bd=4,
                 command=lambda: incrementa('0'))

botao_ponto = Button(frame2,
                     text='.',
                     background='black',
                     foreground='white',
                     activebackground='black',
                     activeforeground='white',
                     font=('Arial', 20, 'bold'),
                     relief=GROOVE,
                     bd=4,
                     command=lambda: incrementa('.'))
# ============================= Posição dos Botões =============================
botao_limpar.place(relx=0, rely=0, relwidth=0.25, relheight=0.14)
botao_raiz.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.14)
botao_dividir.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.14)
botao_vezes.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.14)

botao_7.place(relx=0, rely=0.14, relwidth=0.25, relheight=0.14)
botao_8.place(relx=0.25, rely=0.14, relwidth=0.25, relheight=0.14)
botao_9.place(relx=0.5, rely=0.14, relwidth=0.25, relheight=0.14)
botao_menos.place(relx=0.75, rely=0.14, relwidth=0.25, relheight=0.14)

botao_4.place(relx=0, rely=0.28, relwidth=0.25, relheight=0.14)
botao_5.place(relx=0.25, rely=0.28, relwidth=0.25, relheight=0.14)
botao_6.place(relx=0.5, rely=0.28, relwidth=0.25, relheight=0.14)
botao_mais.place(relx=0.75, rely=0.28, relwidth=0.25, relheight=0.14)

botao_1.place(relx=0, rely=0.42, relwidth=0.25, relheight=0.14)
botao_2.place(relx=0.25, rely=0.42, relwidth=0.25, relheight=0.14)
botao_3.place(relx=0.5, rely=0.42, relwidth=0.25, relheight=0.14)
botao_igual.place(relx=0.75, rely=0.42, relwidth=0.25, relheight=0.28)

botao_0.place(relx=0, rely=0.56, relwidth=0.5, relheight=0.14)
botao_ponto.place(relx=0.5, rely=0.56, relwidth=0.25, relheight=0.14)
# ============================= Execução do programa ============================
janela.mainloop()

