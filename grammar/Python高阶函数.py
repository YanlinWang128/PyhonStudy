# @Time    : 2018/10/21 21:51
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : Python高阶函数.py

import os
import re

# 把函数作为参数传入，这样的函数称为高阶函数
# 函数式编程就是指这种高度抽象的编程范式


# sort(), sorted() 是高阶函数,可以传入函数参数, 自定义排序规则
path = r'F:/HistoryData/09newprocess/'

# 文件目录下必须都满足正则搜索, 不能有其它类型文件或者文件夹
# os.listdir(path) 会搜索出文件夹名
file_list = sorted(os.listdir(path), key=lambda items: int(re.findall(r'p(\d+).csv', items)[0]))
# print(os.listdir(path))
