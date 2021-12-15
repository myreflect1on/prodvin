n = int(input())

k = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        k[i][j] = j + 1
for i in k:
    print(i)
