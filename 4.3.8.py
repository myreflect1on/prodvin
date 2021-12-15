n = int(input())

k = [[0] * (i + 1) for i in range(n)]
for i in range(len(k)):
    for j in range(len(k[i])):
        k[i][j] = j + 1
for i in k:
    print(i)