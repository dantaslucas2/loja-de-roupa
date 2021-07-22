# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Itens.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Classes.iten import Itens
from menage import Bd_manage

class Ui_Form_itens(object):

    def __init__(self, windowpai):
        self.windowpai = windowpai

    def contar(self):
        banco = Bd_manage()
        return banco.mostrar_estampas()

    def cancelar(self):
        self.Form_itens.close()

    def salvar(self):
        if (self.CB_tipo.currentText() == ""):
            print("Informe algum tipo")
        else:
            print("Entrou no else")
            self.iten = [self.CB_tamanho.currentText(),self.CB_tipo.currentText(),self.CB_estampa.currentText()]
            self.windowpai.itens.append(self.iten)
            self.windowpai.atualizar()
            self.cancelar()

    def get(self):
        return self.iten

    def setupUi(self, Form_itens):
        self.iten = None
        self.Form_itens = Form_itens
        Form_itens.setObjectName("Form_itens")
        Form_itens.resize(337, 242)
        self.PB_salvar = QtWidgets.QPushButton(Form_itens)
        self.PB_salvar.setGeometry(QtCore.QRect(11, 182, 93, 28))
        self.PB_salvar.setObjectName("PB_salvar")
        self.PB_salvar.clicked.connect(self.salvar)
        self.PB_cancelar = QtWidgets.QPushButton(Form_itens)
        self.PB_cancelar.setGeometry(QtCore.QRect(226, 182, 93, 28))
        self.PB_cancelar.setObjectName("PB_cancelar")
        self.PB_cancelar.clicked.connect(self.cancelar)
        self.label_tamanho = QtWidgets.QLabel(Form_itens)
        self.label_tamanho.setGeometry(QtCore.QRect(11, 82, 59, 16))
        self.label_tamanho.setObjectName("label_tamanho")
        self.label_tipo = QtWidgets.QLabel(Form_itens)
        self.label_tipo.setGeometry(QtCore.QRect(11, 32, 30, 16))
        self.label_tipo.setObjectName("label_tipo")
        self.CB_tipo = QtWidgets.QComboBox(Form_itens)
        self.CB_tipo.setGeometry(QtCore.QRect(118, 32, 161, 22))
        self.CB_tipo.setObjectName("CB_tipo")
        self.CB_tipo.setFocus()
        self.CB_tipo.addItem("")
        self.CB_tipo.addItem("Macacão")
        self.CB_tipo.addItem("Macaquinho")
        self.CB_tipo.addItem("Vestido")
        self.CB_tipo.addItem("Vestido Longo")
        self.CB_tamanho = QtWidgets.QComboBox(Form_itens)
        self.CB_tamanho.setGeometry(QtCore.QRect(118, 82, 161, 22))
        self.CB_tamanho.setObjectName("CB_tamanho")
        self.CB_tamanho.addItem("")
        self.CB_tamanho.addItem("M")
        self.CB_tamanho.addItem("G")
        self.CB_tamanho.addItem("GG")
        self.CB_tamanho.addItem("XG")
        self.label_estampa = QtWidgets.QLabel(Form_itens)
        self.label_estampa.setGeometry(QtCore.QRect(11, 132, 54, 16))
        self.label_estampa.setObjectName("label_estampa")
        self.CB_estampa = QtWidgets.QComboBox(Form_itens)
        self.CB_estampa.setGeometry(QtCore.QRect(118, 132, 161, 22))
        self.CB_estampa.setObjectName("CB_estampa")
        self.CB_estampa.addItem("")
        for value in self.contar():
            self.CB_estampa.addItem(value[1])
        self.retranslateUi(Form_itens)
        QtCore.QMetaObject.connectSlotsByName(Form_itens)

    def retranslateUi(self, Form_itens):
        _translate = QtCore.QCoreApplication.translate
        Form_itens.setWindowTitle(_translate("Form_itens", "Iten"))
        self.PB_salvar.setText(_translate("Form_itens", "Salvar"))
        self.PB_cancelar.setText(_translate("Form_itens", "Cancelar"))
        self.label_tamanho.setText(_translate("Form_itens", "Tamanho:"))
        self.label_tipo.setText(_translate("Form_itens", "Tipo:"))
        self.label_estampa.setText(_translate("Form_itens", "Estampa:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_itens = QtWidgets.QDialog()
    ui = Ui_Form_itens()
    ui.setupUi(Form_itens)
    Form_itens.show()
    sys.exit(app.exec_())
