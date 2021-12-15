n = int(input())
c = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        c[i][i] = 1
        c[i][n - i - 1] = 1

for i in c:
    print(*i)