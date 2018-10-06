# @Time    : 2018/10/5 13:57
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : set.py

x = set('aeiou')  # 字符集
y = set('abcde')
print(x, type(x), y, type(y))  # {'e', 'a', 'i', 'u', 'o'} <class 'set'> {'e', 'a', 'd', 'b', 'c'} <class 'set'>

"""
Python set 这是一些唯一的,不可变对象的一个无序集合,可变
    1. 这些对象支持与数学集合对应的操作
    2. 根据定义,一个项在集合中只能出现一次,不管它添加了多少次
    3. 集合:尤其在设计数字和数据库的工作中很好用
"""

# 集合相关操作
print('a' in x)  # True  membership
print(x - y)  # Difference 差集 {'i', 'o', 'u'}
print(x | y)  # Union 并集 {'a', 'o', 'i', 'c', 'd', 'u', 'e', 'b'}
print(x & y)  # Intersection 交集 {'a', 'e'}
print(x ^ y)  # Symmetric difference(XOR)  who is in one but not both

print(x > y, x < y)  # Superset, subset  超集,子集 False False

# 作为可迭代的容器, 集合也可以用于, len,for循环和列表解析式
for item in set('abc'):
    print(item * 3, end=" ")
print("\n")

# 集合常量
set1 = set([1, 3, 4, 5])  # {1, 3, 4, 5}
print(set1)
set2 = {1, 3, 5}

# 注意: 在Python中{}仍然是一个字典.空的集合
S = set()  # Initialize an empty set
S.add(1.23)
print(S, type(S))  # {1.23} <class 'set'>

# 集合的解析
set3 = {x * 4 for x in 'frank'}  # {'r', 'f', 'a', 'k', 'n'}
print(set3)

print(set3 | {'ffff', 'wwww'})  # 并集 {'ffff', 'aaaa', 'kkkk', 'nnnn', 'rrrr', 'wwww'}

# 集合的常用用法,为什么用集合
# 1. 可以用来把重复项过滤掉:直接转集合然后转回来即可,集合可迭代,list()对其有效
L = [1, 2, 1, 3, 5, 4, 3]
print(set(L))
L = list(set(L))  # 转为list类型
print(L)  # [1, 2, 3, 4, 5]

# 2. 当遍历图形或其他的回环结构的时候,集合可以用来记录已经访问过的位置

# 3. 在处理较大的数据集合的时候(如: 数据库查询结果)交集,并集,异或集
engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}

print('bob' in engineers)  # True Is bob an engineer?
print(engineers & managers)  # {'sue'} Who is both engineer and manager?
print(engineers | managers)  # All people in either category
print(engineers - managers)  # Engineers who are not managers
print(managers - engineers)  # Managers who are not engineers
print(engineers > managers)  # Are all managers engineers? (superset)
print({'bob', 'sue'} < engineers)  # Are both engineers? (subset)
print(managers ^ engineers)  # Who is in one but not both
