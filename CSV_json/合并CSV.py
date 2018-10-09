# @Time    : 2018/10/9 19:19
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 合并CSV.py


import pandas as pd
import os


def csv_merge(path, save_file_name):
    """
    合并目录下所有同类型CSV文件
    :param path: 目标路径
    :param save_file_name: 合并完成后, 保存的文件名
    :return: 
    """
    # 将该文件夹下的所有文件名存入一个列表  
    file_list = os.listdir(path)
    # 读取第一个CSV文件并包含表头  
    df = pd.read_csv(os.path.join(path, file_list[0]), encoding='gbk')  # 带中文的话, 编码格式改成gbk
    # 将读取的第一个CSV文件写入合并后的文件保存  
    df.to_csv(os.path.join(path, save_file_name), encoding="gbk", index=False)

    # 循环遍历列表中各个CSV文件名，并追加到合并后的文件  
    for i in range(1, len(file_list)):
        df = pd.read_csv(os.path.join(path, file_list[i]), encoding='gbk')
        df.to_csv(os.path.join(path, save_file_name), encoding="gbk", index=False, header=False, mode='a+')


if __name__ == "__main__":
    save_file_name = r'all.csv'  # 合并后要保存的文件名  
    path = r'D:/test/'
    csv_merge(path, save_file_name)


"""
# for filename in os.listdir(path):   # 获取绝对路径
#     print(os.path.join(path,filename))

FileNotFoundError: File b'160801000000_160831235959_181008135719_p1.csv' does not exist
错误原因: 文件如果不在project中,需要加绝对路径
file_list = os.listdir(r'D:/test/')
df = pd.read_csv(file_list[0])
"""
