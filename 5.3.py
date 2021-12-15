import numpy as np

# put your python code here
n = int(input())
b = np.array([list(map(int, input().split())) for i in range(n)])
c = np.transpose(b)

for i in c:
    print(*i)