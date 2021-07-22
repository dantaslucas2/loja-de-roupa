# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cliente.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Classes.Cliente import Clientes
from menage import Bd_manage


class Ui_Form_cliente(object):

    def __init__(self, windowpai=None):
        print("Windowpai", windowpai)
        self.windowpai = windowpai

    def cancelar(self):
        self.Form_cliente.close()

    def salvar(self):
        print(self.LE_nome.text())
        index_bairro = self.CB_bairro.currentIndex()
        c1 = Clientes(self.LE_nome.text(), self.aux_bairro[index_bairro],self.LE_telefone.text(), self.LE_endereco.text())
        if self.windowpai is None:
            pass
        else:
            self.windowpai.contar_clientes()
        self.cancelar()

    def contar_bairro(self):
        banco = Bd_manage()
        self.aux_bairro = []
        return banco.mostrar_bairros()

    def setupUi(self, Form_cliente):
        self.Form_cliente = Form_cliente
        Form_cliente.setObjectName("Form_cliente")
        Form_cliente.resize(259, 240)
        self.gridLayout = QtWidgets.QGridLayout(Form_cliente)
        self.gridLayout.setObjectName("gridLayout")
        self.label_nome = QtWidgets.QLabel(Form_cliente)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.LE_nome = QtWidgets.QLineEdit(Form_cliente)
        self.LE_nome.setObjectName("LE_nome")
        self.gridLayout.addWidget(self.LE_nome, 0, 1, 1, 2)
        self.label_telefone = QtWidgets.QLabel(Form_cliente)
        self.label_telefone.setObjectName("label_telefone")
        self.gridLayout.addWidget(self.label_telefone, 1, 0, 1, 1)
        self.LE_telefone = QtWidgets.QLineEdit(Form_cliente)
        self.LE_telefone.setObjectName("LE_telefone")
        self.gridLayout.addWidget(self.LE_telefone, 1, 1, 1, 2)
        self.label_endereco = QtWidgets.QLabel(Form_cliente)
        self.label_endereco.setObjectName("label_endereco")
        self.gridLayout.addWidget(self.label_endereco, 2, 0, 1, 1)
        self.LE_endereco = QtWidgets.QLineEdit(Form_cliente)
        self.LE_endereco.setObjectName("LE_endereco")
        self.gridLayout.addWidget(self.LE_endereco, 2, 1, 1, 2)
        self.label_bairro = QtWidgets.QLabel(Form_cliente)
        self.label_bairro.setObjectName("label_bairro")
        self.gridLayout.addWidget(self.label_bairro, 3, 0, 1, 1)
        self.CB_bairro = QtWidgets.QComboBox(Form_cliente)
        self.CB_bairro.setObjectName("CB_bairro")
        self.gridLayout.addWidget(self.CB_bairro, 3, 1, 1, 2)
        for value in self.contar_bairro():
            self.CB_bairro.addItem(value[1])
            self.aux_bairro.append(value[0])
        self.PB_salvar = QtWidgets.QPushButton(Form_cliente)
        self.PB_salvar.setObjectName("PB_salvar")
        self.gridLayout.addWidget(self.PB_salvar, 4, 1, 1, 1)
        self.PB_salvar.clicked.connect(self.salvar)
        self.PB_cancelar = QtWidgets.QPushButton(Form_cliente)
        self.PB_cancelar.setObjectName("PB_cancelar")
        self.gridLayout.addWidget(self.PB_cancelar, 4, 2, 1, 1)
        self.PB_cancelar.clicked.connect(self.cancelar)


        self.retranslateUi(Form_cliente)
        QtCore.QMetaObject.connectSlotsByName(Form_cliente)

    def retranslateUi(self, Form_cliente):
        _translate = QtCore.QCoreApplication.translate
        Form_cliente.setWindowTitle(_translate("Form_cliente", "Cadastro de cliente"))
        Form_cliente.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.label_nome.setText(_translate("Form_cliente", "  Nome:"))
        self.label_telefone.setText(_translate("Form_cliente", "  Telefone:"))
        self.label_endereco.setText(_translate("Form_cliente", "  Endereço:"))
        self.label_bairro.setText(_translate("Form_cliente", "  Bairro:"))
        self.PB_salvar.setText(_translate("Form_cliente", "Salvar"))
        self.PB_cancelar.setText(_translate("Form_cliente", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_cliente = QtWidgets.QWidget()
    ui = Ui_Form_cliente()
    ui.setupUi(Form_cliente)
    Form_cliente.show()
    sys.exit(app.exec_())
