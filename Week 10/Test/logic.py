from gui import *
from PyQt6.QtCore import QCoreApplication

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__tax = .10

        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_submit.clicked.connect(lambda: self.submit())

        self.hide_all()


    def submit(self):
        try:
            costFood = float(self.line_food.text())
            costDrink = float(self.line_drink.text())
            costDessert = float(self.line_dessert.text())
        except:
            self.show_disclaimer()
            return

        subtotal = costFood + costDrink + costDessert
        costTax = subtotal * self.__tax
        costTip = ( subtotal + costTax ) * self.get_tip_percentage()

        total = subtotal + costTax + costTip


        # Displaying Results!!!

        displayFood = '${:,.2f}'.format(costFood)
        displayDrink = '${:,.2f}'.format(costDrink)
        displayDessert = '${:,.2f}'.format(costDessert)
        displayTax = '${:,.2f}'.format(costTax)
        displayTip = '${:,.2f}'.format(costTip)
        displayTotal = '${:,.2f}'.format(total)

        self.update_summary(displayFood, displayDrink, displayDessert, displayTax, displayTip, displayTotal)
        self.show_summary()



    def update_summary(self, displayFood, displayDrink, displayDessert, displayTax, displayTip, displayTotal):
                self.label_summary_charges.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">" + displayFood +"</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">" + displayDrink +"</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">" + displayDessert +"</span></p>\n"
""
                        "<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">" + displayTax + "</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">" + displayTip + "</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">" + displayTotal + "</span></p></body></html>", None))

    def clear(self):
        self.hide_all()

        self.line_food.setText('')
        self.line_drink.setText('')
        self.line_dessert.setText('')

        self.group_button_tip.setExclusive(False)
        self.radio_tip10.setChecked(True)
        for radioButton in [self.radio_tip15, self.radio_tip20]:
            radioButton.setChecked(False)
        self.group_button_tip.setExclusive(True)

        self.line_food.setFocus()

    def get_tip_percentage(self):
        if self.radio_tip10.isChecked():
            return .10
        elif self.radio_tip15.isChecked():
            return .15
        elif self.radio_tip20.isChecked():
            return .20


    def show_summary(self):
        self.label_disclaimer.hide()

        self.label_summary.show()
        self.label_summary_master.show()
        self.label_summary_charges.show()

    def show_disclaimer(self):
        self.label_summary.hide()
        self.label_summary_master.hide()
        self.label_summary_charges.hide()

        self.label_disclaimer.show()

    def hide_all(self):
        self.label_summary.hide()
        self.label_summary_master.hide()
        self.label_summary_charges.hide()

        self.label_disclaimer.hide()

        return
