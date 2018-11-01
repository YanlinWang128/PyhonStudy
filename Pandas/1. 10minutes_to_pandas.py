# @Time    : 2018/11/1 22:43
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 1. 10minutes_to_pandas.py

from time import clock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s, s.dtype, type(s))


# 生成时间序列
dates = pd.date_range('20130101', periods=6)  # 起始日期, 天数, 默认间隔为天
# print(dates, list(dates)[0])  # 2013-01-01,  2013-01-01 00:00:00 默认横杆间隔

# 时间序列为索引,生成dataframe
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))  # index 参数为series
print(df)

# 查看数据
print(df.head()) # df.head() 查看前5条数据

# if-then
df.loc[df.AAA >= 5,'BBB'] = -1
df.loc[df.AAA >= 5,['BBB','CCC']] = 555
df['logic'] = np.where(df['AAA'] > 5,'high','low')
start = clock()

end = clock()
print('time: {:.8f}s'.format(end - start))
