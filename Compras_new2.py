# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Compras.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Classes.compras import Compras
from Classes.iten import Itens
from Classes.Desconto import Descontos
from Classes.Pagamento import Pagamento
from Itens_new import Ui_Form_itens
from Cliente import Ui_Form_cliente
from Bairro import Ui_Form_bairro
from Impress.Impress import Documento
import sys
from menage import Bd_manage
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *

class Ui_Form_compras(object):

    def __init__(self):
        self.itens = []
        self.autorizacao = True

    def salvar(self):
            #preparando dados para inserir no banco
        index_cliente = self.CB_cliente.currentIndex()
        index_cliente = self.aux_cliente[index_cliente]
        index_bairro = self.CB_bairro.currentIndex()
        index_bairro = self.aux_bairro[index_bairro]
        temp_var = self.dateEdit.date()
        data = temp_var.toPyDate()
        valor = float(self.LE_valor.text()[2:])
        lista_pagamento = []
        if self.CB_frete.isChecked():
            frete = self.LE_frete.text()
        else:
            frete = None
        if self.CB_dinheiro.isChecked():
            metodo_pg = "Dinheiro"
            lista_pagamento.append([None,valor,data])
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ data atual: ",data,"Data de amanha: ",date)

        elif self.CB_debito.isChecked():
            metodo_pg = "Debito"
            modified_date = data + timedelta(days=1)
            lista_pagamento.append([None,valor,modified_date])
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ data atual: ",data,"Data de amanha: ",modified_date)
        elif self.CB_credito.isChecked():
            vezes = int(self.LB_vezes.text())
            metodo_pg = "Credito "+self.LB_vezes.text()+"x"
            valor_parcelado = (valor/vezes)
            cont = 1
            for i in range(vezes):
                modified_date = data + relativedelta(months=+cont)
                lista_pagamento.append([None,valor_parcelado,modified_date])
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ data atual: ",data,"Data de amanha: ",modified_date)
                cont = cont + 1
            # fim
        print("aux_cliente: ", self.aux_cliente)
        print("index_cliente: ", index_cliente)
        com = Compras(self.LE_local.text(), valor, data, frete, self.aux_cliente[index_cliente-1], self.aux_bairro[index_bairro-1], metodo_pg)
        print("Compra: ", [self.LE_local.text(), valor, data, frete, self.CB_cliente.currentText(), self.CB_bairro.currentText(), metodo_pg])
        print("")
        id_compra = com.ultima_compra()
        print("id_compra: ", id_compra)
        for value in self.itens:
            iten = Itens(value[1],value[0],value[3], value[2], id_compra)
            if value[5] is not None:
                id_iten = iten.ultimo_iten()
                Desconto = Descontos(value[5], id_iten, id_compra)
        for value in lista_pagamento:
            pagamento = Pagamento(id_compra, value[1], value[2])
        lista = [["Macacã", "XG", "Onça","100.0"], ["Vestido Longo", "GG", "Preto","90.0"],["Vestido curto", "M", "Branco","70"]]
        compra = ["Rua dos Romeros", "200.0", "18-05-2020","10","Ana Maria","Olaria","Dinheiro"]
        Documento(lista,compra)
        #documento = Documento([[self.LE_local.text(), valor, data, frete, self.CB_cliente.currentText(), self.CB_bairro.currentText(), metodo_pg],[None]])
        self.cancelar()

    def cancelar(self):
        self.Form_compras.close()

    def mais(self):
        self.Form_itens = QtWidgets.QDialog()
        self.ui = Ui_Form_itens(self)
        self.ui.setupUi(self.Form_itens)
        self.Form_itens.show()

    def menos(self):
        print("Entrou")
        for value in self.itens:
            if (value[0] == self.iten_selecionado[0]) and (value[1] == self.iten_selecionado[1]) and (value[4] == self.iten_selecionado[4]):
                print('Achei')
                self.itens.remove(value)
        self.atualizar()
        print("Deu sinal")

    def iten_click(self, it, col):
        print("it: ",it)
        print("col: ", col)
        print("Tipo ",it.data(0 ,0))
        print("Tamanho ",it.data(1 ,0))
        print("Ëstampa ",it.data(2 ,2))
        print("Vaalor ",it.data(3 ,0))
        print("Identificador ",it.data(4 ,0))
        print("Desconto ",it.data(5 ,0))
        self.iten_selecionado = [it.data(0 ,0),it.data(1 ,0),it.data(2 ,2), it.data(3 ,0), it.data(4 ,0), it.data(5 ,0)]

    def atualizar(self):
        self.LW_itens.clear()
        lista = []
        valor_total = 0
        for i in self.itens:
            print("Entrou no for **********", i)
            lista.append(QtWidgets.QTreeWidgetItem([i[0],i[1],i[2],i[3],i[5]]))
            valor_total = valor_total + float(i[3])
        self.LW_itens.addTopLevelItems(lista)
        print(self.itens)
        if self.CB_frete.isChecked():
            valor_total = valor_total + float(self.LE_frete.text())
        self.LE_valor.setText("R$ "+str(valor_total))
        if self.itens == []:
            self.LE_valor.setText("R$ "+str(0))

    def contar_bairro(self):
        banco = Bd_manage()
        self.aux_bairro = []
        return banco.mostrar_bairros()

    def contar_cliente(self):
        banco = Bd_manage()
        self.aux_cliente = []
        return banco.mostrar_clientes()

    def status_CB(self):
        if self.CB_frete.isChecked():
            self.LE_frete.setDisabled(False)
            self.LE_frete.setText("10")
        else:
            self.LE_frete.setDisabled(True)
            self.LE_frete.setText(None)
        self.atualizar()

    def status_dinheiro(self):
        if self.CB_dinheiro.isChecked():
            self.CB_debito.setChecked(False)
            self.CB_credito.setChecked(False)
            self.LB_vezes.setDisabled(True)
            self.LB_vezes.setText(None)

    def status_debito(self):
        if self.CB_debito.isChecked():
            self.CB_credito.setChecked(False)
            self.CB_dinheiro.setChecked(False)
            self.LB_vezes.setDisabled(True)
            self.LB_vezes.setText(None)

    def status_credito(self):
        if self.CB_credito.isChecked():
            self.CB_debito.setChecked(False)
            self.CB_dinheiro.setChecked(False)
            self.LB_vezes.setDisabled(False)

    def add_cliente(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_cliente(self)
        self.ui.setupUi(self.window)
        self.window.show()

    def add_bairro(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_bairro(self)
        self.ui.setupUi(self.window)
        self.window.show()

    def atualizar_endereco(self):
        if self.autorizacao:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            index_cliente = self.CB_cliente.currentIndex()
            cod_cliente = self.aux_cliente[index_cliente]

            print("cod cliente: ",cod_cliente)
            banco = Bd_manage()
            cliente = banco.pesquisar_clientes(cod_cliente)
            print(cliente)
            if (cliente[0][2] in self.aux_bairro):
                print("Ächouuuuuu")
                inbh = self.aux_bairro.index(cliente[0][2])
                self.CB_bairro.setCurrentIndex(inbh)
                self.LE_local.setText(cliente[0][4])

    def contar_clientes(self):
        self.autorizacao = False
        self.CB_cliente.clear()
        self.aux_cliente.clear()
        for value in self.contar_cliente():
            self.CB_cliente.addItem(value[1])
            self.aux_cliente.append(value[0])
        self.autorizacao = True

    def contar_bairros(self):
        self.autorizacao = False
        self.CB_bairro.clear()
        self.aux_bairro.clear()
        for value in self.contar_bairro():
            self.CB_bairro.addItem(value[1])
            self.aux_bairro.append(value[0])
        self.autorizacao = True

    def setupUi(self, Form_compras):
        self.Form_compras = Form_compras
        Form_compras.setObjectName("Form_compras")
        Form_compras.resize(667, 452)
        self.gridLayout = QtWidgets.QGridLayout(Form_compras)
        self.gridLayout.setObjectName("gridLayout")
        self.CB_debito = QtWidgets.QCheckBox(Form_compras)
        self.CB_debito.setObjectName("CB_debito")
        self.gridLayout.addWidget(self.CB_debito, 11, 3, 1, 1)
        self.CB_credito = QtWidgets.QCheckBox(Form_compras)
        self.CB_credito.setObjectName("CB_credito")
        self.gridLayout.addWidget(self.CB_credito, 11, 4, 1, 1)
        self.LB_data = QtWidgets.QLabel(Form_compras)
        self.LB_data.setObjectName("LB_data")
        self.gridLayout.addWidget(self.LB_data, 8, 0, 1, 1)
        self.label_valor = QtWidgets.QLabel(Form_compras)
        self.label_valor.setObjectName("label_valor")
        self.gridLayout.addWidget(self.label_valor, 10, 0, 1, 1)
        self.label_local = QtWidgets.QLabel(Form_compras)
        self.label_local.setObjectName("label_local")
        self.gridLayout.addWidget(self.label_local, 6, 0, 1, 1)
        self.label_frete = QtWidgets.QLabel(Form_compras)
        self.label_frete.setObjectName("label_frete")
        self.gridLayout.addWidget(self.label_frete, 7, 0, 1, 1)
        self.LW_itens = QtWidgets.QTreeWidget(Form_compras)
        self.LW_itens.setObjectName("LW_itens")
        self.gridLayout.addWidget(self.LW_itens, 0, 0, 4, 7)
        self.LW_itens.setHeaderLabels(['Tipo', 'Tamanho', 'Estampa', 'Valor' , 'Desconto'])
        self.LW_itens.itemClicked.connect(self.iten_click)
        self.label_bairro = QtWidgets.QLabel(Form_compras)
        self.label_bairro.setObjectName("label_bairro")
        self.gridLayout.addWidget(self.label_bairro, 5, 0, 1, 1)
        self.PB_cancelar = QtWidgets.QPushButton(Form_compras)
        self.PB_cancelar.setObjectName("PB_cancelar")
        self.PB_cancelar.clicked.connect(self.cancelar)
        self.gridLayout.addWidget(self.PB_cancelar, 13, 7, 1, 1)
        self.label_cliente = QtWidgets.QLabel(Form_compras)
        self.label_cliente.setObjectName("label_cliente")
        self.gridLayout.addWidget(self.label_cliente, 4, 0, 1, 1)
        self.PB_add_cliente = QtWidgets.QPushButton(Form_compras)
        self.PB_add_cliente.setObjectName("PB_add_cliente")
        self.gridLayout.addWidget(self.PB_add_cliente, 4, 6, 1, 1)
        self.PB_add_cliente.clicked.connect(self.add_cliente)
        self.CB_cliente = QtWidgets.QComboBox(Form_compras)
        self.CB_cliente.setObjectName("CB_cliente")
        for value in self.contar_cliente():
            self.CB_cliente.addItem(value[1])
            self.aux_cliente.append(value[0])
        self.gridLayout.addWidget(self.CB_cliente, 4, 1, 1, 5)
        self.CB_cliente.currentIndexChanged.connect(self.atualizar_endereco)
        self.PB_add_bairro = QtWidgets.QPushButton(Form_compras)
        self.PB_add_bairro.setObjectName("PB_add_bairro")
        self.gridLayout.addWidget(self.PB_add_bairro, 5, 6, 1, 1)
        self.PB_add_bairro.clicked.connect(self.add_bairro)
        self.CB_frete = QtWidgets.QCheckBox(Form_compras)
        self.CB_frete.setObjectName("CB_frete")
        self.gridLayout.addWidget(self.CB_frete, 7, 6, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(Form_compras)
        self.dateEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("dd/MM/yyyy")
        d = QDate(date.today().year, date.today().month, date.today().day)
        self.dateEdit.setDate(d)
        self.gridLayout.addWidget(self.dateEdit, 8, 1, 1, 3)
        self.LE_frete = QtWidgets.QLineEdit(Form_compras)
        self.LE_frete.setObjectName("LE_frete")
        self.gridLayout.addWidget(self.LE_frete, 7, 1, 1, 5)
        self.LE_frete.setDisabled(True)
        self.LE_frete.returnPressed.connect(self.atualizar)
        self.CB_frete.stateChanged.connect(self.status_CB)
        self.CB_bairro = QtWidgets.QComboBox(Form_compras)
        self.CB_bairro.setObjectName("CB_bairro")
        for value in self.contar_bairro():
            self.CB_bairro.addItem(value[1])
            self.aux_bairro.append(value[0])
        self.gridLayout.addWidget(self.CB_bairro, 5, 1, 1, 5)
        self.LE_valor = QtWidgets.QLineEdit(Form_compras)
        self.LE_valor.setObjectName("LE_valor")
        self.gridLayout.addWidget(self.LE_valor, 10, 1, 1, 5)
        self.LE_valor.setDisabled(True)
        self.LE_valor.setText("R$ "+str(0))
        self.LE_local = QtWidgets.QLineEdit(Form_compras)
        self.LE_local.setObjectName("LE_local")
        self.gridLayout.addWidget(self.LE_local, 6, 1, 1, 5)
        self.PB_menos_item = QtWidgets.QPushButton(Form_compras)
        self.PB_menos_item.setObjectName("PB_menos_item")
        self.PB_menos_item.clicked.connect(self.menos)
        self.gridLayout.addWidget(self.PB_menos_item, 1, 7, 1, 1)
        self.label_pg = QtWidgets.QLabel(Form_compras)
        self.label_pg.setObjectName("label_pg")
        self.gridLayout.addWidget(self.label_pg, 11, 0, 1, 1)
        self.PB_salvar = QtWidgets.QPushButton(Form_compras)
        self.PB_salvar.setObjectName("PB_salvar")
        self.PB_salvar.clicked.connect(self.salvar)
        self.gridLayout.addWidget(self.PB_salvar, 13, 6, 1, 1)
        self.LB_vezes = QtWidgets.QLineEdit(Form_compras)
        self.LB_vezes.setText("")
        self.LB_vezes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LB_vezes.setObjectName("LB_vezes")
        self.gridLayout.addWidget(self.LB_vezes, 11, 5, 1, 1)
        self.CB_dinheiro = QtWidgets.QCheckBox(Form_compras)
        self.CB_dinheiro.setObjectName("CB_dinheiro")
        self.gridLayout.addWidget(self.CB_dinheiro, 11, 1, 1, 1)
        self.CB_dinheiro.setChecked(True)
        self.label_vezes = QtWidgets.QLabel(Form_compras)
        self.label_vezes.setObjectName("label_vezes")
        self.gridLayout.addWidget(self.label_vezes, 11, 6, 1, 1)
        self.PB_add_item = QtWidgets.QPushButton(Form_compras)
        self.PB_add_item.setObjectName("PB_add_item")
        self.gridLayout.addWidget(self.PB_add_item, 0, 7, 1, 1)
        self.PB_add_item.clicked.connect(self.mais)
        self.LB_vezes.setDisabled(True)

        self.CB_dinheiro.stateChanged.connect(self.status_dinheiro)
        self.CB_debito.stateChanged.connect(self.status_debito)
        self.CB_credito.stateChanged.connect(self.status_credito)


        self.retranslateUi(Form_compras)
        QtCore.QMetaObject.connectSlotsByName(Form_compras)

    def retranslateUi(self, Form_compras):
        _translate = QtCore.QCoreApplication.translate
        Form_compras.setWindowTitle(_translate("Form_compras", "Compras"))
        Form_compras.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.CB_debito.setText(_translate("Form_compras", "Debito"))
        self.CB_credito.setText(_translate("Form_compras", "Credito"))
        self.LB_data.setText(_translate("Form_compras", "Data do pedido:"))
        self.label_valor.setText(_translate("Form_compras", "Valor total:"))
        self.label_local.setText(_translate("Form_compras", "Local de entrega:"))
        self.label_frete.setText(_translate("Form_compras", "Frete:"))
        self.label_bairro.setText(_translate("Form_compras", "Bairro:"))
        self.PB_cancelar.setText(_translate("Form_compras", "Cancelar"))
        self.label_cliente.setText(_translate("Form_compras", "Cliente:"))
        self.PB_add_cliente.setText(_translate("Form_compras", "Adicionar"))
        self.PB_add_bairro.setText(_translate("Form_compras", "Adicionar"))
        self.CB_frete.setText(_translate("Form_compras", "Cobrar"))
        self.PB_menos_item.setText(_translate("Form_compras", "Remover"))
        self.label_pg.setText(_translate("Form_compras", "Metodo de PG."))
        self.PB_salvar.setText(_translate("Form_compras", "Salvar"))
        self.CB_dinheiro.setText(_translate("Form_compras", "Dinheiro"))
        self.label_vezes.setText(_translate("Form_compras", "X Vezes"))
        self.PB_add_item.setText(_translate("Form_compras", "Adicionar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_compras = QtWidgets.QWidget()
    ui = Ui_Form_compras()
    ui.setupUi(Form_compras)
    Form_compras.show()
    sys.exit(app.exec_())
