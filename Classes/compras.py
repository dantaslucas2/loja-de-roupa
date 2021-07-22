from menage import Bd_manage

class Compras(object):
    """docstring for Compras."""

    def __init__(self, entrega, valor, data, frete, id_cliente, id_bairro, metodo_pg):
        self.banco  = Bd_manage()
        self.banco.criar_compra(entrega, valor, data, frete, id_cliente, id_bairro, metodo_pg)

    def ultima_compra(self):
        print("Teste do ultimo: ",self.banco.ultimo_compra())
        return self.banco.ultimo_compra()
