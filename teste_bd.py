from menage import Bd_manage

m = Bd_manage()

m.criar_cliente("* NÃO INFORMADO * ")
m.criar_cliente("Alberto!! ", "98454-3243")
m.criar_cliente("Gustavo!! ")

print(m.mostrar_clientes())

m.criar_estampa("Onça")
m.criar_estampa("Preto")

print(m.mostrar_estampas())

m.criar_bairro("* NÃO INFORMADO * ")
m.criar_bairro("Penha")
m.criar_bairro("Olaria")

print(m.mostrar_bairros())

#self, entrega, valor, frete, id_cliente, id_bairro
m.criar_compra("shopping da Penha", 123, "2020-01-12",None, 0, 1, "Dinheiro")
m.criar_compra("Caxias shopping", 323, "2020-01-15",34.50, 1, 0, "Debito")

print(m.mostrar_compras())

m.criar_iten("P", "Vestido", 100, 0, 1)
m.criar_iten("G", "macacão", 150, 1, 0)

print(m.mostrar_itens())

m.criar_desconto(32.50, 1, 1)
m.criar_desconto(10, 0, 0)

print(m.mostrar_descontos())



m.deletar_cliente(0)
m.deletar_estampa(0)
m.deletar_bairro(0)
m.deletar_iten(0)
m.deletar_compra(0)
print(m.mostrar_clientes())
