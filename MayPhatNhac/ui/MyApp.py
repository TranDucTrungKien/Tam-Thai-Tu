import sys
from PyQt6.QtWidgets import QApplication
from MainWindowEx import MainWindowEx

app = QApplication(sys.argv)
mainWindow = MainWindowEx()
mainWindow.show()
sys.exit(app.exec())
