# 游戏心跳，现在先按照365天计算，后期会引入农历算法，加入24节气等。
from PyQt5.QtCore import QTimer

class Heartbeat():
    heartrate = 365 #最大天数，按照1年365天算。
    year = 0 #世界时间运行年数
    day = 0 #当前时间内的天数
    result = '' #反馈时间值

    def __init__(self):
        self.timer=QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timerout_slot)


    def timerout_slot(self):
        if self.day >= self.heartrate:
            self.year +=1
            self.day=0
        else:
            self.day +=1
        self.result=="现在是%d的第%d天"%(self.year,self.day)
        print(self.result)



if __name__ == "__main__":
    hb=Heartbeat()
