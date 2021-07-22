from menage import Bd_manage

class Pagamento(object):
    """docstring for Pagamentos."""

    def __init__(self, fkid_compra, valor_pagamento, data_pagamento):
        self.banco  = Bd_manage()
        self.banco.criar_pagamento(fkid_compra, valor_pagamento, data_pagamento)
        print("//////////////////////// pagamento criadooooo")
