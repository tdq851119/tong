# -*- coding: utf-8 -*-
# DATE 2018-08-21
# AUTHER = tongzz
#
import os
import os.path
import unittest
from unittest.loader import TestLoader
from tomorrow import threads
import HTMLTestRunner
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Runall():
    def loadTests(self):
        loader = TestLoader()
        discover=unittest.defaultTestLoader.discover("./testCases", pattern='*.py')  #RechargeCases WithdrawCases PasswdManageCase
        #discover=unittest.defaultTestLoader.discover("./123", pattern='*.py')
        suite = unittest.TestSuite()
        testlist =  discover._tests
        testlist = list(testlist)
        testCasesDict = {}
        testClassDict = {}
        for test in testlist:
            for x in test:
                for y in x:
                    yy = dir(y.__class__)
                    tempList = []
                    for y1 in yy:
                        if y1.startswith("test"):
                            print y1,y.__class__
                            tempList.append(y1)
                        else:
                            continue
                        testClassDict[str(y.__class__)] = y.__class__
                        testCasesDict[str(y.__class__)] = tempList
                    break
        for k in sorted(testClassDict.iterkeys()):
            for testValue in testCasesDict[k]:
                print testClassDict[k],testValue
                suite.addTest(testClassDict[k](testValue))
        return suite
    @threads(4)
    def run(self):
        testCases = self.loadTests()
        timestr = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        # filename = r'D:\workfile\hdb\python\report' + '\\' + timestr + 'result.html'
        filename = r"./report/%s.html" % timestr
        # filename = r'../report/'+now_time+'.html'
        # filename = r'./report/result.html'
        print filename
        fp = file(filename,"wb")
        runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u"钱包金融Android自动化",
        description = u"钱包金融Android自动化")
        runner.run(testCases)
if __name__ == "__main__":
        runTest = Runall()
        runTest.run()