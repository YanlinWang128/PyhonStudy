# @Time    : 2018/10/10 14:56
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 统计某列各个值出现的频次.py

import pandas as pd
import os

input_file = r'F:/HistoryData/08newdeviation/08new_after_deviation.csv'

doc = open(r'F:/HistoryData/08newdeviation/frequency.txt', 'a+')
df2 = pd.read_csv(input_file, header=0)

print(df2['HHL517CG'].count(), file=doc)
print('---' * 20, file=doc)
print(df2['HHL517CG'].describe(), file=doc)
print('---' * 20, file=doc)
print(df2['HHL517CG'].value_counts(), file=doc)
doc.close()
