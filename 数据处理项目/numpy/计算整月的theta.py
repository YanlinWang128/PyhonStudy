# @Time    : 2018/10/18 16:11
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 计算整月的theta.py


import os
import numpy as np
import pandas as pd

# p = np.eye(25) * (10 ** 8)  # 每个文件重置一次
p = np.eye(25) * (10 ** 8)  # 每个文件重置一次
theta = np.zeros((25, 1))
input_path = r'C:/Users/Frank/Desktop/08time_series/'
d1 = d2 = d3 = d4 = 60

for info in os.listdir(input_path):
    domain = os.path.abspath(input_path)  # 获取文件夹的路径
    path_file = os.path.join(domain, info)  # 将路径与文件名结合起来就是每个文件的完整路径
    df2 = pd.read_csv(path_file, header=0)

    print(df2.columns.values.tolist())

    y_output = df2['T12A041A'].tolist()

    u1_difference = df2['u1_difference'].tolist()
    u2_difference = df2['u2_difference'].tolist()
    u3_difference = df2['u3_difference'].tolist()
    u4_difference = df2['u4_difference'].tolist()


    # 新建指定尺寸,全为 10**8 值得列表np.full(tuple(x, y), value)
    # p = np.full((25, 25), 10 ** 8)



    # 1 * n

    def phi(k):
        temp = y_output[(k - 1 - 1):(k - 1 - 5 - 1):-1]
        return np.array([x * -1 for x in temp] + u1_difference[(k - 1 - 1 - 1):(
            k - 1 - 1 - 4 - d1 - 1):-1] + u2_difference[(k - 1 - 1 - 1):(k - 1 - 1 - 4 - d2 - 1):-1] + u3_difference[
                                                                                                       (k - 1 - 1 - 1):(
                                                                                                           k - 1 - 1 - 4 - d3 - 1):-1] + u4_difference[
                                                                                                                                         (
                                                                                                                                             k - 1 - 1 - 1):(
                                                                                                                                             k - 1 - 1 - 4 - d4 - 1):-1])


    # 1* 25
    def phi_1(k):
        temp = y_output[(k - 1 - 1):(k - 1 - 5 - 1):-1]
        return np.array(
            [[x * -1 for x in temp] + u1_difference[(k - 1 - 1 - 1):(k - 1 - 1 - 4 - d1 - 1):-1][
                                      -5:] + u2_difference[(k - 1 - 1 - 1):(k - 1 - 1 - 4 - d2 - 1):-1][
                                             -5:] + u3_difference[
                                                    (k - 1 - 1 - 1):(k - 1 - 1 - 4 - d3 - 1):-1][
                                                    -5:] + u4_difference[
                                                           (k - 1 - 1 - 1):(k - 1 - 1 - 4 - d4 - 1):-1][
                                                           -5:]])


    # print(p, np.shape(p))
    # 控制参数d1, d2, d3, d4 初始化
    # 创建单位矩阵 np.eye(value)
    # identity_matrix_25 = np.eye(25)
    # print(P.T)
    # 转置 a.T
    # 零矩阵  np.zeros(tuple(x, y) , 参数必须为元组
    start_item = max([d1, d2, d3, d4]) + 10
    end_item = len(df2.index) - start_item - 10

    for k in range(start_item, end_item):
        K = p.dot(phi_1(k).T) * ((1 + phi_1(k).dot(p).dot(phi_1(k).T)) ** -1)
        # print(k, K)
        theta = theta + K * (y_output[k - 1] - phi_1(k).dot(theta))
        # print(k, theta.T)
        p = (np.eye(25) - K.dot(phi_1(k))).dot(p)

    print(theta.T.tolist())

"""
[[-1.01575681 -0.19002532 -0.05443981  0.09605609  0.16415831 -0.00205784
   0.00405411  0.00217475  0.00519341  0.00390873  0.31140836  0.08590223
   0.18611989 -0.25154623  0.26859639  0.08872846  0.04026616  0.01721728
   0.01538795 -0.00243144  0.01539683 -0.01631048  0.00823702 -0.07188604
   0.04221205]]

"""


