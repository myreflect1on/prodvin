import numpy as np
n = int(input())
a = np.array([list(map(int, input().split())) for i in range(n)])
m = int(input())
r = np.linalg.matrix_power(a, m)
for i in r:
    print(*i)