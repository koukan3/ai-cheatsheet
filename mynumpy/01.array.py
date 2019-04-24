import numpy as np
from numpy import  random as rd

print("====维度:1D,2D,3D====")
one = np.array([1,2,3])
print(one)
two = np.array([(1.5,2,3),(4,5,6)],dtype=float)
print(two)
three = np.array([[(1.5,2,3),(4,5,6)],[(3,2,1),(4,5,6)]],dtype=float)
print(three)
print("====填充====")
#填充0
print(np.zeros((3,4),dtype=int))
#填充1
print(np.ones((2,3,4),dtype=np.int16))
#填充指定值
print(np.full((2,3),7))
# 2D,n行n列,对角线为1,其他为0
print(np.eye(3))
#x行y列随机数
print(rd.random((2,3)))
#随机
print(np.empty((3,2)))
#前闭后开步长填充
print(np.arange(10,25,3))
#等区间切分
print(np.linspace(0,10,4))

