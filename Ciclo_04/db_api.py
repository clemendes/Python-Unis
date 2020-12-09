# -*- coding: utf-8 -*-
import sqlite3

class MyApp:
    
    def __init__(self):
        # Cria base de dados
        self.con = sqlite3.connect('db.sqlite3')
        # Define um Cursor
        self.cur = self.con.cursor()
        # Cria a tabela 'Exames'
        self.con.text_factory = str
        self.criar_tabela()

    def criar_tabela(self):
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS exames(
                id integer PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                endereco TEXT NOT NULL,
                altura REAL NOT NULL,
                peso   REAL NOT NULL,
                imc    REAL NOT NULL)''')
        except Exception as e:
            print('[x] Erro ao criar tabela [x]:', e)

    def inserir_registro(self, exame):
        try:
            self.cur.execute('''INSERT INTO exames VALUES (NULL, ?, ?, ?, ?, ?)''', exame)
        except Exception as e:
            print('[x] Erro ao inserir registro [x]')
            print('[x] Efetuando Rollback [x]:', e)
            self.con.rollback()
        else:
            self.con.commit()
            print('[!] Registro inserido com sucesso [!]')

    def consultar_registro(self, rowid):
        return self.cur.execute('''SELECT * FROM exames WHERE rowid=?''', (rowid,)).fetchone()

    def listar_registros(self, limit=100):
        return self.cur.execute('''SELECT * FROM exames LIMIT ?''', (limit,)).fetchall()
