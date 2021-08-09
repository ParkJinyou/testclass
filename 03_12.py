'''import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QLabel("Hello")
label.show()
app.exec_()'''

import  sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() #여기까지는 그냥 창 띄우는 용도 (변하지 않음)
        self.setGeometry(100,200,300,400)
        self.setWindowTitle("Jinyoouuu")
        btn = QPushButton("버튼1",self)
        btn.move(80,80)
        btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼 클릭")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()




