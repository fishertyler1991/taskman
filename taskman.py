import sys
import palaToolkit as ptk
from PyQt6.QtWidgets import QApplication, QMainWindow

mainApp = QApplication(sys.argv)
mainWindow = QMainWindow()
mainWindow.setWindowTitle("PalaTaskMan")
mainWindow.setGeometry(100, 100, 800, 600)
mainWindow.show()
sys.exit(mainApp.exec())