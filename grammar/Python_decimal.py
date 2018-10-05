# @Time    : 2018/9/26 9:33
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : Decimal.py


from decimal import Decimal, getcontext

"""
decimal  高精度浮点数运算用这个
区别于round（float [,n]）函数用于返回浮点数四舍五入后的值，小数点后保留n位（默认为0）
    1.round()有一个缺陷,并不是严格的四舍五入, 5 会被舍弃
    2.当保留n位时，第n+1位为数字5，此时它并不会进一位，而是舍弃掉。


四舍五入是基于十进制的，在二进制无法精确表示的时候是会有误差的。
任何需要十进制运算的地方，都需要用 decimal.Decimal 取代 float：
    >>> Decimal(1.45)
    Decimal('1.4499999999999999555910790149937383830547332763671875')
    >>> Decimal('1.45')
    Decimal('1.45')
    >>> Context(prec=2, rounding=ROUND_HALF_UP).create_decimal('1.45')
    Decimal('1.5')
    >>> Decimal('1.45').normalize(Context(prec=2, rounding=ROUND_HALF_UP))
    Decimal('1.5')
    >>> Decimal(Decimal('1.45').quantize(Decimal('.1'), rounding=ROUND_HALF_UP))
    Decimal('1.5')
不过使用十进制运算的代价就是慢
"""

a = Decimal('3.141592653')  # 浮点数,'  ' a = 2.1  Decimal(str(a))
b = Decimal('1.234567898')

# 设置全局精度
getcontext().prec = 20  # 设置精度, 保留多少位小数

print(type(a * b))  # <class 'decimal.Decimal'>
print(a * b)  # eval() arg 1 must be a string, bytes or code object

d = Decimal(1) / Decimal(3)  # 整型
print(type(d), d)  # <class 'decimal.Decimal'> 0.33333333333333333333

result = str(d)  # to string
print(type(result), result)  # <class 'str'> 0.33333333333333333333

# 分数与小数
"""
b = Fraction('1.25')
decimal.Decimal(str(1/3))  # 字符串输入
"""
