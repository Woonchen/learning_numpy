import numpy as np
#資料的索引
# data = np.array([
#     [0,1],
#     [10,-5],
#     [2,6]
# ])
# print(data[1])
# print(data[1,0])

#資料的切片
data = np.arange(24).reshape(2,3,4)
print(data[...,0:2,3]) #...為全都要,冒號前面要冒號後面不要
