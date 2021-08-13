import  sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import*


class MySignal(QObject):#객체생성
    signal1 = pyqtSignal()

    def run(self):
        self.signal1.emit()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.run()

    @pyqtSlot()#장식자
    def signal1_emitted(self):
        print("signal1 emitted")

    @pyqtSlot(int, int)
    def signal2_emitted(self, arg1, arg2):
        print("signal2 emitted", arg1, arg2)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()


