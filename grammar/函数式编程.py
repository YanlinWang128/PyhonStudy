# @Time    : 2018/10/6 16:18
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 函数式编程.py

# 函数式编程
"""
map,reduce,列表推导式
"""
# map(function, iter1, iter2...)
list1 = [-1, -3, 8, -7, 9, -2]
L1 = list(map(abs, list1))
print(L1)  # [1, 3, 8, 7, 9, 2]
L2 = list(map(lambda x: x + 1, list1))
print(L2)
L3 = list(map(lambda x, y: x * y, list1, list1))
print(L3)  # [1, 9, 64, 49, 81, 4]

# 命名规则
# print([object,...][,sep=' '][,end='\n'][, file = sys.stdout])
"""
默认地发送到标准输出流,然而发送到其它文件也是有用的
"""
data = open('data.txt', 'w')
print(L1, L2, L2, sep='---', file=data)
data.close()
print("hello, world!")
