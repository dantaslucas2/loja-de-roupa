from menage import Bd_manage

class Bairro(object):
    """docstring for Bairro."""

    def __init__(self, nome, obs=None):
        self.banco  = Bd_manage()
        self.banco.criar_bairro(nome, obs)
