# @Time    : 2018/11/2 17:53
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : sa.py

from time import clock

start = clock()
y = [ i for i in range(5+1, 1, -1)]
print(y)
end = clock()
print('time: {:.8f}s'.format(end - start))