# @Time    : 2018/11/5 15:12
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 11. Selection By Callable.py

from time import clock
import pandas as pd
import numpy as np

start = clock()

"""
• .loc if you want to label index.
• .iloc if you want to positionally index.

"""
df1 = pd.DataFrame(np.random.randn(6, 4),
                   index=list('abcdef'),
                   columns=list('ABCD'))
df2 = df1.loc[lambda df: df.A > 0, :]  # 指定行, 任意列
df3 = df1.loc[:, lambda df: ['A', 'B']]  # 指定列, 任意行

end = clock()
print('time: {:.8f}s'.format(end - start))
