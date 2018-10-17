# @Time    : 2018/10/16 10:52
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : aa.py

def f(m , n):
    if m == 0 : return n+1
    elif n==0: return f(m-1,1)
    else:return f(m-1, f(m, n-1))
print(f(3,3))