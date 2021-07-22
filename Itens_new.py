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
from random import randint

class Ui_Form_itens(object):

    def __init__(self, windowpai):
        print("Windowpai", windowpai)
        self.windowpai = windowpai

    def contar(self):
        banco = Bd_manage()
        return banco.mostrar_estampas()

    def cancelar(self):
        #self.windowpai.window.close()
        self.Form_itens.close()

    def salvar(self):
        if ((self.CB_tipo.currentText() == "") or (self.CB_tamanho.currentText() == "") or (self.CB_estampa.currentText() == "")):
            print("Preencha os campos tipo, tamanho e estampa")
        else:
            if (self.CB_desconto.isChecked()):
                desconto = self.LE_desconto.text()
            else:
                desconto = None
            print("-******************", self.CB_tipo.currentText())
            print("Entrou no else")
            self.iten = [self.CB_tipo.currentText(),self.CB_tamanho.currentText(),self.CB_estampa.currentText(), self.LE_valor.text(), str(randint(0,1000)), desconto]
            self.windowpai.itens.append(self.iten)
            self.windowpai.atualizar()
            self.cancelar()

    def get(self):
        return self.iten

    def status_CB(self):
        if self.CB_desconto.isChecked():
            self.LE_desconto.setDisabled(False)
            self.precificar()
        else:
            self.LE_desconto.setDisabled(True)
            self.LE_desconto.setText("0")
            self.precificar()

    def precificar(self):
        if ((self.CB_tipo.currentText() != "") and (self.CB_tamanho.currentText() != "") and (self.CB_estampa.currentText() != "")):
            if ((self.CB_tipo.currentText() == "Macacão") or self.CB_tipo.currentText() == "Vestido Longo"):
                if ((self.CB_tamanho.currentText() == "M") or self.CB_tamanho.currentText() == "G"):
                    print("macacão/vestido longo - M/G") # valor 100
                    if (self.CB_desconto.isChecked()):
                        print("Com desconto")
                        valor_final = str( 100.0 - float(self.LE_desconto.text()) )
                        self.LE_valor.setText(valor_final)
                    else:
                        print("Sem desconto")
                        self.LE_valor.setText("100.0")
                else:
                    print("macacão/vestido longo - GG/XG") # valor 120
                    if (self.CB_desconto.isChecked()):
                        print("Com desconto")
                        valor_final = str( 120.0 - float(self.LE_desconto.text()) )
                        self.LE_valor.setText(valor_final)
                    else:
                        print("Sem desconto")
                        self.LE_valor.setText("120.0")
            elif ((self.CB_tipo.currentText() == "Macaquinho") or self.CB_tipo.currentText() == "Vestido"):
                if ((self.CB_tamanho.currentText() == "M") or self.CB_tamanho.currentText() == "G"):
                    print("macaquinho/vestido - M/G") # valor 80
                    if (self.CB_desconto.isChecked()):
                        print("Com desconto")
                        valor_final = str( 80.0 - float(self.LE_desconto.text()) )
                        self.LE_valor.setText(valor_final)
                    else:
                        print("Sem desconto")
                        self.LE_valor.setText("80.0")
                else:
                    print("macaquinho/vestido - GG/XG") # valor 100
                    if (self.CB_desconto.isChecked()):
                        print("Com desconto")
                        valor_final = str( 100.0 - float(self.LE_desconto.text()) )
                        self.LE_valor.setText(valor_final)
                    else:
                        print("Sem desconto")
                        self.LE_valor.setText("100.0")
        else:
            self.LE_valor.setText("")

    def setupUi(self, Form_itens):
        self.iten = None
        self.Form_itens = Form_itens
        Form_itens.setObjectName("Form_itens")
        Form_itens.resize(251, 314)
        self.gridLayout = QtWidgets.QGridLayout(Form_itens)
        self.gridLayout.setObjectName("gridLayout")
        self.label_tipo = QtWidgets.QLabel(Form_itens)
        self.label_tipo.setObjectName("label_tipo")
        self.gridLayout.addWidget(self.label_tipo, 0, 0, 1, 1)
        self.CB_tipo = QtWidgets.QComboBox(Form_itens)
        self.CB_tipo.setObjectName("CB_tipo")
        self.gridLayout.addWidget(self.CB_tipo, 0, 1, 1, 2)
        self.CB_tipo.setFocus()
        self.CB_tipo.addItem("")
        self.CB_tipo.addItem("Macacão")
        self.CB_tipo.addItem("Macaquinho")
        self.CB_tipo.addItem("Vestido")
        self.CB_tipo.addItem("Vestido Longo")
        self.CB_tipo.currentTextChanged.connect(self.precificar)
        self.label_tamanho = QtWidgets.QLabel(Form_itens)
        self.label_tamanho.setObjectName("label_tamanho")
        self.gridLayout.addWidget(self.label_tamanho, 1, 0, 1, 1)
        self.CB_tamanho = QtWidgets.QComboBox(Form_itens)
        self.CB_tamanho.setObjectName("CB_tamanho")
        self.gridLayout.addWidget(self.CB_tamanho, 1, 1, 1, 2)
        self.CB_tamanho.addItem("")
        self.CB_tamanho.addItem("M")
        self.CB_tamanho.addItem("G")
        self.CB_tamanho.addItem("GG")
        self.CB_tamanho.addItem("XG")
        self.CB_tamanho.currentTextChanged.connect(self.precificar)
        self.label_estampa = QtWidgets.QLabel(Form_itens)
        self.label_estampa.setObjectName("label_estampa")
        self.gridLayout.addWidget(self.label_estampa, 2, 0, 1, 1)
        self.CB_estampa = QtWidgets.QComboBox(Form_itens)
        self.CB_estampa.setObjectName("CB_estampa")
        self.gridLayout.addWidget(self.CB_estampa, 2, 1, 1, 2)
        self.CB_estampa.addItem("")
        for value in self.contar():
            self.CB_estampa.addItem(value[1])
        self.CB_estampa.currentTextChanged.connect(self.precificar)
        self.CB_desconto = QtWidgets.QCheckBox(Form_itens)
        self.CB_desconto.setObjectName("CB_desconto")
        self.gridLayout.addWidget(self.CB_desconto, 3, 0, 1, 1)
        self.CB_desconto.stateChanged.connect(self.status_CB)
        self.LE_desconto = QtWidgets.QLineEdit(Form_itens)
        self.LE_desconto.setObjectName("LE_desconto")
        self.gridLayout.addWidget(self.LE_desconto, 3, 1, 1, 1)
        self.LE_desconto.setDisabled(True)
        self.LE_desconto.setText(str(0.0))
        self.LE_desconto.editingFinished.connect(self.precificar)
        self.LE_desconto.returnPressed.connect(self.precificar)
        self.label = QtWidgets.QLabel(Form_itens)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.LE_valor = QtWidgets.QLineEdit(Form_itens)
        self.LE_valor.setObjectName("LE_valor")
        self.LE_valor.setDisabled(True)
        self.gridLayout.addWidget(self.LE_valor, 4, 1, 1, 1)
        self.PB_salvar = QtWidgets.QPushButton(Form_itens)
        self.PB_salvar.setObjectName("PB_salvar")
        self.gridLayout.addWidget(self.PB_salvar, 5, 1, 1, 1)
        self.PB_salvar.setAutoDefault(False)
        self.PB_salvar.clicked.connect(self.salvar)
        self.PB_cancelar = QtWidgets.QPushButton(Form_itens)
        self.PB_cancelar.setObjectName("PB_cancelar")
        self.PB_cancelar.setAutoDefault(False)
        self.gridLayout.addWidget(self.PB_cancelar, 5, 2, 1, 1)
        self.PB_cancelar.clicked.connect(self.cancelar)

        self.retranslateUi(Form_itens)
        QtCore.QMetaObject.connectSlotsByName(Form_itens)

    def retranslateUi(self, Form_itens):
        _translate = QtCore.QCoreApplication.translate
        Form_itens.setWindowTitle(_translate("Form_itens", "Iten"))
        Form_itens.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.label_tipo.setText(_translate("Form_itens", "Tipo:"))
        self.label_tamanho.setText(_translate("Form_itens", "Tamanho:"))
        self.label_estampa.setText(_translate("Form_itens", "Estampa:"))
        self.CB_desconto.setText(_translate("Form_itens", "Desconto"))
        self.label.setText(_translate("Form_itens", "Valor:"))
        self.PB_salvar.setText(_translate("Form_itens", "Salvar"))
        self.PB_cancelar.setText(_translate("Form_itens", "Cancelar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_itens = QtWidgets.QWidget()
    ui = Ui_Form_itens(None)
    ui.setupUi(Form_itens)
    Form_itens.show()
    sys.exit(app.exec_())
