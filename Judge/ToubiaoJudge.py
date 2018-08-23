# -*- coding: utf-8 -*-
import time
from Elements import ToubiaoElements
from appium.webdriver.webdriver import By
from selenium.common.exceptions import NoSuchElementException
class judgeToubiao():
    def __init__(self,driver):
        self.driver=driver

    '''投标校验'''
    def ToubiaoCheck(self):
        checktoubiao = u"恭喜投标成功"
        time.sleep(2)
        source = self.driver.page_source
        if checktoubiao in source:
            sta="success"
            print u"---------------------检查点校验通过--------------------"
        else:
            sta="fail"
            print u"---------------------检查点校验未通过--------------------"
        return sta

    '''分享标校验'''
    def ToubiaoShare(self):
        if self.driver.find_element(By.ID, ToubiaoElements.click_weixin):
            print u"---------------------检查点校验未通过--------------------"
            sta="fail"
        else :
            print u"---------------------检查点校验通过--------------------"
            sta = "success"
        return sta



