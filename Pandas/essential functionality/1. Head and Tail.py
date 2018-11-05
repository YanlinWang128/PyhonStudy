# @Time    : 2018/11/5 13:05
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 1. Head and Tail.py

from time import clock
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

start = clock()

index = pd.date_range('1/1/2000', periods=8)
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=['A', 'B', 'C'])

# 展示前五条, 后五条数据
print(df.head(), df.tail(), sep='\n------\n')

end = clock()
print('time: {:.8f}s'.format(end - start))
