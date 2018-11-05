# @Time    : 2018/11/5 13:16
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 2. Attributes and the raw ndarray(s).py

from time import clock
import pandas as pd
import numpy as np

start = clock()

index = pd.date_range('1/1/2000', periods=8)
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=['A', 'B', 'C'])

# 切片属性
df1 = df[:2]

# columns 属性 重命名列
df.columns = [x.lower() for x in df.columns]


# s.values 序列的值
# df.values dataframe的值



end = clock()
print('time: {:.8f}s'.format(end - start))