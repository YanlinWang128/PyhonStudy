# 对于匹配好工况段
现阶段的思路:确定好边界索引,遍历每个工况段,求偏差,不满足条件的标记
```
if (abs(df2['UNIT2:THRPRESS'][i] - sequence_mean) > deviation):
df2.loc[i, 'deviation'] = 1 
```
标记完成后,最后选择(或取补集)完成数据筛选
```
df2 = df2[df2['deviation'] != 1]
```