# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Configuracao.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Estampa import Ui_Form_estampa
from Cliente import Ui_Form_cliente
from Bairro import Ui_Form_bairro

class Ui_Form_configuracao(object):

    def estampa(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_estampa()
        self.ui.setupUi(self.window)
        self.window.show()

    def cliente(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_cliente()
        self.ui.setupUi(self.window)
        self.window.show()

    def bairro(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_bairro()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form_configuracao):
        Form_configuracao.setObjectName("Form_configuracao")
        Form_configuracao.resize(212, 296)
        self.PB_cliente = QtWidgets.QPushButton(Form_configuracao)
        self.PB_cliente.setGeometry(QtCore.QRect(11, 41, 191, 31))
        self.PB_cliente.setObjectName("PB_cliente")
        self.PB_cliente.clicked.connect(self.cliente)
        self.PB_estampa = QtWidgets.QPushButton(Form_configuracao)
        self.PB_estampa.setGeometry(QtCore.QRect(11, 109, 191, 31))
        self.PB_estampa.setObjectName("PB_estampa")
        self.PB_estampa.clicked.connect(self.estampa)
        self.PB_bairro = QtWidgets.QPushButton(Form_configuracao)
        self.PB_bairro.setGeometry(QtCore.QRect(11, 177, 191, 31))
        self.PB_bairro.setObjectName("PB_bairro")
        self.PB_bairro.clicked.connect(self.bairro)
        self.PB_tipo = QtWidgets.QPushButton(Form_configuracao)
        self.PB_tipo.setGeometry(QtCore.QRect(11, 245, 191, 31))
        self.PB_tipo.setObjectName("PB_tipo")

        self.retranslateUi(Form_configuracao)
        QtCore.QMetaObject.connectSlotsByName(Form_configuracao)

    def retranslateUi(self, Form_configuracao):
        _translate = QtCore.QCoreApplication.translate
        Form_configuracao.setWindowTitle(_translate("Form_configuracao", "Configuração"))
        Form_configuracao.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.PB_cliente.setText(_translate("Form_configuracao", "Criar Cliente"))
        self.PB_estampa.setText(_translate("Form_configuracao", "Criar Estampa"))
        self.PB_bairro.setText(_translate("Form_configuracao", "Criar Bairro"))
        self.PB_tipo.setText(_translate("Form_configuracao", "Criar Tipo"))
