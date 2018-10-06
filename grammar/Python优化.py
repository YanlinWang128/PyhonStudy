# @Time    : 2018/10/6 20:06
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : Python优化.py

a = 10
# 增强语句
"""
增强语句,a只出现1次,只需计算一次,更加快速
"""
a += 10
print(a)

# 列表解析 比手动的for循环语句运行的快很多,列表解析的迭代在解释器内部以C语言执行

# 使用满足迭代协议 的方法: map,zip,filter迭代器
