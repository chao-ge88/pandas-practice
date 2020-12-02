import numpy as np
a = [1, 2, 3, 4]
b = np.array([1, 2, 3, 4])
print(a)
print(b)
print(type(a))
print(type(b))
print(a[1])
print(b[1])
print(a[0:2])
print(b[0:2])
c = a*2
d = b*2
print(c)
print(d)

a = [[1, 2], [3, 4], [5, 6]]  # 大列表里面嵌套小列表
f = np.array([[1, 2], [3, 4], [5, 6]])  # 创建二维数组的一种方式
print(a)
print(f)

x = np.arange(5)  # 1个参数：起点默认值0，步长取默认值1，左闭右开
y = np.arange(5, 10)  # 2个参数：第1个参数为起点，第二个参数为终点，步长取默认值1，左闭右开
z = np.arange(5, 10, 2)  # 3个参数：第1个参数为起点，第2个参数为终点，第2个参数为步长，左闭右开
print(x)
print(y)
print(z)

c = np.random.randn(3)  # 服从正态分布的3个随机数
print(c)

d = np.arange(12).reshape(3, 4)  # 12个整数生成3行4列的两维数组
print(d)

e = np.random.randint(0, 10, (4, 4))  # 起点0终点10生成4行4列二维数组
print(e)