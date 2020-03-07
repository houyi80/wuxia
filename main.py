#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from Ui_testform import Ui_Form

class Myform(QMainWindow,Ui_Form):
    def __init__(self):
        super(Myform,self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myform = Myform()
    myform.show()

    sys.exit(app.exec_())