# @Time    : 2018/11/2 10:44
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 单输入预测对比_基于原始值.py

from time import clock
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start = clock()


def theta_caculate(delay):
    input_path = r'C:/Users/Frank/Desktop/tongliu/mat_data_1102.csv'
    d1 = d2 = d3 = d4 = delay

    na, nb1, nb2, nb3, nb4 = 10, 10, 10, 10, 10
    # phi_(k)的长度
    matrix_length = na + nb1 + nb2 + nb3 + nb4 + 4

    # 初始值
    p = np.eye(matrix_length) * (10 ** 10)  # 每个文件重置一次
    theta = np.zeros((matrix_length, 1))

    df2 = pd.read_csv(input_path, header=0)

    # print(df2.columns.values.tolist())
    theta_first_value = [0]
    y_output = df2['y'].tolist()
    difference_length = len(df2.index) - 1
    # print(difference_length)

    u1_difference = df2['u_difference'].tolist()
    # u1_difference = df2['u1_difference'].tolist()
    # u2_difference = df2['u2_difference'].tolist()
    # u3_difference = df2['u3_difference'].tolist()
    # u4_difference = df2['u4_difference'].tolist()
    u2_difference = [0] * difference_length
    u3_difference = [0] * difference_length
    u4_difference = [0] * difference_length

    # 1* 25
    def phi_1(k):
        temp = y_output[(k - 1 - 1):(k - na - 1 - 1):-1]
        return np.array([[x * -1 for x in temp] +
                         u1_difference[(k - d1 - 2):(k - d1 - nb1 - 2 - 1):-1] +
                         u2_difference[(k - d2 - 2):(k - d2 - nb2 - 2 - 1):-1] +
                         u3_difference[(k - d3 - 2):(k - d3 - nb3 - 2 - 1):-1] +
                         u4_difference[(k - d4 - 2):(k - d4 - nb4 - 2 - 1):-1]])

    start_item = max([na, d1 + nb1, d2 + nb2, d3 + nb3, d4 + nb4]) + 3
    end_item = len(df2.index) - start_item

    for k in range(start_item, end_item):
        K = p.dot(phi_1(k).T) * ((1 + phi_1(k).dot(p).dot(phi_1(k).T)) ** -1)
        theta = theta + K * (y_output[k - 1] - phi_1(k).dot(theta))
        # theta_first_value.append(theta.T.tolist()[0][5])
        p = (np.eye(matrix_length) - K.dot(phi_1(k))).dot(p)

    # print(len(theta.T.tolist()[0]), theta.T.tolist())
    # print(p.shape, p)
    # a, b = np.linalg.eig(p)
    # print('--' * 10)
    # print(a)

    # plt.plot(theta_first_value, color='red', linewidth=2, linestyle='--', label='theta_first_value')
    # plt.legend(loc='best')  # 显示在最好的位置
    # plt.title('theta_sixth_value')
    # plt.show()  # 显示图
    return theta.T.tolist()[0]


def predict(theta, delay):
    input_file = r'C:/Users/Frank/Desktop/tongliu/mat_data_1102.csv'

    df2 = pd.read_csv(input_file, header=0)
    # print(df2.columns.values.tolist())
    na, nb1, nb2, nb3, nb4 = 10, 10, 10, 10, 10
    # phi_(k)的长度
    matrix_length = na + nb1 + nb2 + nb3 + nb4 + 4
    y_output = df2['y'].tolist()

    difference_length = len(df2.index) - 1  # difference 长度
    # print(difference_length)

    u1_difference = df2['u_difference'].tolist()

    u2_difference = [0] * difference_length
    u3_difference = [0] * difference_length
    u4_difference = [0] * difference_length
    # u1_difference = df2['u1_difference'].tolist()
    # u2_difference = df2['u2_difference'].tolist()
    # u3_difference = df2['u3_difference'].tolist()
    # u4_difference = df2['u4_difference'].tolist()


    # d1 = d2 = d3 = d4 = 20
    d1 = d2 = d3 = d4 = delay

    start_item = max([na, d1 + nb1, d2 + nb2, d3 + nb3, d4 + nb4]) + 3
    end_item = len(df2.index) - start_item
    # end_item = 100

    # start_item = 20

    # y(k)--->  y_index_5 = start_item
    # y = [(y_output[start_item - 6]), (y_output[start_item - 5]), (y_output[start_item - 4]), (y_output[start_item - 3]),
    #      (y_output[start_item - 2])]

    y = []

    def y_predict(k):
        # b = k - start_item
        y_k = 0
        for i in range(0, na):
            y_k = y_k - theta[i] * y_output[k - 1 + i - 1]
        for i in range(0, nb1 + 1):
            y_k = y_k + theta[na + i] * u1_difference[k - 1 - (d1 - 1 + i) - 2]
        for i in range(0, nb2 + 1):
            y_k = y_k + theta[na + nb1 + 1 + i] * u2_difference[k - 1 - (d2 - 1 + i) - 2]
        for i in range(0, nb3 + 1):
            y_k = y_k + theta[na + nb1 + 1+ nb2+1+ i] * u3_difference[k - 1 - (d3 - 1 + i) - 2]
        for i in range(0, nb4 + 1):
            y_k = y_k + theta[na + nb1 + 1+ nb2+1+nb3+1+ i] * u4_difference[k - 1 - (d4 - 1 + i) - 2]
        # y.append(y_k)
        return y_k

    # print(y_predict(20, y))
    # print(y)
    # print(end_item -start_item, )
    for item in range(start_item, end_item):
        y.append(y_predict(item))
    # print(y)
    # print(y[5:10])
    # 够不到,所以全部取了数据
    # print(len(y[5:]), y[5:])
    # print(len(y_output[start_item - 1:end_item - 1]), y_output[start_item - 1:end_item - 1])

    # 计算 误差(均方误差)
    #  c = [a[i] - b[i] for i in range(len(a))]
    # sum([(y-m*x -b)**2 for x,y in zip(X,Y)])/len(X)
    predict_value = y
    primary_value = y_output[start_item - 1:end_item - 1]

    # print(len(predict_value), len(primary_value))

    """
    def error_caculate(primary_value, predict_value):
        return 1 - (np.std(np.array(predict_value[1:]) - np.array(primary_value[:-1]) - (
        np.array(primary_value[1:] - np.array(primary_value[:-1]))), ddof=1) / np.std(
            np.array(primary_value[1:]) - np.array(primary_value[:-1]), ddof=1))
    """

    #     def error_caculate(primary_value, predict_value):

    # return 1 - (np.std(np.array(predict_value[1:]) - np.array(primary_value[1:]) , ddof=1) / np.std(np.array(primary_value[1:]) - np.array(primary_value[:-1]), ddof=1))
    #     # error_value = math.sqrt(sum([(y - x) ** 2 for x, y in zip(predict_value, primary_value)]) / len(predict_value))
    def error_caculate(primary_value, predict_value):
        return 1 - (np.sum(np.fabs(np.array(predict_value[1:]) - np.array(primary_value[1:]))) / np.sum(np.fabs(
            np.array(primary_value[1:]) - np.array(primary_value[:-1]))))

    print(delay, error_caculate(primary_value, predict_value))
    plt.figure()
    plt.plot(predict_value, color='red', linewidth=2, linestyle='--', label='predicted_value')
    plt.plot(primary_value, color='blue', linewidth=2, linestyle='--', label='primary_value')
    plt.legend(loc='best')  # 显示在最好的位置
    # plt.title('theta_sixth_value')
    # plt.show()  # 显示图


if __name__ == '__main__':
    for delay in range(15, 21):
        predict(theta_caculate(delay), delay)
    end = clock()
    print('time: {:.8f}s'.format(end - start))
