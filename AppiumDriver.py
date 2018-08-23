# -*- coding:utf-8 -*-
# DATE 2018-08-21
# AUTHER = tongzz
#
from appium import webdriver
#from string import maketrans
#import mysql.connector
import time
class Driver():
    #def __init__(self):
    #    pass
    # ===============================================================================
    # 初始化appium，并获取driver
    # ===============================================================================
    def getDriver(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'  # 设备系统k
        self.desired_caps['platformVersion'] = '5.1.1'  # 设备系统版本
        self.desired_caps['deviceName'] = '9c570495'  # 设备名称 95AQACPM48RPJ  9c570495
        self.desired_caps['appPackage'] = 'com.haodaibao.android'
        self.desired_caps['appActivity'] = 'com.haodaibao.android.views.launch.imp.LaunchActivity'
        #想用sendskeys输入中文时曹会用到这两个参数，否则不需要（意思是：使用unicodeKeyboard的编码方式来发送字符串，再就是将键盘给隐藏起来）
        self.desired_caps['unicodeKeyboard'] = 'True'
        self.desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",self.desired_caps)
        self.driver.implicitly_wait(30)
        print self.driver
        return self.driver


