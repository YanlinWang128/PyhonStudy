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
    # 初始值
    p = np.eye(25) * (10 ** 10)  # 每个文件重置一次
    theta = np.zeros((25, 1))
    input_path = r'C:/Users/Frank/Desktop/tongliu/mat_data_1102.csv'
    # d1 = d2 = d3 = d4 = 20
    d1 = d2 = d3 = d4 = delay

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
        temp = y_output[(k - 1 - 1):(k - 5 - 1 - 1):-1]
        return np.array(
            [[x * -1 for x in temp] + u1_difference[(k - 1 - 2):(k - 1 - 3 - d1 - 2 - 1):-1][
                                      -5:] + u2_difference[(k - 1 - 2):(k - 1 - 3 - d2 - 2 - 1):-1][
                                             -5:] + u3_difference[
                                                    (k - 1 - 2):(k - 1 - 3 - d3 - 2 - 1):-1][
                                                    -5:] + u4_difference[
                                                           (k - 1 - 2):(k - 1 - 3 - d4 - 2 - 1):-1][
                                                           -5:]])

    start_item = max([d1, d2, d3, d4]) + 7
    end_item = len(df2.index) - start_item

    for k in range(start_item, end_item):
        K = p.dot(phi_1(k).T) * ((1 + phi_1(k).dot(p).dot(phi_1(k).T)) ** -1)
        theta = theta + K * (y_output[k - 1] - phi_1(k).dot(theta))
        theta_first_value.append(theta.T.tolist()[0][5])
        p = (np.eye(25) - K.dot(phi_1(k))).dot(p)

    # print(theta.T.tolist())
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

    # 新建指定尺寸,全为 10**8 值得列表np.full(tuple(x, y), value)
    # p = np.full((25, 25), 10 ** 8)
    # d1 = d2 = d3 = d4 = 20
    d1 = d2 = d3 = d4 = delay
    # p = np.eye(25) * (10 ** 8)
    # print(p, type(p))
    # theta = [-1.01575681, -0.19002532, -0.05443981, 0.09605609, 0.16415831, -0.00205784, 0.00405411, 0.00217475, 0.00519341,
    #          0.00390873, 0.31140836, 0.08590223, 0.18611989, -0.25154623, 0.26859639, 0.08872846, 0.04026616, 0.01721728,
    #          0.01538795, -0.00243144, 0.01539683, -0.01631048, 0.00823702, -0.07188604, 0.04221205]

    # p不重置theta
    # theta = [-0.947811753254557, -0.1602734752309542, -0.03448030850601901, -0.005926564828329537, 0.1484914112222206,
    #          -0.0009167907050742148, -0.00044047889180056266, -0.0008603608454455753, -0.0010497972228475556,
    #          -0.0013690907990828963, -0.004879941649358138, 0.003607438592081519, -0.007032472427834018,
    #          0.003372239159058352, 0.00011472812084576332, -0.0002654366964989808, 0.004595917416402356,
    #          0.010732629284789675, 0.001118314301918791, -0.0012206028988971187, 0.005343735508116856, 0.003180975195237934,
    #          0.0039830257801174605, 0.008527858527091375, 0.0009007565552914656]

    # p重置 8月
    # theta = [-1.7028312516445685, -0.07480296496442014, 0.7220634732026288, 0.5982655166312942, -0.5426947732164331,
    #          3.074454800615896e-12, 0.0012091042997661502, 0.0026199396225510354, 0.002128107268327021,
    #          0.0007014104813494111, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    # print(len(theta))
    # theta = [-0.9029480111671384, -0.16503698879737178, -0.03424944594539166, 0.07284690911381228, 0.02938588806486347,
    #          -0.0014456847406357379, 0.002115590437710819, 0.0010846521986086497, 0.0008478601902866012,
    #          -0.002130105791762442, 0.012999753427970972, -0.05422752155261134, -0.015329473306421218, 0.2042414983329011,
    #          -0.21055033554233857, 0.040480245562364986, 0.03543423061205737, -0.024597124147032152, -0.022184427493531455,
    #          0.048293656763363814, -0.017177130563323994, 0.024175591833472104, 0.08195463940153712, 0.022963894800442405,
    #          0.026008763881279533]
    # print(theta)



    # print(y_k, y_output[19], y_k - y_output[19])

    start_item = max([d1, d2, d3, d4]) + 7
    end_item = len(df2.index) - start_item
    # end_item = 100

    # start_item = 20

    # y(k)--->  y_index_5 = start_item
    # y = [(y_output[start_item - 6]), (y_output[start_item - 5]), (y_output[start_item - 4]), (y_output[start_item - 3]),
    #      (y_output[start_item - 2])]

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
