import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class FormLayout(QWidget):
    def __init__(self):
        super(FormLayout, self).__init__()
        self.init_ui()

    def init_ui(self):
        fbox = QFormLayout()
        label_name = QLabel("Name")
        self.edit_name = QLineEdit()

        fbox.addRow(label_name, self.edit_name)

        hbox = QHBoxLayout()
        checkbox1 = QCheckBox("PyQt")
        checkbox1.stateChanged.connect(lambda: self.check_Qt(checkbox1))
        checkbox2 = QCheckBox("PyGame")
        checkbox2.toggled.connect(lambda: self.check_game(checkbox2))
        checkbox3 = QCheckBox("PyTorch")
        checkbox3.toggled.connect(lambda: self.check_torch(checkbox3))
        hbox.addWidget(checkbox1)
        hbox.addWidget(checkbox2)
        hbox.addWidget(checkbox3)
        hbox.addStretch()
        fbox.addRow(hbox)

        btn_submit = QPushButton("Submit")
        btn_submit.clicked.connect(self.naming)
        self.edit_name.returnPressed.connect(btn_submit.click)
        btn_cancel = QPushButton("Cancel")
        fbox.addRow(btn_submit, btn_cancel)


        self.setLayout(fbox)
        self.setWindowTitle("Problem 3")
        self.show()

    def naming(self):
        print(f"Name is {self.edit_name.text()}")

    def check_Qt(self, state):
        if state.isChecked():
            print("PyQt is selected")
        else:
            print("PyQt is deselected")

    def check_game(self, state):
        if state.isChecked():
            print("PyGame is selected")
        else:
            print("PyGame is deselected")

    def check_torch(self, state):
        if state.isChecked():
            print("PyTorch is selected")
        else:
            print("PyTorch is deselected")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Hi = FormLayout()
    sys.exit(app.exec())
