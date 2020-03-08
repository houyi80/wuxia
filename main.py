# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys,time
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QTimer,QThread,pyqtSignal
from Ui_testform import Ui_Form


class Myform(QMainWindow,Ui_Form):
    def __init__(self):
        super(Myform,self).__init__()
        self.setupUi(self)

        self.step = 0
        # 初始化一个定时器
        self.timer = QTimer(self)
        # 定义时间超时连接start_app
        self.timer.timeout.connect(self.start)
        # 定义时间任务是一次性任务
        # self.timer.setSingleShot(True)
        # 启动时间任务
        self.timer.start(1000)
        self.work = WorkThread()
        self.work.trigger.connect(self.UpText)

        self.datawork = DataThread()
        self.datawork.datatrigger.connect(self.pbr)

    def start(self):
        self.work.start()
        self.datawork.start()

    def UpText(self,str):
        self.infoBox.append(str)

    def pbr(self,):
        if self.step >=365:
            self.step =0
            return
        self.step +=1
        self.pb_time.setValue(self.step)

class WorkThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self):
        super(WorkThread,self).__init__()

    def run(self):
        self.trigger.emit(time.strftime("%H:%M:%S"))

class DataThread(QThread):
    datatrigger = pyqtSignal()
    
    def __init__(self):
        super(DataThread,self).__init__()

    def run(self):        
        self.datatrigger.emit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myform = Myform()
    myform.show()
    sys.exit(app.exec_())