# @Time    : 2018/9/26 9:33
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : Decimal.py


from decimal import Decimal, getcontext

"""
decimal  高精度浮点数运算

"""

a = Decimal('3.141592653')  # 浮点数,'  ' a = 2.1  Decimal(str(a))
b = Decimal('1.234567898')
getcontext().prec = 20  # 设置精度, 保留多少位小数

print(type(a * b))  # <class 'decimal.Decimal'>
print(a * b)  # eval() arg 1 must be a string, bytes or code object

d = Decimal(1) / Decimal(3)  # 整型
print(type(d), d)

result = str(d)  # to string
print(type(result), result)