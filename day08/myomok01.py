import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5 import uic
from PyQt5.uic.Compiler.qtproxies import QtWidgets
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.Qt import QSize, QRect

form_class = uic.loadUiType("myomok01.ui")[0]


class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.arr2D = [
                [1,0,0,0,0, 0,0,0,0,0],
                [0,1,0,0,0, 0,0,0,0,0],
                [0,0,2,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],

                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0]
            ]
        self.pb2D = []    

        for i in range(10):
            pb_line = []
            for j in range(10):
                tmp = QPushButton(self)
                tmp.setToolTip(str(i)+","+str(j))
                tmp.setIconSize(QSize(40, 40))
                tmp.setGeometry(QRect(j*40, i*40, 40, 40))
                tmp.setIcon(QtGui.QIcon("0.png"))
                tmp.clicked.connect(self.btnClick)
                pb_line.append(tmp)
            self.pb2D.append(pb_line)
        
        self.myrender()    
    
    def myrender(self):        
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("0.png"))
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("1.png"))
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("2.png"))
    
    def btnClick(self):
        #self.pb2D[0][9].setIcon(QtGui.QIcon("1.png"))
        #print(self.toolTip())
        print(self.sender().toolTip())
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")    
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        self.arr2D[i][j] = 1
        
        self.myrender()
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
 