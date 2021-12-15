n = int(input())
m = int(input())
s = 0
c = 0
max = -100000000000
b = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        if b[i][j] > max:
            max = b[i][j]
            x = i
            y = j

print(x, y)