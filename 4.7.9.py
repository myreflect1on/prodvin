import numpy as np
num = list(input().split())

n = int(num[0])
m = int(num[1])
a = np.array([list(map(int, input().split())) for i in range(n)])
pr = input()
b = np.array([list(map(int, input().split())) for i in range(n)])

c = a + b
for i in c:
    print(*c)