import sqlite3

class Criar_banco(object):
    def __init__(self):
        # criando e conectando...
        self.conn = sqlite3.connect('roupasmae.db')
        # definindo um cursor
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE estampas (
 	        id_estampa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 	        nm_estampa TEXT NOT NULL,
            observacao TEXT
            );
            """)
        print("tabela estampa criada com sucesso!!")

        self.cursor.execute("""
        CREATE TABLE clientes (
 	        id_cliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 	        nm_cliente TEXT NOT NULL,
            fkid_bairro INTEGER,
            telefone TEXT,
            endereco TEXT,
            FOREIGN KEY(fkid_bairro) REFERENCES bairros(id_bairro)
            );
            """)
        print("tabela cliente criada com sucesso!!")

        self.cursor.execute("""
        CREATE TABLE bairros (
 	        id_bairro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 	        nm_bairro TEXT NOT NULL,
            observacao TEXT
            );
            """)
        print("tabela bairro criada com sucesso!!")

        self.cursor.execute("""
        CREATE TABLE compras (
 	        id_compra INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 	        entrega TEXT NOT NULL,
            valor REAL,
            data DATE NOT NULL,
            frete REAL,
            fkid_cliente INTEGER,
            fkid_bairro INTEGER,
            metodo_pg TEXT,
            FOREIGN KEY(fkid_bairro) REFERENCES bairros(id_bairro),
            FOREIGN KEY(fkid_cliente) REFERENCES clientes(id_cliente)
            );
            """)
        print("tabela compras criada com sucesso!!")

        self.cursor.execute("""
        CREATE TABLE itens (
 	        id_iten INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 	        tamanho TEXT NOT NULL,
            tipo TEXT NOT NULL,
            valor REAL NOT NULL,
            fkid_compra INTEGER NOT NULL,
            fkid_estampa INTEGER NOT NULL,
            FOREIGN KEY(fkid_compra) REFERENCES compras(id_compra),
            FOREIGN KEY(fkid_estampa) REFERENCES estampas(id_estampa)
            );
            """)
        print("tabela itens criada com sucesso!!")

        self.cursor.execute("""
        CREATE TABLE descontos (
 	        id_desconto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 	        valor_desconto REAL NOT NULL,
            fkid_iten INTEGER NOT NULL,
            fkid_compra INTEGER NOT NULL,
            FOREIGN KEY(fkid_iten) REFERENCES itens(id_iten),
            FOREIGN KEY(fkid_compra) REFERENCES compras(id_compra)
            );
            """)
        print("tabela descontos criada com sucesso!!")

        self.cursor.execute("""
        CREATE TABLE pagamentos (
 	        id_pagamento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            fkid_compra INTEGER NOT NULL,
            valor_pagamento REAL NOT NULL,
            data_pagamento DATE NOT NULL,
            FOREIGN KEY(fkid_compra) REFERENCES compras(id_compra)
            );
            """)
        print("tabela descontos criada com sucesso!!")




        self.conn.commit()
        print('Banco criado com sucesso!')
        # desconectando
        self.conn.close()
Criar_banco()
