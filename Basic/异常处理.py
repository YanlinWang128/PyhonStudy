# @Time    : 2018/9/30 12:40
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : 异常处理.py

try:
    alp = "abcdefghijklmnopqrstuvwxyz"
    idx = eval(input("Please enter an integer:  "))
    print(alp[idx])
except NameError:   # NameError, 用户输入非整数字符时
    print("INPUT ERROR, NOT AN INTEGER")
except:   # 其他错误,比如超过范围
    print("INPUT ERROR")
else:
    print("没有发生异常")
finally:
    print("程序执行完毕,不知道发生了异常没有")


"""
try-except 一般只用来检测极少发生的情况,或者未知情况

一般情况,如索引是否超过范围,在程序里面用if直接判断即可

try-except语句会影响代码可读性,会增加代码维护难度,在关键地方使用即可

"""

