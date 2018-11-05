# @Time    : 2018/11/5 22:12
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 创建dataframe.py

from time import clock
import pandas as pd
import numpy as np

start = clock()

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([pd.Timedelta(days=i) for i in range(3)])
df = pd.DataFrame(dict(A=s, B=td))
df['C'] = df['A'] + df['B']

end = clock()
print('time: {:.8f}s'.format(end - start))
