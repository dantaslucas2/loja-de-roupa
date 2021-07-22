from menage import Bd_manage

class Estampa(object):
    """docstring for Estampa."""

    def __init__(self, nome):
        self.banco  = Bd_manage()
        self.banco.criar_estampa(nome)
