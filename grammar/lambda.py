# @Time    : 2018/9/30 13:17
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : lambda.py

f = lambda x, y: x + y
"""
lambda 函数(lambda表达式) 用于定义简单的,能够在一行内表示的函数
返回一个函数类型
"""
print(type(f))
print(f(10, 20))
