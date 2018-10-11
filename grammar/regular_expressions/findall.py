# @Time    : 2018/10/11 11:44
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : findall.py
import re
import os

print(int(re.findall(r'p(\d+).csv', '160901000000_160930235959_181008143619_p1.csv')[0]))
# print(re.match(r'p(\d+).csv', '160901000000_160930235959_181008143619_p1.csv').group())

list1 = [7, -8, 5, 4, 0, -2, -5]
# 要求1.正数在前负数在后 2.整数从小到大 3.负数从大到小
# 解题思路：先按照正负排先后，再按照大小排先后。
list1.sort(key=lambda x: (x < 0, abs(x)))

print(list1)

path = r'F:/HistoryData/09newprocess/'
file_list = os.listdir(path)
print(file_list)
file_list.sort(key=lambda items: int(re.findall(r'p(\d+).csv', items)[0]))
