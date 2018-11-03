# @Time    : 2018/10/18 16:11
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 计算整月的theta.py


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def theta_caculate(delay):
    input_path = r'C:/Users/Frank/Desktop/tongliu/mat_data_1102.csv'
    d1 = d2 = d3 = d4 = delay

    na, nb1, nb2, nb3, nb4 = 5, 10, 0, 0, 0
    # phi_(k)的长度
    matrix_length = na + nb1 + nb2 + nb3 + nb4 + 4

    # 初始值
    p = np.eye(matrix_length) * (10 ** 10)  # 每个文件重置一次
    theta = np.zeros((matrix_length, 1))

    df2 = pd.read_csv(input_path, header=0)

    # print(df2.columns.values.tolist())
    # theta_first_value = [0]
    y_output = df2['y'].tolist()
    difference_length = len(df2.index) - 1
    # print(difference_length)

    u1_difference = df2['u_difference'].tolist()
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

    # y = [(y_output[start_item - 6]), (y_output[start_item - 5]), (y_output[start_item - 4]), (y_output[start_item - 3]),
    #      (y_output[start_item - 2])]
    y = [y_output[start_item - i] for i in range(na+1, 1, -1) ]
    # print(y)
    # print('baba',len(y))

    # print(y[na-1: 0:-1], y[0])
    def y_predict(k):
        # b = k - start_item
        temp = y[-na:][::-1]
        # print('helloha', len(temp), temp)
        return np.array([[x * -1 for x in temp] +
                         u1_difference[(k - d1 - 2):(k - d1 - nb1 - 2 - 1):-1] +
                         u2_difference[(k - d2 - 2):(k - d2 - nb2 - 2 - 1):-1] +
                         u3_difference[(k - d3 - 2):(k - d3 - nb3 - 2 - 1):-1] +
                         u4_difference[(k - d4 - 2):(k - d4 - nb4 - 2 - 1):-1]])

    # print(y_predict(50).shape)
    for item in range(start_item, end_item):
        # print('result',np.sum(np.array(theta.T.tolist()[0]) * np.array(y_predict(item)[0])))
        y.append(np.sum(np.array(theta.T.tolist()[0]) * np.array(y_predict(item)[0])))

    # print(len(theta.T.tolist()[0]), theta.T.tolist()[0])

    predict_value = y[na:][:61]
    primary_value = y_output[start_item - 1:end_item - 1][:61]

    def error_caculate(primary_value, predict_value):
        return 1 - (np.sum(np.fabs(np.array(predict_value[1:]) - np.array(primary_value[1:]))) / np.sum(np.fabs(
            np.array(primary_value[1:]) - np.array(primary_value[:-1]))))

    print(delay, error_caculate(primary_value, predict_value))
    # print(p.shape, p)
    # a, b = np.linalg.eig(p)
    # print('--' * 10)
    # print(a)

    plt.plot(predict_value, color='red', linewidth=2, linestyle='--', label='predicted_value')
    plt.plot(primary_value, color='blue', linewidth=2, linestyle='--', label='primary_value')
    plt.legend(loc='best')  # 显示在最好的位置
    # plt.legend(loc='best')  # 显示在最好的位置
    # plt.title('theta_sixth_value')
    # plt.show()  # 显示图
    return theta


if __name__ == '__main__':
    for delay in range(4, 36):
        theta_caculate(delay)

# print()
"""
        # print(p, np.shape(p))
        # 控制参数d1, d2, d3, d4 初始化
        # 创建单位矩阵 np.eye(value)
        # identity_matrix_25 = np.eye(25)
        # print(P.T)
        # 转置 a.T
        # 零矩阵  np.zeros(tuple(x, y) , 参数必须为元组

        def phi(k):
            temp = y_output[(k - 1 - 1):(k - 1 - 5 - 1):-1]
            return np.array([x * -1 for x in temp] + u1_difference[(k - 1 - 1 - 1):(
                k - 1 - 1 - 4 - d1 - 1):-1] + u2_difference[(k - 1 - 1 - 1):(k - 1 - 1 - 4 - d2 - 1):-1] + u3_difference[
                                                                                                           (k - 1 - 1 - 1):(
                                                                                                               k - 1 - 1 - 4 - d3 - 1):-1] + u4_difference[
                                                                                                                                             (
                                                                                                                                                 k - 1 - 1 - 1):(
                                                                                                                                                 k - 1 - 1 - 4 - d4 - 1):-1])

8 月 不重置p theta
[-0.947811753254557, -0.1602734752309542, -0.03448030850601901, -0.005926564828329537, 0.1484914112222206, -0.0009167907050742148, -0.00044047889180056266, -0.0008603608454455753, -0.0010497972228475556, -0.0013690907990828963, -0.004879941649358138, 0.003607438592081519, -0.007032472427834018, 0.003372239159058352, 0.00011472812084576332, -0.0002654366964989808, 0.004595917416402356, 0.010732629284789675, 0.001118314301918791, -0.0012206028988971187, 0.005343735508116856, 0.003180975195237934, 0.0039830257801174605, 0.008527858527091375, 0.0009007565552914656]
8 重置p
[-0.9130166305850802, -0.16366567946942107, -0.08301533388572699, 0.06870030696574138, 0.0909940945319406, -0.0012545512051814628, 0.0014544399132686338, 0.0017666228809133226, 0.002020066524392353, -0.0037471861689967077, 0.11211277943474644, 0.01730450197080619, 0.057543236477990964, 0.17010521511462975, -0.18566320910540854, 0.03977242725122014, 0.04114835281539401, -0.02288171253603298, -0.018669013812583794, 0.04142331514598825, -0.0370400250168526, 0.020587779875055206, 0.052806452669436, 0.07321127940575609, -0.005193168334853946]
"""
