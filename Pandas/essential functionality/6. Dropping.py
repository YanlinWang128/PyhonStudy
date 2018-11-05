# @Time    : 2018/11/5 14:18
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 6. Dropping.py

from time import clock
import pandas as pd
import numpy as np

start = clock()

df = pd.DataFrame({'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
                   'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
                   'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})

# 删掉一行, axis= 0 删行
df.drop(['a', 'd'], axis=0)
# 删除一列, axis=1
df.drop(['one'], axis=1)

end = clock()
print('time: {:.8f}s'.format(end - start))