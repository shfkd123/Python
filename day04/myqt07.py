import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import random


form_class = uic.loadUiType("myqt07.UI")[0]

class windowClass(QMainWindow, form_class):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        a = self.le1.text()
        b= "";
        
        rand = random.random()
        print(rand)

        if rand < 0.33:
            b = "가위"
        elif rand>0.33 and rand<0.66:
            b = "바위"
        elif rand > 0.66:
            b = "보"
            
        if a == b:
            result = "비김"
            
        if str(a) == "가위" :
            if  str(b) == "바위" :
                result = "짐"
            elif  str(b) == "보" :
                result = "이김"
        
        if str(a) == "바위" :
            if  str(b) == "보" :
                result = "짐"
            elif  str(b) == "가위" :
                result = "이김"
        
        if str(a) == "보" :
            if  str(b) == "가위" :
                result = "짐"
            elif  str(b) == "바위" :
                result = "이김"
        
          
        self.le2.setText(str(b))
        self.le3.setText(result)   
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = windowClass() 
    myWindow.show()
    sys.exit(app.exec())



