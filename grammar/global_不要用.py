# @Time    : 2018/10/21 21:34
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : global_不要用.py


# 全局变量
a = 10


# 在函数内用global声明可以修改全局变量
# 这种方法太过于危险,不方便调试, 不用

def global_try():
    global a

    # 此时可修改 全局变量
    a = 20


print('调用之前a: ', a)
global_try()

print('调用之后a: ', a)
