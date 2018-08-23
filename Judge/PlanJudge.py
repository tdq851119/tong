# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchElementException
class judgePlan():
    def __init__(self,driver):
        self.driver=driver

    def planCheck(self,planmoney):
        #设置金额保留两位数
        planMoney = float(planmoney)
        planmo = '%.2f' % planMoney
        print u"设置金额保留两位小数后为:" + planmo

        text1 = u"成功加入" + planmo + u"元"
        print "text1为：" + text1

        try :
            #self.driver.find_element_by_id("tv_success_text")
            text2=self.driver.find_element_by_id("tv_success_text").text

            #将text文本去掉逗号
            text=text2.replace(",","")
            print "text为：" + text

            print u"---------------------找到检查点元素-----------------------"
        except NoSuchElementException:
            print u"--------------------没有找到检查点元素--------------------"
            text="null"

        if  text1==text:
            sta = "success"
            print u"---------------------检查点校验通过----------------------"
        else:
            sta = "fail"
            print u"---------------------检查点校验未通过--------------------"
        return sta
        # source = driver.page_source
        # if checkplan in source:
        #     sta = "success"
        #     print u"---------------------检查点校验通过--------------------"
        # else:
        #     sta = "fail"
        #     print u"---------------------检查点校验未通过--------------------"
        # return sta
