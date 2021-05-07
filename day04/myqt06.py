import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from PyQt5 import uic
import random

form_class = uic.loadUiType("myqt06.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        

    def btnClick(self):

        le1 = int(self.le1.text())
        le2 = int(self.le2.text())
        
        sum = 0
        for i in range(le1, le2+1):
            if(i % 2 == 0):
                sum += i
        self.le3.setText(str(sum))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
     




