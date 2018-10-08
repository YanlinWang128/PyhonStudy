# @Time    : 2018/10/8 11:09
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : csv_data_filtering.py
import pandas as pd
import os


def csv_data_filtering(input_file):
    """
    对数据进行筛选,不满足条件的文件直接删除
    :param input_file: 
    :return: 
    """
    df2 = pd.read_csv(input_file, encoding='gbk', header=0)

    # 删除属性列
    cols = df2.columns.size
    df2 = df2.drop(df2.columns[2:cols:2], axis=1)

    #
    outfile = df2[(df2['UNIT2:JT66801A'] <= 368) & (df2['UNIT2:JT66801A'] >= 352)]


    if (not outfile.empty):  # 没有数据剩余
        outfile.to_csv(input_file, index=False, encoding='gbk')  # 筛选数据后导出到源文件
        print('Already processed, export  to {}'.format(input_file))
    else:
        print("{} is empty".format(input_file))


if __name__ == "__main__":
    input_file = "D:/test.csv"
    csv_data_filtering(input_file)
    # fileName = "rawData2018.07.01.csv"  # 文件名,不是路径名
    # csv_data_filtering(fileName)
