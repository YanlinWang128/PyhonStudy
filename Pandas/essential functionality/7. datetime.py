# @Time    : 2018/11/5 14:37
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 7. datetime.py

from time import clock
import pandas as pd
import numpy as np

start = clock()

s = pd.Series(pd.period_range('20130101', periods=4, freq='D'))


s1 = s.dt.strftime('%Y/%m/%d')


s3 = pd.Series(pd.timedelta_range('1 day 00:00:05', periods=4, freq='s'))
# s.dt.days, s.dt.seconds,  s.dt.components


end = clock()
print('time: {:.8f}s'.format(end - start))