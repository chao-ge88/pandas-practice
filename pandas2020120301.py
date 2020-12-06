import pandas as pd
df1 = pd.DataFrame({'公司': ['恒盛', '创锐', '快学'], '分数': ['60', '70', '80']})
df2 = pd.DataFrame({'公司': ['恒盛', '创锐', '京西'], '股价': [50, 70, 120]})
print(df1)
print(df2)
df3 = pd.merge(df1, df2, on='公司')  # 根据列名合并共有的内容
print(df3)
df4 = pd.merge(df1, df2, how='outer')  # 根据列名取并集的内容
print(df4)
df5 = pd.merge(df1, df2, how='left')  # 优先根据左边表的内容进行合并
print(df5)
df6 = pd.merge(df1, df2, how='right')  # 优先根据右边表的内容进行合并
print(df6)
df7 = pd.merge(df1, df2, left_index=True, right_index=True)  # 按照行索引进行合并
print(df7)
