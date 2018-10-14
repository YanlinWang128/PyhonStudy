# @Time    : 2018/10/8 11:36
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : data_filtering 按功率.py
import os
import pandas as pd
import datetime as dt
import re


# 筛选功率 满负荷330正负8
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

    # 根据功率筛选, 只需要 满功率330+_8
    df2 = df2[(df2['JT66801A'] <= 338) & (df2['JT66801A'] >= 322)]

    # 检测空白值并填充,向上填充数据
    df2.fillna(method='ffill', inplace=True)
    while (blank_detect(df2)):
        df2.fillna(method='ffill', inplace=True)

    # 低过入口温度的均值
    df2['u2'] = ((df2['HAG10T01'] + df2['HAG10T02'] + df2['HAG10T03'] + df2['HAG10T04'] + df2['HAG10T05'] + df2[
        'HAG10T06'] + df2['HAG10T13'] + df2['HAG10T14'] + df2['HAG10T15'] + df2['HAG10T16'] + df2['HAG10T17'] + df2[
                      'HAG10T18']) / 12)
    # 炉膛AB侧烟温, 给水温度
    df2['u3'] = (df2['HBKCT101'] + df2['HBKCT201']) / 2
    df2['LYTFW'] = (df2['LABCT301'] + df2['LABCT302']) / 2

    outfile = df2
    if (outfile.empty):  # 没有数据剩余
        print("Already processed, no eligible data ")
    else:
        outfile.to_csv(output_path, index=False)  # 筛选数据后导出到源文件
        print('Already processed, export  to {}'.format(output_path))


def deviation_filtering(df2, deviation):
    """
    筛选出与均值偏差 不超过 deviation的数据 
    :param df2:  输入的 pandas dataframe
    :param deviation: 偏差值
    :return: 处理完毕的dataframe
    """

    # 燃烧器摆角筛选
    df2 = df2[(df2['HHL517CG'] < 10) & (df2['HHL517CG'] > -10)].reset_index(drop=True)
    segment_sequence = segment_sequences(df2)
    # 找到每段开始索引和结束索引
    count = 0  # 记录不满足的个数
    for seg in segment_sequence:
        begin_index = df2[df2['date'] == seg[0]].index.tolist()[0]
        end_index = df2[df2['date'] == seg[1]].index.tolist()[0]

        # 找到数据起始和结束的索引,选中 求均值
        sequence_mean = round(df2['THRPRESS'][begin_index:end_index + 1].mean(), 4)
        print(sequence_mean)

        # 标记偏差小于0.35的值,为deviation列值为0,符合要求,供下一步筛选用
        for i in range(begin_index, end_index + 1):
            if (abs(df2['THRPRESS'][i] - sequence_mean) > deviation):
                df2.loc[i, 'deviation'] = 1
                count += 1
    df2 = df2[df2['deviation'] != 1]
    df2 = df2.drop(['deviation'], axis=1)
    print(count)

    return df2


def segment_sequences(df2):
    # 划分对应的时间工况段
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
    segment_sequence = list(zip(begin, end))
    print(segment_sequence)
    return segment_sequence


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


if __name__ == "__main__":
    dir_path = r'F:/HistoryData/08new/'
    output_path = dir_path[:-1] + 'process/'
    save_file_name = r'all08.csv'  # 合并后要保存的文件名

    if (not os.path.exists(output_path)):
        os.mkdir(output_path)

    # 对目录下的所有文件进行筛选操作, 筛选完放入目标文件夹
    for parent, dir_names, file_names in os.walk(dir_path):
        for filename in file_names:
            csv_data_filtering(os.path.join(parent, filename), os.path.join(output_path, filename))

    # 对目标文件夹内的所有数据进行合并
    csv_merge(output_path, save_file_name)
    input_file = r'F:/HistoryData/08newprocess/all08.csv'
    df2 = pd.read_csv(input_file, header=0)
    df2 = deviation_filtering(df2, 0.35)
    output = r'F:/HistoryData/all08.csv'
    df2.to_csv(output, index=False)
