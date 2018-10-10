# @Time    : 2018/10/10 19:30
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : Myfunction.py

import pandas as df



def blank_detect(df2):
    """
    检测是否有空白值,并统计空白值
    :param df2: 传入参数为 pandas dataframe 格式
    :return blank_numbers:  返回空白值的数目 (int类型)
    """
    blank_numbers = int(df2.isnull().any().sum())
    print("No blank" if (blank_numbers == 0) else "All is {} blank".format(blank_numbers))
    return blank_numbers