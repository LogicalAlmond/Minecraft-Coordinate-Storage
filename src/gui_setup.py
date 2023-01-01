from PyQt5 import QtCore, QtGui, QtWidgets
from database_commands import DbSetup as dbInit

COLUMNWIDTH = 712/5

class Ui_MainWindow(object):
    
    def __init__(self):
        self.database = dbInit()

    def submitData(self):
        db = self.database
        name = self.nameComboBox.currentText()
        xcoord = int(self.xCoordLineEdit.text())
        ycoord = int(self.yCoordLineEdit.text())
        zcoord = int(self.zCoordLineEdit.text())
        explored = self.exploredComboBox.currentText()
        queryParams = (name, xcoord, ycoord, zcoord, explored)
        self.database.submitQuery(queryParams)
        newData = db._reloadData()
        self.loadData(newData)
        
    def initData(self):
        data = self.database.queryAll()
        self.loadData(data)
        
    def loadData(self, data):
        rowCount = len(data)
        self.tableWidget.setRowCount(rowCount)
        currentIndex = 0
        for row in data:
            self.tableWidget.setItem(currentIndex, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(currentIndex, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(currentIndex, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(currentIndex, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(currentIndex, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(currentIndex, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            currentIndex += 1
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        
        # CentralWidget and MainFrame
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainFrame.setObjectName("MainFrame")
        
        # TableFrame
        self.TableFrame = QtWidgets.QFrame(self.MainFrame)
        self.TableFrame.setGeometry(QtCore.QRect(0, 130, 801, 461))
        self.TableFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TableFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TableFrame.setObjectName("TableFrame")
        
        # TableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.TableFrame)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 801, 421))
        self.tableWidget.setFont(font)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.setColumnWidth(0, 60)
        self.tableWidget.setColumnWidth(1, int(COLUMNWIDTH))
        self.tableWidget.setColumnWidth(2, int(COLUMNWIDTH))
        self.tableWidget.setColumnWidth(3, int(COLUMNWIDTH))
        self.tableWidget.setColumnWidth(4, int(COLUMNWIDTH))
        self.tableWidget.setColumnWidth(5, int(COLUMNWIDTH))
        
        # SubmitFrame
        self.submitFrame = QtWidgets.QFrame(self.MainFrame)
        self.submitFrame.setGeometry(QtCore.QRect(0, 0, 801, 131))
        self.submitFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.submitFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.submitFrame.setObjectName("submitFrame")
        
        # TitleFrame
        self.titleLabel = QtWidgets.QLabel(self.submitFrame)
        self.titleLabel.setGeometry(QtCore.QRect(300, 10, 201, 21))
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        
        # SubmitButton
        self.submitButton = QtWidgets.QPushButton(self.submitFrame)
        self.submitButton.setGeometry(QtCore.QRect(10, 80, 80, 22))
        self.submitButton.clicked.connect(self.submitData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(13)
        font.setBold(True)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        
        # ExploreComboBox
        self.exploredComboBox = QtWidgets.QComboBox(self.submitFrame)
        self.exploredComboBox.setGeometry(QtCore.QRect(710, 80, 81, 22))
        self.exploredComboBox.setFont(font)
        self.exploredComboBox.setObjectName("exploredComboBox")
        self.exploredComboBox.addItem("")
        self.exploredComboBox.addItem("")
        
        # CoordLineEdit (input boxs). This deals with all information to be submitted
        self.xCoordLineEdit = QtWidgets.QLineEdit(self.submitFrame)
        self.xCoordLineEdit.setGeometry(QtCore.QRect(270, 80, 113, 22))
        self.xCoordLineEdit.setFont(font)
        self.xCoordLineEdit.setObjectName("xCoordLineEdit")
        self.yCoordLineEdit = QtWidgets.QLineEdit(self.submitFrame)
        self.yCoordLineEdit.setGeometry(QtCore.QRect(420, 80, 113, 22))
        self.yCoordLineEdit.setObjectName("yCoordLineEdit")
        self.zCoordLineEdit = QtWidgets.QLineEdit(self.submitFrame)
        self.zCoordLineEdit.setGeometry(QtCore.QRect(570, 80, 113, 22))
        self.zCoordLineEdit.setObjectName("zCoordLineEdit")
        self.nameLabel = QtWidgets.QLabel(self.submitFrame)
        self.nameLabel.setGeometry(QtCore.QRect(120, 60, 111, 20))
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.nameComboBox = QtWidgets.QComboBox(self.submitFrame)
        self.nameComboBox.setGeometry(QtCore.QRect(100, 80, 161, 22))
        self.nameComboBox.setFont(font)
        self.nameComboBox.setObjectName("nameComboBox")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        self.nameComboBox.addItem("")
        
        # Setup for x-coord label and input
        self.xCoordLabel = QtWidgets.QLabel(self.submitFrame)
        self.xCoordLabel.setGeometry(QtCore.QRect(270, 60, 111, 20))
        self.xCoordLabel.setFont(font)
        self.xCoordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.xCoordLabel.setObjectName("xCoordLabel")
        
        # Setup for y-coord label and input
        self.yCoordLabel = QtWidgets.QLabel(self.submitFrame)
        self.yCoordLabel.setGeometry(QtCore.QRect(420, 60, 111, 20))
        self.yCoordLabel.setFont(font)
        self.yCoordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.yCoordLabel.setObjectName("yCoordLabel")
        
        # Setup for z-coord label and input
        self.zCoordLabel = QtWidgets.QLabel(self.submitFrame)
        self.zCoordLabel.setGeometry(QtCore.QRect(570, 60, 111, 20))
        self.zCoordLabel.setFont(font)
        self.zCoordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.zCoordLabel.setObjectName("zCoordLabel")
        
        # Setup for explored label and input
        self.exploredLabel = QtWidgets.QLabel(self.submitFrame)
        self.exploredLabel.setGeometry(QtCore.QRect(707, 60, 81, 20))
        self.exploredLabel.setFont(font)
        self.exploredLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exploredLabel.setObjectName("exploredLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "X-Coordinate"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Y-Coordinate"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Z-Coordinate"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Explored?"))
        self.titleLabel.setText(_translate("MainWindow", "Minecraft Coordinates"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.exploredComboBox.setItemText(0, _translate("MainWindow", "No"))
        self.exploredComboBox.setItemText(1, _translate("MainWindow", "Yes"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.nameComboBox.setItemText(0, _translate("MainWindow", "Stronghold"))
        self.nameComboBox.setItemText(1, _translate("MainWindow", "Mansion"))
        self.nameComboBox.setItemText(2, _translate("MainWindow", "Monument"))
        self.nameComboBox.setItemText(3, _translate("MainWindow", "Pillager Outpost"))
        self.nameComboBox.setItemText(4, _translate("MainWindow", "Mineshaft"))
        self.nameComboBox.setItemText(5, _translate("MainWindow", "Ruined Portal"))
        self.nameComboBox.setItemText(6, _translate("MainWindow", "Jungle Temple"))
        self.nameComboBox.setItemText(7, _translate("MainWindow", "Desert Temple"))
        self.nameComboBox.setItemText(8, _translate("MainWindow", "Witch Hut"))
        self.nameComboBox.setItemText(9, _translate("MainWindow", "Shipwreck"))
        self.nameComboBox.setItemText(10, _translate("MainWindow", "Igloo"))
        self.nameComboBox.setItemText(11, _translate("MainWindow", "Ancient City"))
        self.nameComboBox.setItemText(12, _translate("MainWindow", "Cave"))
        self.nameComboBox.setItemText(13, _translate("MainWindow", "Village"))
        self.nameComboBox.setItemText(14, _translate("MainWindow", "Other"))
        self.xCoordLabel.setText(_translate("MainWindow", "X-coordinate"))
        self.yCoordLabel.setText(_translate("MainWindow", "Y-coordinate"))
        self.zCoordLabel.setText(_translate("MainWindow", "Z-coordinate"))
        self.exploredLabel.setText(_translate("MainWindow", "Explored?"))
