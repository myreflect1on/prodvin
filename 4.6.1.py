n = list(input().split())

co = 0
c = [['.' for _ in range(int(n[1]))] for _ in range(int(n[0]))]
for i in range(int(n[0])):
    for j in range(int(n[1])):
        if co % 2 == 0:
            c[i][j] = '.'
        else:
            c[i][j] = '*'
        co += 1
    co += 1
for i in c:
    print(*i)
