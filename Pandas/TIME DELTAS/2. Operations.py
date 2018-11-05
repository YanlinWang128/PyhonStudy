# @Time    : 2018/11/5 22:08
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 2. Operations.py

from time import clock
import pandas as pd
import numpy as np
from datetime import datetime

start = clock()
# 时间序列
s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))

td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])

df = pd.DataFrame(dict(A = s, B = td))

# 时间序列
series1 =  s - datetime(2011, 1, 1, 3, 5)

print(df)
end = clock()
print('time: {:.8f}s'.format(end - start))