import numpy as np

#觀察資料的形狀
# data = np.zeros(10)
# print(data.shape)

#資料的轉置
# data = np.array([
#     [1,6,-3], 
#     [7,-7,2]
# ])
# print(data)
# print(data.T)
# print(data.shape)
# print(data.T.shape)

#重塑資料形狀、扁平化資料
# data = np.arange(10)
# newdata = data.reshape(2,5)
# print(newdata)
# print(newdata.ravel())

#常用的初始化矩陣
# data = np.zeros(120).reshape(4,2,53)
# print(data)
# print(data.shape)

data = np.arange(9).reshape(3,3)
print(data)
print(data.T)
