# @Time    : 2018/10/10 10:23
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 删除满足条件的列.py

import pandas as pd
import os
import re
import io

# 删除属性列
path = r'D:/test/a.csv'
output_path = r'D:/test/output.csv'

# cols  重命名的列
cols = ['date', 'LAECF411', 'Unname2', 'HBKCT101', 'Unname4', 'HBKCT201', 'Unname6', 'T12A041A', 'Unname8', 'JT66801A',
        'Unname10', 'THRPRESS', 'Unname12', 'HHL517CG', 'Unname14', 'HHL527CG', 'Unname16', 'HHL617CG', 'Unname18',
        'HHL627CG', 'Unname20', 'LABCT301', 'Unname22', 'LABCT302', 'Unname24', 'HAG10T01', 'Unname26', 'HAG10T02',
        'Unname28', 'HAG10T03', 'Unname30', 'HAG10T04', 'Unname32', 'HAG10T05', 'Unname34', 'HAG10T06', 'Unname36',
        'HAG10T16', 'Unname38', 'HAG10T17', 'Unname40', 'HAG10T18', 'Unname42', 'HAG10T13', 'Unname44', 'HAG10T14',
        'Unname46', 'HAG10T15', 'Unname48', 'AIRFLOW', 'Unname50', 'TOTFUELF', 'Unname52', 'MSTMFLOW', 'Unname54',
        'T10A042A', 'Unname56', 'TOTFWFLW', 'Unname58', 'FWFLOWD', 'Unname60', 'Unname61']

df2 = pd.read_csv(path, encoding='gbk', header=0)
print(df2.columns.values.tolist())

# 暴力规范列名
df2.columns = cols
print(df2.columns.values.tolist())

# 删除不需要的列名
cols_del = ['Unname2', 'Unname4', 'Unname6', 'Unname8', 'Unname10', 'Unname12', 'Unname14', 'Unname16', 'Unname18',
        'Unname20', 'Unname22', 'Unname24', 'Unname26', 'Unname28', 'Unname30', 'Unname32', 'Unname34', 'Unname36',
        'Unname38', 'Unname40', 'Unname42', 'Unname44', 'Unname46', 'Unname48', 'Unname50', 'Unname52', 'Unname54',
        'Unname56', 'Unname58', 'Unname60', 'Unname61']

df2.drop(cols_del, inplace=True, axis=1)
df2.to_csv(output_path, index=False, encoding='gbk')





# dataframe列名更改
# pf2 = pd.DataFrame(Df, columns = cols)
