from gui_setup import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.initData()
MainWindow.show()
sys.exit(app.exec_())