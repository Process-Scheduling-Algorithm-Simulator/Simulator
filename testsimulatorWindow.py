


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox, QMainWindow, QVBoxLayout, QGridLayout
from mainWindow import*
from testSchedulingAlgo import*
import sys
import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
import matplotlib.pyplot as plt
import random
import randomcolor
plt.style.use('ggplot')










class MatplotlibFigure(QWidget):
    def __init__(self):
        super().__init__()        
        self.initializewidget()
        self.plot(0)
                


        

    def initializewidget(self):

        gridlayout = QGridLayout()
        self.setLayout(gridlayout)
        self.figure = plt.figure(figsize=(5,5))
        self.canvas = FigureCanvas(self.figure)
        gridlayout.addWidget(self.canvas,0,0,1,2)
        

    def plot(self,number):
        print("gannt begins")
        print(startTime)
        print(length)
        
        colors = []

        for i in range(number):
            color = randomcolor.RandomColor().generate()
            colors.append(color)     
       
        print(colors)

        gnt = self.figure.add_subplot(111)

        # gnt.set_ylim(0, 30) 
        gnt.set_xlim(0, 70) 

        gnt.set_xlabel('Time')
        gnt.set_xticks(np.arange(0, 70, 5)) 


        gnt.set_yticks([15]) 
        gnt.set_yticklabels(['process'])

        
        


        size = len(startTime)

        for i in range(size):
            name = 'p' + str(startTime[i][0] + 1)
            processName.append(name)
        
        print(processName)

        for i in range(size):
            index = startTime[i][0]
            start = startTime[i][1]
            duration = length[i][1]
            gnt.broken_barh([(start, duration)], (10, 10), facecolors = (colors[index][0]))
           
        self.canvas.draw()
        gnt.legend(processName,bbox_to_anchor =(1.12, 1.17))









class Ui_MainWindow1(object):

    def __init__(self):
        super().__init__()
        self.n = 1
        self.option = 0
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1149, 1020)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"background-color:#fff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1151, 310))
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
        if self.option == 2 or self.option == 3:
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
        else :
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
            self.tableWidget.horizontalHeader().setDefaultSectionSize(188)
            self.tableWidget.horizontalHeader().setHighlightSections(True)



        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(940, 720, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Tekton Pro")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn.setFont(font)
        self.btn.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 26px;\n"
"    min-width: 5em;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}")
        self.btn.setObjectName("btn")



        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 311, 1180, 140))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"border : 4px dashed rgb(255, 11, 15)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        if self.option == 1 :
            self.label = QtWidgets.QLabel(self.frame)
            self.label.setGeometry(QtCore.QRect(20, 40, 191, 41))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Black")
            font.setPointSize(-1)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setStyleSheet("QLabel\n"
            "{\n"
            "font-size : 20px;\n"
            "border : none;\n"
            "}\n"
            "\n"
            "")
            self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        if self.option == 1 : self.label_2.setGeometry(QtCore.QRect(340, 40, 241, 51))
        else: self.label_2.setGeometry(QtCore.QRect(20, 40, 260, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"font-size : 20px;\n"
"border : none;\n"
"}\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(750, 40, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"font-size : 20px;\n"
"border : none;\n"
"}\n"
"\n"
"")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 460, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.averageTAT = QtWidgets.QLineEdit(self.frame)
        self.averageTAT.setGeometry(QtCore.QRect(1040, 50, 90, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.averageTAT.setFont(font)
        self.averageTAT.setStyleSheet("QLineEdit\n"
"{\n"
"padding : 1px 2px 2px 2px;\n"
"}")
        self.averageTAT.setObjectName("averageTAT")
        self.averageWT = QtWidgets.QLineEdit(self.frame)
        if self.option == 1: self.averageWT.setGeometry(QtCore.QRect(600, 50, 90, 31))
        else: self.averageWT.setGeometry(QtCore.QRect(270, 50, 90, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.averageWT.setFont(font)
        self.averageWT.setStyleSheet("QLineEdit\n"
"{\n"
"padding : 1px 2px 2px 2px;\n"
"}")
        self.averageWT.setObjectName("averageWT")
        
        if self.option == 1:
            self.timeQuantum = QtWidgets.QLineEdit(self.frame)
            self.timeQuantum.setGeometry(QtCore.QRect(200, 50, 81, 31))
            font = QtGui.QFont()
            font.setFamily("Source Sans Pro Black")
            font.setPointSize(14)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            self.timeQuantum.setFont(font)
            self.timeQuantum.setStyleSheet("QLineEdit\n"
            "{\n"
            "padding : 1px 2px 2px 2px;\n"
            "}")
            self.timeQuantum.setObjectName("timeQuantum")
            self.timeQuantum.setText('0')

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.btn.clicked.connect(self.simulate)

        self.btn.clicked.connect(self.plot_data)

        self.matplot = MatplotlibFigure()
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 550, 920, 450))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        
    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulator"))
        self.tableWidget.setSortingEnabled(False)
        if self.option == 2 or self.option == 3 :
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
        else :
            item = self.tableWidget.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Process"))
            item = self.tableWidget.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Arrival Time"))
            item = self.tableWidget.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "Brust Time"))
            item = self.tableWidget.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Completion Time"))
            item = self.tableWidget.horizontalHeaderItem(4)
            item.setText(_translate("MainWindow", "Turn Around Time"))
            item = self.tableWidget.horizontalHeaderItem(5)
            item.setText(_translate("MainWindow", "Waiting Time"))

        self.btn.setText(_translate("MainWindow", "Simulate"))
        
        if self.option == 1 :self.label.setText(_translate("MainWindow", "Time Quantum : "))
        self.label_2.setText(_translate("MainWindow", "Average Waiting Time : "))
        self.label_3.setText(_translate("MainWindow", "AverageTurnAround Time : "))
        self.label_4.setText(_translate("MainWindow", "Gantt Chart "))



    def plot_data(self):
                # comment this line
        # self.canvas.setParent(self)   # comment this line
        self.verticalLayout.addWidget(self.matplot)  # <--- Add this line
        self.matplot.plot(self.n)   
        


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
                self.tableWidget.setItem(j,3, ct ) 

                tat = QtWidgets.QTableWidgetItem()
                tat.setText(str(fcfs.turnAroundTime[j]))
                self.tableWidget.setItem(j,4, tat) 

                wt = QtWidgets.QTableWidgetItem()
                wt.setText(str(fcfs.waitingTime[j]))
                self.tableWidget.setItem(j,5, wt)
            
            self.averageWT.setText(str(round((sum(fcfs.waitingTime)/self.n),2)))
            self.averageTAT.setText(str(round((sum(fcfs.turnAroundTime)/self.n),2)))
            print("fcfs got completed")
            



        if self.option == 1:
            tq = int(self.timeQuantum.text())
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

                

            rr.getCompletionTime(tq)
            rr.getTurnAroundTime()
            rr.getWaitingTime()

            for j in range(self.n):
                ct = QtWidgets.QTableWidgetItem()
                ct.setText(str(rr.completionTime[j]))
                self.tableWidget.setItem(j,3, ct ) 

                tat = QtWidgets.QTableWidgetItem()
                tat.setText(str(rr.turnAroundTime[j]))
                self.tableWidget.setItem(j,4, tat) 

                wt = QtWidgets.QTableWidgetItem()
                wt.setText(str(rr.waitingTime[j]))
                self.tableWidget.setItem(j,5, wt) 
            
            self.averageWT.setText(str(round((sum(rr.waitingTime)/self.n),2)))
            self.averageTAT.setText(str(round((sum(rr.turnAroundTime)/self.n),2)))

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

            self.averageWT.setText(str(round((sum(pnp.waitingTime)/self.n),2)))
            self.averageTAT.setText(str(round((sum(pnp.turnAroundTime)/self.n),2)))


        
        if self.option == 3:
            pp = priority_prem(self.n)
            
            for z in range(self.n):
                for j in range(4):
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

            self.averageWT.setText(str(round((sum(pp.waitingTime)/self.n),2)))
            self.averageTAT.setText(str(round((sum(pp.turnAroundTime)/self.n),2)))

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
                self.tableWidget.setItem(j,3, ct ) 

                tat = QtWidgets.QTableWidgetItem()
                tat.setText(str(sjf.turnAroundTime[j]))
                self.tableWidget.setItem(j,4, tat) 

                wt = QtWidgets.QTableWidgetItem()
                wt.setText(str(sjf.waitingTime[j]))
                self.tableWidget.setItem(j,5, wt) 

            self.averageWT.setText(str(round((sum(sjf.waitingTime)/self.n),2)))
            self.averageTAT.setText(str(round((sum(sjf.turnAroundTime)/self.n),2)))

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
                self.tableWidget.setItem(j,3, ct ) 

                tat = QtWidgets.QTableWidgetItem()
                tat.setText(str(srtf.turnAroundTime[j]))
                self.tableWidget.setItem(j,4, tat) 

                wt = QtWidgets.QTableWidgetItem()
                wt.setText(str(srtf.waitingTime[j]))
                self.tableWidget.setItem(j,5, wt)  

            self.averageWT.setText(str(round((sum(srtf.waitingTime)/self.n),2)))
            self.averageTAT.setText(str(round((sum(srtf.turnAroundTime)/self.n),2)))
        
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
