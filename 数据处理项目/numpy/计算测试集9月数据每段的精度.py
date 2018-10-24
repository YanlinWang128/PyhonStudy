# @Time    : 2018/10/23 19:48
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 计算测试集9月数据每段的精度.py
import pandas as pd
import os
import math
import numpy as np

path = r'C:/Users/Frank/Desktop/09time_series/'
for info in os.listdir(path):
    # 将路径与文件名结合起来就是每个文件的完整路径
    path_file = os.path.join(os.path.abspath(path), info)
    df2 = pd.read_csv(path_file, header=0)

    # df2 = pd.read_csv(input_file, header=0)
    # print(df2.columns.values.tolist())
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

    theta = [-0.9504787561331044, -0.16455410856133795, -0.032208523640073906, -0.0016657151452271507, 0.14890634970727676, 0.0018128497905697662, 0.001499392600299226, 0.001462227262926927, 0.0013061218614014256, 0.0016620474949730788, -0.00454427092721587, -0.0040635143218932385, -0.005976850315835837, 0.0033787585162168244, -0.0015993782824658782, 0.003098713088855372, 0.011158216649671098, 0.0012784170291542001, 0.0011200982566052895, 0.005944729377494164, -0.011018845684328612, 0.005861570974270512, 0.006319242130136507, -0.008570530331351914, 0.0016927839211352037]
    # print(theta)



    # print(y_k, y_output[19], y_k - y_output[19])

    start_item = max([d1, d2, d3, d4]) + 10
    end_item = len(df2.index) - start_item - 10
    # start_item = 20

    # y(k)--->  y_index_5 = start_item
    # y = [(y_output[start_item - 6]), (y_output[start_item - 5]), (y_output[start_item - 4]), (y_output[start_item - 3]),
    # (y_output[start_item - 2])]
    y = []


    def y_predict(k):
        # b = k - start_item
        y_k = -theta[0] * y_output[k - 2] - theta[1] * y_output[k - 3] - theta[2] * y_output[k - 4] - theta[3] * \
                                                                                                      y_output[k - 5] - \
              theta[4] * y_output[k - 6] + theta[5] * u1_difference[k - 1 - (d1 - 1) - 2] + theta[6] * u1_difference[
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

        return y_k


    # print(y_predict(20, y))
    # print(y, len(y))
    for item in range(start_item, end_item):
        y.append(y_predict(item))
    # print(len(y), y)

    # 够不到,所以全部取了数据
    # print(len(y[5:]), y[5:])
    # print(len(y_output[start_item - 1:end_item - 1]), y_output[start_item - 1:end_item - 1])

    # 计算 误差(均方误差)
    #  c = [a[i] - b[i] for i in range(len(a))]
    # sum([(y-m*x -b)**2 for x,y in zip(X,Y)])/len(X)
    predict_value = y
    primary_value = y_output[start_item - 1:end_item - 1]
    error_value = math.sqrt(sum([(y - x) ** 2 for x, y in zip(predict_value, primary_value)]) / len(predict_value))

    print('第{}段,均方根误差为{}'.format(info[:3], error_value))
