import pandas as pd
df1 = pd.DataFrame({'公司': ['恒盛', '创锐', '快学'], '分数': ['60', '70', '80']})
df2 = pd.DataFrame({'公司': ['恒盛', '创锐', '京西'], '股价': [50, 70, 120]})
print(df1)
print(df2)
df3 = pd.concat([df1, df2], axis=0)  # 全连接的形式进行拼接，不需要对其，直接合并，参数axis制定连结轴向，0为按行纵向拼接
print(df3)
df4 = pd.concat([df1, df2], ignore_index=True)  # 忽略原有索引
print(df4)
df5 = pd.concat([df1, df2], axis=1)  # 按列横向拼接
print(df5)
df6 = df1.append(df2)  # 类似concat函数的纵向拼接
print(df6)
df7 = df1.append({'公司': '腾飞', '分数': '90'}, ignore_index=True)  # 新增元素，需要设置ignore_index参数为真忽略原索引
print(df7)
df8 = df2.append({'公司': '翱翔', '股价': '200'}, ignore_index=True)  # 练习添加元素
print(df8)

