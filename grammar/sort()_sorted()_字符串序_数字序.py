# @Time    : 2018/10/11 12:48
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : sort()_sorted()_字符串序_数字序.py


import os
import re

path = r'F:/HistoryData/09newprocess/'
file_list = sorted(os.listdir(path), key=lambda items: int(re.findall(r'p(\d+).csv', items)[0]))
