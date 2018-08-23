# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchElementException
class judgeOutMoney():
    def __init__(self,driver):
        self.driver=driver

    def OutMoneyCheck(self,outmoney):
        #设置金额保留两位数
        outmo=float(outmoney)
        outmo1='%.2f' % outmo
        print u"设置金额保留两位小数后为:"+outmo1

        text1 = u"成功转出" + outmo1 + u"元"
        print "text1为：" + text1

        # time.sleep(3)
        try :
            self.driver.find_element_by_id("mainTex")
            text2=self.driver.find_element_by_id("mainTex").text

            #将text文本去掉逗号
            text=text2.replace(",","")
            print "text为：" + text

            print u"---------------------找到检查点元素-----------------------"
        except NoSuchElementException:
            print u"--------------------没有找到检查点元素--------------------"
            text="null"
        if  text1==text:
            sta="success"
            print u"---------------------检查点校验通过----------------------"
        else:
            sta="fail"
            print u"---------------------检查点校验未通过--------------------"
        return sta