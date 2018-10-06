# @Time    : 2018/10/5 12:16
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 数字类型.py

# 浮点数 默认float类型

# 进制
print(hex(78))  # 0x4x
print(oct(78))  # 0o116
print(int(78.8))  # 78
print(bin(64))  # 0b1000000

# eval() 解析字符串,将字符串作为Python代码解析
print(eval('64'))
print(eval('0o100'))
print(eval('0x40'))
print(eval('0b1000000'))  # 二进制

# 二进制的位数 X.bit_length(); len(bin(X)) -2 减去0b标头
# 其中 X.bit_length() 方法 计算效率最高
X = 100
print(X, bin(X), X.bit_length(), len(bin(X)) - 2)  # 100 0b1100100 7 7

# 内置函数pow(),指数表达式**,计算n方和方根
print(pow(5, 2), pow(5, 0.5))
print(5 ** 2, 5 ** 0.5)
