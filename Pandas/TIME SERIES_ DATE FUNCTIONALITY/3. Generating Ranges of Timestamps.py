# @Time    : 2018/11/5 20:22
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 3. Generating Ranges of Timestamps.py

from time import clock
import pandas as pd
import numpy as np
from datetime import datetime
from pandas.tseries.offsets import *

start = clock()

d = datetime(2008, 8, 18, 9, 0)
d1 = d + DateOffset(months=4, days=5)
# 根据开始时刻, 时间间隔, 条数创建 时间序列
series1 = pd.date_range(start, periods=10, freq='2h20min')
rng = pd.date_range('1/1/2012', periods=100, freq='S')
# 时间序列
series2 = pd.Period('2012-1-1 19:00', freq='5H')

# 时间运算, 每个加上一秒
rng = pd.date_range('2014-1-1', periods=100, freq='D') + pd.Timedelta('1s')
p = pd.Period('2014-07-01 09:00', freq='H')
"""
p + Hour(2)
p + timedelta(minutes=120)
p + Minute(5)

"""

prng = pd.period_range('1/1/2011', '1/1/2012', freq='s')
idx = pd.period_range('2014-07-01 09:00', periods=5, freq='H')
span = pd.period_range('1215-01-01', '1381-01-01', freq='D')

# 时间索引 转化为序列
s_naive = pd.Series(pd.date_range('20130101',periods=3))

print(s_naive)
# print(rng)
# ts.shift(1)


"""
pd.date_range('20130101',periods=100000,freq='T'))


rng2 = pd.date_range('2011-01-01', '2012-01-01', freq='W')
ts2 = pd.Series(np.random.randn(len(rng2)), index=rng2)


"""
end = clock()
print('time: {:.8f}s'.format(end - start))