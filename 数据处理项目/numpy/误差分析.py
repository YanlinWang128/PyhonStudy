# @Time    : 2018/10/22 16:40
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 误差分析.py


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math
import re


# import sys
# # 修改 递归深度,指标不治本,TODO
# sys.setrecursionlimit(1000000) #例如这里设置为一百万
# 最原始的数据打开有中文,按照gbk打开

def error_analysis(input_file):
    df2 = pd.read_csv(input_file, header=0)
    print(df2.columns.values.tolist())
    y_output = df2['T12A041A'].tolist()

    u1_difference = df2['u1_difference'].tolist()
    u2_difference = df2['u2_difference'].tolist()
    u3_difference = df2['u3_difference'].tolist()
    u4_difference = df2['u4_difference'].tolist()
    # 新建指定尺寸,全为 10**8 值得列表np.full(tuple(x, y), value)
    # p = np.full((25, 25), 10 ** 8)
    d1 = d2 = d3 = d4 = 60

    p = np.eye(25) * (10 ** 8)
    # print(p, type(p))
    # theta = [-1.01575681, -0.19002532, -0.05443981, 0.09605609, 0.16415831, -0.00205784, 0.00405411, 0.00217475, 0.00519341,
    #          0.00390873, 0.31140836, 0.08590223, 0.18611989, -0.25154623, 0.26859639, 0.08872846, 0.04026616, 0.01721728,
    #          0.01538795, -0.00243144, 0.01539683, -0.01631048, 0.00823702, -0.07188604, 0.04221205]

    theta = [-0.9130166305850802, -0.16366567946942107, -0.08301533388572699, 0.06870030696574138, 0.0909940945319406,
             -0.0012545512051814628, 0.0014544399132686338, 0.0017666228809133226, 0.002020066524392353,
             -0.0037471861689967077, 0.11211277943474644, 0.01730450197080619, 0.057543236477990964,
             0.17010521511462975, -0.18566320910540854, 0.03977242725122014, 0.04114835281539401, -0.02288171253603298,
             -0.018669013812583794, 0.04142331514598825, -0.0370400250168526, 0.020587779875055206, 0.052806452669436,
             0.07321127940575609, -0.005193168334853946]
    # print(theta)



    # print(y_k, y_output[19], y_k - y_output[19])

    start_item = max([d1, d2, d3, d4]) + 10
    end_item = len(df2.index) - start_item - 10
    # start_item = 20

    # y(k)--->  y_index_5 = start_item
    y = [(y_output[start_item - 6]), (y_output[start_item - 5]), (y_output[start_item - 4]), (y_output[start_item - 3]),
         (y_output[start_item - 2])]

    def y_predict(k, y):
        b = k - start_item
        y_k = -theta[0] * y[4 + b] - theta[1] * y[b + 3] - theta[2] * y[b + 2] - theta[3] * y[
            b + 1] - theta[4] * y[b] + theta[5] * u1_difference[k - 1 - (d1 - 1) - 2] + theta[6] * u1_difference[
            k - 1 - (d1) - 2] + theta[7] * u1_difference[k - 1 - (d1 + 1) - 2] + theta[8] * u1_difference[
            k - 1 - (d1 + 2) - 2] + theta[9] * u1_difference[k - 1 - (d1 + 3) - 2] + theta[10] * u2_difference[
            k - 1 - (d2 - 1) - 2] + theta[11] * u2_difference[
            k - 1 - (d2) - 2] + theta[12] * u2_difference[k - 1 - (d2 + 1) - 2] + theta[13] * u2_difference[
            k - 1 - (d2 + 2) - 2] + theta[14] * u2_difference[k - 1 - (d2 + 3) - 2] + theta[15] * u3_difference[
            k - 1 - (d3 - 1) - 2] + theta[16] * u3_difference[
            k - 1 - (d3) - 2] + theta[17] * u3_difference[k - 1 - (d3 + 1) - 2] + theta[18] * u3_difference[
            k - 1 - (d3 + 2) - 2] + theta[19] * u3_difference[k - 1 - (d3 + 3) - 2] + theta[20] * u4_difference[
            k - 1 - (d4 - 1) - 2] + theta[21] * u4_difference[
            k - 1 - (d4) - 2] + theta[22] * u4_difference[k - 1 - (d4 + 1) - 2] + theta[23] * u4_difference[
            k - 1 - (d4 + 2) - 2] + theta[24] * u4_difference[k - 1 - (d4 + 3) - 2]
        y.append(y_k)
        return y_k

    # print(y_predict(20, y))
    print(y)
    for item in range(start_item, end_item):
        y_predict(item, y)
    print(y)

    print(len(y[5:end_item]), y[5:end_item])
    print(len(y_output[start_item - 1:end_item - 1]), y_output[start_item - 1:end_item - 1])

    # 计算 误差(均方误差)
    #  c = [a[i] - b[i] for i in range(len(a))]
    # sum([(y-m*x -b)**2 for x,y in zip(X,Y)])/len(X)
    predict_value = y_output[start_item - 1:end_item - 1]
    primary_value = y[5:end_item]
    # 均方根误差
    error_value = math.sqrt(sum([(y - x) ** 2 for x, y in zip(predict_value, primary_value)]) / len(predict_value))
    # 误差均值
    error_mean = sum([(y - x) for x, y in zip(predict_value, primary_value)]) / len(predict_value)
    print(error_value)
    return error_value


if __name__ == '__main__':
    # input_file = r'C:/Users/Frank/Desktop/08time_series/002.csv'

    path = r'C:/Users/Frank/Desktop/08time_series/'
    # os.path.join(path, file_list[0]
    # file_list = sorted(os.listdir(path), key=lambda items: int(re.findall(r'p(\d+).csv', items)[0]))
    file_list = os.listdir(path)
    # for file in file_list:
    #     input_file = os.path.join(path, file)
    #     error_analysis(input_file)
    error_list = [error_analysis(os.path.join(path, file)) for file in file_list]

    print(error_list)
    print(max(error_list), min(error_list))
    ax = plt.subplot(111)
    x = np.linspace(1, 35, 35)
    plt.plot(x, error_list, color='blue', linewidth=2, linestyle='--', label='MEAN')
    ax.xaxis.set_major_locator(MultipleLocator(5))
    plt.title('MEAN')
    # plt.legend(loc='best')
    plt.show()
