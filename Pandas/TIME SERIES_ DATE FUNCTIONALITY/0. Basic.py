# @Time    : 2018/11/5 16:31
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 0. Basic.py

from time import clock
import pandas as pd
import numpy as np

start = clock()
rng = pd.date_range('1/1/2011', periods=72, freq='H')
print(rng[:5])

# Index pandas objects with dates:
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts.head())

# to 45 minute frequency and forward fill
converted = ts.asfreq('45Min', method='pad')
print(converted.head())


# Daily means 直接可以解析时间求得,每日的均值
day_mean = ts.resample('D').mean()



"""
与时间相关的概念
Timestamp  时间戳(to_datetime, Timestamp)
DatetimeIndex   Index of Timestamp  (to_datetime, date_range, bdate_range, DatetimeIndex)
Period   Represents a single time span (Period)
PeriodIndex  Index of Period (period_range, PeriodIndex)
"""
end = clock()
print('time: {:.8f}s'.format(end - start))
