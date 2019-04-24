import numpy as np

'''
保存数组
'''
one = np.array([1,2,3])
two = np.array([(1.5,2,3),(4,5,6)],dtype=float)
three = np.array([[(1.5,2,3),(4,5,6)],[(3,2,1),(4,5,6)]],dtype=float)

#保存数组为二进制文件，格式为npy
#np.save("datas/array3D",three)
#保存多个数组，格式npz，未压缩
#np.savez("datas/arraysNPZ",one,two)
#savetxt: ValueError: Expected 1D or 2D array, got 3D array instead
#np.savetxt("datas/saveastxt.txt",two,delimiter="\t")
'''
加载数组
'''
#加载npy，npz
loadresult = np.load("datas/array3D.npy")
print(loadresult)
loadtxt = np.loadtxt("datas/test.txt")
print(loadtxt)
loadcsv = np.genfromtxt("datas/excel.csv",delimiter=",")
print(loadcsv)