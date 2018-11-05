# @Time    : 2018/11/5 15:08
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 10. Selection By Position.py

from time import clock
import pandas as pd
import numpy as np

start = clock()
s1 = pd.Series(np.random.randn(5), index=list(range(0, 10, 2)))
# 对于序列,   通过绝对位置筛选
s2 = s1.iloc[:3]
# 选择指定数据, 赋值, iloc切片
s1.iloc[:3] = 0

# 对于dataframe操作
df1 = pd.DataFrame(np.random.randn(6, 4),
                   index=list(range(0, 12, 2)),
                   columns=list(range(0, 8, 2)))
df2 = df1.iloc[:3] # 通过绝对位置选择指定行  df1.iloc[1:3, :]

df3 = df1.iloc[1:5, 2:4] # 选择指定行列

# 通过列表选择指定行列
df4 = df1.iloc[[1, 3, 5], [1, 3]]


end = clock()
print('time: {:.8f}s'.format(end - start))
