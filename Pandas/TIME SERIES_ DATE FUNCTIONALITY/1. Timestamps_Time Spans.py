# @Time    : 2018/11/5 16:38
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 1. Timestamps_Time Spans.py

from time import clock
import pandas as pd
import numpy as np
from datetime import datetime

start = clock()

# 新建时间戳
print(pd.Timestamp(datetime(2012, 5, 1)))  # Timestamp('2012-05-01 00:00:00')
print(pd.Timestamp('2012-05-01'))  # pd.Timestamp('2012-05-01')
print(pd.Timestamp(2012, 5, 1))  # Timestamp('2012-05-01 00:00:00')

# 新建一段时间 Period
period1 = pd.Period('2011-01') # Period('2011-01', 'M') 默认为 M月
period2 = pd.Period('2012-05', freq='D') # Period('2012-05-01', 'D')

dates = [pd.Timestamp('2012-05-01'), pd.Timestamp('2012-05-02'), pd.Timestamp('2012-05-03')]



end = clock()
print('time: {:.8f}s'.format(end - start))
