# @Time    : 2018/10/10 15:30
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 燃烧器摆角筛选.py

import pandas as pd
import datetime as dt

input_file = r'F:/HistoryData/08newdeviation/08new_after_deviation1200.csv'
output_file = r'F:/HistoryData/08newburnerangle/08new_after_burnerangle.csv'
df2 = pd.read_csv(input_file, header=0)

# 选取满足条件的时间序列, 功率+-8
# 划分对应的时间工况段

# 燃烧器摆角参数筛选
df2.drop(['deviation'], inplace=True, axis=1)

df2 = df2[(df2['HHL517CG'] < 10) & (df2['HHL517CG'] > -10)].reset_index(drop=True)
# 重新设置索引

print(df2)
# print(df2.count())
print(type(df2))

date = df2['date']
print(df2.columns.values.tolist())

begin = [date[0]]
end = []
print('合并前', len(date))  # 时间项,不包括标题
for i in range(0, len(date) - 1):
    if pd.Timestamp(date[i + 1]) - pd.Timestamp(date[i]) != dt.timedelta(seconds=1):
        begin.append(date[i + 1])
        end.append(date[i])
end.append(date[len(date) - 1])
print(len(begin), len(end))

# 划分完毕的时间对列表
segment_sequence = list(zip(begin, end))
print(segment_sequence)


# 找到每段开始索引和结束索引
count = 0  # 记录不满足的个数
for seg in segment_sequence:
    # begin_time = seg[0]
    begin_index = df2[df2['date'] == seg[0]].index.tolist()[0]
    #print(begin_index)
    # end_time = seg[1]
    end_index = df2[df2['date'] == seg[1]].index.tolist()[0]

    periods = end_index - begin_index + 1
    #print(periods)
    if periods >= 1200:
        for i in range(begin_index, end_index + 1):
            df2.loc[i, 'deviation'] = 1
        count += 1

df2 = df2[df2['deviation'] == 1]
df2.drop(['deviation'], inplace=True, axis=1)
print(df2)
print(count)
df2.to_csv(output_file, index=False)