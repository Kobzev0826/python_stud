# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:50:42 2020

@author: User
"""
from PyQt5 import uic, QtWidgets, QtCore
import sys
#from time import sleep
#from socket import *
#import os
#from PyQt5.QtCore import QThread


'''
def Open_File(self):
    global filedir
    filedir = QtWidgets.QFileDialog().getOpenFileName(filter='rbf_file (*.rbf)')
    #print(filedir[0])                                                    
    
    win.lineEdit.setText(str(filedir[0]))
'''


#работа с GUI
app= QtWidgets.QApplication([])
win=uic.loadUi('main.ui')

#win.pushButton_2.clicked.connect(Open_File)

win.show()
sys.exit(app.exec())