# @Time    : 2018/10/11 15:42
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 每段数据的方差分析.py

import pandas as pd
import datetime as dt

input_file = r'F:/HistoryData/08_35.csv'

# 数据读取,dataframe格式
df2 = pd.read_csv(input_file, header=0)
# df2.drop(['deviation'], inplace=True, axis=1)
# 选取满足条件的时间序列, 功率+-8
# 划分对应的时间工况段
date = df2['date']
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
    print('原始段数', len(begin), len(end))

    # 划分完毕的时间对列表
    segment_sequence = list(zip(begin, end))
    print(segment_sequence)

    # 创建一个空的dataframe,用来存储数据
    df_data = pd.DataFrame(columns=["段号", "start_time","end_time","条目数", "最大值", "最小值", "均值", "方差", "标准差"])

    # 找到每段开始索引和结束索引
    count = 0  # 记录不满足的个数
    time_all = 0

    for seg in segment_sequence:
        # begin_time = seg[0]
        begin_index = df2[df2['date'] == seg[0]].index.tolist()[0]
        # end_time = seg[1]
        end_index = df2[df2['date'] == seg[1]].index.tolist()[0]
        periods = end_index - begin_index + 1
        if periods >= 1200:
            count += 1
            time_all += periods
            for i in range(begin_index, end_index + 1):
                df2.loc[i, 'deviation'] = 1

            df_data.loc[count, '段号'] = count
            df_data.loc[count, '条目数'] = periods

            max_value = df2[df2['deviation'] == 1]['LYTFW'].max()
            min_value = df2[df2['deviation'] == 1]['LYTFW'].min()
            # most_value = df2[df2['deviation'] == 1]['LYTFW'].mode()

            df_data.loc[count, '最大值'] = max_value
            df_data.loc[count, '最小值'] = min_value
            # df_data.loc[count, '众数'] = most_value

            mean_value = df2[df2['deviation'] == 1]['LYTFW'].mean()
            var_value = df2[df2['deviation'] == 1]['LYTFW'].var()
            std_value = df2[df2['deviation'] == 1]['LYTFW'].std()

            df_data.loc[count, '均值'] = mean_value
            df_data.loc[count, '方差'] = var_value
            df_data.loc[count, '标准差'] = std_value

            df_data.loc[count, 'start_time'] = seg[0]
            df_data.loc[count, 'end_time'] = seg[1]

            # 核心: 每次处理一段记得 清除标记列
            df2.drop(['deviation'], inplace=True, axis=1)


            # print('第{}段,条目为:{}, 给水温度均值为:{}, 给水温度方差为: {}'.format(count, periods, mean_value, std_value))
    # print('总段数:{}, 总条目:{}, 总小时数{}'.format(count, time_all, time_all / 3600))
    df_data.to_csv(r'8月方差.csv', encoding='gbk', index=False)
