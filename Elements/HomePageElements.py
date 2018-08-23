# -*- coding: utf-8 -*-
import MySQLdb
import datetime
db = MySQLdb.connect("172.28.38.88","mysqladmin","123465","hdb",charset='utf8')
cursor = db.cursor()
#查询日息宝计划的利率最小值和最大值
sql_day_min = "SELECT min(rate_min) FROM plan_info where plan_type_id=22 AND del_flag=0"
cursor.execute(sql_day_min)
financial_day_minRate = cursor.fetchone()
sql_day_max = "SELECT max(rate_max) FROM plan_info where plan_type_id=22 AND del_flag=0"
cursor.execute(sql_day_max)
financial_day_maxRate = cursor.fetchone()

#查询月息宝计划的利率最小值和最大值
sql_month_min = "SELECT min(rate_min) FROM plan_info where plan_type_id=21 AND del_flag=0"
cursor.execute(sql_month_min)
financial_month_minRate = cursor.fetchone()
sql_month_max = "SELECT max(rate_max) FROM plan_info where plan_type_id=21 AND del_flag=0"
cursor.execute(sql_month_max)
financial_month_maxRate = cursor.fetchone()

#查询散标的利率最小值和最大值
sql_bid_min = "SELECT min(real_finance_rate) FROM audit_bid_info WHERE global_status=16 or global_status=18 or global_status=19 or global_status= 20 or global_status= 23 \
                                                                      or global_status=24 or global_status=29 or global_status=35 or global_status=36 or global_status=40"
cursor.execute(sql_bid_min)
financial_bid_minRate = cursor.fetchone()
sql_bid_max = "SELECT max(real_finance_rate) FROM audit_bid_info WHERE global_status=16 or global_status=18 or global_status=19 or global_status= 20 or global_status= 23 \
                                                                      or global_status=24 or global_status=29 or global_status=35 or global_status=36 or global_status=40"
cursor.execute(sql_bid_max)
financial_bid_maxRate = cursor.fetchone()

#计算活期日息宝的7日预期年化值：从“昨天”（含）开始往前数7天，取平均值
#1）获取昨天的日期
yesterday = (datetime.date.today() + datetime.timedelta(days=-1))
#2）获取8天前的日期
eight_days_earlier = (datetime.date.today() + datetime.timedelta(days=-8))
#3）计算7日预期年化
sql_current_rate = "SELECT AVG(seven_day_rate)*365 FROM rxb_rate WHERE date <= yesterday AND date >= eight_days_earlier"
cursor.execute(sql_current_rate)
current_rate = cursor.fetchone()
#首页-非强制升级弹窗
#1)×
cancel = "cancelImg"
#2)版本号
version = "versionCodeTex"
#3)【立即升级】按钮
upgrade = "loadingProgressView"

#首页-推荐项目
recommend_title = "tv_optimization_title"
recommend_rate = "tv_optimization_rate"
recommend_status = "tv_optimization_status"
recommend_deadline = "tv_optimization_dealine"
recommend_repayType = "tv_optimization_repaytype"
recommend_minbid = "tv_optimization_minbid"

#首页-“全部理财”banner
banner_left = "iv_left_banner"
banner_right = "iv_right_banner"

#首页-5个理财入口：因为这5个入口的id相同，因此使用【text】作为唯一标识
#1）日息宝计划
financial_day_title = "日息宝计划"
financial_day_rate = round(financial_day_minRate,2)+"%~"+round(financial_day_maxRate,2)+"%"
#2）月息宝计划
financial_month_title = "月息宝计划"
financial_month_rate = round(financial_month_minRate,2)+"%~"+round(financial_month_maxRate,2)+"%"
#3）活期日息宝
financial_current_title = "活期日息宝"
financial_current_rate = "7日预期年化"+current_rate+"%"
#4）散标
financial_bid_title = "散标"
financial_bid_rate = round(financial_bid_minRate,2)+"%~"+round(financial_bid_maxRate,2)+"%"
#5）基金：暂时不知道收益率从哪里取值，先在这里写死
financial_fund_title = "基金"
financial_fund_rate = "7日年化收益率1.5680%"