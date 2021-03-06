import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5 import uic

tickers=["BTC","ETH","BCH","ETC"]
from_class = uic.loadUiType('bull.ui')[0]

class MyWindow(QMainWindow,from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)

    def timeout(self):
        for i,ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i,0,item)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
