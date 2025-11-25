import sys
import palaToolkit as ptk
import PyQt6.QtWidgets as _Q
from time import time

DEF_X = 100
DEF_Y = 100
DEF_W = 800
DEF_H = 600

def getProcs() -> str:
    if ptk._checkOS() == ptk.OS_TYPES.UNIX:
        return "Llol" + str(time())

class TASKMANAPP(_Q.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PalaTaskMan")
        self.setGeometry(DEF_X, DEF_Y, DEF_W, DEF_H)

        overLabel = _Q.QWidget()
        self.setCentralWidget(overLabel)
        mainLayout = _Q.QVBoxLayout()
        overLabel.setLayout(mainLayout)

        self.textLabelA = _Q.QLabel("Task Manager")
        self.buttonLabelA = _Q.QPushButton("Click this")
        mainLayout.addWidget(self.textLabelA)
        mainLayout.addWidget(self.buttonLabelA)

        self.buttonLabelA.clicked.connect(self.BLA_Clicked)

    def BLA_Clicked(self):
        self.textLabelA.setText(getProcs())


mainApp = _Q.QApplication(sys.argv)
mainWindow = TASKMANAPP()
mainWindow.show()

sys.exit(mainApp.exec())