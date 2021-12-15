n = int(input())
mat = [list(map(int, input().split())) for i in range(n)]
c = [[0] * n for _ in range(n)]
y = 'YES'
s = set(range(1, n + 1))
for i in mat:
    if set(i) != s:
        y = 'NO'
l = n - 1
k = n - 1
for i in range(n):
    for j in range(n):
        c[i][j] = mat[l][i]
        l -= 1
    k -= 1
    l = n - 1
for i in c:
    if set(i) != s:

        y = 'NO'
print(y)