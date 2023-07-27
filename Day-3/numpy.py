import numpy as np

a = np.arange(15).reshape(3,5)
print(a)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)

b = np.array([1.1,2,3,4,5])
print(b)
print(b.dtype)

# Creating arrays with all zeros
arrZeros = np.zeros((10,5))
print(arrZeros)

# Creating arrays with all ones
arrOnes = np.ones((10,5))
print(arrOnes)

print(np.arange(0, 20, 2).reshape(2,5))



# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:")
print(arr)

# Basic array operations
print("\nBasic Array Operations:")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

# Array broadcasting
print("\nArray Broadcasting:")
arr_broadcast = arr + 10
print("Original Array:", arr)
print("Broadcasted Array:", arr_broadcast)

# Indexing and Slicing
print("\nIndexing and Slicing:")
print("First Element:", arr[0])
print("Last Element:", arr[-1])
print("Slice 2nd to 4th Element:", arr[1:4])

# Multi-dimensional arrays
print("\nMulti-dimensional Arrays:")
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)

# Shape and Reshaping
print("\nShape and Reshaping:")
print("Original Shape:", arr_2d.shape)
reshaped_arr = arr_2d.reshape(1, 9)
print("Reshaped Array:", reshaped_arr)

# # Multi-dimensional arrays
# print("\nMulti-dimensional Arrays:")
# arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr_2d)
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# # Array Operations with Broadcasting
# print("\nArray Operations with Broadcasting:")
# arr_2d_sum = arr_2d + arr.reshape(3,3)
# print("Sum with Broadcasting:")
# print(arr_2d_sum)

# NumPy Random Module
print("\nNumPy Random Module:")
random_arr = np.random.rand(3, 3)  # 3x3 random array between 0 and 1
print(random_arr)

# Matrix Operations
print("\nMatrix Operations:")
mat_a = np.array([[1, 2], [3, 4]])
mat_b = np.array([[5, 6], [7, 8]])
mat_product = np.dot(mat_a, mat_b)
print("Matrix A:")
print(mat_a)
print("Matrix B:")
print(mat_b)
print("Matrix Product:")
print(mat_product)
