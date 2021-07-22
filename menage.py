import sqlite3

class Bd_manage(object):

    def __init__(self):
        print("Iniciou o contrutor")
        self.ccon = None
        self.cursor = None
        print("copilou tudo!!")

    def conectar_banco(self):
        # criando e conectando...
        self.conn = sqlite3.connect('roupasmae.db')
        # definindo um cursor
        self.cursor = self.conn.cursor()

    def desconectar(self):
        self.conn.commit()
        print('Dados gravados com sucesso!')
        # desconectando
        self.conn.close()

    #------------ Buscar ultima inserção ------------
                # compras
    def ultimo_compra(self):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT MAX(id_compra) FROM compras;
        """)
        flexa = self.cursor.fetchall()
        self.desconectar()
        return flexa[0][0]

    def ultimo_iten(self):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT MAX(id_iten) FROM itens;
        """)
        flexa = self.cursor.fetchall()
        self.desconectar()
        return flexa[0][0]


    #------------ Inserir dados ------------
                # cliente
    def criar_cliente(self, nome_cliente, fkid_bairro, telefone=None, endereco=None):
        print("nome_cliente", nome_cliente)
        print("nome_cliente", fkid_bairro)
        print("nome_cliente", telefone)
        print("nome_cliente", endereco)
        self.conectar_banco()
        self.cursor.execute("""
        INSERT INTO clientes (nm_cliente, fkid_bairro, telefone, endereco)
        VALUES (?,?,?,?)
        """,(nome_cliente, fkid_bairro, telefone, endereco))
        print("cliente criado com sucesso!!")
        self.desconectar()
                # estampa
    def criar_estampa(self, nome_estampa, obs=None):
        print("nome_estampa", nome_estampa)
        self.conectar_banco()
        self.cursor.execute("""
        INSERT INTO estampas (nm_estampa, observacao)
        VALUES (?,?)
        """,(nome_estampa, obs))
        print("estampa criada com sucesso!!")
        self.desconectar()
                # bairro
    def criar_bairro(self, nome_bairro, obs=None):
        print("nome_bairro", nome_bairro)
        self.conectar_banco()
        self.cursor.execute("""
        INSERT INTO bairros (nm_bairro, observacao)
        VALUES (?,?)
        """,(nome_bairro, obs))
        print("bairro criado com sucesso!!")
        self.desconectar()
                # iten
    def criar_iten(self, tamanho, tipo, valor, cd_compra, cd_estampa):
        self.conectar_banco()
        self.cursor.execute("""
        INSERT INTO itens (tamanho, tipo, valor, fkid_compra, fkid_estampa)
        VALUES (?,?,?,?,?)
        """,(tamanho, tipo, valor, cd_compra, cd_estampa))
        print("iten criado com sucesso!!")
        self.desconectar()
                # compra
    def criar_compra(self, entrega, valor, data, frete, fkid_cliente, fkid_bairro, metodo_pg):
        print("fk_cliente: ",  fkid_cliente, "\n fk_bairro: ", fkid_bairro, "\n metodo pagamento: ", metodo_pg)
        self.conectar_banco()
        self.cursor.execute("""
        INSERT INTO compras (entrega, valor, data, frete, fkid_cliente, fkid_bairro, metodo_pg)
        VALUES (?,?,?,?,?,?,?)
        """,(entrega, valor, data, frete, fkid_cliente, fkid_bairro, metodo_pg))
        print("compra criada com sucesso!!")
        self.desconectar()
                # desconto
    def criar_desconto(self, valor_desconto, fkid_iten, fkid_compra):
        self.conectar_banco()
        self.cursor.execute("""
        INSERT INTO descontos (valor_desconto, fkid_iten, fkid_compra)
        VALUES (?,?,?)
        """,(valor_desconto, fkid_iten, fkid_compra))
        print("desconto criado com sucesso!!")
        self.desconectar()
                # pagamento
    def criar_pagamento(self, fkid_compra, valor_pagamento, data_pagamento):
        self.conectar_banco()
        self.cursor.execute("""
        INSERT INTO pagamentos (fkid_compra, valor_pagamento, data_pagamento)
        VALUES (?,?,?)
        """,(fkid_compra, valor_pagamento, data_pagamento))
        print("pagamento criado com sucesso!!")
        self.desconectar()


    #------------ Mostrar dados ------------
                # clientes
    def mostrar_clientes(self):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT * FROM clientes;
        """)
        flexa = self.cursor.fetchall()
        self.desconectar()
        return flexa
                # estampas
    def mostrar_estampas(self):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT * FROM estampas;
        """)
        flexa = self.cursor.fetchall()
        self.desconectar()
        return flexa
                # bairro
    def mostrar_bairros(self):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT * FROM bairros;
        """)
        flexa = self.cursor.fetchall()
        print(flexa)
        self.desconectar()
        return flexa
                # iten
    def mostrar_itens(self):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT * FROM itens;
        """)
        flexa = self.cursor.fetchall()
        self.desconectar()
        return flexa
                # compras
    def mostrar_compras(self):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT * FROM compras;
        """)
        flexa = self.cursor.fetchall()
        self.desconectar()
        return flexa
                # desconto
    def mostrar_descontos(self):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT * FROM descontos;
        """)
        flexa = self.cursor.fetchall()
        self.desconectar()
        return flexa

    #------------ Pesquisar dados por codigo da compra------------******
                # iten
    def pesquisar_itens_cod_compra(self, id):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT * FROM itens WHERE fkid_compra=?;
        """,(id, ))
        flexa = self.cursor.fetchall()
        self.desconectar()
        return flexa
                # desconto
    def pesquisar_descontos_cod_compra(self):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT * FROM descontos;
        """)
        flexa = self.cursor.fetchall()
        self.desconectar()
        return flexa
                # Pagamento
    def pesquisar_Pagamento_cod_compra(self):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT * FROM pagamentos;
        """)
        flexa = self.cursor.fetchall()
        self.desconectar()
        return flexa
    #------------ Pesquisar dados por codigo------------******
                # bairro
    def pesquisar_bairros(self, id):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT * FROM bairros WHERE id_bairro=?;
        """,(id, ))
        flexa = self.cursor.fetchall()
        self.desconectar()
        return flexa

    def pesquisar_clientes(self, id):
        self.conectar_banco()
        self.cursor.execute("""
        SELECT * FROM clientes WHERE id_cliente=?;
        """,(id, ))
        flexa = self.cursor.fetchall()
        self.desconectar()
        return flexa

    #------------ Deletar dados ------------******
    def deletar_cliente(self,id_n):
        self.conectar_banco()
        self.cursor.execute("""
        DELETE FROM clientes
        WHERE id_cliente = ?
        """, (id_n,))
        self.desconectar()
        print("Cliente Exluido ")

    def deletar_bairro(self,id_n):
        self.conectar_banco()
        self.cursor.execute("""
        DELETE FROM bairros
        WHERE id_bairro = ?
        """, (id_n,))
        self.desconectar()
        print("Bairro Exluido ")

    def deletar_estampa(self,id_n):
        self.conectar_banco()
        self.cursor.execute("""
        DELETE FROM estampas
        WHERE id_estampa = ?
        """, (id_n,))
        self.desconectar()
        print("Estampa Exluida ")

    def deletar_iten(self,id_n):
        self.conectar_banco()
        self.cursor.execute("""
        DELETE FROM itens
        WHERE id_iten = ?
        """, (id_n,))
        self.desconectar()
        print("Iten Exluido ")

    def deletar_compra(self,id_n):
        self.conectar_banco()
        self.cursor.execute("""
        DELETE FROM compras
        WHERE id_compra = ?
        """, (id_n,))
        self.desconectar()
        print("compra Exluida ")

    #------------ Deletar dados por codigo da compra ------------******

    def deletar_pagamento_por_compra(self, id):
        self.conectar_banco()
        self.cursor.execute("""
        DELETE FROM pagamentos WHERE fkid_compra=?;
        """,(id, ))
        self.desconectar()

    def deletar_desconto_por_compra(self, id):
        self.conectar_banco()
        self.cursor.execute("""
        DELETE FROM descontos WHERE fkid_compra=?;
        """,(id, ))
        self.desconectar()

    def deletar_iten_por_compra(self, id):
        self.conectar_banco()
        self.cursor.execute("""
        DELETE FROM itens WHERE fkid_compra=?;
        """,(id, ))
        self.desconectar()


    #------------ Alterar dados ------------*********
    def alterar_aluno(self, nome_n, nascimento_n, id_n):
        self.conectar_banco()
        self.cursor.execute("""
        UPDATE alunos
        SET nome = ?, nascimento = ?
        WHERE id = ?
        """, (nome_n, nascimento_n, id_n))
        print("Dados do aluno alterado")
        self.desconectar()


Bd_manage()
