def matrix(a=1, b=0, c=0):
    if b ==  0:
        return [[c for _ in range(a)] for _ in range(a)]
    else:
        return [[c for _ in range(b)] for _ in range(a)]

print(matrix())
print(matrix(3))
print(matrix(3, 1))               # матрица 2 × 5 из 0
print(matrix(3, 4, 9))