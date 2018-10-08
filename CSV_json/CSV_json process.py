# @Time    : 2018/10/8 8:35
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : CSV_json process.py

import csv
import pandas as pd
import numpy as np
from csv import reader
import datetime


def csv_merge(fileName):

    inputFile = "" + fileName

    df2 = pd.read_csv(inputFile)

    Periods = df2.__len__()  # #索引数 ,事件序列个数
    startTime = df2['date'][0]
    # startTime=pd.datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
    endTime = df2['date'][df2.__len__() - 1]  # 此处的年份也需要改
    # 对每个采样间隔处理数据

    Interval = "5T"
    outFile = 'D:/aa/raw/interval-5min/' + fileName

    # 这个函数的作用就是产生一个DatetimeIndex(时间序列数据的索引)
    df2.index = pd.date_range(startTime, endTime, periods=Periods)

    # 根据产
    # ..生的索引,间隔 采样 求均值
    sampling = df2.resample(Interval).mean()  # 1T   即一分钟, AMQW:年月季周
    # df2.rename(columns={'': 'date'}, inplace=True)
    # 输出为CSV文件
    sampling.reset_index(inplace=True)
    sampling.rename(columns={'index': 'date'}, inplace=True)
    sampling.to_csv(outFile, index=0)
    # print(sampling)


if __name__ == "__main__":
    fileName = "rawData2018.07.01.csv"  # 文件名,不是路径名
    csv_merge(fileName)
