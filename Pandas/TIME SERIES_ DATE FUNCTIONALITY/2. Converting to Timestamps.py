# @Time    : 2018/11/5 16:50
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 2. Converting to Timestamps.py

from time import clock
import pandas as pd
import numpy as np
from datetime import datetime

start = clock()

# 新建时间序列转换为 时间戳序列
series1 = pd.to_datetime(pd.Series(['Jul 31, 2009', '2010-01-10', None]))
print(series1)

# 对具体某一值转为时间戳
timestamp1 = pd.to_datetime('2010/11/12')
timestamp2 = pd.Timestamp('2010/11/12')  # 貌似简洁一些

timestamp3 = pd.to_datetime('2010/11/12', format='%Y/%m/%d')




end = clock()
print('time: {:.8f}s'.format(end - start))
