# @Time    : 2018/10/19 12:38
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : y 初始值.py

import os
import pandas as pd
import numpy as np

# import sys
# # 修改 递归深度,指标不治本,TODO
# sys.setrecursionlimit(1000000) #例如这里设置为一百万
# 最原始的数据打开有中文,按照gbk打开
input_file = 'C:/Users/Frank/Desktop/08time_series/001.csv'
df2 = pd.read_csv(input_file, header=0)
print(df2.columns.values.tolist())
y_output = df2['T12A041A'].tolist()

u1_difference = df2['u1_difference'].tolist()
u2_difference = df2['u2_difference'].tolist()
u3_difference = df2['u3_difference'].tolist()
u4_difference = df2['u4_difference'].tolist()
# 新建指定尺寸,全为 10**8 值得列表np.full(tuple(x, y), value)
# p = np.full((25, 25), 10 ** 8)
d1 = d2 = d3 = d4 = 2

p = np.eye(25) * (10 ** 8)
# print(p, type(p))
theta = [-1.01575681, -0.19002532, -0.05443981, 0.09605609, 0.16415831, -0.00205784, 0.00405411, 0.00217475, 0.00519341,
         0.00390873, 0.31140836, 0.08590223, 0.18611989, -0.25154623, 0.26859639, 0.08872846, 0.04026616, 0.01721728,
         0.01538795, -0.00243144, 0.01539683, -0.01631048, 0.00823702, -0.07188604, 0.04221205]

# print(theta)
y_20 = -theta[0] * y_output[19 - 1] - theta[1] * y_output[18 - 1] - theta[2] * y_output[17 - 1] - theta[3] * y_output[
    16 - 1] - theta[4] * y_output[15 - 1] + theta[5] * u1_difference[20 - 1 - (d1 - 1) - 2] + theta[6] * u1_difference[
    20 - 1 - (d1) - 2] + theta[7] * u1_difference[20 - 1 - (d1 + 1) - 2] + theta[8] * u1_difference[
    20 - 1 - (d1 + 2) - 2] + theta[9] * u1_difference[20 - 1 - (d1 + 3) - 2] + theta[10] * u2_difference[
    20 - 1 - (d2 - 1) - 2] + theta[11] * u2_difference[
    20 - 1 - (d2) - 2] + theta[12] * u2_difference[20 - 1 - (d2 + 1) - 2] + theta[13] * u2_difference[
    20 - 1 - (d2 + 2) - 2] + theta[14] * u2_difference[20 - 1 - (d2 + 3) - 2] + theta[15] * u3_difference[
    20 - 1 - (d3 - 1) - 2] + theta[16] * u3_difference[
    20 - 1 - (d3) - 2] + theta[17] * u3_difference[20 - 1 - (d3 + 1) - 2] + theta[18] * u3_difference[
    20 - 1 - (d3 + 2) - 2] + theta[19] * u3_difference[20 - 1 - (d3 + 3) - 2] + theta[20] * u4_difference[
    20 - 1 - (d4 - 1) - 2] + theta[21] * u4_difference[
    20 - 1 - (d4) - 2] + theta[22] * u4_difference[20 - 1 - (d4 + 1) - 2] + theta[23] * u4_difference[
    20 - 1 - (d4 + 2) - 2] + theta[24] * u4_difference[20 - 1 - (d4 + 3) - 2]


print(y_20, y_output[19], y_20-y_output[19])

"""
[[-1.01575681 -0.19002532 -0.05443981  0.09605609  0.16415831 -0.00205784
   0.00405411  0.00217475  0.00519341  0.00390873  0.31140836  0.08590223
   0.18611989 -0.25154623  0.26859639  0.08872846  0.04026616  0.01721728
   0.01538795 -0.00243144  0.01539683 -0.01631048  0.00823702 -0.07188604
   0.04221205]]

for k in range(20, 1001):
    K = p.dot(phi_1(k).T) * ((1 + phi_1(k).dot(p).dot(phi_1(k).T)) ** -1)
    # print(k, K)
    theta = theta + K * (y_output[k - 1] - phi_1(k).dot(theta))
    print(k-19, theta.T)
    p = (np.eye(25) - K.dot(phi_1(k))).dot(p)

"""
