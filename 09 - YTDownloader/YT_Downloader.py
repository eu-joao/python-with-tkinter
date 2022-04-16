from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

from pytube import YouTube
from pytube import Playlist


caminho_download = ''
lista_opcoes = ['Baixar áudio', 'Baixar vídeo',
                'Baixar playlist (vídeo)', 'Baixar playlist (áudio)']

# Configurações da janela
janela = Tk()
janela.title('')

# dimensões da janela
largura, altura = 370, 410

# pegando a resolução do sistema
largura_so = janela.winfo_screenwidth()
altura_so = janela.winfo_screenheight()

# posição da janela
posx = largura_so // 2 - largura // 2
posy = altura_so // 2 - altura // 2

# configurações finais da janela
janela.resizable(False, False)
janela.geometry(f'{largura}x{altura}+{posx}+{posy}')
janela.iconbitmap(r'09 - YTDownloader\imagens\icone.ico')
janela.configure(background='white')

# definindo o estilo da janela
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Funções


def pegar_caminho():
    global caminho_download

    caminho_download = filedialog.askdirectory()
    entry_caminho_download.delete(0, END)
    entry_caminho_download.insert(0, caminho_download)


def baixar_midia():
    if (opcoes.get() == lista_opcoes[0]):
        yt = YouTube(entry_url.get())
        yt.streams.filter(only_audio=True).first().download(
            output_path=caminho_download)

    elif (opcoes.get() == lista_opcoes[1]):
        yt = YouTube(entry_url.get())
        yt.streams.get_highest_resolution().download(output_path=caminho_download)

    elif (opcoes.get() == lista_opcoes[2]):
        playlist = Playlist(entry_url.get())

        for video in playlist:
            yt = YouTube(video)
            yt.streams.get_highest_resolution().download(output_path=caminho_download)

    elif (opcoes.get() == lista_opcoes[3]):
        playlist = Playlist(entry_url.get())

        for audio in playlist:
            yt = YouTube(audio)
            yt.streams.filter(only_audio=True).first().download(
                output_path=caminho_download)

    messagebox.showinfo('', 'A operação foi concluída!')


logo_programa = PhotoImage(file=r'09 - YTDownloader\imagens\logo.png')
titulo = Label(janela,
               image=logo_programa,
               text='YT Downloader',
               compound=LEFT,
               font=('Arial', 26, 'bold'),
               foreground='black',
               background='white').pack()

separador = ttk.Separator(janela, orient='horizontal')
separador.pack(fill='x')

# URL
label_url = Label(janela,
                  text='Vídeo/Playlist URL:',
                  bg='white',
                  fg='black',
                  font=('calibri', 12))
label_url.place(relx=0.03, rely=0.3, relwidth=0.37, relheight=0.06)

entry_url = ttk.Entry(janela)
entry_url.place(relx=0.04, rely=0.37, relwidth=0.92, relheight=0.08)

# Caminho para download
label_caminho = Label(janela,
                      text='Salvar em:',
                      bg='white',
                      fg='black',
                      font=('calibri', 12))
label_caminho.place(relx=0.04, rely=0.48, relwidth=0.2, relheight=0.06)

entry_caminho_download = ttk.Entry(janela)
entry_caminho_download.place(
    relx=0.04, rely=0.55, relwidth=0.7, relheight=0.08)

botao_selecionar = ttk.Button(janela, text='Selecionar', command=pegar_caminho)
botao_selecionar.place(relx=0.74, rely=0.55, relwidth=0.22, relheight=0.08)

# Opções para download
label_opcoes = Label(janela,
                     text='Opções para download:',
                     bg='white',
                     fg='black',
                     font=('calibri', 12))
label_opcoes.place(relx=0.03, rely=0.66, relwidth=0.44, relheight=0.06)

opcoes = ttk.Combobox(janela, values=lista_opcoes)
opcoes.place(relx=0.47, rely=0.66, relwidth=0.49, relheight=0.06)

# Botão de download
botao_download = ttk.Button(
    janela, text='INICIAR DOWNLOAD', command=baixar_midia)
botao_download.place(relx=0.3, rely=0.83, relwidth=0.38, relheight=0.08)

janela.mainloop()