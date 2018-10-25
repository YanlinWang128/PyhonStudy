# @Time    : 2018/10/25 17:03
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 数据筛选.py

import pandas as pd

input_file = r'C:/Users/Frank/Desktop/try1025/1.csv'
output_file = r'C:/Users/Frank/Desktop/try1025/1_caculate.csv'
df2 = pd.read_csv(input_file, header=0)

# 新建一个dataframe(可指定列名) 空数据
dfnew = pd.DataFrame(columns=['a', 'b', 'c'])

# 筛选出a列大于0的行
# df2 = df2[df2.a > 0]
# 多条件筛选
# df2 = [(df2.a>0)&(df2.b<10)]


# 返回筛选后的数据的 a,b两列
dfnew1 = df2[(df2.TOTFUELF > 0) & (df2.THRPRESS < 1)][['TOTFUELF', 'THRPRESS']]
dfnew1.to_csv(output_file, index=False)
