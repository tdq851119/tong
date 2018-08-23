# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchElementException
import re
class judgeInMoney():
    def __init__(self,driver):
        self.driver=driver

    def InMoneyCheck(self,inmoney):
        #设置金额保留两位小数
        inmo=float(inmoney)
        inmo1='%.2f' % inmo
        print u"设置金额保留两位小数后为:"+inmo1
        # #将金额设置带千分符
        # #inmo2=int(inmo1)
        # inmo3="{:,}".format(inmo1)
        # print u"设置千分符后的金额为:"+inmo3
        # print type(inmo3)
        text1=u"成功转入"+inmo1+u"元"
        print "text1为："+text1

        try:
            # self.driver.find_element_by_id("mainTex")
            text2 = self.driver.find_element_by_id("mainTex").text
            print text2

            # #取出获取文本的数字
            # text000 = re.sub(u"成功转入", "", text)
            # text00 = str(text000)
            # print "text00:"+text00
            # text0= re.sub(u"元", "", text00)
            # text=str(text0)
            # print "text"+text

            #将text文本去掉，
            text=text2.replace(",", "")
            print "text为："+text

            print u"---------------------找到检查点元素-----------------------"
        except NoSuchElementException:
            print u"--------------------没有找到检查点元素--------------------"
            text="null"
        if text1 == text:
            sta = "success"
            print u"---------------------检查点校验通过--------------------"
        else:
            sta = "fail"
            print u"---------------------检查点校验未通过--------------------"
        return sta