n = int(input())
l = [['.' for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            l[i][j] = '*'
        if j == n - i - 1:
            l[i][j] = '*'
        if i == n // 2:
            l[i][j] = '*'
        if j == n // 2:
            l[i][j] = '*'
for i in l:
    print(*i, sep=' ')