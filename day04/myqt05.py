import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from PyQt5 import uic
import random

form_class = uic.loadUiType("myqt05.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        

    def btnClick(self):
        rand = random.random()

        le1 = self.le1.getText()
        le2 = self.le2.text()
        le3 = self.le3.text();
        
        if rand < 0.5:
            le2 = self.le2.setText("홀")
        else:
            le2 = self.le2.setText("짝")
            
        if le1 == le2:
            le3 = self.le3.setText("성공!")
        else:
            le3 = self.le3.setText("실패!")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
     




