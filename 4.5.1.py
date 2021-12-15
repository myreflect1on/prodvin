n = int(input())
m = int(input())
b = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        b[i][j] = i*j
for i in range(n):
    for j in range(m):
        print(str(b[i][j]).ljust(3), end=' ')
    print()




