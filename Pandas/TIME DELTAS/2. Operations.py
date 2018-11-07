# @Time    : 2018/11/5 22:08
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 2. Operations.py

from time import clock
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

start = clock()
# 时间序列
s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))

td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])

df = pd.DataFrame(dict(A = s, B = td))

# 时间序列, 时间差得到时间序列
series1 =  s - datetime(2011, 1, 1, 3, 5)
series2 = s + timedelta(minutes=5)
y = s - s[0]
y = s - s.shift()
# 时间戳
series3 = datetime(2011, 1, 1, 3, 5) - s
series4 = timedelta(minutes=5) + s

# 时间戳序列
# pd.timedelta_range(start='1 days', end='2 days', freq='30T')
# pd.timedelta_range(start='1 days', periods=5, freq='2D5H')


# 时间序列
s = pd.Series(np.arange(100), index=pd.timedelta_range('1 days', periods=100, freq='h'))

print(df)
end = clock()
print('time: {:.8f}s'.format(end - start))