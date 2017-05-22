'''
time.time -- shortdesc

time.time is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2017 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import calendar
from lib2to3.fixer_util import String
import os
import sys
import time
from turtledemo.clock import tick


os.environ
print(os.environ)
print(os.abc)
#打印当前时间�?
ticks=time.time();
print("当前时间戳：",ticks)
#获取当前时间
localtime=time.localtime(time.time())
print("当前时间是：",localtime)
#格式化当前时�?
print(time.asctime(time.localtime(ticks)))
print(time.asctime())
# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())) 
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
print(time.strftime("%Y/%m/%d %H:%M %S",time.localtime()))

#python 的日历类
cal = calendar.month(2017, 8)
print("以下输出2017�?8月份的日�?:")
print(cal)