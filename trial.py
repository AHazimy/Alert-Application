from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
#import os 
import pandas as pd
import winsound
import time
from MainWindow import Ui_MainWindow
from dialog import Ui_Dialog
#import sys
from threading import *
from datetime import datetime as dt
import socket

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(522,441)
        self.start_btn.clicked.connect(self.thread)
        self.stop_btn.clicked.connect(self.stop_loop)
        self.comboBox.addItems(['Sound 1','Sound 2'])
        self.play_btn.clicked.connect(self.play_test_thread)
        # self.listen_thread()
        #widget=QWidget()
        #self.setCentralWidget(self.splitter_3)

    init_value=0
    
    date_list=[]

    def start_loop(self):  
        self.date_list.clear()      
        self.init_value=0
        self.date_label.setText('')
        self.label.setStyleSheet('background-color:rgb(0, 255, 0)')
        self.label.setText('Nothing Yet')
        #self.scan_label.setText('Stopped')
        while self.init_value!=1:
            self.start_btn.setEnabled(False)
            self.comboBox.setEnabled(False)
            self.play_btn.setEnabled(False)
            s = socket.socket()        
    
            # Define the port on which you want to connect
            port = 12345   
            s.connect(('127.0.0.1', port))
            #print(s.recv(1024).decode())
            
            x=s.recv(1024).decode()
            
            print("Current value is:\n"+x+"\nCurrent Date is: "+str(dt.now()))
            # close the connection
            #s.close()
            time.sleep(1)
            # if x==1:
            #     break 
            # try:
            #     df = pd.read_csv('trial_2.csv', delim_whitespace=True)
            # except:
            #     continue
            # x = df.at[0,'Status']

            # print(x)
            if int(x) == 1:
                now=dt.now()
                
                self.date_list.append(now.strftime("%Y-%m-%d %H:%M:%S"))
                self.label.setText('Target Detected')
                self.date_label.setText(str(self.date_list[0]))
                #self.thread_color()
                winsound.PlaySound(str(self.comboBox.currentText()+".wav"), winsound.SND_FILENAME)
                self.label.setStyleSheet('background-color:yellow')
                time.sleep(0.5)
                self.label.setStyleSheet('background-color:red')

                # if x==1:
                #     break

            elif int(x) !=1:             
                self.label.setStyleSheet('background-color:rgb(0, 255, 0)')
                self.label.setText('Nothing Yet')
                self.date_list.clear()
                # if x==1:
                #     self.label.setStyleSheet('background-color:rgb(0, 255, 0)')
                #     self.label.setText('Nothing Yet')
                #     break 

            self.scan_label.setText('Scanning....')
            #time.sleep(1)
        self.label.setStyleSheet('background-color:rgb(0, 255, 0)')
        self.label.setText('Nothing Yet')
        self.scan_label.setText('Stopped')


    def play_test(self):
        winsound.PlaySound(str(self.comboBox.currentText()+".wav"), winsound.SND_FILENAME)

    def play_test_thread(self):
        t1=Thread(target=self.play_test, daemon=True)
        t1.start()

    def stop_loop(self):   
        self.init_value=1
        #time.sleep(0.5)       
        self.label.setStyleSheet('background-color:rgb(0, 255, 0)')
        self.label.setText('Nothing Yet')
        self.scan_label.setText('Stopped')
        self.start_btn.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.play_btn.setEnabled(True)



    def thread(self):
        t1=Thread(target=self.start_loop, daemon=True)
        t1.start()


   

app = QApplication([])
window = MainWindow()
window.show()
app.exec()


