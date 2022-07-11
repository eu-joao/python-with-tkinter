import mysql.connector
from mysql.connector import errorcode

import os

from dotenv import load_dotenv


load_dotenv()

class BancoDeDados:
    def __init__(self):
        self.usuario = os.environ['USUARIO']
        self.senha = os.environ['SENHA']
        self.host = os.environ['HOST']
        self.nome_do_banco = os.environ['DB']
        self.erro = False

    def conectar(self):
        try:
            print("Conectado ao banco de dados")
            self.cnx = mysql.connector.connect(user=self.usuario, password=self.senha, 
                                           host=self.host, database=self.nome_do_banco)
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as err:
            self.erro = True

            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("A senha ou usuário estão incorretos!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print(f"O banco de dados '{self.nome_do_banco}' não existe!")
            else:
                print(err)

    def desconectar(self):
        self.cnx.close()

    def criar_tabela(self):
        if not self.erro:
            self.conectar()
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS contatos (
                                    id INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
                                    nome VARCHAR(20) NOT NULL,
                                    sobrenome VARCHAR(20),
                                    numero VARCHAR(11) NOT NULL UNIQUE,
                                    email VARCHAR(30));""")
    
    # C do CRUD
    def CREATE(self, nome, sobrenome, numero, email):
        if not self.erro:
            self.conectar()
            self.cursor.execute(f"""INSERT INTO contatos (nome, sobrenome, numero, email) VALUES (
                                    '{nome}', 
                                    '{sobrenome}', 
                                    '{numero}', 
                                    '{email}');""")
            self.cnx.commit()
            self.desconectar()
    
    # R do CRUD
    def READ(self):
        self.conectar()
        self.cursor.execute("""SELECT * FROM contatos;""")
        return self.cursor.fetchall()

    # U do CRUD
    def UPDATE(self, id, nome, sobrenome, numero, email):
        self.conectar()
        self.cursor.execute(f"""UPDATE contatos SET nome = '{nome}', 
                                                   sobrenome = '{sobrenome}', 
                                                   numero = '{numero}',
                                                   email = '{email}'
                               WHERE id = '{id['values'][0]}';""")
        self.cnx.commit()
        self.desconectar()
    
    # D do CRUD
    def DELETE(self, values):
        if values['values']:
            id_contato = values['values'][0]
            self.conectar()
            self.cursor.execute(f"DELETE FROM contatos WHERE id = {id_contato};")
            self.cnx.commit()
            self.desconectar()
    
    def SEARCH(self, k, v):
        self.conectar()
        self.cursor.execute(f"SELECT * FROM contatos WHERE {k} = '{v}';")
        return self.cursor.fetchall()
        