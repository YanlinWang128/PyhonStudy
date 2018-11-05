# @Time    : 2018/11/5 11:02
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : shite.py

from time import clock

start = clock()


"""
y = s - s.shift(1) # 行移位 
df.p['xx_1'] = df.p["xx"].shift(1) # 向下移动一位
df.p['xx'] - df.p["xx_1"]

"""

end = clock()
print('time: {:.8f}s'.format(end - start))