# @Time    : 2018/10/5 12:52
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : Python_fractions.py

from fractions import Fraction

# 分数类型,更精确
# 浮点数是有精度概念的
print(1 / 3)  # 0.3333333333333333

x = Fraction(1, 3)
y = Fraction(4, 6)

print(x + y, type(x + y))  # 1 <class 'fractions.Fraction'>
print(x * y, type(x * y))  # 2/9 <class 'fractions.Fraction'>

print(x, type(x))

print("---" * 20)
# 分数也可以通过浮点数来创建
a = Fraction('.25')
b = Fraction('1.25')

print(a, type(a))
print(a + b, type(a + b))

# Fraction,float,int  convert
print(str(0.25678))  # 0.25678 string

# Fraction + int -> Fraction
print(x + 2, type(x + 2))  # 7/3 7/3 <class 'fractions.Fraction'>
# Fraction + float -> float
print(x + 2.0, type(x + 2.0))  # 2.3333333333333335 <class 'float'>
