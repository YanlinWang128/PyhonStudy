# @Time    : 2018/11/5 13:20
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 3. Flexible binary operations .py

from time import clock
import pandas as pd
import numpy as np

start = clock()

df = pd.DataFrame({'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
                   'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
                   'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})
# dataframe 复制
dfmi = df.copy()

# 逻辑判断
"""
(df > 0).all()
(df > 0).any() # 按column 返回
(df > 0).any().any() # 返回最终值

(df+df == df * 2).all()

df.empty

"""
end = clock()
print('time: {:.8f}s'.format(end - start))
