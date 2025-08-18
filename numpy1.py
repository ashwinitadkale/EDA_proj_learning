import numpy as np 
# arr=np.array([1,2,3])
# mat=np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(mat)
# zeroes=np.zeros((3,3))
# print(zeroes)
# ones=np.ones((3,3))
# print(ones)
# random=np.random.rand(2,3)
# print(random)
# range_arr=np.arange(0,10,12)
# print(range_arr)
# linspace_arr=np.linspace(0,1,5)
# print(linspace_arr)

# b=np.array([[1,2,3],[4,5,6]])
# print(b)
# print(b[1,2])
# print(b[:,1])

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
print(a + b)  # b is broadcasted to match a's shape

# data = np.array([[1, 2], [3, 4]])
# print(data.sum())       # total sum
# print(data.sum(axis=0)) # sum column-wise
# print(data.mean())      # mean
# print(data.min())       # min
# print(data.max())       # max
# print(data.std())       # standard deviation

arr = np.array([1, 2, 3, 4, 5])
print(arr[arr > 3])  # filter
print(arr % 2 == 0)  # boolean mask
