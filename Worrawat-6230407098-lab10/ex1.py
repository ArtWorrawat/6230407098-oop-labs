import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Exercise1(QWidget):
    def __init__(self):
        super(Exercise1, self).__init__()
        self.init_ui()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept
        else:
            event.ignore

    def init_ui(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
        btn.move(100, 50)
        label = QLabel(f"My name is {sys.argv[1]}", self)
        label.move(100, 25)

        self.setGeometry(500, 300, 300, 200)
        self.setWindowTitle('Exercise 1')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exercise1()
    sys.exit(app.exec_())
