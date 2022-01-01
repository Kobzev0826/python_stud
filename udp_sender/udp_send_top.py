# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:20:10 2020 by Vega.su

@author: Kobzev V.A.
"""


#from PyQt5 import uic, QtWidgets, QtCore
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import sys
#import UDP_send as udp
from time import sleep
from socket import *
import os
from PyQt5.QtCore import QThread
from main_ui import Ui_Dialog

#----------------------------------------------------------------------------
class ProgressBarThread(QThread):
    def __init__(self, mainwindow, parent=None):
        super(ProgressBarThread, self).__init__(parent)
        self.mainwindow = mainwindow
    
    
    def run(self):
        file_path = ui.lineEdit.text()
        sleep_time = float(ui.lineEdit_2.text()) * 0.000001
        print(sleep_time)
        #ui.lineEdit_2.setText(sleep_time)
        file_size = os.path.getsize(file_path)
        IPADDR = ip_conf()# '192.168.137.255'
    
        PORTNUM = 100
    
        s=socket(AF_INET,SOCK_DGRAM, 0)

        s.connect((IPADDR,PORTNUM)) 
        
        value=self.mainwindow.progressBar.value()
        step = 255/file_size
        print(step)
        with open (file_path,'rb') as in_file:
            while True:
                hexdata = in_file.read(256).hex()
                
                if len(hexdata) == 0:
                    #print('rich the end')
                    self.mainwindow.progressBar.setValue(100)
                    break
    
            
                s.send(bytes.fromhex(hexdata.upper()))
                value = value + 1
                #print(value)
                self.mainwindow.progressBar.setValue(value*step*100)
                sleep(sleep_time)
        ui.label_2.setText('Succesfully completed')
#----------------------------------------------------------------------------        


def ip_conf():
    ip=''
    host = gethostbyname(gethostname()).split('.')[:-1]
    for item in host:
        ip = ip + item+'.'
    return(ip+'255')        

#функция запускающая отдельный поток, созданный классом
def launch_progressbar_filling(ui):
    try:
        ProgresbarThread_instance.start()
    except:
        ui.label_2.setText('Error with sending')
#функция для обзора файла
def Open_File(self):
    global filedir
    filedir = QFileDialog().getOpenFileName(filter='rbf_file (*.rbf)')
    #print(filedir[0])                                                    
    
    ui.lineEdit.setText(str(filedir[0]))

#работа с GUI
#Create app
app = QApplication(sys.argv)

#init
Dialog = QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ProgresbarThread_instance = ProgressBarThread(mainwindow=ui)#экземпляр класса
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#подключения объекта
ui.pushButton.clicked.connect(launch_progressbar_filling)
ui.pushButton_2.clicked.connect(Open_File)

#exit from app
try:
    sys.exit(app.exec_())
except:
    print('Fail')