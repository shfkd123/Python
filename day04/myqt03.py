import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from PyQt5 import uic

form_class = uic.loadUiType("myqt03.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)

    def btnClick(self):
        
        le1 = int(self.le1.text())
        le2 = int(self.le2.text())
        
        self.le3.setText(str(le1 + le2))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
     




