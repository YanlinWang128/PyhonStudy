# @Time    : 2018/11/5 10:53
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 12.Timedeltas 时间间隔.py

from time import clock
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

start = clock()

# 时间序列可以运算
s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))

s1 = s - s.max()
s2 = s.max() - s
s4 = s - datetime(2011, 1, 1, 3, 5, 12)  # 减去一个时间,得到差值
s5 = s + timedelta(minutes=5)
s6 = datetime(2011, 1, 1, 3, 5) - s
s7 = timedelta(minutes=5) + s

print(s4, s5, sep='\n------\n')

### 时间间隔函数的处理
deltas = pd.Series([timedelta(days=i) for i in range(3)])
df = pd.DataFrame(dict(A=s, B=deltas))
df['New Dates'] = df['A'] + df['B']
# 对应时间相加
df['Delta'] = df['A'] - df['New Dates']
print(df.dtypes)

end = clock()
print('time: {:.8f}s'.format(end - start))
