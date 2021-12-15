from functools import reduce
m = input().split()
n = int(input())
l = 0
# for i in range(len(m)):
#     l += int(m[i])*(n**int((len(m)) - i - 1))
# print(l)
print(reduce(lambda x, m, n: int(x)*n**(len(m) - x -1), m))