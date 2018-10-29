# @Time    : 2018/10/25 10:43
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 模型测试.py
import numpy as np
import pandas as pd

path_file = r'C:/Users/Frank/Desktop/tongliu/mat_data_10_26.csv'
df2 = pd.read_csv(path_file, header=0)
print(df2.columns.values.tolist())

y_output = df2['y'].tolist()
print(len(y_output), y_output)
print('---' * 10)
print(df2['u_difference'].tolist())

# u1_difference = ([-1, 1] * 100)
u1_difference = df2['u_difference'].tolist()[:-1]  # 构造列表
u2_difference = [0] * (len(y_output) - 1)
u3_difference = [0] * (len(y_output) - 1)
u4_difference = [0] * (len(y_output) - 1)

print(len(y_output), len(u1_difference), len(u2_difference))
# print(len(u2_difference), u2_difference)

p = np.eye(25) * (10 ** 8)  # 每个文件重置一次
theta = np.zeros((25, 1))

d1 = d2 = d3 = d4 = 20


# 1* 25
def phi_1(k):
    temp = y_output[(k - 1 - 1):(k - 5 - 1 - 1):-1]
    return np.array(
        [[x * -1 for x in temp] + u1_difference[(k - 1 - 2):(k - 1 - 3 - d1 - 2 - 1):-1][
                                  -5:] + u2_difference[(k - 1 - 2):(k - 1 - 3 - d2 - 2 - 1):-1][
                                         -5:] + u3_difference[(k - 1 - 2):(k - 1 - 3 - d3 - 2 - 1):-1][
                                                -5:] + u4_difference[(k - 1 - 2):(k - 1 - 3 - d4 - 2 - 1):-1][-5:]])


# print([x * -1 for x in y_output[(27 - 1 - 1):(27 - 5 - 1 - 1):-1]])
# print(u1_difference[(27 - 1 - 2):(27 - 1 - 3 - d1 - 2 - 1):-1][-5:])
# print('---' * 10)
# print(u2_difference[(27 - 1 - 2):(27 - 1 - 3 - d1 - 2 - 1):-1][-5:])
# print('---' * 10)

start_item = max([d1, d2, d3, d4]) + 7
end_item = len(df2.index) - start_item
print(start_item, end_item)

print(phi_1(start_item).shape)

for k in range(start_item, end_item):
    K = p.dot(phi_1(k).T) * ((1 + phi_1(k).dot(p).dot(phi_1(k).T)) ** -1)
    theta = theta + K * (y_output[k - 1] - phi_1(k).dot(theta))
    p = (np.eye(25) - K.dot(phi_1(k))).dot(p)

print(len(theta.T.tolist()), theta.T.tolist())
