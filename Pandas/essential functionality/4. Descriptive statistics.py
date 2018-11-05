# @Time    : 2018/11/5 13:27
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 4. Descriptive statistics.py

from time import clock
import pandas as pd
import numpy as np

start = clock()
"""
skew()   # 样本偏度
kurt()  # 样本峰度
var() 
std() 
cov() 无偏协方差
corr()  相关性系数
"""
# dataframe 统计方法 基于没有缺失数据的假设而构建的, 需要处理空白值
"""
mad = lambda x: np.fabs(x - x.mean()).mean()


"""


df = pd.DataFrame({'one': pd.Series(np.random.randn(100)),
                   'two': pd.Series(np.random.randn(100)),
                   'three': pd.Series(np.random.randn(100))})
# 均值: mean(), 默认参数0, 按列, 1, 按行
print(df.mean(0), df['one'].mean())  # df.mean(1)

# sum() 默认列,  skipna= True 默认跳过非数
print(df.sum(0, skipna=False))  # df.sum(axis=1, skipna=True)

# 区别于Numpy的标准差, pandas的std(), 默认是无偏估计(n-1)
print(df.std(0))  # df.std(1)


# Numpy计算 某列 数据
mean1 = np.mean(df['one'])
statistic = df.describe(percentiles=[.05, .25, .75, .95])
print(statistic)
# 常用方法
"""
min, max, var , abs, median,


count Number of non-NA observations
sum Sum of values
mean Mean of values
mad Mean absolute deviation
median Arithmetic median of values
min Minimum
max Maximum
mode Mode
abs Absolute Value
prod Product of values
std Bessel-corrected sample standard deviation
var Unbiased variance
sem Standard error of the mean
skew Sample skewness (3rd moment)
kurt Sample kurtosis (4th moment)
quantile Sample quantile (value at %)
cumsum Cumulative sum
cumprod Cumulative product
cummax Cumulative maximum
cummin Cumulative minimum


"""

end = clock()
print('time: {:.8f}s'.format(end - start))
