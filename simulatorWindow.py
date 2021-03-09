
from PyQt5 import QtCore, QtGui, QtWidgets
from mainWindow import*
from schedulingAlgo import*


class Ui_MainWindow1(object):

    def __init__(self):
        super().__init__()
        self.n = 2
        self.option = 0
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1149, 883)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"background-color:#fff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1251, 401))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget::Item\n"
"{\n"
"background-color :rgb(73, 85, 255);\n"
"}\n"
"\n"
"")
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(self.n)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.test = QtWidgets.QPushButton(self.centralwidget)
        self.test.setGeometry(QtCore.QRect(440, 550, 211, 81))
        self.test.setObjectName("test")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.test.clicked.connect(self.simulate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulator"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Process"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Arrival Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Brust Time"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Priority"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Completion Time"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Turn Around Time"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Waiting Time"))
        self.test.setText(_translate("MainWindow", "test"))

    def simulate(self):

        if self.option == 0:
            fcfs = FCFS(self.n)
            
            for z in range(self.n):
                for j in range(3):
                    if j == 0:
                        process = self.tableWidget.item(z, j).text()
                        fcfs.processName[z] = process
                    if j == 1:
                        at = int(self.tableWidget.item(z, j).text())
                        fcfs.arrivalTime.append([at,z])
                        fcfs.testat[z] = at
                    if j == 2:
                        bt = int(self.tableWidget.item(z, j).text())
                        fcfs.burstTime.append([bt,z])
                        fcfs.testbt[z] = bt

                

            fcfs.getCompletionTime()
            fcfs.getTurnAroundTime()
            fcfs.getWaitingTime()

            for j in range(self.n):
                ct = QtWidgets.QTableWidgetItem()
                ct.setText(str(fcfs.completionTime[j]))
                self.tableWidget.setItem(j,4, ct ) 

                tat = QtWidgets.QTableWidgetItem()
                tat.setText(str(fcfs.turnAroundTime[j]))
                self.tableWidget.setItem(j,5, tat) 

                wt = QtWidgets.QTableWidgetItem()
                wt.setText(str(fcfs.waitingTime[j]))
                self.tableWidget.setItem(j,6, wt) 


        if self.option == 1:
            rr = RR(self.n)
            
            for z in range(self.n):
                for j in range(3):
                    if j == 0:
                        process = self.tableWidget.item(z, j).text()
                        rr.processName[z] = process
                    if j == 1:
                        at = int(self.tableWidget.item(z, j).text())
                        rr.arrivalTime.append([at,z])
                        rr.testat[z] = at
                    if j == 2:
                        bt = int(self.tableWidget.item(z, j).text())
                        rr.burstTime.append([bt,z])
                        rr.testbt[z] = bt

                

            rr.getCompletionTime()
            rr.getTurnAroundTime()
            rr.getWaitingTime()

            for j in range(self.n):
                ct = QtWidgets.QTableWidgetItem()
                ct.setText(str(rr.completionTime[j]))
                self.tableWidget.setItem(j,4, ct ) 

                tat = QtWidgets.QTableWidgetItem()
                tat.setText(str(rr.turnAroundTime[j]))
                self.tableWidget.setItem(j,5, tat) 

                wt = QtWidgets.QTableWidgetItem()
                wt.setText(str(rr.waitingTime[j]))
                self.tableWidget.setItem(j,6, wt) 
        

        if self.option == 2:
            pnp = priority_nonprem(self.n)
            
            for z in range(self.n):
                for j in range(4):
                    if j == 0:
                        process = self.tableWidget.item(z, j).text()
                        pnp.processName[z] = process
                    if j == 1:
                        at = int(self.tableWidget.item(z, j).text())
                        pnp.arrivalTime.append([at,z])
                        pnp.testat[z] = at
                    if j == 2:
                        bt = int(self.tableWidget.item(z, j).text())
                        pnp.burstTime.append([bt,z])
                        pnp.testbt[z] = bt
                    if j == 3:
                        pri = int(self.tableWidget.item(z, j).text())
                        pnp.priority.append([pri,z])


                

            pnp.getCompletionTime()
            pnp.getTurnAroundTime()
            pnp.getWaitingTime()

            for j in range(self.n):
                ct = QtWidgets.QTableWidgetItem()
                ct.setText(str(pnp.completionTime[j]))
                self.tableWidget.setItem(j,4, ct ) 

                tat = QtWidgets.QTableWidgetItem()
                tat.setText(str(pnp.turnAroundTime[j]))
                self.tableWidget.setItem(j,5, tat) 

                wt = QtWidgets.QTableWidgetItem()
                wt.setText(str(pnp.waitingTime[j]))
                self.tableWidget.setItem(j,6, wt) 

        
        if self.option == 3:
            pp = priority_prem(self.n)
            
            for z in range(self.n):
                for j in range(3):
                    if j == 0:
                        process = self.tableWidget.item(z, j).text()
                        pp.processName[z] = process
                    if j == 1:
                        at = int(self.tableWidget.item(z, j).text())
                        pp.arrivalTime.append([at,z])
                        pp.testat[z] = at
                    if j == 2:
                        bt = int(self.tableWidget.item(z, j).text())
                        pp.burstTime.append([bt,z])
                        pp.testbt[z] = bt
                    if j == 3:
                        pri = int(self.tableWidget.item(z, j).text())
                        pp.priority.append([pri,z])

                

            pp.getCompletionTime()
            pp.getTurnAroundTime()
            pp.getWaitingTime()

            for j in range(self.n):
                ct = QtWidgets.QTableWidgetItem()
                ct.setText(str(pp.completionTime[j]))
                self.tableWidget.setItem(j,4, ct ) 

                tat = QtWidgets.QTableWidgetItem()
                tat.setText(str(pp.turnAroundTime[j]))
                self.tableWidget.setItem(j,5, tat) 

                wt = QtWidgets.QTableWidgetItem()
                wt.setText(str(pp.waitingTime[j]))
                self.tableWidget.setItem(j,6, wt)

        if self.option == 4:
            sjf = SJF(self.n)
            
            for z in range(self.n):
                for j in range(3):
                    if j == 0:
                        process = self.tableWidget.item(z, j).text()
                        sjf.processName[z] = process
                    if j == 1:
                        at = int(self.tableWidget.item(z, j).text())
                        sjf.arrivalTime.append([at,z])
                        sjf.testat[z] = at
                    if j == 2:
                        bt = int(self.tableWidget.item(z, j).text())
                        sjf.burstTime.append([bt,z])
                        sjf.testbt[z] = bt

                

            sjf.getCompletionTime()
            sjf.getTurnAroundTime()
            sjf.getWaitingTime()

            for j in range(self.n):
                ct = QtWidgets.QTableWidgetItem()
                ct.setText(str(sjf.completionTime[j]))
                self.tableWidget.setItem(j,4, ct ) 

                tat = QtWidgets.QTableWidgetItem()
                tat.setText(str(sjf.turnAroundTime[j]))
                self.tableWidget.setItem(j,5, tat) 

                wt = QtWidgets.QTableWidgetItem()
                wt.setText(str(sjf.waitingTime[j]))
                self.tableWidget.setItem(j,6, wt) 

        if self.option == 5:
            srtf = SRTF(self.n)
            
            for z in range(self.n):
                for j in range(3):
                    if j == 0:
                        process = self.tableWidget.item(z, j).text()
                        srtf.processName[z] = process
                    if j == 1:
                        at = int(self.tableWidget.item(z, j).text())
                        srtf.arrivalTime.append([at,z])
                        srtf.testat[z] = at
                    if j == 2:
                        bt = int(self.tableWidget.item(z, j).text())
                        srtf.burstTime.append([bt,z])
                        srtf.testbt[z] = bt

                

            srtf.getCompletionTime()
            srtf.getTurnAroundTime()
            srtf.getWaitingTime()

            for j in range(self.n):
                ct = QtWidgets.QTableWidgetItem()
                ct.setText(str(srtf.completionTime[j]))
                self.tableWidget.setItem(j,4, ct ) 

                tat = QtWidgets.QTableWidgetItem()
                tat.setText(str(srtf.turnAroundTime[j]))
                self.tableWidget.setItem(j,5, tat) 

                wt = QtWidgets.QTableWidgetItem()
                wt.setText(str(srtf.waitingTime[j]))
                self.tableWidget.setItem(j,6, wt)  



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
