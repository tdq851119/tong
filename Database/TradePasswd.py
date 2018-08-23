# -*- coding: utf-8 -*-
# DATE 2018-08-21
# AUTHER = tongzz
#

import MySQLdb
from Elements.LoginElements import *
import datetime
import sys
class Tradepasswd():
    def __init__(self):
        self.db_config={
            'host': '172.28.38.59',
            'usr': 'mysqladmin',
            'passwd': '123465',
            'port': '3306',
            'db': 'hdb'
        }
    def tradePasswd(self):
        try:
            conn = MySQLdb.connect(host=self.db_config['host'],user=self.db_config['usr'],passwd=self.db_config['passwd'],db=self.db_config['db'])
            conn.autocommit(True)
            curr = conn.cursor()
            curr.execute("SET NAMES utf8")
            curr.execute("USE %s"% self.db_config['db'])
            # print u"******************** 操作数据库对象成功 ********************"
            # return conn,curr
            tradepasswd_sql = "UPDATE member set trade_pwd = NULL where uname = " + username + ";"
            curr.execute(tradepasswd_sql)
            # curr.fetchone()
            print u"恢复交易密码成功"
            curr.close()
            conn.close()
        except MySQLdb.Error,e:
            print "Mysql Error %d:%s"%(e.args[0],e.args[1])
        return  tradepasswd_sql
