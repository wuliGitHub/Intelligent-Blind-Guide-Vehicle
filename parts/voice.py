#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 11:40
# @Author  : Ryu
# @Site    : 
# @File    : voice.py
# @Software: PyCharm
import wave
from pyaudio import PyAudio,paInt16
import time
import numpy as np
import donkeycar.parts.voice_recognize as voice  # 导入语音识别和语音合成的函数
import os
NUM_SAMPLES = 2000
chunk = 1024
def save_wave_file(filename,data):
	# 语音识别需要保存的格式为 单声道、双字节、16K频率
    wf = wave.open(filename,'wb')
    wf.setnchannels(1)   #set channel
    wf.setsampwidth(2)  #采样字节  1 or 2
    wf.setframerate(16000)  #采样频率  8K or 16K
    wf.writeframes(b"".join(data))
    wf.close()
def voice_control(filename):
    file = filename
    f = open(file,'r')
    command = f.read()
    f.close()  # close file aviod IOException
    print (command)
    if "图" in command or "书" in command:
        os.system('mplayer %s' % 'music/tsg.mp3')
        return "/home/pi/mycar/models/mypilot.h5"
    elif "教" in command or "室" in command:
        os.system('mplayer %s' % 'music/js.mp3')
        return "/home/pi/mycar/models/mypilot2.h5"
    else:
        return "no"



def monitor():
    print ("声音检测实现语音识别和合成，Press Ctrl+C to exit ")
    pa = PyAudio()  # 实例化pyaudio
    stream = pa.open(format=paInt16,
                     channels=1,
                     rate=16000,
                     input=True,
                     frames_per_buffer=NUM_SAMPLES)
    print('开始缓存录音')

    # 初始化缓存数组
    audioBuffer = []
    rec = []
    # 初始化标志位
    audioFlag = False
    t = False
    while True:
        try:
            # 读取采样音频并获取特征信息
            data = stream.read(NUM_SAMPLES, exception_on_overflow=False)  # add exception para
            audioBuffer.append(data)  # 录音源文件
            audioData = np.fromstring(data, dtype=np.short)  # 字符串创建矩阵
            largeSampleCount = np.sum(audioData > 1000)  # 采样变量
            temp = np.max(audioData)  # 获取声音强度
            print (temp)

            if temp > 4000 and t == False:  # 设置声音检测阈值，需根据麦克风适当调整
                t = 1  # 开始录音
                print ("检测到语音信号，开始录音")
                begin = time.time()
                print (temp)

            if t:
                saveCount=1
                end = time.time()
                if end - begin > 5:
                    timeFlag = 1  # 5s录音结束
                if largeSampleCount > 20:
                    saveCount = 4
                else:
                    saveCount -= 1
                if saveCount < 0:
                    saveCount = 0
                if saveCount > 0:
                    rec.append(data)  # 合成数据
                else:
                    if len(rec) > 0 or timeFlag:
                        save_wave_file('detected_voice.wav', rec)  # 保存检测的语音
                        voice.identify_synthesize('detected_voice.wav')  # 调用百度语音实现语音识别和语音合成
                        # os.system('mplayer %s' % 'synthesis.mp3')	# play synthesis
                        mode=voice_control('result.txt')
                        # 清除缓存
                        rec = []
                        t = 0
                        timeFlag = 0
                        print (1)
                        print (mode)
                        print (2)
                        return mode

                        break

        except KeyboardInterrupt:
            break

    # 释放资源
    stream.stop_stream()
    stream.close()
    pa.terminate()
