import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from Ui_MainWindow import Ui_MainWindow
from DataStore import DataStore

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ds = DataStore()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.ui.bmr_batton.clicked.connect(self.showBMR)
        self.ui.bmi_button.clicked.connect(self.showBMI)

        self.ui.bmr_calculate_button.clicked.connect(self.calcBMR)
        self.ui.bmi_calculate_button.clicked.connect(self.calcBMI)


    def show(self):
        self.main_win.show()

    def showBMR(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bmr)

    def showBMI(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bmi)

    def calcBMR(self):
        if self.ui.bmr_male_radio.isChecked():
            gender = "male"
        else:
            gender = "female"
        height = int(self.ui.bmr_height_input.text())
        weight = int(self.ui.bmr_weight_input.text())
        age = int(self.ui.bmr_age_input.text())

        if self.ui.bmr_sedentary.isChecked():
            activity = "sedentary"
        elif self.ui.bmr_lighthy.isChecked():
            activity = "lighthy"
        elif self.ui.bmr_moderately.isChecked():
            activity = "moderately"
        elif self.ui.bmr_very.isChecked():
            activity = "very"
        else:
            activity = "extremely"

        result = self.ds.bmr_calc(gender, height, weight, age, activity)

        output = "The BMR for a {} year old {}, who is {} cm tall and {} kg heavy with a {} activity level is {} calories.".format(age, gender, height, weight, activity, result)

        self.ui.bmr_output_label.setText(output)

    def calcBMI(self):
        height = int(self.ui.bmi_height_input.text())
        weight = int(self.ui.bmi_weight_input.text())

        result = self.ds.bmi_calc(height, weight)

        outpuut = "You entered the following information for BMI: Height {} cm & Weight: {} kg. This meansyourBMI is {}".format(height, weight, result)

        self.ui.bmi_output_label.setText(outpuut)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())