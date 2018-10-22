# @Time    : 2018/10/22 10:47
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : Python_generator生成器.py


"""
通过列表生成式，我们可以直接创建一个列表。
但是，受到内存限制，列表容量肯定是有限的。
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。


通过生成器
就不必创建完整的list，从而节省大量的空间


在Python中，这种一边循环一边计算的机制，称为生成器（Generator）

生成器有很多种创建方法
1. 只要把一个列表生成式的[]改成()
2. 使用了 yield 的函数被称为生成器（generator）
    跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作
    
    在调用生成器运行的过程中
    每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值
    并在下一次执行 next() 方法时从当前位置继续运行


迭代器保存的是算法,每次调用__next__，计算出下一个值,没有下一个,抛出StopIteration的错误。
"""

L = [x * x for x in range(10)]
print(type(L), L)

g = (x * x for x in range(10))
print(type(g), g)  # <class 'generator'> <generator object <genexpr> at 0x0000020A11858780>

"""
    print(g.__next__())  # 0
    print(g.__next__())  # 1 需要逐个迭代, 一般我们用for循环来迭代
"""
# 用for循环来迭代, 用生成器来写算法, 避免列表推导式占用很大内存
for n in g:
    print(type(n), n)


# yield b 中断,返回后面的值
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
