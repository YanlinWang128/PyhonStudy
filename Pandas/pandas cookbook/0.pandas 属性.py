# @Time    : 2018/11/1 22:38
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 0.pandas 属性.py

from time import clock
import pandas as pd

start = clock()
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df.head())  # df.head() 读取前五条数据

"""
Data Structures

Series 一维标记的均匀数组
DataFrame  二维尺寸可变的表格结构

关系:
for col in df.columns:
    series = df[col]
# do something with series

"""

end = clock()
print('time: {:.8f}s'.format(end - start))
