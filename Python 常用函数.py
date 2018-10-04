# @Time    : 2018/9/30 15:25
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : Python 常用函数.py



# 内置函数
"""
    all() 函数一般针对组合数据类型,如果其中每个元素都是True,则返回True,否则返回False
    注: 整数0, 空字符串"", 空列表[]等都被当做是False
    
    any() 函数与all() 函数相反,只要组合数据类型中的任何一个是True, 则返回True
    全部元素都是False时返回False
    
    hash() 函数对于能够计算哈希的数据类型返回哈希值
    
    id() 对每个数据返回唯一编号,Python将数据存储在内存中的地址作为其唯一编号
    
    reversed() 返回输入组合数据类型的逆序形式
    
    sort() 对一个序列进行排序, 默认从小到大排序
    
    type() 返回数据类型
"""
ls = [1, 2, 5, 0]
print(all(ls))

print(any(ls))

print(hash("hello, China"))