import random as r
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
l = sum(matrix, [])
r.shuffle(l)
matrix = [[l.pop() for j in range(4)] for i in range(4)]
print(matrix)

