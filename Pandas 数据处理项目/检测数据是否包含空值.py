# @Time    : 2018/10/10 19:12
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 检测数据是否包含空值.py
import os
import pandas as pd


def blank_detect(df2):
    """
    检测是否有空白值,并统计空白值
    :param df2: 传入参数为 pandas dataframe 格式
    :return blank_numbers:  返回空白值的数目 (int类型)
    """
    blank_numbers = int(df2.isnull().any().sum())
    print("No blank" if (blank_numbers == 0) else "All is {} blank".format(blank_numbers))
    return blank_numbers


if __name__ == "__main__":
    input_file = r'F:/HistoryData/08newburnerangle/08new_after_burnerangle.csv'
    df2 = pd.read_csv(input_file, header=0)
    #print(df2[df2.isnull().values == True])
    blank_detect(df2)
