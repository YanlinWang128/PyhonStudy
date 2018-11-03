# @Time    : 2018/10/25 10:38
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : mat_to_csv.py


import scipy.io
import pandas as pd

def mat_to_csv():
    features_struct = scipy.io.loadmat(r'C:/Users/Frank/Desktop/tongliu/y.mat')


    # print(features_struct)
    # 读取字典某列数据
    features = features_struct['y']

    # 注意: 未指定列名的数据, 默认标题是列索引号0, 该条数据,应该是标题, 需要加入columns指定
    dfdata = pd.DataFrame(features,  columns=['y'])
    list_temp = [x for x in range(201)]
    dfdata['a'] = list_temp

    print(dfdata)
    datapath1 = r'C:/Users/Frank/Desktop/tongliu/y.csv'
    # dfdata.to_csv(datapath1, index=False)

def add_df_line(df2):
    u = scipy.io.loadmat(r'C:/Users/Frank/Desktop/tongliu/u.mat')
    df2['u'] = u['u']
    return df2

def read_mat():
    u = scipy.io.loadmat(r'C:/Users/Frank/Desktop/tongliu/u.mat')
    y = scipy.io.loadmat(r'C:/Users/Frank/Desktop/tongliu/y.mat')
    print(u)
    print(y)
    dfdata = pd.DataFrame(y['y'], columns=['y'])
    dfdata['u'] = u['u']
    dfdata.to_csv(r'C:/Users/Frank/Desktop/tongliu/mat_data_1102.csv', index=False)

def read_mat_u1234_y():
    u1 = scipy.io.loadmat(r'C:/Users/Frank/Desktop/tongliu/u1.mat')
    u2 = scipy.io.loadmat(r'C:/Users/Frank/Desktop/tongliu/u2.mat')
    u3 = scipy.io.loadmat(r'C:/Users/Frank/Desktop/tongliu/u3.mat')
    u4 = scipy.io.loadmat(r'C:/Users/Frank/Desktop/tongliu/u4.mat')
    y = scipy.io.loadmat(r'C:/Users/Frank/Desktop/tongliu/y.mat')
    print(u1)
    print(y)
    dfdata = pd.DataFrame(y['y'], columns=['y'])
    dfdata['u1'] = u1['u1']
    dfdata['u2'] = u2['u2']
    dfdata['u3'] = u3['u3']
    dfdata['u4'] = u4['u4']
    dfdata.to_csv(r'C:/Users/Frank/Desktop/tongliu/mat_data_1102.csv', index=False)
if __name__ == '__main__':
    read_mat()
    # read_mat_u1234_y()

"""
读写 mat 格式数据(字典格式)

data = scipy.io.loadmat('matData.mat')  # 读取mat文件
# print(data.keys())   # 查看mat文件中的所有变量
print(data['matrix1'])
print(data['matrix2'])
matrix1 = data['matrix1'] 
matrix2 = data['matrix2']
print(matrix1)
print(matrix2)
scipy.io.savemat('matData2.mat',{'matrix1':matrix1, 'matrix2':matrix2})  # 写入mat文件


"""