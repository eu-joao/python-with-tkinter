from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

from datetime import datetime
from dateutil.relativedelta import relativedelta


# Configurações da Janela
janela = Tk()
largura, altura = 550, 350
# pegando a resolução do sistema
largura_so = janela.winfo_screenwidth()
altura_so = janela.winfo_screenheight()
# posição da janela
posx = largura_so // 2 - largura // 2
posy = altura_so // 2 - altura // 2
janela.geometry(f'{largura}x{altura}+{posx}+{posy}')
janela.title('')
#janela.resizable(False, False)
janela.configure(background='white')
janela.iconbitmap('10 - Calculadora de datas\Ícone\ícone.ico')

estilo = ttk.Style(janela)
estilo.theme_use('clam')


def obter_diferenca():
    # calculando a diferenca entre as datas
    primeira_data = entry_primeira_data.get()
    segunda_data = entry_segunda_data.get()

    dia1, mes1, ano1 = map(int, primeira_data.split('/'))
    dia2, mes2, ano2 = map(int, segunda_data.split('/'))

    primeira_data_1 = datetime(ano1, mes1, dia1)
    segunda_data_2 = datetime(ano2, mes2, dia2)

    diferenca = relativedelta(segunda_data_2, primeira_data_1)

    label_diferenca.configure(
        text=f'{diferenca.years} anos, {diferenca.months} meses e {diferenca.days} dias')

    # calculando os dias corridos
    d1 = datetime.strptime(f'{ano1}-{mes1}-{dia1}', '%Y-%m-%d')
    d2 = datetime.strptime(f'{ano2}-{mes2}-{dia2}', '%Y-%m-%d')

    label_dias_corridos.configure(text=f'{abs((d2 - d1).days)} dias corridos')


label_titulo = Label(janela, background='white', foreground='black',
                     text='Diferença entre datas', font=('Arial', 25, 'bold')).pack()

label_sub_titulo = Label(janela, background='white', foreground='gray',
                         text='Quantidade de dias, meses e anos entre duas datas de forma rápida e objetiva', font=('Arial', 11)).pack()

label_primeira_data = Label(janela, background='white', foreground='red',
                            text='Primeira data*', font=('Arial', 12))
label_primeira_data.place(relx=0.24, rely=0.24, relheight=0.05, relwidth=0.2)

label_segunda_data = Label(janela, background='white', foreground='red',
                           text='Segunda data*', font=('Arial', 12))
label_segunda_data.place(relx=0.55, rely=0.24, relheight=0.05, relwidth=0.2)

entry_primeira_data = DateEntry(
    janela, font=('Arial', 14), justify=CENTER)
entry_primeira_data.place(relx=0.18, rely=0.3, relheight=0.08, relwidth=0.3)

entry_segunda_data = DateEntry(
    janela, font=('Arial', 14), justify=CENTER)
entry_segunda_data.place(relx=0.5, rely=0.3, relheight=0.08, relwidth=0.3)

label_dias_corridos = Label(janela, background='white', foreground='black',
                            text='0 dias corridos', font=('Arial', 25))
label_dias_corridos.place(relx=0.25, rely=0.6, relheight=0.1, relwidth=0.5)

label_diferenca = Label(janela, background='white', foreground='gray',
                        text='0 anos, 0 meses e 0 dias', font=('Arial', 18))
label_diferenca.place(relx=0.1, rely=0.7, relheight=0.1, relwidth=0.8)


botao_calcular = ttk.Button(janela, text='CALCULAR', command=obter_diferenca)
botao_calcular.place(relx=0.4, rely=0.45, relheight=0.08, relwidth=0.2)

label_autoria = Label(janela, background='white', foreground='black',
                      text='João Santos © 2022', font=('Arial', 12))
label_autoria.place(relx=0.1, rely=0.9, relheight=0.1, relwidth=0.8)

janela.mainloop()