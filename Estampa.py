# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Estampa.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Classes.estampa import Estampa

class Ui_Form_estampa(object):

    def salvar(self):
        e =Estampa(self.LE_nome.text())
        self.cancelar()

    def cancelar(self):
        self.Form_estampa.close()

    def setupUi(self, Form_estampa):
        self.Form_estampa = Form_estampa
        Form_estampa.setObjectName("Form_estampa")
        Form_estampa.resize(268, 165)
        self.label_nome = QtWidgets.QLabel(Form_estampa)
        self.label_nome.setGeometry(QtCore.QRect(11, 50, 121, 16))
        self.label_nome.setObjectName("label_nome")
        self.LE_nome = QtWidgets.QLineEdit(Form_estampa)
        self.LE_nome.setGeometry(QtCore.QRect(127, 50, 121, 22))
        self.LE_nome.setObjectName("LE_nome")
        self.PB_salvar = QtWidgets.QPushButton(Form_estampa)
        self.PB_salvar.setGeometry(QtCore.QRect(11, 111, 93, 28))
        self.PB_salvar.setObjectName("PB_salvar")
        self.PB_salvar.clicked.connect(self.salvar)
        self.PB_cancelar = QtWidgets.QPushButton(Form_estampa)
        self.PB_cancelar.setGeometry(QtCore.QRect(160, 110, 93, 28))
        self.PB_cancelar.setObjectName("PB_cancelar")
        self.PB_cancelar.clicked.connect(self.cancelar)

        self.retranslateUi(Form_estampa)
        QtCore.QMetaObject.connectSlotsByName(Form_estampa)

    def retranslateUi(self, Form_estampa):
        _translate = QtCore.QCoreApplication.translate
        Form_estampa.setWindowTitle(_translate("Form_estampa", "Estampa"))
        Form_estampa.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.label_nome.setText(_translate("Form_estampa", "Nome da estampa:"))
        self.PB_salvar.setText(_translate("Form_estampa", "Salvar"))
        self.PB_cancelar.setText(_translate("Form_estampa", "Cancelar"))
