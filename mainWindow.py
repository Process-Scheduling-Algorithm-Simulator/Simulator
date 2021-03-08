


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 171, 51))
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"border : none;\n"
"color : #fff;\n"
"font-size : 22px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 161, 41))
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"border : none;\n"
"color : #fff;\n"
"font-size : 22px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(220, 60, 161, 41))
        self.textEdit.setStyleSheet("QTextEdit\n"
"{\n"
"border:none;\n"
"border-radius:2px;\n"
"font-size:22px;\n"
"}")
        self.textEdit.setObjectName("textEdit")
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
        self.start.setObjectName("start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulator"))
        self.label.setText(_translate("MainWindow", "CPU - SCHEDULING"))
        self.label_2.setText(_translate("MainWindow", "SIMULATION PROGRAM"))
        self.label_3.setText(_translate("MainWindow", "No of Process   : "))
        self.label_4.setText(_translate("MainWindow", "Algorithm         :"))
        self.textEdit.setStatusTip(_translate("MainWindow", "  Input the number of process"))
        self.comboBox.setStatusTip(_translate("MainWindow", "  Select the Scheduling Algorithm"))
        self.comboBox.setItemText(1, _translate("MainWindow", "FCFS"))
        self.comboBox.setItemText(2, _translate("MainWindow", "RR"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Priority-np"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Priorit-p"))
        self.comboBox.setItemText(5, _translate("MainWindow", "SJF"))
        self.comboBox.setItemText(6, _translate("MainWindow", "SRTF"))
        self.start.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
