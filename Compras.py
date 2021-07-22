# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Compras.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Classes.compras import Compras
from Classes.iten import Itens
from Itens import Ui_Form_itens
from Impress.Impress import Documento
import sys
from menage import Bd_manage

class Ui_Form_compras(object):

    def __init__(self):
        self.itens = []
        self.descontos = []

    def salvar(self):
        if (self.LE_valor.text() == ""):
            print("VAZIOOOOOOOOOOOOOOOOOOOOO")
            self.LE_valor.setText("0")
        index_cliente = self.CB_cliente.currentIndex()
        index_bairro = self.CB_bairro.currentIndex()
        com = Compras(self.LE_local.text(), self.LE_valor.text(), self.aux_cliente[index_cliente], self.aux_bairro[index_bairro])
        id_temp = com.ultima_compra()
        print("id_temp: ", id_temp)
        for value in self.itens:
            iten = Itens(value[0],value[1],value[2], id_temp)
        self.cancelar()

    def cancelar(self):
        self.Form_compras.close()

    def mais(self):
        self.ui.setupUi(self.window)
        self.window.show()

    def menos(self):
        print("Entrou")
        for value in self.itens:
            if (value.tamanho == self.iten_selecionado[0]) and (value.tipo == self.iten_selecionado[1]):
                print('Achei')
                self.itens.remove(value)
        self.atualizar()
        print("Deu sinal")

    def iten_click(self, it, col):
        print(it, col, it.text(col))
        print(it.data(0 ,0))
        print(it.data(1 ,0))
        print(it.data(2 ,2))

        self.iten_selecionado = [it.data(0 ,0),it.data(1 ,0),it.data(2 ,2)]

    def atualizar(self):
        for i in range(15):
            self.LW_itens.takeTopLevelItem(0)
        for i in self.itens:
            print("Entrou no for **********", i)
            QtWidgets.QTreeWidgetItem(self.LW_itens,[i[0],i[1],i[2]])
        print(self.itens)
        if self.itens == []:
            self.LE_valor.setDisabled(True)
        else:
            self.LE_valor.setDisabled(False)

    def contar_bairro(self):
        banco = Bd_manage()
        self.aux_bairro = []
        return banco.mostrar_bairros()

    def contar_cliente(self):
        banco = Bd_manage()
        self.aux_cliente = []
        return banco.mostrar_clientes()


    def setupUi(self, Form_compras):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_itens(self)
        self.itens
        self.Form_compras = Form_compras
        Form_compras.setObjectName("Form_compras")
        Form_compras.resize(345, 344)
        self.LW_itens = QtWidgets.QTreeWidget(Form_compras)
        self.LW_itens.setGeometry(QtCore.QRect(11, 40, 330, 141))
        self.LW_itens.setObjectName("LW_itens")
        self.LW_itens.setHeaderLabels(['Tipo', 'Tamanho', 'Estampa'])
        self.LW_itens.itemClicked.connect(self.iten_click)
        self.label_local = QtWidgets.QLabel(Form_compras)
        self.label_local.setGeometry(QtCore.QRect(11, 250, 93, 16))
        self.label_local.setObjectName("label_local")
        self.label_valor = QtWidgets.QLabel(Form_compras)
        self.label_valor.setGeometry(QtCore.QRect(11, 280, 35, 16))
        self.label_valor.setObjectName("label_valor")
        self.label_itens = QtWidgets.QLabel(Form_compras)
        self.label_itens.setGeometry(QtCore.QRect(11, 20, 33, 16))
        self.label_itens.setObjectName("label_itens")
        self.label_bairro = QtWidgets.QLabel(Form_compras)
        self.label_bairro.setGeometry(QtCore.QRect(11, 222, 39, 16))
        self.label_bairro.setObjectName("label_bairro")
        self.PB_salvar = QtWidgets.QPushButton(Form_compras)
        self.PB_salvar.setGeometry(QtCore.QRect(11, 309, 101, 28))
        self.PB_salvar.setObjectName("PB_salvar")
        self.PB_salvar.clicked.connect(self.salvar)
        self.PB_cancelar = QtWidgets.QPushButton(Form_compras)
        self.PB_cancelar.setGeometry(QtCore.QRect(202, 309, 101, 28))
        self.PB_cancelar.setObjectName("PB_cancelar")
        self.PB_cancelar.clicked.connect(self.cancelar)
        self.CB_bairro = QtWidgets.QComboBox(Form_compras)
        self.CB_bairro.setGeometry(QtCore.QRect(60, 222, 151, 22))
        self.CB_bairro.setObjectName("CB_bairro")
        for value in self.contar_bairro():
            self.CB_bairro.addItem(value[1])
            self.aux_bairro.append(value[0])
        self.LE_local = QtWidgets.QLineEdit(Form_compras)
        self.LE_local.setGeometry(QtCore.QRect(111, 251, 137, 22))
        self.LE_local.setObjectName("LE_local")
        self.LE_valor = QtWidgets.QLineEdit(Form_compras)
        self.LE_valor.setGeometry(QtCore.QRect(60, 280, 88, 22))
        self.LE_valor.setObjectName("LE_valor")
        self.PB_mais = QtWidgets.QPushButton(Form_compras)
        self.PB_mais.setGeometry(QtCore.QRect(230, 190, 51, 28))
        self.PB_mais.setObjectName("PB_mais")
        self.PB_mais.clicked.connect(self.mais)
        self.PB_menos = QtWidgets.QPushButton(Form_compras)
        self.PB_menos.setGeometry(QtCore.QRect(290, 190, 51, 28))
        self.PB_menos.setObjectName("PB_menos")
        self.PB_menos.clicked.connect(self.menos)
        self.label_cliente = QtWidgets.QLabel(Form_compras)
        self.label_cliente.setGeometry(QtCore.QRect(10, 190, 55, 16))
        self.label_cliente.setObjectName("label_cliente")
        self.CB_cliente = QtWidgets.QComboBox(Form_compras)
        self.CB_cliente.setGeometry(QtCore.QRect(70, 190, 151, 22))
        self.CB_cliente.setObjectName("CB_cliente")
        self.LE_valor.setDisabled(True)
        for value in self.contar_cliente():
            self.CB_cliente.addItem(value[1])
            self.aux_cliente.append(value[0])

        self.retranslateUi(Form_compras)
        QtCore.QMetaObject.connectSlotsByName(Form_compras)

    def retranslateUi(self, Form_compras):
        _translate = QtCore.QCoreApplication.translate
        Form_compras.setWindowTitle(_translate("Form_compras", "Compras"))
        Form_compras.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.label_local.setText(_translate("Form_compras", "Local de entrga:"))
        self.label_valor.setText(_translate("Form_compras", "Valor:"))
        self.label_itens.setText(_translate("Form_compras", "Itens:"))
        self.label_bairro.setText(_translate("Form_compras", "Bairro:"))
        self.label_cliente.setText(_translate("Form_compras", "Cliente:"))
        self.PB_salvar.setText(_translate("Form_compras", "Salvar"))
        self.PB_cancelar.setText(_translate("Form_compras", "Cancelar"))
        self.PB_mais.setText(_translate("Form_compras", "+"))
        self.PB_menos.setText(_translate("Form_compras", "-"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_menu = QtWidgets.QDialog()
    ui = Ui_Form_compras()
    ui.setupUi(Ui_Form_compras)
    Ui_Form_compras.show()
    sys.exit(app.exec_())
