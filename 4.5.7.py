n = int(input())
b = [list(map(int, input().split())) for i in range(n)]
l = n - 1
k = n - 1
c = [[0] * n for _ in range(n)]
for i in range(b):
    for j in range(b):
        c[i][j] = b[l][i]
        print(l)
        l -= 1
    k -= 1
    l = n - 1
for i in c:
    print(*i)