n = int(input())
s = 0
b = []
for i in range(n):
    b.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i == j:
            s += b[i][j]
print(s)