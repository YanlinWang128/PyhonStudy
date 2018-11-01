# @Time    : 2018/11/1 19:42
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 5.Numpy计算_元素智能.py

from time import clock
import numpy as np

start = clock()

# 1.基本运算
## 1.1 数组与标量
a = np.array([1, 2, 3, 4])
print(a + 1)  # [2 3 4 5]
print(2 ** a)  # 满足迭代,逐个元素进行运算 [ 2  4  8 16]

# 所有运算符都是元素智能的：
b = np.ones(4) + 1
print(a - b)  # [-1.  0.  1.  2.]
print(a * b)  # [2. 4. 6. 8.],  Numpy 中的乘是对应元素相乘, 不是矩阵乘法

c = np.ones((3, 3))
print(c * c)  # 对应相乘  [[1. 1. 1.], [1. 1. 1.], [1. 1. 1.]]
print(c.dot(c))  # 矩阵相乘 [[3. 3. 3.], [3. 3. 3.], [3. 3. 3.]]

# 比较运算 >=, ！=,
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print(a == b) # [False  True False  True]
print(a > b) # [False  True False  True]

if True in (a == b):
    print('hello')

# 逻辑运算：
a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
print(np.logical_or(a, b))
print(np.logical_and(a, b))


# 超越函数：
a = np.arange(5)
b = np.sin(a)
# c = np.log(a)
d = np.exp(a)
print(a, b, c, d)

# 转置
a = np.triu(np.ones((3, 3)), 1)   # see help(np.triu) 上三角矩阵
print(a)
print(a.T)  #   转置操作只产生数组的view a += a.T 错误
b = a.T.copy()
print(np.may_share_memory(a, b))  # False 检查是否共享内存
end = clock()
print('time: {:.8f}s'.format(end - start))

"""
Numpy 运算 --> 元素智能
所有运算符都是元素智能的
c.dot(c) 矩阵相乘
c * c 矩阵元素相乘

"""
"""
#  数值修约
numpy.around(a)：平均到给定的小数位数。 
numpy.round_(a)：将数组舍入到给定的小数位数。 
numpy.rint(x)：修约到最接近的整数。 
numpy.fix(x, y)：向 0 舍入到最接近的整数。 
numpy.floor(x)：返回输入的底部(标量 x 的底部是最大的整数 i)。 
numpy.ceil(x)：返回输入的上限(标量 x 的底部是最小的整数 i). 
numpy.trunc(x)：返回输入的截断值。


# 算数运算
numpy.log(x)：计算自然对数。 
numpy.log10(x)：计算常用对数。 
numpy.log2(x)：计算二进制对数。 
numpy.log1p(x)：log(1 + x)。
numpy.sqrt(x)：平方根。 
numpy.cbrt(x)：立方根。 

numpy.add(x1, x2)：对应元素相加。 
numpy.reciprocal(x)：求倒数 1/x。 
numpy.negative(x)：求对应负数。 
numpy.multiply(x1, x2)：求解乘法。 
numpy.divide(x1, x2)：相除 x1/x2。 
numpy.power(x1, x2)：类似于 x1^x2。 
numpy.subtract(x1, x2)：减法。 
numpy.fmod(x1, x2)：返回除法的元素余项。 
numpy.mod(x1, x2)：返回余项。 
numpy.modf(x1)：返回数组的小数和整数部分。 
numpy.remainder(x1, x2)：返回除法余数。

# 数学运算
numpy.fabs(x)：绝对值。 
numpy.sign(x)：符号函数。 
numpy.maximum(x1, x2)：最大值。 
numpy.minimum(x1, x2)：最小值。 
numpy.nan_to_num(x)：用 0 替换 NaN。 
numpy.interp(x, xp, fp, left, right, period)：线性插值。 

# 代数运算
numpy.linalg.eigvals(a)：计算矩阵的特征值。 
numpy.linalg.qr(a ,mode)：计算矩阵的 QR 因式分解。
numpy.linalg.det(a)：计算数组的行列式。 
numpy.linalg.inv(a)：计算逆矩阵。


numpy.linalg.cholesky(a)：Cholesky 分解。 
numpy.linalg.svd(a ,full_matrices,compute_uv)：奇异值分解。 
numpy.linalg.eig(a)：计算正方形数组的特征值和右特征向量。 
numpy.linalg.eigh(a, UPLO)：返回 Hermitian 或对称矩阵的特征值和特征向量。 
numpy.linalg.eigvalsh(a, UPLO)：计算 Hermitian 或真实对称矩阵的特征值。 
numpy.linalg.norm(x ,ord,axis,keepdims)：计算矩阵或向量范数。 
numpy.linalg.cond(x ,p)：计算矩阵的条件数。 
numpy.linalg.matrix_rank(M ,tol)：使用奇异值分解方法返回秩。 
numpy.linalg.slogdet(a)：计算数组的行列式的符号和自然对数。 
numpy.trace(a ,offset,axis1,axis2,dtype,out)：沿数组的对角线返回总和。 
numpy.linalg.solve(a,b)：求解线性矩阵方程或线性标量方程组。 
numpy.linalg.tensorsolve(a,b ,axes)：为 x 解出张量方程a x = b 
numpy.linalg.lstsq(a,b ,rcond)：将最小二乘解返回到线性矩阵方程。 
numpy.linalg.pinv(a ,rcond)：计算矩阵的（Moore-Penrose）伪逆。 
numpy.linalg.tensorinv(a ,ind)：计算N维数组的逆。 


"""