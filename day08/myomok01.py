import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui
from PyQt5.Qt import QPushButton, QRect, QSize
from sympy.printing import str

form_class = uic.loadUiType("myomok01.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.flag_wb = True
        self.arr2D = [
                 [0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
                ,[0,0,0,0,0, 0,0,0,0,0]
            ]
        self.pb2D = []
        self.cnt = 0
        
        for i in range(10):
            pb_line = []
            for j in range(10):
                tmp = QPushButton(self)
                tmp.setIconSize(QSize(40, 40))
                tmp.setGeometry(QRect(40 * j, 40 * i, 40, 40))
                tmp.setToolTip(str(i) + "," + str(j))
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
        arr_ij = self.sender().toolTip().split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = 0
        if self.flag_wb:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
        up = self.getUP(i,j, stone)
        print("up", up)
        
        self.myrender()
        self.flag_wb = not self.flag_wb   
    
    #i가 3 j가 2로 생각 stone은 내가 돌을 놓은 값    
    def getUP(self,i,j,stone): 
        cnt = 0
        
        while True:
            i -= 1
            if self.arr2D[i][j] == stone :
                cnt += 1
            else :
                return cnt
        
                
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())