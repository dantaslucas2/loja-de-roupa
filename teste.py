from PyQt5 import QtGui, QtWidgets
import sys

def handler(item, column_no):
    print(item, column_no)

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QTreeWidget()

    items = [QtWidgets.QTreeWidgetItem("item: {}") ]
    win.insertTopLevelItems(0, items)
    win.itemDoubleClicked.connect(handler)

    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
