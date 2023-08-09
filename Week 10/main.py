from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__DEFAULTDISCLAIMERTEXT = self.label_disclaimer.text()
        # Control Mappings
        self.button_save.clicked.connect(lambda: self.save())

    def save(self):
        name = self.set_name.text().strip()
        age = self.set_age.text().strip()

        if not age.isdigit():
            self.label_disclaimer.setText("Enter correct age value")
            self.set_age.setFocus()
            return

        status = self.__get_status()

        self.label_disclaimer.setText(self.__DEFAULTDISCLAIMERTEXT)
        age10 = int(age)*10

        with open('data.csv', 'a', newline='') as file:
            csvfile = csv.writer(file)
            csvfile.writerow( [name, age10, status] )

        # Clean up
        self.label_disclaimer.setText("Entry Saved")
        self.set_name.setText("")
        self.set_age.setText("")

        self.group_status.setExclusive(False)
        for radioButton in [self.check_both, self.check_staff, self.check_student]:
            radioButton.setChecked(False)
        self.group_status.setExclusive(True)
        self.set_name.setFocus()

        return


    def __get_status(self):

        if self.check_staff.isChecked():
            return "Staff"
        elif self.check_student.isChecked():
            return "Student"
        elif self.check_both.isChecked():
            return "Both"

        return "NA"


def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()