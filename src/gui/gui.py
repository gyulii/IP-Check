
from PySide6.QtWidgets import QApplication, QWidget , QMainWindow

from MainWindow import Ui_MainWindow

import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

app = QApplication(sys.argv)
w = MainWindow()
app.exec()