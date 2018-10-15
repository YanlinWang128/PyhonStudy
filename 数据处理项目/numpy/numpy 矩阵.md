#numpy 矩阵常用操作(array 下标从0开始)

### 矩阵的创建
#### 特殊矩阵的创建
ones创建全1矩阵 
zeros创建全0矩阵 
eye创建单位矩阵 
```
ones、zeros、eye、empty 
ones创建全1矩阵 
zeros创建全0矩阵 
eye创建单位矩阵 
empty创建空矩阵（实际有值）

zeros_like（a）函数创建一个和a形状相同，并且元素全部为0的数组。
a_ones = np.ones((3,4)) # 创建3*4的全1矩阵
a_eye = np.eye(3) # 创建3阶单位矩阵
a_empty = np.empty((3,4)) # 创建3*4的空矩阵 
a_diag = np.diag([1, 3, 5,7]) # 创建对角矩阵
```
### 创建指定格式的矩阵  读列表: reshape(x, y)
```
A.shape = (3,4)


a = arrange(6)  # 从0开始,返回数组  [0 1 2 3 4 5]
a = arange(15).reshape(3, 5)
print(a)
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
print(a.shape)  # (3, 5)

一个常见的错误包括用多个数值参数调用array而不是提供一个由数值组成的列表作为一个参数。
a = array(1,2,3,4)    # WRONG
a = array([1,2,3,4])  # RIGHT 

```
## 矩阵创建案例
```
python中随机生成10-99的整数，构成一个5×5的矩阵, 然后求转置

import numpy as np
import random

# i, j  是 python的 行列参数,列表推导式
before = np.array([[random.randint(10, 99) for i in range(5)] for j in range(5)])
result = before.T
print(result)
```

##  np.mean与np.average的区别在于average可以进行加权求和
# 矩阵的赋值 b[0] = 2,  b = 2
给矩阵元素同一赋值, b = 2
x = np.zeros((6,6))
T = np.full(x.shape,3)


T  = np.full((25, 25), 5)
```python
import numpy as np
a=np.array([1,2,3])
b=a
b[0]=11  # [11  2  3]  # 不用共享索引

b=a.copy()  # 深度拷贝,用这个处理数据
```
# 数组的深度复制
```
这个复制方法完全复制数组和它的数据
 d = a.copy()  
```
### 常用矩阵运算符(常规运算符求的是每个运算符对应操作)
+	矩阵对应元素相加
-	矩阵对应元素相减
*	矩阵对应元素相乘
/	矩阵对应元素相除，如果都是整数则取商
%	矩阵对应元素相除后取余数
**	矩阵每个元素都取n次方，如**2：每个元素都取平方


### 矩阵点乘
* matlab中:
矩阵点乘:矩阵对应位置的数进行相乘
矩阵乘法:矩阵相乘 


python中的a1*a2相当于matlab中的a1.*a2
Python中的 点乘(dot)就时matlab中的乘法, 数学矩阵相乘
 a1.dot(a2)相当于matlab中的a1*a2
 
* 常用矩阵函数
np.sin(a)	对矩阵a中每个元素取正弦,sin(x)
np.cos(a)	对矩阵a中每个元素取余弦,cos(x)
np.exp(a)	对矩阵a中每个元素取指数函数,ex
np.sqrt(a)	对矩阵a中每个元素开根号√x


# 数学矩阵相乘a.dot(b)
a1 = np.array([[1,2,3],[4,5,6]]) # a1为2*3矩阵
a2 = np.array([[1,2],[3,4],[5,6]]) # a2为3*2矩阵
print(a1.dot(a2)) # 结果还是一个矩阵


## 矩阵转置
print(a.transpose())
print(a.T)

## 矩阵的逆(需要导入numpy.linalg)
```python
import numpy as np
import numpy.linalg as lg


a = np.eye(3) # 3阶单位矩阵
print(lg.inv(a)) # 单位矩阵的逆为他本身

b = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(lg.inv(b))

```

## 矩阵信息获取
### 矩阵求和
```
矩阵求和的函数是sum()，可以对行，列，或整个矩阵求和
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.sum())           # 对整个矩阵求和,结果 21
print(a.sum(axis=0)) # 对行方向求和,结果 [5 7 9]
print(a.sum(axis=1)) # 对列方向求和,结果 [ 6 15]
```

### 最大最小值 
```python
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.max()) #获取整个矩阵的最大值 结果： 6
print(a.min()) #结果：1

# 可以指定关键字参数axis来获得行最大（小）值或列最大（小）值
# axis=0 行方向最大（小）值，即获得每列的最大（小）值
# axis=1 列方向最大（小）值，即获得每行的最大（小）值
# 例如
print(a.max(axis=0))# 结果为 [4 5 6]
print(a.max(axis=1))# 结果为 [3 6]

# 要想获得最大最小值元素所在的位置，可以通过argmax函数来获得
print(a.argmax(axis=1))# 结果为 [2 2]
```
### 平均值 
```python
#获得矩阵中元素的平均值可以通过函数mean()
#同样地，可以获得整个矩阵、行或列的平均值。
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.mean()) #结果为： 3.5

# 同样地，可以通过关键字axis参数指定沿哪个方向获取平均值
print(a.mean(axis=0)) # 结果 [ 2.5  3.5  4.5]
print(a.mean(axis=1)) # 结果 [ 2.  5.]
```

### 方差,标准差
```
方差的函数为var(), 标准差函数 std()
方差函数var()相当于函数mean(abs(x - x.mean())**2),其中x为矩阵。
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.var()) # 方差, 结果 2.91666666667
print(a.std()) # 标准差

print(a.var(axis=0)) # 结果 [ 2.25  2.25  2.25]
print(a.var(axis=1)) # 结果 [ 0.66666667  0.66666667]
```

### 累积和
```
某位置累积和指的是该位置之前(包括该位置)所有元素的和。
例如序列[1,2,3,4,5]，其累计和为[1,3,6,10,15]，即第一个元素为1，第二个元素为1+2=3，……，第五个元素为1+2+3+4+5=15。
矩阵求累积和的函数是cumsum()，可以对行，列，或整个矩阵求累积和。
import numpy as np

a = np.array([[1,2,3],[4,5,6]])

print(a.cumsum())            # 对整个矩阵求累积和
# 结果 [ 1  3  6 10 15 21]

print(a.cumsum(axis=0))  # 对行方向求累积和
# 结果
[[1 2 3]
 [5 7 9]]

print(a.cumsum(axis=1))  # 对列方向求累积和
# 结果
[[ 1  3  6]
 [ 4  9 15]]
```