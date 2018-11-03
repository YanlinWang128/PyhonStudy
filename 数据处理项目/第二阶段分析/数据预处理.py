# @Time    : 2018/10/22 19:00
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 数据预处理.py


import os
import pandas as pd
import datetime as dt
import re
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter


def csv_data_filtering(input_file, output_path):
    """
    对数据进行筛选,不满足条件的属性,直接删除
    :param input_file: 输入文件
    :param output_path: 输出文件路径
    :return: no
    """
    # 最原始的数据打开有中文,按照gbk打开
    df2 = pd.read_csv(input_file, encoding='gbk', header=0)
    # 删除属性列
    df2 = del_attribution_columns(df2)

    # 根据功率筛选, 只需要 满功率300以上的
    df2 = df2[(df2['JT66801A'] >= 300)]

    # 检测空白值并填充,向上填充数据
    df2.fillna(method='ffill', inplace=True)
    while (blank_detect(df2)):
        df2.fillna(method='ffill', inplace=True)

    # 低过入口温度的均值
    df2['u2'] = ((df2['HAG10T01'] + df2['HAG10T02'] + df2['HAG10T03'] + df2['HAG10T04'] + df2['HAG10T05'] + df2[
        'HAG10T06'] + df2['HAG10T13'] + df2['HAG10T14'] + df2['HAG10T15'] + df2['HAG10T16'] + df2['HAG10T17'] + df2[
                      'HAG10T18']) / 12)
    # 炉膛AB侧烟温
    df2['u3'] = (df2['HBKCT101'] + df2['HBKCT201']) / 2
    # 给水温度
    df2['LYTFW'] = (df2['LABCT301'] + df2['LABCT302']) / 2

    outfile = df2
    if (outfile.empty):  # 没有数据剩余
        print("Already processed, no eligible data ")
    else:
        outfile.to_csv(output_path, index=False)  # 筛选数据后导出到源文件
        print('Already processed, export  to {}'.format(output_path))


def del_attribution_columns(df2):
    """
    删除项目中 无列名的属性列: 先重新命名,然后删除
    :param df2: 输入的  pandas dataframe
    :return: 处理过后的 dataframe
    """
    # cols  重命名的列
    cols = ['date', 'LAECF411', 'Unname2', 'HBKCT101', 'Unname4', 'HBKCT201', 'Unname6', 'T12A041A', 'Unname8',
            'JT66801A',
            'Unname10', 'THRPRESS', 'Unname12', 'HHL517CG', 'Unname14', 'HHL527CG', 'Unname16', 'HHL617CG', 'Unname18',
            'HHL627CG', 'Unname20', 'LABCT301', 'Unname22', 'LABCT302', 'Unname24', 'HAG10T01', 'Unname26', 'HAG10T02',
            'Unname28', 'HAG10T03', 'Unname30', 'HAG10T04', 'Unname32', 'HAG10T05', 'Unname34', 'HAG10T06', 'Unname36',
            'HAG10T16', 'Unname38', 'HAG10T17', 'Unname40', 'HAG10T18', 'Unname42', 'HAG10T13', 'Unname44', 'HAG10T14',
            'Unname46', 'HAG10T15', 'Unname48', 'AIRFLOW', 'Unname50', 'TOTFUELF', 'Unname52', 'MSTMFLOW', 'Unname54',
            'T10A042A', 'Unname56', 'TOTFWFLW', 'Unname58', 'FWFLOWD', 'Unname60', 'Unname61']

    # 暴力规范列名
    df2.columns = cols

    # 删除不需要的列名
    cols_del = ['Unname2', 'Unname4', 'Unname6', 'Unname8', 'Unname10', 'Unname12', 'Unname14', 'Unname16', 'Unname18',
                'Unname20', 'Unname22', 'Unname24', 'Unname26', 'Unname28', 'Unname30', 'Unname32', 'Unname34',
                'Unname36',
                'Unname38', 'Unname40', 'Unname42', 'Unname44', 'Unname46', 'Unname48', 'Unname50', 'Unname52',
                'Unname54',
                'Unname56', 'Unname58', 'Unname60', 'Unname61']

    df2.drop(cols_del, inplace=True, axis=1)
    return df2


def csv_merge(path, save_file_name):
    """
    合并目录下所有同类型CSV文件
    :param path: 目标路径
    :param save_file_name: 合并完成后, 保存的文件名
    :return: 
    """
    # 将该文件夹下的所有文件名存入一个列表

    file_list = sorted(os.listdir(path), key=lambda i: int((re.findall('p(\d+).csv', i)[0])))
    # 读取第一个CSV文件并包含表头  
    df = pd.read_csv(os.path.join(path, file_list[0]))  # 带中文的话, 编码格式改成gbk
    # 将读取的第一个CSV文件写入合并后的文件保存  
    df.to_csv(os.path.join(path, save_file_name), index=False)

    # 循环遍历列表中各个CSV文件名，并追加到合并后的文件  
    for i in range(1, len(file_list)):
        df = pd.read_csv(os.path.join(path, file_list[i]))
        df.to_csv(os.path.join(path, save_file_name), index=False, header=False, mode='a+')
    print("all csv merged")


def blank_detect(df2):
    """
    检测是否有空白值,并统计空白值
    :param df2: 传入参数为 pandas dataframe 格式
    :return blank_numbers:  返回空白值的数目 (int类型)
    """
    blank_numbers = int(df2.isnull().any().sum())
    print("No blank" if (blank_numbers == 0) else "All is {} blank".format(blank_numbers))
    return blank_numbers


def add_difference(df2):
    # 最后一位没有下一位,不包括
    print(df2.index, len(df2.index))
    # 计算差值
    df2['u1_difference'] = (df2["LAECF411"] - (df2["LAECF411"].shift(1))).shift(-1)
    df2['u2_difference'] = (df2["u2"] - (df2["u2"].shift(1))).shift(-1)
    df2['u3_difference'] = (df2["u3"] - (df2["u3"].shift(1))).shift(-1)
    df2['u4_difference'] = (df2["TOTFUELF"] - (df2["TOTFUELF"].shift(1))).shift(-1)

    return df2


def plot_difference_value(y, title, line=0):
    # x = np.linspace(-2*np.pi, 2*np.pi, 1000) 产生n个刻度对应,len(y)

    ax = plt.subplot(111)
    # plt.plot(x, y, color='blue', linewidth=2)
    plt.plot(y, color='blue', linewidth=2)
    if line != 0:
        plt.plot([0, len(y)], [line, line], 'r--', lw=2.5)
        plt.text(0, line + 2, r'$y\ =\ {}$'.format(line), fontdict={'size': 12, 'color': 'r'})
        plt.plot([0, len(y)], [-line, -line], 'r--', lw=2.5)
        plt.text(0, -line - 8, r'$y\ =\ {}$'.format(-line), fontdict={'size': 12, 'color': 'r'})
    # 刻度格式
    # ax.xaxis.set_major_locator(MultipleLocator(8))
    # ax.yaxis.set_major_locator(MultipleLocator(10))

    # 坐标值显示
    # ax.xaxis.set_major_formatter(FormatStrFormatter('%1.0f'))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%1.4f'))
    plt.title(title)
    plt.show()


def column_analysis(y, analysis_list):
    """
    对某列数据进行分析
    :param y: 列数据(一个列表)
    :param analysis_list: 需要分析的y值列
    :return: 
    """
    all_count = len(y)
    print('总条数:', all_count)
    print('max: ', max(y), 'min: ', min(y))
    # step = [7, 8, 9, 10, 11, 12, 13, 14, 15]
    # step = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(analysis_list)):
        count = len([x for x in y if (x >= -analysis_list[i] and x <= analysis_list[i])])
        print('正负{}范围条数: '.format(analysis_list[i]), count, '(异常条数: {})'.format(all_count - count),
              '占{:.5f}%'.format((count / all_count) * 100))


def data_preprocession():
    """
    第一步处理,对导出的原始数据进行预处理,包括:筛选功率300以上的,文件合并
    :return: 
    """
    dir_path = r'F:/HistoryData/08new/'
    output_path = dir_path[:-1] + 'process_mw300/'
    save_file_name = r'all08.csv'  # 合并后要保存的文件名

    if (not os.path.exists(output_path)):
        os.mkdir(output_path)

    # 对目录下的所有文件进行筛选操作, 筛选完放入目标文件夹
    for parent, dir_names, file_names in os.walk(dir_path):
        for filename in file_names:
            csv_data_filtering(os.path.join(parent, filename), os.path.join(output_path, filename))

    # 对目标文件夹内的所有数据进行合并
    csv_merge(output_path, save_file_name)

    """
    input_file = r'F:/HistoryData/09newprocess_300_370/all09.csv'
    df2 = pd.read_csv(input_file, header=0)
    df2 = deviation_filtering(df2, 0.35)
    output = r'F:/HistoryData/09newprocess_300_370/all09_300_370.csv'
    df2.to_csv(output, index=False)
    """


# 对文件夹内的所有段(或整文件), 计算difference差值
def process_add_difference(path):
    """
    对文件夹内的所有段(或整文件), 计算difference差值
    :param path: 需要添加文件所在的文件夹
    :return: 
    """
    # 遍历文件夹下的所有文件
    for info in os.listdir(path):
        # 将路径与文件名结合起来就是每个文件的完整路径
        path_file = os.path.join(os.path.abspath(path), info)
        df2 = pd.read_csv(path_file, header=0)
        print(df2.columns.values.tolist())

        # 调用对每个 dataframe 添加difference的函数
        # df2 = add_difference(df2)
        df2['y_difference'] = (df2["T12A041A"] - (df2["T12A041A"].shift(1))).shift(-1)
        output_file = path_file
        df2.to_csv(output_file, index=False)

        # path = r'C:/Users/Frank/Desktop/08time_series/'

        # output_file = r'F:/HistoryData/08newprocess_mw300/all08_caculated.csv'
        # input_file = r'F:/HistoryData/08newprocess_mw300/all08.csv'


# 绘图分析列
def plot_column():
    """
    绘图分析  u1_difference, u4_difference
    :return: 
    """
    input_file = r'F:/HistoryData/08newprocess_mw300/all08_caculated.csv'
    df2 = pd.read_csv(input_file, header=0)
    print(len(df2.index))
    y = df2['u1_difference'].tolist()[:-1]
    for items in y:
        if items > 30:
            print()
    # x = np.linspace(1, len(y), len(y))
    analysis_list = [0.5, 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 30, 40]
    column_analysis(y, analysis_list)
    plot_difference_value(y, 'u1_difference')


# 找到表格中异常值(比如大于30的值)得位置
def value_index_find():
    """
    找到表格中异常值(比如大于30的值)得位置
    :return: 
    """
    input_file = r'F:/HistoryData/08newprocess_mw300/all08_caculated.csv'
    df2 = pd.read_csv(input_file, header=0)
    print(len(df2.index))
    y = df2['u1_difference'].tolist()[:-1]
    for i in range(len(y)):
        if y[i] > 10:
            # 除去表头和索引0开始,i+2
            print('表格第{}行'.format(i + 2), y[i])


def main():
    print('hello, my darling!')
    input_file = r'F:/HistoryData/08newprocess_mw300/all08_caculated.csv'
    df2 = pd.read_csv(input_file, header=0)
    print(len(df2.index))
    u4 = df2['u4_difference'].tolist()
    u1 = df2['u1_difference'].tolist()

    # x = np.linspace(1, len(y), len(y))
    analysis_list_u4 = [x / 20 for x in range(1,41)]
    analysis_list_u1 = [x / 10 for x in range(1,81)]

    column_analysis(u1, analysis_list_u1)
    # column_analysis(u4, analysis_list_u4)

    print('---' * 30)



    # plot_difference_value(y, 'u4_difference')


def time_break_difference_to_0():
    input_file = r'F:/HistoryData/08newprocess_mw300/all08_caculated.csv'
    df2 = pd.read_csv(input_file, header=0)
    print(len(df2.index))
    for i in range(1, len(df2.index) - 1):
        if pd.Timestamp(df2.date[i]) - pd.Timestamp(df2.date[i - 1]) != dt.timedelta(seconds=1):
            df2.loc[i - 1, 'u4_difference'] = 0
    df2.to_csv(input_file, index=False)


def shift():
    # 添加新的 差值列
    input_file = r'C:/Users/Frank/Desktop/tongliu/mat_data_1102.csv'

    df2 = pd.read_csv(input_file, header=0)
    # 原始数据, y,u
    df2['y_difference'] = (df2["y"] - (df2["y"].shift(1))).shift(-1)
    df2['u_difference'] = (df2["u"] - (df2["u"].shift(1))).shift(-1)
    #  _u1234_y
    # df2['y_difference'] = (df2["y"] - (df2["y"].shift(1))).shift(-1)
    # df2['u1_difference'] = (df2["u1"] - (df2["u1"].shift(1))).shift(-1)
    # df2['u2_difference'] = (df2["u2"] - (df2["u2"].shift(1))).shift(-1)
    # df2['u3_difference'] = (df2["u3"] - (df2["u3"].shift(1))).shift(-1)
    # df2['u4_difference'] = (df2["u4"] - (df2["u4"].shift(1))).shift(-1)
    df2.to_csv(input_file, index=False)


if __name__ == "__main__":
    # pass
    # pass
    # value_index_find()
    # plot_column()

    # u4_difference 置0,绘图
    # time_break_difference_to_0()
    main()


    # caculated()

"""
u1: 0.5
一个采样周期输入的变化量大于0.1
u4: 0.1
"""
