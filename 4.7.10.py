import numpy as np
num1 = list(input().split())

n1 = int(num1[0])
m1 = int(num1[1])
a = np.array([list(map(int, input().split())) for i in range(n1)])
pr = input()
num2 = list(input().split())
n2 = int(num2[0])
m2 = int(num2[1])
b = np.array([list(map(int, input().split())) for i in range(n2)])

c = a.dot(b)
for i in c:
    print(*i)