import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Exercise2(QMainWindow):
    def __init__(self):
        super(Exercise2, self).__init__()
        self.init_ui()

    def init_ui(self):


        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        edit_menu = QMenu('Edit', self)
        copy_act = QAction("Copy", self)
        paste_act = QAction("Paste", self)

        edit_menu.addAction(copy_act)
        edit_menu.addAction(paste_act)


        new_act = QAction('New', self)
        file_menu.addAction(new_act)
        file_menu.addMenu(edit_menu)

        exit_act = QAction(QIcon('app-icon.jpg'), 'Exit', self)
        exit_act.setShortcut("Ctrl+Q")
        exit_act.setStatusTip("Exit application")
        exit_act.triggered.connect(QApplication.instance().quit)
        exit_act.setStatusTip("Saveee")


        save_act = QAction('save', self)
        save_act.setShortcut("Ctrl+S")
        file_menu.addAction(save_act)
        file_menu.addAction(exit_act)

        self.statusBar().showMessage(f"By {sys.argv[1]}")
        self.setGeometry(500, 300, 300, 200)
        self.setWindowTitle("Exercise2")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = Exercise2()
    sys.exit(app.exec_())