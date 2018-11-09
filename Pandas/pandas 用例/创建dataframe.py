# @Time    : 2018/11/5 22:12
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 创建dataframe.py

from time import clock
import pandas as pd
import numpy as np

start = clock()

# 用例1, 自定义序列 + 字典
s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([pd.Timedelta(days=i) for i in range(3)])
df = pd.DataFrame(dict(A=s, B=td))
df['C'] = df['A'] + df['B']

# 用例2. 自定义列表 + 字典
original_df = pd.DataFrame({"foo": range(5), "bar": range(5, 10)})
df = pd.DataFrame({'data1': [3 * x ** 3 + 6 for x in range(-1000, 1000)], 'data2': np.random.randn(2000)})

# 创建一个空的dataframe
df3 = pd.DataFrame(columns=['a'])
df3.drop(['a'], inplace=True)
print(df3)
end = clock()
print('time: {:.8f}s'.format(end - start))
