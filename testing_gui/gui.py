#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QPushButton,QFileDialog,QLineEdit
from PyQt5.QtCore import  QCoreApplication
#from PyQt5 import uic, QtWidgets, QtCore


class Example(QWidget):

    def __init__(self):
        super().__init__()

        

        
        self.initUI()

    def initUI(self):


       
        btn = QPushButton('Open File', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(self.Open_File)
        btn.resize(btn.sizeHint())
        btn.move(150, 50)

        btn1 = QPushButton('Send', self)
        btn1.setToolTip('This button is <b>Send</b> your file')
        btn1.clicked.connect(self.Send)
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 50)

        lineEdit = QLineEdit(self)
        lineEdit.move(50,10)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('udp sender')
        self.show()
        
    def Send(self):
        print('Send')


    
    def Open_File(self):
        filedir = QFileDialog.getOpenFileName(filter='rbf_file (*.rbf)')
        self.lineEdit.setText('path')
    
    


'''
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
'''

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())