#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 14:41
# @Author  : Ft
# @Site    : 
# @File    : Playsound.py
import os
class playsound:
    def __init__(self):
        self.th=0
        self.an=0
    def run_threaded(self,angle,throttle):
        print ("happy")
        if angle is not None and throttle is not None:
            self.throttle=throttle
            self.angle=angle
            print ("happy")
            if self.angle<-0.2 and self.an!=1: #左转
                self.an=1
                os.system('mplayer %s' % 'music/2.mp3')
            elif self.angle>0.2 and self.an!=2:#右转
                self.an=2
                os.system('mplayer %s' % 'music/3.mp3')
            elif self.throttle<0.6 and self.th==2:    #减速
                self.th=0
                os.system('mplayer %s' % 'music/4.mp3')
            elif self.throttle >0.3 and self.throttle<0.6 and self.th!=1: #前进
                self.th=1
                os.system('mplayer %s' % 'music/0.mp3')
            elif self.throttle>0.6 and self.th!=2: #加速前进
                self.th=2
                os.system('mplayer %s' % 'music/1.mp3')
            elif self.throttle==0 and self.angle==0 and self.th!=0 and  self.an!=0:
                self.th=0
                self.an=0
                os.system('mplayer %s' % 'music/5.mp3')
    def update(self):
        print ("happy newyear")
        if self.angle<-0.2 and self.an!=1: #左转
            self.an=1
            os.system('mplayer %s' % 'music/2.mp3')
        elif self.angle>0.2 and self.an!=2:#右转
            self.an=2
            os.system('mplayer %s' % 'music/3.mp3')
        elif self.throttle<0.6 and self.th==2:    #减速
            self.th=0
            os.system('mplayer %s' % 'music/4.mp3')
        elif self.throttle >0.3 and self.throttle<0.6 and self.th!=1: #前进
            self.th=1
            os.system('mplayer %s' % 'music/0.mp3')
        elif self.throttle>0.6 and self.th!=2: #加速前进
            self.th=2
            os.system('mplayer %s' % 'music/1.mp3')
        elif self.throttle==0 and self.angle==0 and self.th!=0 and  self.an!=0:
            self.th=0
            self.an=0
            os.system('mplayer %s' % 'music/5.mp3')

