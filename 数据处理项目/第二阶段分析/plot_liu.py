# @Time    : 2018/10/24 16:06
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : plot_liu.py

import numpy as np
import pandas as pd
import scipy
from scipy import io
import matplotlib.pyplot as plt


def column_plot_liu():
    input_file = r'C:/Users/Frank/Desktop/HDL181016_160904.csv'
    df2 = pd.read_csv(input_file, header=0)

    print(df2.columns.values.tolist())

    y = df2['tongliu'].tolist()

    plt.plot(y, color='blue', linewidth=2)

    plt.title('tongliu')
    plt.show()


def mat_to_csv():
    features_struct = scipy.io.loadmat(r'C:/Users/Frank/Desktop/tongliu/y.mat')
    print(features_struct)
    features = features_struct['y']
    dfdata = pd.DataFrame(features)
    datapath1 = r'C:/Users/Frank/Desktop/tongliu/y.csv'
    dfdata.to_csv(datapath1, index=False)


if __name__ == '__main__':
    # input_file = r'C:/Users/Frank/Desktop/tongliu/u.csv'
    # df2 = pd.read_csv(input_file, header=0)
    # df2['u2_difference'] = (df2["u2"] - (df2["u2"].shift(1))).shift(-1)

    # a = ([1, -1] * 101)[:-1]
    # print(len(a), a)
    a = [1, 2, 3, 4, 5,6, 7, 8, 9]
    print(a)
    print(a[::-1])

    print(a[-5::-1])
    print(a[8: 1:-1])
    print(a[8: 0:-1])
    print(a[8: 2:-1])


    print(a[1:8])
