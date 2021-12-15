import math
n = int(input())
k = []
def pascal(n):
    for i in range(n + 1):
        k.append(int(math.factorial(n)/(math.factorial(i)*math.factorial(n - i))))
    return k


print(pascal(n))