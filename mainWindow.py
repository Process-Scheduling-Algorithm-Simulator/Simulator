
from PyQt5 import QtCore, QtGui, QtWidgets
from simulatorWindow import*
import color


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.n = 0                                         # n for number of processes
        self.option = 0                                    # option for selection of algo

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
" background-image : https://home.sophos.com/en-us/medialibrary/Microsites/Home/SecurityCenter/ai-article-pic10.jpg;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backgroundImage = QtWidgets.QLabel(self.centralwidget)
        self.backgroundImage.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.backgroundImage.setText("")
        self.backgroundImage.setPixmap(QtGui.QPixmap("images/main_background2.jpg"))
        self.backgroundImage.setScaledContents(True)
        self.backgroundImage.setObjectName("backgroundImage")

        #for label1

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 40, 471, 101))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"color : #fff;\n"
"font-size : 42px;\n"
"}")
        self.label.setObjectName("label")

        #for label2

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 120, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"\n"
"font-size : 24px;\n"
"color : rgb(255, 85, 6);\n"
"}")
        self.label_2.setObjectName("label_2")

        #frame 
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(350, 220, 411, 221))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"\n"
"border: 4px dashed #fff;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #label3

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 171, 51))
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"border : none;\n"
"color : #fff;\n"
"font-size : 22px;\n"
"}")
        self.label_3.setObjectName("label_3")
        
         #label3

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 161, 41))
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"border : none;\n"
"color : #fff;\n"
"font-size : 22px;\n"
"}")
        self.label_4.setObjectName("label_4")
        
        #comboBox

        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(220, 120, 161, 41))
        self.comboBox.setStyleSheet("QComboBox\n"
"{\n"
"background-color : #fff;\n"
"font-size : 18px;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        icon = QtGui.QIcon.fromTheme("none")
        self.comboBox.addItem(icon, "")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        #lineEdit

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"padding : 1px 2px 2px 2px;\n"
"}")
        self.lineEdit.setGeometry(QtCore.QRect(220, 60, 161, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(500, 460, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Nueva Std")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("QPushButton\n"
"{\n"
"  background-color: rgb(255, 16, 80);\n"
"  border-radius : 2px;\n"
"  color: white;\n"
"  padding: 15px 28px;\n"
"  text-align: center;\n"
"  font-size: 24px;\n"
"}\n"
"")
        self.onlyInt = QtGui.QIntValidator()
        self.lineEdit.setValidator(self.onlyInt)              #validations for number of processes

        self.start.setObjectName("start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.start.clicked.connect(self.getNum)                 #connecting to getN  
        self.start.clicked.connect(self.getAlgo)                #connecting to getAlgo

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulator"))
        self.label.setText(_translate("MainWindow", "CPU - SCHEDULING"))
        self.label_2.setText(_translate("MainWindow", "SIMULATION PROGRAM"))
        self.label_3.setText(_translate("MainWindow", "No of Process   : "))
        self.label_4.setText(_translate("MainWindow", "Algorithm         :"))
        self.comboBox.setStatusTip(_translate("MainWindow", "  Select the Scheduling Algorithm"))
        self.comboBox.setItemText(1, _translate("MainWindow", "FCFS"))
        self.comboBox.setItemText(2, _translate("MainWindow", "RR"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Priority-np"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Priority-p"))
        self.comboBox.setItemText(5, _translate("MainWindow", "SJF"))
        self.comboBox.setItemText(6, _translate("MainWindow", "SRTF"))
        self.start.setText(_translate("MainWindow", "Start"))

    def getNum(self):
        self.n = int(self.lineEdit.text())
        color.number = self.n
        
        
    def getAlgo(self):
        txt = self.comboBox.currentText()
        if txt == "FCFS": self.option = 0
        if txt == "RR": self.option = 1
        if txt == "Priority-np": self.option = 2
        if txt == "Priority-p": self.option = 3
        if txt == "SJF": self.option = 4
        if txt == "SRTF": self.option = 5
        self.openSimulator()

    def openSimulator(self):                                  #calling the second window
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.n = self.n                                    # setting the n and option variables of simulator window
        self.ui.option = self.option
        self.ui.setupUi(self.window)
        self.window.show()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
