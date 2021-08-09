import  sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit # 모듈자체

form_class = uic.loadUiType('window.ui')[0]

class MyWindow(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)


    def inquiry(self):
        price = pykorbit.get_current_price('BTC')
        self.lineEdit.setText(str(price))
        price_2 = pykorbit.get_current_price('ETH')
        self.lineEdit_2.setText(str(price_2))
        price_3 = pykorbit.get_current_price('XRP')
        self.lineEdit_3.setText(str(price_3))
        price_4 = pykorbit.get_current_price('ADA')
        self.lineEdit_4.setText(str(price_4))


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()