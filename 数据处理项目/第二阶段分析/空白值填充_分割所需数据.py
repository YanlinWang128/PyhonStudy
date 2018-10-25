# @Time    : 2018/10/25 14:03
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 空白值填充_分割所需数据.py
import pandas as pd
import numpy as py
import os


def blank_detect(df2):
    """
    检测是否有空白值,并统计空白值
    :param df2: 传入参数为 pandas dataframe 格式
    :return blank_numbers:  返回空白值的数目 (int类型)
    """
    blank_numbers = int(df2.isnull().any().sum())
    print("No blank" if (blank_numbers == 0) else "All is {} blank".format(blank_numbers))
    return blank_numbers


if __name__ == '__main__':
    input_path = r'F:/HistoryData/08new'
    for info in os.listdir(input_path):
        domain = os.path.abspath(input_path)  # 获取文件夹的路径
        path_file = os.path.join(domain, info)  # 将路径与文件名结合起来就是每个文件的完整路径

        df2 = pd.read_csv(path_file, header=0, encoding='gbk')
        df2.fillna(method='bfill', inplace=True)
        df2.fillna(method='ffill', inplace=True)
        df2.fillna(method='bfill', inplace=True)


        # while (blank_detect(df2)):
        #     df2.fillna(method='ffill', inplace=True)

        blank_detect(df2)


        dfnew = pd.DataFrame()
        dfnew['date'] = df2['时间']
        dfnew['TOTFUELF'] = df2['UNIT2:TOTFUELF']
        dfnew['THRPRESS'] = df2['UNIT2:THRPRESS']
        dfnew['JT66801A'] = df2['UNIT2:JT66801A']


        output_path = r'F:/HistoryData/08data1025/'
        output_path_file = os.path.join(output_path, info)
        dfnew.to_csv(output_path_file, index=False)

        # print(df2.columns.values.tolist())
"""

        dfnew = pd.DataFrame(df2.pop('TOTFUELF'), columns=['TOTFUELF'])

        dfnew['THRPRESS'] = df2.pop('THRPRESS')
        dfnew['date'] = df2.pop('时间')
"""