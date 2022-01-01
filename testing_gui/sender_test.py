from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import sys
from main_ui import Ui_Dialog
from gui import Example


#Create app
app = QApplication(sys.argv)

#init
Dialog = QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

#Connection

ui.buttonBox.clicked.connect(Example.Open_File())

#Main Loop
sys.exit(app.exec_(self))

print('Hello World!')