import numpy as np

def ismagic(a):
    if np.array_equal(np.unique(a.sum(axis=1)),np.unique(a.sum(axis=0))):
        return True
    else:
        return False

n = int(input())
b = np.matrix([list(map(int, input().split())) for i in range(n)])

print(ismagic(b))