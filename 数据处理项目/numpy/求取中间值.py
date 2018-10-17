# @Time    : 2018/10/16 9:35
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 求取中间值.py
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


"""
# 25 * 1
def K(k):
    temp = (1 + phi_1(k).dot(p(k - 1)).dot(phi_1(k).T)) ** -1
    return p(k - 1).dot(phi_1(k).T) * temp


"""
"""

def p(k):
    if k == 19:
        return np.full((25, 25), 10 ** 8)
    if k > 19:
        temp = np.eye(25) - K(k).dot(phi_1(k))
        return temp.dot(p(k - 1))
    if k < 19:
        print("theta  19  为初始值")

"""

# print(p, np.shape(p))
# 控制参数d1, d2, d3, d4 初始化



# 创建单位矩阵 np.eye(value)
# identity_matrix_25 = np.eye(25)
# print(P.T)

# 转置 a.T
# 零矩阵  np.zeros(tuple(x, y) , 参数必须为元组



# print(theta, np.shape(theta))
"""

def theta(k):
    if k == 19:
        return np.zeros((25, 1))
    if k > 19:
        temp = y_output[k - 1] - phi_1(k).dot(theta(k - 1))
        return theta(k - 1) + K(k) * temp
    if k < 19:
        print("theta  19  为初始值")
"""

# print(K(20), np.shape(K(20)))
# print(theta(50), np.shape(theta(50)))
# print(phi_1(20))
# print(type(np.eye(25) - K(20).dot(phi_1(20))))
p = np.eye(25) * (10 ** 8)
# print(p, type(p))
theta = np.zeros((25, 1))
# print(theta)
for k in range(20, 1001):
    K = p.dot(phi_1(k).T) * ((1 + phi_1(k).dot(p).dot(phi_1(k).T)) ** -1)
    # print(k, K)
    theta = theta + K * (y_output[k - 1] - phi_1(k).dot(theta))
    print(k-19, theta.T)
    p = (np.eye(25) - K.dot(phi_1(k))).dot(p)
