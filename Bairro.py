# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bairro.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Classes.bairro import Bairro


class Ui_Form_bairro(object):

    def __init__(self, windowpai=None):
        self.windowpai = windowpai

    def salvar(self):
        bairro = Bairro(self.LE_nome.text())
        if self.windowpai is None:
            pass
        else:
            self.windowpai.contar_bairros()
        self.cancelar()

    def cancelar(self):
        self.Form_bairro.close()

    def setupUi(self, Form_bairro):
        self.Form_bairro = Form_bairro
        Form_bairro.setObjectName("Form_bairro")
        Form_bairro.resize(238, 127)
        self.gridLayout = QtWidgets.QGridLayout(Form_bairro)
        self.gridLayout.setObjectName("gridLayout")
        self.PB_cancelar = QtWidgets.QPushButton(Form_bairro)
        self.PB_cancelar.setObjectName("PB_cancelar")
        self.gridLayout.addWidget(self.PB_cancelar, 1, 2, 1, 1)
        self.PB_cancelar.clicked.connect(self.cancelar)
        self.PB_salvar = QtWidgets.QPushButton(Form_bairro)
        self.PB_salvar.setObjectName("PB_salvar")
        self.PB_salvar.clicked.connect(self.salvar)
        self.gridLayout.addWidget(self.PB_salvar, 1, 1, 1, 1)
        self.LE_nome = QtWidgets.QLineEdit(Form_bairro)
        self.LE_nome.setObjectName("LE_nome")
        self.gridLayout.addWidget(self.LE_nome, 0, 1, 1, 2)
        self.label_nome = QtWidgets.QLabel(Form_bairro)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)

        self.retranslateUi(Form_bairro)
        QtCore.QMetaObject.connectSlotsByName(Form_bairro)

    def retranslateUi(self, Form_bairro):
        _translate = QtCore.QCoreApplication.translate
        Form_bairro.setWindowTitle(_translate("Form_bairro", "Cadastro de bairo"))
        Form_bairro.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.PB_cancelar.setText(_translate("Form_bairro", "Cancelar"))
        self.PB_salvar.setText(_translate("Form_bairro", "Salvar"))
        self.label_nome.setText(_translate("Form_bairro", "   Bairro:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_bairro = QtWidgets.QWidget()
    ui = Ui_Form_bairro()
    ui.setupUi(Form_bairro)
    Form_bairro.show()
    sys.exit(app.exec_())
