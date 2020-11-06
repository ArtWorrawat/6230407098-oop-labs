import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
        btn = QPushButton('OK', self)
        btn1 = QPushButton('CANCEL', self)
        btn.move(90, 250)
        btn1.move(190, 250)


        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        emtry = QLabel(' ')
        grid.addWidget(emtry, 9, 0)
        emtry1 = QLabel(' ')
        grid.addWidget(emtry, 10, 0)
        self.setLayout(grid)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle(f'Review by {sys.argv[1]}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    sys.exit(app.exec())