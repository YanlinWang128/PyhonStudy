# @Time    : 2018/10/8 11:36
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : data_filtering.py
import os
import pandas as pd


def csv_data_filtering(input_file, output_path):
    """
    对数据进行筛选,不满足条件的文件直接删除
    :param input_file: 输入文件
    :param output_path: 输出文件路径
    :return: no
    """
    df2 = pd.read_csv(input_file, encoding='gbk', header=0)

    # 删除属性列
    cols = df2.columns.size
    df2.drop(df2.columns[2:cols:2], axis=1, inplace=True)  # True 直接替换

    # 根据功率筛选, 只需要 满功率330+_8
    # 删除不需要的行数据
    df2 = df2[(df2['UNIT2:JT66801A'] <= 338) & (df2['UNIT2:JT66801A'] >= 322)]

    # 低过入口温度的均值
    df2['u2'] = (df2['UNIT2:HAG10T01'] + df2['UNIT2:HAG10T02'] + df2['UNIT2:HAG10T03'] + df2['UNIT2:HAG10T04'] + df2[
        'UNIT2:HAG10T05'] + df2['UNIT2:HAG10T06'] + df2['UNIT2:HAG10T13'] + df2['UNIT2:HAG10T14'] + df2[
                     'UNIT2:HAG10T15'] + df2['UNIT2:HAG10T16'] + df2['UNIT2:HAG10T17'] + df2['UNIT2:HAG10T18']) / 12
    # 炉膛AB侧烟温
    df2['u3'] = (df2['UNIT2:HBKCT101'] + df2['UNIT2:HBKCT201']) / 2

    # 给水温度
    df2['LYTFW'] = (df2['UNIT2:LABCT301'] + df2['UNIT2:LABCT302']) / 2

    outfile = df2

    if (outfile.empty):  # 没有数据剩余
        print("Already processed, no eligible data ")
    else:
        outfile.to_csv(output_path, index=False, encoding='gbk')  # 筛选数据后导出到源文件
        print('Already processed, export  to {}'.format(output_path))


if __name__ == "__main__":
    dir_path = r'F:/HistoryData/08/'
    output_path = dir_path[:-1] + 'process/'
    if (not os.path.exists(output_path)):
        os.mkdir(output_path)
    for parent, dir_names, file_names in os.walk(dir_path):
        for filename in file_names:  # 对目录下的所有文件进行操作
            csv_data_filtering(os.path.join(parent, filename), os.path.join(output_path, filename))
