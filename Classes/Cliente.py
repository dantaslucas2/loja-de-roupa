from menage import Bd_manage

class Clientes(object):
    """docstring for Clientes."""

    def __init__(self, nome, id_bairro, telefone, endereco):
        self.banco  = Bd_manage()
        print(self.banco.mostrar_clientes)
        self.banco.criar_cliente(nome, id_bairro, telefone, endereco)
