import numpy as np

# data = np.empty([3, 3])
# print(data)

# data = np.zeros([10, 5])
# print(data)

# data = np.ones([10, 5, 7])
# print(data)

# data = np.arange(7)
# print(data)


A = np.array([
    [1,6,-2]
    ])
B = np.array([
    [7,3,-2]
    ])
C = np.array([
    [1,6], 
    [5,7], 
    [8,-1]
    ])

# result = A+B
# print(result)

# result = A*B
# print(result)

# result = A==B
# print(result)

# result = A>=B
# print(result)

# result = A@C   #A.dot(C)
# print(result)

# result = np.outer(A, B)
# print(result)

#-------------
# result = C.sum()
# print(result)

# result = C.max()
# print(result)

# result = C.mean() #平均
# print(result)

# result = C.std() #標準差
# print(result)
#--------------

result = C.sum(axis=0)  #針對colume做總和
print(result)

result = C.sum(axis=1)  #針對row做總和
print(result)

result = C.cumsum()  #逐值累加
print(result)

result = C.cumsum(axis=0)  #針對colume做逐值累加
print(result)