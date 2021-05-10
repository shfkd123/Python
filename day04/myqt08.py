import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import random


form_class = uic.loadUiType("myqt08.UI")[0]

class windowClass(QMainWindow, form_class):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        a = int(self.le1.text())
        
        for i in range(1, 10):
            tb = self.tb.setText(str(a) + "*" + i + "=" + str(a*i) + "\n")   
        self.tb.setText(tb);   
            
       
#        self.tb.append(str(a) +"X 1"+"="+str( a*1) +"\n" )
#        self.tb.append(str(a) +"X 2"+"="+str( a*2) +"\n" )
#        self.tb.append(str(a) +"X 3"+"="+str( a*3) +"\n" )
#        self.tb.append(str(a) +"X 4"+"="+str( a*4) +"\n" )
#        self.tb.append(str(a) +"X 5"+"="+str( a*5) +"\n" )
#        self.tb.append(str(a) +"X 6"+"="+str( a*6) +"\n" )
#        self.tb.append(str(a) +"X 7"+"="+str( a*7) +"\n" )
#        self.tb.append(str(a) +"X 8"+"="+str( a*8) +"\n" )
#        self.tb.append(str(a) +"X 9"+"="+str( a*9) +"\n" )
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = windowClass() 
    myWindow.show()
    sys.exit(app.exec())



