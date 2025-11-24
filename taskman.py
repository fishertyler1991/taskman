import sys
import palaToolkit as ptk
import PyQt6.QtWidgets as _Q

#Define global vars
DEF_X = 100
DEF_Y = 100
DEF_W = 800
DEF_H = 600

#Define global classes/funcs

def getProcs() -> str:
    return "Llol"

#Define secondary global vars

#Create main app and Window
mainApp = _Q.QApplication(sys.argv)
mainWindow = _Q.QMainWindow()
mainWindow.setWindowTitle("PalaTaskMan")
mainWindow.setGeometry(DEF_X, DEF_Y, DEF_W, DEF_H)

#Build base app
overLabel = _Q.QWidget()
mainWindow.setCentralWidget(overLabel)
mainLayout = _Q.QVBoxLayout()
textLabelA = _Q.QLabel("Task Manager")
buttonLabelA = _Q.QPushButton("Click this")
mainLayout.addWidget(textLabelA)
mainLayout.addWidget(buttonLabelA)
overLabel.setLayout(mainLayout)

#Display app
mainWindow.show()

#Start loop and handle exit
sys.exit(mainApp.exec())

#testing beta branch