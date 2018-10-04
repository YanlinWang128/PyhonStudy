# @Time    : 2018/9/30 11:50
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : Python_random.py

import random

# 随机生成一个[0,1)的浮点数 random(),不包括1
print("random():", random.random())
print("random():", round(random.random(), 3))  # 四舍五入保留三位小数 round(x, n)

# 随机生成一个[a, b]之间的整数  randint(a, b)
print("randint(1000, 9999):", random.randint(1000, 9999))

# 随机生成0-20之间的偶数
# randrange(start, stop[, step]) 生成一个[start, stop)之间以step为步数的随机整数
print("randrange(0, 21, 2):", random.randrange(0, 21, 2))

# 随机生成一个[a, b]之间的浮点数
print("uniform(0, 23):", random.uniform(0, 23))

# 从序列中随机返回一个元素
list_string = ['a', 'b', 'c', 'd', 'e']
print("choice(list):", random.choice(list_string))
print("choice(string):", random.choice('abcd'))

# 对序列元素进行随机排序
list_number = [1, 2, 3, 4, 5]
random.shuffle(list_number)
print(type(random.shuffle(list_number)))  # NoneType
print("shuffle(list):", list_number)  # 直接在原始列表中乱序,不返回值

# 从指定序列中随机获取k个元素,以列表类型返回
print("sample(sequence):", random.sample('abcdefg', 2))  # ['a', 'c']

# Python seed()方法
"""
1. seed() 函数指定随机数种子,默认是时钟,不必单独设置
2. 只要种子设置相同, 每次生成的随机数序列也相同. 这种情况便于测试和同步数据
"""

random.seed(10)
print("Random number with seed 10 : ", random.random())  # 0.5714025946899135

# 生成同一个随机数
random.seed(10)
print("Random number with seed 10 : ", random.random())  # 0.5714025946899135

# 生成同一个随机数
random.seed(10)
print("Random number with seed 10 : ", random.random())  # 0.5714025946899135
