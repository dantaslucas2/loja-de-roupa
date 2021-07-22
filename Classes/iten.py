from menage import Bd_manage

class Itens(object):
    """docstring for Itens."""

    def __init__(self, tamanho, tipo, valor, id_estampa, id_compra):
        self.tamanho = tamanho
        self.tipo = tipo
        self.valor = valor
        self.id_estampa = id_estampa
        self.id_compra = id_compra
        self.banco  = Bd_manage()
        print("tamanho: ", self.tamanho,"tipo: ", self.tipo,"compra: ", self.id_compra,"estampa: ", self.id_estampa)
        self.banco.criar_iten(self.tamanho, self.tipo, self.valor, self.id_compra, self.id_estampa)

    def ultimo_iten(self):
        print("Teste do ultimo: ",self.banco.ultimo_iten())
        return self.banco.ultimo_iten()
