import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Exercise1(QWidget):

    def __init__(self):
        super(Exercise1, self).__init__()
        self.label = []
        self.slider = []
        self.fbox = QFormLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.add_btn = QPushButton("Add")
        self.sub_btn = QPushButton("Subtract")
        self.mul_btn = QPushButton("Multiply")
        self.div_btn = QPushButton("Divide")
        self.line_edit = QLineEdit()
        self.prev_sender = None
        self.button_toggle = ""


        self.init_value = 50
        self.init_ui()

    def init_ui(self):

        self.labeling()
        self.slidering(1)
        self.slider[0].valueChanged[int].connect(self.change_value)
        self.slider[0].valueChanged[int].connect(self.calc)
        self.fbox.addRow(self.label[0], self.slider[0])

        self.labeling()
        self.slidering(2)
        self.slider[1].valueChanged[int].connect(self.change_value2)
        self.slider[1].valueChanged[int].connect(self.calc)
        self.fbox.addRow(self.label[1], self.slider[1])

        self.click_check = 0

        self.add_btn.clicked.connect(self.button_pressed)
        self.sub_btn.clicked.connect(self.button_pressed)
        self.mul_btn.clicked.connect(self.button_pressed)
        self.div_btn.clicked.connect(self.button_pressed)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.add_btn)
        hbox2.addWidget(self.sub_btn)
        hbox2.addWidget(self.mul_btn)
        hbox2.addWidget(self.div_btn)
        self.fbox.addRow(QLabel())
        self.fbox.addRow(hbox2)

        self.line_edit.setAlignment(Qt.AlignRight)
        self.line_edit.setReadOnly(True)
        self.fbox.addRow(QLabel())
        self.fbox.addRow(QLabel('Result   '),self.line_edit)

        self.setLayout(self.fbox)
        self.setGeometry(300, 200, 500, 100)
        self.setWindowTitle("Simple Calculator")
        self.show()

    def labeling(self):
        label = QLabel('')
        label.setText(str(self.init_value))
        label.setFont(QFont("Arial", 20))
        label.setStyleSheet("color: blue")
        self.label.append(label)

    def slidering(self, count):
        slider = QSlider(Qt.Horizontal, self)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.setTickPosition(QSlider.TicksAbove)
        slider.setTickInterval(5)
        self.slider.append(slider)

    def change_value(self, value):
        updated_value = value
        self.label[0].setText(str(updated_value))

    def change_value2(self, value):
        updated_value = value
        self.label[1].setText(str(updated_value))

    def button_pressed(self):
        sender = self.sender()
        if self.click_check == 0:
            self.click_check = 1
            sender.setStyleSheet("background-color: green")
            self.line_edit.setStyleSheet("color: yellow; background-color: grey")
            self.prev_sender = sender
            self.calc()
        else:
            self.prev_sender.setStyleSheet("")
            sender.setStyleSheet("background-color: green")
            self.prev_sender = sender
            self.calc()

        if sender.text() == "Add":
            self.button_toggle = "Add"
        elif sender.text() == "Multiply":
            self.button_toggle = "Multiply"
        elif sender.text() == "Subtract":
            self.button_toggle = "Subtract"
        elif sender.text() == "Divide":
            self.button_toggle = "Divide"


    def calc(self):
        if self.button_toggle == "Add":
            self.line_edit.setText(str(int(self.label[0].text()) + int(self.label[1].text())))
        elif self.button_toggle == "Subtract":
            self.line_edit.setText(str(int(self.label[0].text()) - int(self.label[1].text())))
        elif self.button_toggle == "Multiply":
            self.line_edit.setText(str(int(self.label[0].text()) * int(self.label[1].text())))
        elif self.button_toggle == "Divide":
            if self.label[1].text() == "0":
                self.line_edit.setText("Cant divide by zero")
            else:
                self.line_edit.setText(str(int(self.label[0].text()) / int(self.label[1].text())))
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Hi = Exercise1()
    sys.exit(app.exec_())
