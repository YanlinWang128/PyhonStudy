# @Time    : 2018/9/26 10:38
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : string.py

string1 = 'hello,world,frank'
# 字符串不可变性
"""
常用string操作 + *
split(',')   len(str)
'he' in str
原始字符串:  r'D:\Frank\Videos'

"""

"""
字符串以Unicode编码存储,因此,字符串的英文字符和中文字符都算作1个字符
split(sep = None, maxsplit = -1)  字符串分割,返回一个列表

str.replace(old,new[,count])  字符串替换前count次
str.encode('utf-8')  # 设置编码
for x in str: print(X) # 迭代,成员关系
'spam' in S
[c * 2 for c in str]
map(ord, S)

str.strip([chars])   字符串格式化,在其左侧和右侧去掉chars中列出的字符

str.rstrip()    去除右侧空白字符

str.upper()  字符串转大写

str.startwith()
str.endwith()

str .find('str')   # Find  the offset of a substring, return index
hex()
oct()
str.zfill()   字符串填充
"""
# split(sep = None, maxsplit = -1) 默认按照空格分割字符, 可指定分割个数
print(string1.split(','))
print("-----" * 20)

## integer convert to bignumber
"""
Python3中的整数类型会自动提供额外的精度
    例如,可以打印 2的100000000次方
    
print(len(str(2 ** 1000000)))  # 301030
"""

# 切片
print("hello"[0::2])  # 右侧不包括,  index from 0 to -1

# 字符串格式化
print('%s,eggs, and %s' % ('spam', 'spam!'))

# 显示字符的ASCII值
print(ord('A'))  # 65

# 三行引用编写多行字符串块,或注释
print('---' * 20)
str1 = """hello,
world,
Python
"""
print(str1)

# 原始(raw)字符串抑制转义  r'D:\Frank\Videos'
"""myfile = open(r'D:\nk\Videos', w)  抑制转义字符'\n'"""


