import pandas as pd
pd1 = pd.DataFrame({'公司': ['斯托姆', '德尔塔', '福家聚'], '分数': ['60', '70', '80']})
pd2 = pd.DataFrame({'公司': ['斯托姆', '德尔塔', '内习升'], '股价': [50, 70, 120]})
print(pd1)
print(pd2)
pd3 = pd.merge(pd1, pd2, on='公司')  # 根据列名合并共有的内容
print(pd3)
pd4 = pd.merge(pd1, pd2, how='outer')  # 根据列名取并集的内容
print(pd4)
pd5 = pd.merge(pd1, pd2, how='left')  # 优先根据左边表的内容进行合并
print(pd5)
pd6 = pd.merge(pd1, pd2, how='right')  # 优先根据右边表的内容进行合并
print(pd6)
pd7 = pd.merge(pd1, pd2, left_index=True, right_index=True)  # 按照行索引进行合并
print(pd7)