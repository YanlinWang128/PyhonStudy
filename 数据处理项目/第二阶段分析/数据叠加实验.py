# @Time    : 2018/10/25 14:46
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 数据叠加实验.py

import numpy as np
import pandas as pd
import time


def try1try():
    file_path = r'C:/Users/Frank/Desktop/try1025/all08_1025.csv'
    df2 = pd.read_csv(file_path, header=0)
    print(df2.columns.values.tolist())

    # 提取数据THRPRESS, TOTFUELF
    THRPRESS = df2['THRPRESS'].tolist()
    TOTFUELF = df2['TOTFUELF'].tolist()  # u
    print(len(THRPRESS), len(TOTFUELF))

    # y1 系数, 初始值为1
    a = 0.1

    # 延时,初值设置为 60
    d = 60

    # 开始时刻 63, 结束时刻,数据长度
    start_item = 63
    end_item = len(THRPRESS)

    y1 = [0] * (start_item - 1)  # 62

    # k时刻, start - end

    def y1_caculate(k):
        k1_next = 1.918 * y1[k - 1 - 1] - 0.92 * y1[k - 2 - 1] + 0.0003998 * TOTFUELF[k - d - 1] + 0.0007997 * TOTFUELF[
            k - d - 2] + 0.0003998 * TOTFUELF[k - d - 3]
        y1.append(k1_next)

    print(len(y1), y1)

    for k in range(start_item, end_item + 1):  # 传入为时刻
        # print(k)
        y1_caculate(k)

    # print(len(y1), y1)

    # np.sum([THRPRESS, np.array(y1)*a], axis=0)
    if len(y1) == len(THRPRESS):
        y = [a * y1[i] + THRPRESS[i] for i in range(0, len(y1))]  # 0:列
        df2['y'] = y
    else:
        print('y1列和 THRPRESS列数据个数不同')
    print(len(y), y[-100:])

    df2.to_csv(r'C:/Users/Frank/Desktop/try1025/y_a0_1_all08_1025.csv', index=False)


if __name__ == '__main__':
    start = time.clock()
    try1try()
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))
