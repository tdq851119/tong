# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchElementException
class judgeSuggest():
    def __init__(self,driver):
        self.driver=driver

    def suggestCheck(self,text2):
        text1 = text2
        text = u"谢谢你的建议，我们将持续为您改进"
        try:
            text2 = self.driver.find_element_by_id("msgTex").get_attribute
            print u"----------------------找到检查点元素----------------------"
        except NoSuchElementException:
            print u"--------------------没有找到检查点元素--------------------"
            text2 = "null"
        time.sleep(3)
        if text == text1 and text == text2:
            sta = "success"
            print u"---------------------检查点校验通过--------------------"
        else:
            sta = "fail"
            print u"---------------------检查点校验未通过--------------------"
        return sta

