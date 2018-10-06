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

str.rstrip()    去除右侧空白字符, 用于去除文本末尾换行符

str.upper()  字符串转大写

str.startwith()
str.endwith()

str .find('str')   # Find  the offset of a substring, return index
hex()
oct()
str.zfill()   字符串填充
ASCII码与值 ord(), chr()
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

# 切片 和切片对象等同  S[1:3]==S[slice(1, 3)]
print("hello"[0::2])  # 右侧不包括,  index from 0 to -1
print("hello"[::-1])  # olleh 步长为-1 表示切片会从右往左输出, 字符串反转
print("helloha"[5:1:-1])  # holl 步长为-1 表示切片会从右往左输出, 右侧不包括

# 字符串格式化
print('%d,eggs, and %s' % (1, 'spam!'))

# ASCII码与值 ord(), chr()
print(ord('A'), chr(65))  # 65

# 三行引用编写多行字符串块,或注释
print('---' * 20)
str1 = """hello,
world,
Python
"""
print(str1)

# 原始(raw)字符串抑制转义  r'D:\Frank\Videos'
"""myfile = open(r'D:\nk\Videos', w)  抑制转义字符'\n'"""

# 字符串操作之 偏移替换
Xstring = 'xxxxSPAMxxxxSPAMxxxx'
where = Xstring.find('SPAM')
Xstring = Xstring[:where] + 'Python' + Xstring[(where + 4)]

# join 字符串方法join(), 将列表合并成一个字符串
L = ['a', 'b', 'c']  # 字符列表,可以合并成字符串, 数字列表不可以
S = ''.join(L)
print(S)
S = 'wyl'.join(L)  # 字符串中间填充拼接
print(S)
