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
print(f'\n{data1}')
print(f'\n{data2}')
print(f'\n{a}')
print(f'\n{b}')
print(f'\n{c}')
print(f'\n{d}')
print(f'\n{e}')
print(f'\n{f}')