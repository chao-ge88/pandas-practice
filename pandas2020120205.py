import pandas as pd
import numpy as np

s = pd.Series(['丁一', '王二', '张三'])
print(s)

a = pd.DataFrame([[1, 2], [3, 4], [5, 6]])
print(f'\n{a}')

b = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['date', 'score'], index=['A', 'B', 'C'])
print(f'\n{b}')

c = pd.DataFrame()
data = [1, 3, 5]
score = [2, 4, 6]
c['data'] = data
c['score'] = score
print(f'\n{c}')

d = pd.DataFrame({'a': [1, 3, 5], 'b': [2, 4, 6]}, index=['x', 'y', 'z'])
print(f'\n{d}')

e = pd.DataFrame.from_dict({'a': [1, 3, 5], 'b': [9, 8, 7]}, orient='index')
print(f'\n{e}')

a = np.arange(12).reshape(3, 4)
f = pd.DataFrame(a, index=[1, 2, 3], columns=['班级', '姓名', "学号", '分数'])
print(f'\n{f}')

g = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['date', 'score'], index=['A', 'B', 'C'])
g.index.name = '公司'
print(f'\n{g}')

h = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['date', 'score'], index=['A', 'B', 'C'])
h.index.name = '公司'
h = h.rename(index={'A': '万科', 'B': '阿里', 'C': '百度'}, columns={'date': '日期', 'score': '分数'})
print(f'\n{h}')
