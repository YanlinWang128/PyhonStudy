# @Time    : 2018/10/8 8:48
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : csv操作.py
import pandas as pd
import os

fileName = "test.csv"

inputFile = r"D:/" + fileName

# 表中有中文必须为 'gbk' 编码,默认的utf8处理中文转码有问题
df2 = pd.read_csv(inputFile, encoding='gbk', header=0)
Periods = df2.__len__()  # 返回的是索引,对应的是数据行数,总行数为 len +1
print(Periods)
print(df2.columns.size)

outfile = df2[(df2['UNIT2:JT66801A'] <= 368) & (df2['UNIT2:JT66801A'] >= 352)]
if (outfile.empty):  # 没有数据剩余
    os.remove(inputFile)
else:
    outfile.to_csv(inputFile, index=False, encoding='gbk')  # 筛选数据后导出到源文件

print(type(outfile))
print(outfile)
# print(df2['UNIT2:JT66801A'])
# df2[(df2['UNIT2:JT66801A'] >= 352)]
# print(df2)
"""
read_csv参数
    header=None:表名原数据没有列索引,这样read_csv为自动加上列索引(0-n)
    header=0，表示文件第0行（即第一行，python，索引从0开始）为列索引
    index_col=0;为指定数据中哪一列作为Dataframe的行索引，也可以可指定多列，形成层次索引，
        默认为None,即不指定行索引，这样系统会自动加上行索引（0-）

# 过滤dataframe行数据,删除掉数据
df[df['creativeID']<=10000]  # 保留的数据 &
    
df_w = pd.read_table(
r'C:\web_list_n.txt', encoding='ISO-8859-1', sep=',', header=None)


"""
