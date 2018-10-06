# @Time    : 2018/10/6 16:18
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 函数式编程.py

# 函数式编程
"""
map,reduce,列表推导式, lambda表达式
map() 可以用来模拟for循环
"""
# map(function, iter1, iter2...)
list1 = [-1, -3, 8, -7, 9, -2]
L1 = list(map(abs, list1))
print(L1)  # [1, 3, 8, 7, 9, 2]
L2 = list(map(lambda x: x + 1, list1))
print(L2)
L3 = list(map(lambda x, y: x * y, list1, list1))
print(L3)  # [1, 9, 64, 49, 81, 4]

# 基于布尔表达式的运作方式
"""
1. 布尔表达式 not, and, or 
2. ((A and B) or C) 几乎可以用以用来模拟 if/else 语句
"""

# if/else 三元表达式
# Y if X else Z  在X为真时会返回Y,否则返回Z
# 对应 ((X and Y) or Z)

# 列表解析 比手动的for循环语句运行的快很多,列表解析的迭代在解释器内部以C语言执行








# 命名规则
# print([object,...][,sep=' '][,end='\n'][, file = sys.stdout])
"""
默认地发送到标准输出流,然而发送到其它文件也是有用的
"""
data = open('data.txt', 'w')
print(L1, L2, L2, sep='---', file=data)
data.close()
print("hello, world!")
