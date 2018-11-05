# @Time    : 2018/11/5 22:02
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 1. Parsing.py

from time import clock
import pandas as pd
import numpy as np

start = clock()
print(pd.Timedelta('1 days'))  # 1 days 00:00:00  Timedelta('1 days 00:00:00')
"""
pd.Timedelta(days=1, seconds=1)
pd.Timedelta('1 days 2 hours')

pd.Timedelta(np.timedelta64(1, 'ms'))


"""
end = clock()
print('time: {:.8f}s'.format(end - start))