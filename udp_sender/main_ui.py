# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(508, 383)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLineWidth(0)
        self.label.setMidLineWidth(10)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 5, 2, 1, 1)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        font2 = QFont()
        font2.setPointSize(14)
        self.progressBar.setFont(font2)
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 3, 1, 1, 2)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font3 = QFont()
        font3.setPointSize(12)
        self.pushButton_2.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_3, 6, 2, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setPointSize(7)
        font4.setItalic(True)
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_3, 7, 2, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)

        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 2)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setUnderline(True)
        self.label_2.setFont(font5)

        self.gridLayout.addWidget(self.label_2, 7, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"UDP_sender", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0443\u0437\u0430 \u043c\u0435\u0436\u0434\u0443 \u043f\u0430\u043a\u0435\u0442\u0430\u043c\u0438 (\u043c\u043a\u0441)", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Dialog", u"100", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Created by 010-Kobzev", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label_2.setText("")
    # retranslateUi

