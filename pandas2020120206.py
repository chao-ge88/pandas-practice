import pandas as pd
import numpy as np
data1 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['c1', 'c2', 'c3'], index=['r1', 'r2', 'r3'])
data2 = pd.DataFrame(np.arange(1, 10).reshape(3, 3), columns=['c1', 'c2', 'c3'], index=['r1', 'r2', 'r3'])
a = data1['c1']
b = data1[['c1']]
c = data1[['c1', 'c3']]
d = data1[0:4]
e = data1.iloc[0:1]
f = data1.iloc[-1]
g = data1.loc[['r2', 'r3']]
h = data1.head()  # 用于显示前五行数据
i = data1[['c1', 'c3']][0:2]  # 用于选取c1和c3列前两行数据，也可以写成data1[0:2][['c1','c3']]
j = data1.iloc[0:2][['c1', 'c3']]  # 官方推荐形式
k = data1.iloc[0]['c3']
p = data1.loc[['r1', 'r2'], ['c1', 'c3']]
m = data1.iloc[0:2, [0, 2]]
n = data1[data1['c1'] > 1]
o = data1[(data1['c1'] > 1) & (data1['c2'] == 5)]
q = data1.sort_values(by='c2', ascending=False)  # by指定用那一列排序，ascending（上升）默认升序，False为降序
r = data1['c3']-data1['c1']
s = 0
t = 0
print(f'\n{data1}')
print(f'\n{data2}')
print(f'\n{a}')
print(f'\n{b}')
print(f'\n{c}')
print(f'\n{d}')
print(f'\n{e}')
print(f'\n{f}')
print(f'\n{g}')
print(f'\n{h}')
print(f'\n{j}')
print(f'\n{k}')
print(f'\n{p}')
print(f'\n{m}')
print(f'\n{n}')
print(f'\n{o}')
print(f'\n{q}')
print(f'\n{r}')
print(f'\n{s}')
print(f'\n{t}')