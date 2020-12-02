import pandas as pd
import time

start = time.time()
data = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['A列', 'B列'])  # 创建一个DataFrame
#  sheet_name用于指定工作表名称，columns用于指定要写入的列，index是否需要行索引信息，encoding用于指定编码方式
data.to_excel(r'C:\Users\Administrator\Desktop\data1.xlsx', sheet_name='20201130学习日报',
              columns=['A列'], index=False, encoding='utf-8')
end = time.time()
times = end - start
print('运行时间为%.8f' % times)