import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class FormLayout(QWidget):
    def __init__(self):
        super(FormLayout, self).__init__()
        self.init_ui()

    def init_ui(self):
        label_name = QLabel("Name")
        edit_name = QLineEdit()

        fbox = QFormLayout()
        label = QLabel("Simple Form")
        label.move(20, 0)
        label.setFont(QFont('Arial', 18))
        label.setStyleSheet("color: rgb(0, 0, 255);")
        fbox.addRow(QLabel(''), label)
        fbox.addRow(label_name, edit_name)
        vbox = QVBoxLayout()

        hbox = QHBoxLayout()
        radio_male = QRadioButton("Male")
        radio_female = QRadioButton("Female")
        hbox.addWidget(radio_male)
        hbox.addWidget(radio_female)
        hbox.addStretch()
        fbox.addRow(QLabel("Gender"), hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(QPushButton("Submit"))
        hbox.addWidget(QPushButton("Cancel"))
        fbox.addRow(hbox)

        self.setLayout(fbox)
        self.setGeometry(500, 250, 300, 100)
        self.setWindowTitle("Problem 1")
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    Hi = FormLayout()
    sys.exit(app.exec())