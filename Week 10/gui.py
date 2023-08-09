# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiJsBSqK.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(240, 220)
        MainWindow.setMinimumSize(QSize(240, 220))
        MainWindow.setMaximumSize(QSize(240, 220))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_save = QPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(70, 140, 91, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_save.sizePolicy().hasHeightForWidth())
        self.button_save.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setKerning(True)
        self.button_save.setFont(font)
        self.button_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(20, 20, 51, 21))
        self.set_age = QLineEdit(self.centralwidget)
        self.set_age.setObjectName(u"set_age")
        self.set_age.setGeometry(QRect(99, 50, 121, 25))
        self.set_name = QLineEdit(self.centralwidget)
        self.set_name.setObjectName(u"set_name")
        self.set_name.setGeometry(QRect(99, 20, 121, 25))
        self.label_age = QLabel(self.centralwidget)
        self.label_age.setObjectName(u"label_age")
        self.label_age.setGeometry(QRect(20, 50, 51, 21))
        self.label_disclaimer = QLabel(self.centralwidget)
        self.label_disclaimer.setObjectName(u"label_disclaimer")
        self.label_disclaimer.setGeometry(QRect(60, 180, 121, 16))
        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(10, 100, 51, 21))
        self.check_student = QRadioButton(self.centralwidget)
        self.group_status = QButtonGroup(MainWindow)
        self.group_status.setObjectName(u"group_status")
        self.group_status.addButton(self.check_student)
        self.check_student.setObjectName(u"check_student")
        self.check_student.setGeometry(QRect(50, 100, 61, 20))
        self.check_staff = QRadioButton(self.centralwidget)
        self.group_status.addButton(self.check_staff)
        self.check_staff.setObjectName(u"check_staff")
        self.check_staff.setGeometry(QRect(120, 100, 61, 20))
        self.check_both = QRadioButton(self.centralwidget)
        self.group_status.addButton(self.check_both)
        self.check_both.setObjectName(u"check_both")
        self.check_both.setGeometry(QRect(170, 100, 61, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.set_name.setFocus()
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lab 10", None))
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_age.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.label_disclaimer.setText(QCoreApplication.translate("MainWindow", u"Please fill out all values", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.check_student.setText(QCoreApplication.translate("MainWindow", u"Student", None))
        self.check_staff.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.check_both.setText(QCoreApplication.translate("MainWindow", u"Both", None))
    # retranslateUi

