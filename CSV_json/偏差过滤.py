# @Time    : 2018/10/8 17:07
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 偏差过滤.py

import pandas as pd
import datetime as dt

input_file = r'D:/rawData201608.csv'
deviation = 0.35  # 偏差设定值
# 数据读取,dataframe格式
df2 = pd.read_csv(input_file, encoding='gbk', header=0)

# 选取满足条件的时间序列, 功率+-8
# 划分对应的时间工况段
date = df2['时间']
print(df2.columns.values.tolist())

if (len(date) > 0):
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
        begin_index = df2[df2['时间'] == seg[0]].index.tolist()[0]
        # end_time = seg[1]
        end_index = df2[df2['时间'] == seg[1]].index.tolist()[0]

        # 小于3个的段不处理,跳过 continue
        if end_index - begin_index < 3:
            continue
        print(seg[0], begin_index, seg[1], end_index)

        # 找到数据起始和结束的索引,选中 求均值
        sequence_mean = round(df2['UNIT2:THRPRESS'][begin_index:end_index + 1].mean(), 4)
        print(sequence_mean)

        # 标记偏差小于0.35的值,为deviation列值为0,符合要求,供下一步筛选用
        for i in range(begin_index, end_index + 1):
            if (abs(df2['UNIT2:THRPRESS'][i] - sequence_mean) > deviation):
                df2.loc[i, 'deviation'] = 1
                count += 1
                # else:
                #     df2['deviation'][i] = 0
    df2 = df2[df2['deviation'] != 1]
    print(count)
    df2.to_csv(input_file, index=False, encoding='gbk')  # 筛选数据后导出到源文件

    # a = data[data.time == '2016-09-01 00:38:00'].index.tolist()
    # 对划分的每一段求均值

    """
    # print("begin", len(begin))
    # print("end", len(end))
    print('合并后', len(begin))
    df2.index = df2['时间']
    beginremove = []
    endremove = []
    timerange = zip(begin, end)
    for i, v in timerange:
        if (i == v or pd.Timestamp(v) - pd.Timestamp(i) < dt.timedelta(seconds=30)):
            # print("remove", i, v)
            beginremove.append(i)
            endremove.append(v)
    begin = [i for i in begin if i not in beginremove]
    end = [i for i in end if i not in endremove]

    """
