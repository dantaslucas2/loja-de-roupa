from menage import Bd_manage

class Descontos(object):
    """docstring for Descontos."""

    def __init__(self, valor, iten, compra):
        self.valor = valor
        self.id_iten = iten
        self.compra = compra
        self.banco  = Bd_manage()
        self.banco.criar_desconto(self.valor, self.id_iten, self.compra)
