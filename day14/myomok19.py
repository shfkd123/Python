import sys
import numpy as np
from tensorflow.keras.models import load_model
model = load_model('models/20201213_202430.h5')
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic, QtGui
from PyQt5.Qt import QPushButton, QSize, QRect, QMessageBox
from _ast import If
from astropy.time.utils import split


form_class = uic.loadUiType("myomok01.ui")[0]

def getComIJ(arr2D):
        input = np.zeros((20,20))
        for i in range(20):
            for j in range(20):
                if arr2D[i][j] == 1 :
                    input[i][j] = 1
                if arr2D[i][j] == 2 :
                    input[i][j] = -1
            
        input = input.reshape((1,20,20,1))
        
        #print(input.shape)
        #print(input)
        
        output = model.predict(input).squeeze()
        output = output.reshape((20, 20))
        for i in range(20):
            for j in range(20):
                if arr2D[i][j] > 0 : #돌이 벌써 놓아진 상황
                    output[i][j] = 0
                    
        print(output)
        print(output.shape)
        i, j = np.unravel_index(np.argmax(output), output.shape)
        return i, j
        #print(i,j)

class WindowClass(QMainWindow, form_class):
        
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag_ing = True
        self.flag_wb = True
        self.arr2D = [
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                                                   
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                                                        
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                                                        
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
               

            ]
        #컴퓨터가 놓는 자리 
        self.arr_seq = [
            {'i':0, 'j':0},
            {'i':0, 'j':1},
            {'i':0, 'j':2},
            {'i':0, 'j':3},
            {'i':0, 'j':4}
        ]
        self.arr_idx = 0

        self.pb2D = []
        
        
        for i in range(20):
            pb_line = []
            for j in range(20):
                tmp = QPushButton(self)
                tmp.setToolTip(str(i)+","+str(j))
                tmp.setIconSize(QSize(40,40))
                tmp.setGeometry(QRect(j*40,i*40,40,40))
                tmp.setIcon(QtGui.QIcon('0.png'))
                tmp.clicked.connect(self.btnClick)
                pb_line.append(tmp)
            self.pb2D.append(pb_line)
            
        self.pb_reset.clicked.connect(self.myreset)
        self.myrender()         
            
    def myreset(self):
        self.flag_wb = True
        self.flag_ing = True
        self.arr_idx = 0
        
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j] = 0
        self.myrender()
         
    def myrender(self): 
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j] == 0 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
    
                    
    def btnClick(self):
        if not self.flag_ing :
            return 
        print(self.sender().toolTip())
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = 1
        self.arr2D[i][j] = 1
            
        up = self.getUP(i,j,stone)   
        dw = self.getDW(i,j,stone)    
        le = self.getLE(i,j,stone)    
        ri = self.getRI(i,j,stone)
            
        ur = self.getUR(i,j,stone)    
        dl = self.getDL(i,j,stone)    
        ul = self.getUL(i,j,stone)    
        dr = self.getDR(i,j,stone)    
        
        d1 = up+1+dw
        d2 = le+1+ri
        d3 = ur+1+dl
        d4 = ul+1+dr
        
        self.myrender()
        
        if d1==5 or d2 == 5 or d3 == 5 or d4 == 5 :
            QMessageBox.about(self, "오목", "흑돌 승리!")
            self.flag_ing = False
            return
            
        self.flag_wb = not self.flag_wb
        

        #com_i = self.arr_seq[self.arr_idx]['i']
        #com_j = self.arr_seq[self.arr_idx]['j']
        
        com_i,com_j = getComIJ(self.arr2D)
        print(com_i, com_j)
        
        stone = 2
        self.arr2D[com_i][com_j] = 2
        self.arr_idx+=1
            
        up = self.getUP(com_i,com_j,stone)   
        dw = self.getDW(com_i,com_j,stone)    
        le = self.getLE(com_i,com_j,stone)    
        ri = self.getRI(com_i,com_j,stone)
                    
        ur = self.getUR(com_i,com_j,stone)    
        dl = self.getDL(com_i,com_j,stone)    
        ul = self.getUL(com_i,com_j,stone)    
        dr = self.getDR(com_i,com_j,stone)    
        
        d1 = up+1+dw
        d2 = le+1+ri
        d3 = ur+1+dl
        d4 = ul+1+dr
        
        self.myrender()
        
        if d1==5 or d2 == 5 or d3 == 5 or d4 == 5 :
            QMessageBox.about(self, "오목", "백돌 승리!")
            self.flag_ing = False
                        
        self.flag_wb = not self.flag_wb
        
    def getUP(self,i,j,stone): 
        cnt = 0
        try : 
            while True:
                i += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :
            return cnt

    def getDW(self,i,j,stone): 
        cnt = 0
        try :
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :
            return cnt
    
    def getRI(self,i,j,stone): 
        cnt = 0
        try :
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :
            return cnt
    
    def getLE(self,i,j,stone): 
        cnt = 0
        try :
            while True:
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :
            return cnt

    def getUR(self,i,j,stone): 
        cnt = 0
        try :
            while True:
                j += 1
                i += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :
            return cnt
    
    def getDL(self,i,j,stone): 
        cnt = 0
        try :
            while True:
                j += -1
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :
            return cnt
    
    def getUL(self,i,j,stone): 
        cnt = 0
        try :
            while True:
                i += -1
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :
            return cnt
        
    def getDR(self,i,j,stone): 
        cnt = 0
        try :
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :
            return cnt    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
 

 