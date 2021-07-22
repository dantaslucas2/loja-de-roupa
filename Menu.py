# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Compras_new2 import Ui_Form_compras
from Historico import Ui_Form_historico
from Configuracao import Ui_Form_configuracao
from menage import Bd_manage
import sys


class Ui_Form_menu(object):

    def abrir_historico(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_historico()
        self.ui.setupUi(self.window)
        self.window.show()

    def abrir_venda(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_compras()
        self.ui.setupUi(self.window)
        self.window.show()

    def abrir_configuracao(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_configuracao()
        self.ui.setupUi(self.window)
        self.window.show()

    def abrir_financeiro(self):
        bs = Bd_manage()
        print("Clientes : \n", bs.mostrar_clientes())
        print("Itens : \n", bs.mostrar_itens())
        print("Estampas : \n", bs.mostrar_estampas())
        print("Bairros : \n", bs.mostrar_bairros())
        print("Compras : \n", bs.mostrar_compras())

    def setupUi(self, Form_menu):
        Form_menu.setObjectName("Form_menu")
        Form_menu.resize(246, 247)
        self.splitter = QtWidgets.QSplitter(Form_menu)
        self.splitter.setGeometry(QtCore.QRect(50, 42, 151, 171))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.PB_venda = QtWidgets.QPushButton(self.splitter)
        self.PB_venda.setObjectName("PB_venda")
        self.PB_venda.clicked.connect(self.abrir_venda)
        self.PB_historico = QtWidgets.QPushButton(self.splitter)
        self.PB_historico.setObjectName("PB_historico")
        self.PB_historico.clicked.connect(self.abrir_historico)
        self.PB_financeiro = QtWidgets.QPushButton(self.splitter)
        self.PB_financeiro.setObjectName("PB_financeiro")
        self.PB_financeiro.clicked.connect(self.abrir_financeiro)
        self.PB_configuracao = QtWidgets.QPushButton(self.splitter)
        self.PB_configuracao.setObjectName("PB_configuracao")
        self.PB_configuracao.clicked.connect(self.abrir_configuracao)

        self.retranslateUi(Form_menu)
        QtCore.QMetaObject.connectSlotsByName(Form_menu)

    def retranslateUi(self, Form_menu):
        _translate = QtCore.QCoreApplication.translate
        Form_menu.setWindowTitle(_translate("Form_menu", "Menu"))
        Form_menu.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.PB_venda.setText(_translate("Form_menu", "Registrar Venda"))
        self.PB_configuracao.setText(_translate("Form_menu", "Configuração"))
        self.PB_historico.setText(_translate("Form_menu", "Historico de vendas"))
        self.PB_financeiro.setText(_translate("Form_menu", "Financeiro"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_menu = QtWidgets.QDialog()
    ui = Ui_Form_menu()
    ui.setupUi(Form_menu)
    Form_menu.show()
    sys.exit(app.exec_())
