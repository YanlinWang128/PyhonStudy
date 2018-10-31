# @Time    : 2018/10/31 10:04
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 切片.py



list = [i for i in range(100)]
print(len(list))

list_1 = list[80:2:-1]
print(len(list_1))
# 逆序输出
list_reverse = list[::-1]
print(list_reverse)


"""

# 注意切片要点
# 1. 索引左闭右开, 无论大小关系
# 2. 负号表示 从右侧往左侧读取

"""
