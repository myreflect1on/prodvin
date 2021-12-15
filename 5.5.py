n = int(input())
b = [list(map(int, input().split())) for i in range(n)]
l = n - 1
c = [[0] * n for _ in range(n)]
for i in b:
    c[l] = i
    l -= 1

y = 'YES'

for i in range(n):
    for j in range(n):
        if b[i][j] != b[j][i]:
            y = 'NO'
print(y)
