import math
p = int(input())
k = []
b = []
def pascal(n):
    for i in range(n + 1):
        k.append(int(math.factorial(n)/(math.factorial(i)*math.factorial(n - i))))
    return k
for i in range(p):
    b.append(list(pascal(i)))
    k.clear()
print(b)

