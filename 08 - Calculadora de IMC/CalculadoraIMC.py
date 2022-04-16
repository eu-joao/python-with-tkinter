from tkinter import *

# Cores utilizadas
AZUL = '#1f5eaf'
BRANCO = '#FFFFFF'
CINZA = '#989881'
LARANJA = '#ff5202'

TEXTO = """O IMC é o parâmetro adotado pela Organização Mundial de Saúde para calcular o peso ideal de cada pessoa.
Diz-se que o indivíduo tem peso normal quando o resultado do IMC está entre 18,5 e 24,9."""

# Variáveis importantes
imc = grauObesidade = 0
classificacao = ''

# Configuração da janela
janela = Tk()
janela.title('')
janela.resizable(False, False)
# dimensões da janela
largura, altura = 750, 300
# pegando a resolução do sistema
largura_SO = janela.winfo_screenwidth()
altura_SO = janela.winfo_screenheight()
# posição da janela
posx = largura_SO // 2 - largura // 2
posy = altura_SO // 2 - altura // 2
janela.geometry(f'{largura}x{altura}+{posx}+{posy}')
janela.configure(background=BRANCO)
# ícone da aplicação
janela.iconbitmap('08 - Calculadora de IMC\Ícone\ícone.ico')

# Funções


def limpar():
    entryPeso.delete(0, END)
    entryAltura.delete(0, END)


def calcular_imc():
    global imc, classificacao, grauObesidade

    altura = float(str(entryAltura.get()).replace(',', '.'))
    peso = float(str(entryPeso.get()).replace(',', '.'))

    imc = peso / (pow(altura, 2))

    if (imc < 18.5):
        classificacao, grauObesidade = 'MAGREZA', 0
    elif (imc <= 24.9):
        classificacao, grauObesidade = 'NORMAL', 0
    elif (imc <= 29.9):
        classificacao, grauObesidade = 'SOBREPESO', 1
    elif (imc <= 39.9):
        classificacao, grauObesidade = 'OBESIDADE', 2
    elif (imc > 40):
        classificacao, grauObesidade = 'OBESIDADE GRAVE', 3

    resultado.configure(
        text=f'IMC: {imc:.2f} kg/m² | Classificação: {classificacao} | Obesidade (Grau): {grauObesidade}')


# Labels
titulo = Label(janela,
               text='Cálculo do IMC',
               font=('Ivy', 20, 'bold'),
               bg=BRANCO,
               fg=AZUL)

descricao = Label(janela,
                  text=TEXTO,
                  font=('Ivy', 10, 'bold'),
                  bg=BRANCO,
                  fg=CINZA,
                  anchor=NW,
                  justify=LEFT)

titulo_entry_altura = Label(janela,
                            text='Altura (ex.: 1,70)',
                            font=('Ivy', 12),
                            bg=BRANCO,
                            fg=AZUL)

titulo_entry_peso = Label(janela,
                          text='Peso (ex.: 69,2)',
                          font=('Ivy', 12),
                          bg=BRANCO,
                          fg=AZUL)

resultado = Label(janela,
                  text='Preencha os campos para ver suas estatísticas',
                  font=('Ivy', 15, 'bold'),
                  bg=BRANCO,
                  fg=LARANJA,
                  relief=FLAT,
                  highlightbackground=LARANJA,
                  highlightthickness=2)

titulo.place(relx=0.01, rely=0.01, relwidth=0.3, relheight=0.1)
descricao.place(relx=0.025, rely=0.12, relwidth=1, relheight=0.2)
titulo_entry_altura.place(relx=0.01, rely=0.25, relwidth=0.2, relheight=0.1)
titulo_entry_peso.place(relx=0.34, rely=0.25, relwidth=0.2, relheight=0.1)
resultado.place(relx=0.029, rely=0.6, relwidth=0.94, relheight=0.34)

# Entrys
entryAltura = Entry(janela,
                    font=('Ivy', 12),
                    fg='black',
                    relief=RIDGE,
                    bd=2)

entryPeso = Entry(janela,
                  font=('Ivy', 12),
                  fg='black',
                  relief=RIDGE,
                  bd=2)

entryAltura.place(relx=0.03, rely=0.34, relwidth=0.3, relheight=0.08)
entryPeso.place(relx=0.36, rely=0.34, relwidth=0.3, relheight=0.08)

# Botões
bt_calcular = Button(janela,
                     text='Calcular    >',
                     font=('arial', 12),
                     fg=BRANCO,
                     bg=AZUL,
                     relief=RAISED,
                     activeforeground=BRANCO,
                     activebackground=AZUL,
                     command=calcular_imc)

bt_limpar = Button(janela,
                   text='Limpar    >',
                   font=('arial', 12),
                   fg=BRANCO,
                   bg=LARANJA,
                   relief=RAISED,
                   activebackground=LARANJA,
                   activeforeground=BRANCO,
                   command=limpar)

bt_calcular.place(relx=0.03, rely=0.45, relwidth=0.14, relheight=0.09)
bt_limpar.place(relx=0.19, rely=0.45, relwidth=0.14, relheight=0.09)

janela.mainloop()

