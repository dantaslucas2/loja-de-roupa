# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Historico.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget
from menage import Bd_manage

class Ui_Form_historico(object):

    def atualizar(self):
        self.LW_compras.clear()
        banco = Bd_manage()
        com = banco.mostrar_compras()
        for value in com:
            print("Value  ",value)
            if str(value[4]) == "None":
                frete = ""
            else:
                frete = "R$ "+str(value[4])
            cliente = banco.pesquisar_clientes(value[5])
            bairro = banco.pesquisar_bairros(value[6])
            l1 = QTreeWidgetItem([str(value[0]),cliente[0][1],bairro[0][1],"R$ "+str(value[2]), frete, value[7]])
            self.LW_compras.addTopLevelItem(l1)
            con = banco.pesquisar_itens_cod_compra(value[0])
            for i in con:
                print(i)
                l2 = QTreeWidgetItem([str(i[0]),str(i[2]),i[1],str(i[3])])
                l1.addChild(l2)
            #l1.addTopLevelItem(l2)
            # pesquisar itens com esse id de compras
            #
    def excluir(self):
        banco = Bd_manage()
        banco.deletar_pagamento_por_compra(self.iten_selecionado)
        banco.deletar_desconto_por_compra(self.iten_selecionado)
        banco.deletar_iten_por_compra(self.iten_selecionado)
        banco.deletar_compra(self.iten_selecionado)
        self.atualizar()
        print("Excluido")

    def cancelar(self):
        self.Form_historico.close()

    def iten_click(self, it, col):
        self.iten_selecionado = it.data(0 ,0)

    def setupUi(self, Form_historico):
        self.Form_historico = Form_historico
        self.Form_historico.setObjectName("Form_historico")
        self.Form_historico.resize(463, 346)
        self.LW_compras = QtWidgets.QTreeWidget(Form_historico)
        self.LW_compras.setGeometry(QtCore.QRect(10, 10, 441, 271))
        self.LW_compras.setObjectName("LW_compras")
        self.LW_compras.setHeaderLabels(['Compra', 'Cliente','Bairro', 'Valor total', 'Frete', 'Metodo de pagamento'])
        self.LW_compras.setColumnWidth(0, 10)
        self.LW_compras.setColumnWidth(1, 100)
        self.LW_compras.setColumnWidth(2, 60)
        self.LW_compras.setColumnWidth(3, 70)
        self.LW_compras.setColumnWidth(4, 70)
        self.LW_compras.itemClicked.connect(self.iten_click)
        self.atualizar()
        self.PB_excluir = QtWidgets.QPushButton(Form_historico)
        self.PB_excluir.setGeometry(QtCore.QRect(10, 300, 141, 31))
        self.PB_excluir.setObjectName("PB_excluir")
        self.PB_excluir.clicked.connect(self.excluir)
        self.PB_alterar = QtWidgets.QPushButton(Form_historico)
        self.PB_alterar.setGeometry(QtCore.QRect(160, 300, 141, 31))
        self.PB_alterar.setObjectName("PB_alterar")
        self.PB_voltar = QtWidgets.QPushButton(Form_historico)
        self.PB_voltar.setGeometry(QtCore.QRect(310, 300, 141, 31))
        self.PB_voltar.setObjectName("PB_voltar")
        self.PB_voltar.clicked.connect(self.cancelar)

        self.retranslateUi(Form_historico)
        QtCore.QMetaObject.connectSlotsByName(Form_historico)

    def retranslateUi(self, Form_historico):
        _translate = QtCore.QCoreApplication.translate
        Form_historico.setWindowTitle(_translate("Form_historico", "Histórico de compras"))
        Form_historico.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.PB_excluir.setText(_translate("Form_historico", "Excluir"))
        self.PB_alterar.setText(_translate("Form_historico", "Alterar"))
        self.PB_voltar.setText(_translate("Form_historico", "Voltar"))
