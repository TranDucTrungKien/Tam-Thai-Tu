import sys
from PyQt6.QtWidgets import QApplication
from MainWindowEx import MainWindowEx


app = QApplication(sys.argv)
window = MainWindowEx()
window.setWindowTitle("Máy tính đơn giản")
window.show()
sys.exit(app.exec())

