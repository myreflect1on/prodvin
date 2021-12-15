n = int(input())

b = [list(map(int, input().split())) for i in range(n)]
c = 'YES'

for i in range(n):
    for j in range(n):
        if b[i][j] != b[j][i]:
            c = 'NO'


print(c)