# @Time    : 2018/10/8 11:06
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : Python_os.py

import os

dirpath = 'E:/xmind/'
"""
os.walk(dirpath) 返回一个三元组
    当前搜索目录,父目录
    子目录
    目录下的文件列表
"""
for parent, dir_names, file_names in os.walk(dirpath):
    for filename in file_names:  # 对目录下的所有文件进行操作
        print(os.path.join(parent, filename))

# for filename in os.listdir(dirpath):
#     print(os.path.join(dirpath, filename))