# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerVDJDfX.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QButtonGroup, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(350, 500)
        MainWindow.setMinimumSize(QSize(350, 500))
        MainWindow.setMaximumSize(QSize(350, 500))
        font = QFont()
        font.setUnderline(False)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(100, 10, 141, 16))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setUnderline(False)
        self.label_title.setFont(font1)
        self.label_title.setLayoutDirection(Qt.LeftToRight)
        self.label_food = QLabel(self.centralwidget)
        self.label_food.setObjectName(u"label_food")
        self.label_food.setGeometry(QRect(40, 60, 49, 21))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setUnderline(False)
        self.label_food.setFont(font2)
        self.label_drink = QLabel(self.centralwidget)
        self.label_drink.setObjectName(u"label_drink")
        self.label_drink.setGeometry(QRect(40, 100, 49, 21))
        self.label_drink.setFont(font2)
        self.label_dessert = QLabel(self.centralwidget)
        self.label_dessert.setObjectName(u"label_dessert")
        self.label_dessert.setGeometry(QRect(40, 140, 61, 21))
        self.label_dessert.setFont(font2)
        self.line_food = QLineEdit(self.centralwidget)
        self.line_food.setObjectName(u"line_food")
        self.line_food.setGeometry(QRect(150, 60, 141, 22))
        self.line_food.setAcceptDrops(False)
        self.line_food.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_drink = QLineEdit(self.centralwidget)
        self.line_drink.setObjectName(u"line_drink")
        self.line_drink.setGeometry(QRect(150, 100, 141, 22))
        self.line_drink.setAcceptDrops(False)
        self.line_drink.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_dessert = QLineEdit(self.centralwidget)
        self.line_dessert.setObjectName(u"line_dessert")
        self.line_dessert.setGeometry(QRect(150, 140, 141, 22))
        self.line_dessert.setAcceptDrops(False)
        self.line_dessert.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_tip = QLabel(self.centralwidget)
        self.label_tip.setObjectName(u"label_tip")
        self.label_tip.setGeometry(QRect(30, 180, 31, 16))
        self.label_tip.setFont(font2)
        self.button_submit = QPushButton(self.centralwidget)
        self.button_submit.setObjectName(u"button_submit")
        self.button_submit.setGeometry(QRect(70, 410, 91, 41))
        self.button_submit.setFont(font1)
        self.button_clear = QPushButton(self.centralwidget)
        self.button_clear.setObjectName(u"button_clear")
        self.button_clear.setGeometry(QRect(190, 410, 101, 41))
        self.button_clear.setFont(font1)
        self.radio_tip10 = QRadioButton(self.centralwidget)
        self.group_button_tip = QButtonGroup(MainWindow)
        self.group_button_tip.setObjectName(u"group_button_tip")
        self.group_button_tip.setExclusive(True)
        self.group_button_tip.addButton(self.radio_tip10)
        self.radio_tip10.setObjectName(u"radio_tip10")
        self.radio_tip10.setGeometry(QRect(80, 180, 61, 20))
        self.radio_tip10.setFont(font2)
        self.radio_tip10.setChecked(True)
        self.radio_tip15 = QRadioButton(self.centralwidget)
        self.group_button_tip.addButton(self.radio_tip15)
        self.radio_tip15.setObjectName(u"radio_tip15")
        self.radio_tip15.setGeometry(QRect(160, 180, 61, 20))
        self.radio_tip15.setFont(font2)
        self.radio_tip20 = QRadioButton(self.centralwidget)
        self.group_button_tip.addButton(self.radio_tip20)
        self.radio_tip20.setObjectName(u"radio_tip20")
        self.radio_tip20.setGeometry(QRect(240, 180, 61, 20))
        self.radio_tip20.setFont(font2)
        self.label_disclaimer = QLabel(self.centralwidget)
        self.label_disclaimer.setObjectName(u"label_disclaimer")
        self.label_disclaimer.setEnabled(True)
        self.label_disclaimer.setGeometry(QRect(80, 250, 191, 81))
        self.label_summary = QLabel(self.centralwidget)
        self.label_summary.setObjectName(u"label_summary")
        self.label_summary.setEnabled(True)
        self.label_summary.setGeometry(QRect(130, 230, 91, 21))
        self.label_summary_master = QLabel(self.centralwidget)
        self.label_summary_master.setObjectName(u"label_summary_master")
        self.label_summary_master.setGeometry(QRect(70, 260, 71, 131))
        self.label_summary_charges = QLabel(self.centralwidget)
        self.label_summary_charges.setObjectName(u"label_summary_charges")
        self.label_summary_charges.setGeometry(QRect(230, 260, 81, 141))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test 10", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"BILL CALCULATOR", None))
        self.label_food.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Food</p></body></html>", None))
        self.label_drink.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Drink</p></body></html>", None))
        self.label_dessert.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Dessert</p></body></html>", None))
        self.label_tip.setText(QCoreApplication.translate("MainWindow", u"Tip", None))
        self.button_submit.setText(QCoreApplication.translate("MainWindow", u"SUBMIT", None))
        self.button_clear.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.radio_tip10.setText(QCoreApplication.translate("MainWindow", u"10%", None))
        self.radio_tip15.setText(QCoreApplication.translate("MainWindow", u"15%", None))
        self.radio_tip20.setText(QCoreApplication.translate("MainWindow", u"20%", None))
        self.label_disclaimer.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Food, drink, and dessert </span></p>\n"
"<p align=\"center\" style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">need to be numeric </span></p>\n"
"<p align=\"center\" style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-bloc"
                        "k-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">e.g. 10.25 not $10.25</span></p></body></html>", None))
        self.label_summary.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">SUMMARY</span></p></body></html>", None))
        self.label_summary_master.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Food:</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Drink:</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Dessert:</span></p>\n"
""
                        "<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Tax:</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Tip:</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Total:</span></p></body></html>", None))
        self.label_summary_charges.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Food:</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Drink:</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Dessert:</span></p>\n"
""
                        "<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Tax:</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Tip:</span></p>\n"
"<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Total:</span></p></body></html>", None))
    # retranslateUi

