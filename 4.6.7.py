n = list(input().split())

co = 1
c = [[0 for _ in range(int(n[1]))] for _ in range(int(n[0]))]
for i in range(0, int(n[1])):
    for j in range(0, int(n[0])):
        c[j][i] = (i + j) % int(n[1]) + 1

for i in range(int(n[0])):
    for j in range(int(n[1])):
        print(str(c[i][j]).ljust(3), end=' ')
    print()