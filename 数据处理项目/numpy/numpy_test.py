# @Time    : 2018/10/14 21:48
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : numpy_test.py


import os
import pandas as pd
import numpy as np

# 最原始的数据打开有中文,按照gbk打开
input_file = 'C:/Users/Frank/Desktop/08_35.csv'
df2 = pd.read_csv(input_file, encoding='gbk', header=0)
print(df2.columns.values.tolist())
print(df2['date'].tolist()[0])
