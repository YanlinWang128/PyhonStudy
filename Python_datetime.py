# @Time    : 2018/9/30 14:41
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : Python_datetime.py

from datetime import datetime, timedelta
from time import sleep, time

"""
    以不同格式显示时间和日期是程序中最常用到的功能
    datetime库可以从系统中获得时间,并以用户选择的格式输出
    datetime库以格林威治时间为基础,每天由3600 * 24 秒精确定义
    该库包含两个常量,表示datetime能表示的最小最大年份,1-9999
    datetime.MINYEAR, datetime.MAXYEAR
    
    多种日期表示方式
"""
# 根据日期计算星期后返回 1-7,对应星期一到星期日
print(datetime.now().isoweekday())

# 根据格式化字符串format进行格式化显示
print(datetime.now())
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


"""
一、自己定义时间格式：
    1、datetime(2017,2,22,16,5,26)；
    2、datetime.strptime('2017-02-22 16:05:26', '%Y-%m-%d %H:%M:%S')

二、将datetime转化成timestamp格式：
    datetime(2017,2,22,16,5,26).timestamp()

三、将timestamp转化成datetime格式：
    datetime.fromtimestamp(1487750726.0)

四、将datetime转化成str格式：
    datetime(2017,2,22,16,5,26).strftime('%Y-%m-%d %H:%M:%S')

五、利用timedelta进行时间相加：
    datetime.strptime('2017-02-22 16:05:26', '%Y-%m-%d %H:%M:%S') + timedelta(hours=10, days=2)

六、利用timedelta进行时间相减：
    datetime.strptime('2017-02-22 14:05:26', '%Y-%m-%d %H:%M:%S') - timedelta(hours=1)
    
    timedelta对象表示一个时间段，timedelta对象可以通过手动实例化得到
    也可以通过上述三个对象（datetime, date, time）相减得到。
    手动实例化timedelta时，可以传入的参数有：
    days, seconds, microseconds, milliseconds, minutes, hours, weeks
    

"""
# time
"""
python中time模块也经常用来表示时间,日期
但是因为该模块下的函数都是对同名C函数的直接调用，所以返回的对象都不太pythonic
所以我们一般不用，经常使用的就两个函数：
time.sleep(5)  # 程序睡眠5s

time.time() # 返回当前的时间戳 
>>> from datetime import datetime, timedleta
>>> now = datetime.now()
>>> last = datetime(year=2016, month=3, day=10， hour=8)
>>> delta = now - last
>>> delta
datetime.timedelta(282, 47010, 328000)

"""
sleep(5)  # 程序睡眠5s

print(time()) # 返回当前的时间戳 1538290809.2759438