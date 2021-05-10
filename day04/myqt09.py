import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


form_class = uic.loadUiType("myqt09.UI")[0]

class windowClass(QMainWindow, form_class):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.btnClick)
        self.pb2.clicked.connect(self.btnClick)
        self.pb3.clicked.connect(self.btnClick)
        self.pb4.clicked.connect(self.btnClick)
        self.pb5.clicked.connect(self.btnClick)
        self.pb6.clicked.connect(self.btnClick)
        self.pb7.clicked.connect(self.btnClick)
        self.pb8.clicked.connect(self.btnClick)
        self.pb9.clicked.connect(self.btnClick)
        self.pb0.clicked.connect(self.btnClick)
        self.pbcall.clicked.connect(self.btnClick)
        
    def btnClick(self):
        a1 = int(self.pb1.text())
        self.le1.setText(str(a1))
        a2 = int(self.pb2.text())
        self.le1.setText(str(a2))
        a3 = int(self.pb3.text())
        self.le1.setText(str(a3))
        a4 = int(self.pb4.text())
        self.le1.setText(str(a4))
        a5 = int(self.pb5.text())
        self.le1.setText(str(a5))
        a6 = int(self.pb6.text())
        self.le1.setText(str(a6))
        a7 = int(self.pb7.text())
        self.le1.setText(str(a7))
        a8 = int(self.pb8.text())
        self.le1.setText(str(a8))
        a9 = int(self.pb9.text())
        self.le1.setText(str(a9))
        a0 = int(self.pb0.text())
        self.le1.appendText(str(a0))
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = windowClass() 
    myWindow.show()
    sys.exit(app.exec())



