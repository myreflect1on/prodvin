import numpy as np



a = np.array([[1, 1, 1],[2, 2, 2], [3, 3, 3]])
b = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])



c = a.dot(b)
l = np.array([[1, -1, 0], [3, -4, 2]])
n = np.array([[1, 2], [3, 4], [5, 6]])

z = np.array([[1, 0], [4, 1]])
k = z.dot(z.dot(z))
print(4 * 25)