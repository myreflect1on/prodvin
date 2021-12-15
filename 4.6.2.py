n = int(input())
c = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        c[i][n - i - 1] = 1
        if i + j + 1 > n:
            c[i][j] = 2
for i in c:
    print(*i)