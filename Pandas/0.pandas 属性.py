# @Time    : 2018/11/1 22:38
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 0.pandas 属性.py

from time import clock
import pandas as pd

start = clock()

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