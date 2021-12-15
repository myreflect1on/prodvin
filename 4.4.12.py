n = int(input())
s = 0
c = 0
max = -1**99
b = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        if i >= j and i < n - 1 - j or i >= j and i > n - 1 - j:
            if b[i][j] > max:
                max = b[i][j]
print(max)
