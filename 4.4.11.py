n = int(input())
s = 0
b = []
c = 0
for i in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    s = sum(b[i]/len(b[i]))
    for j in range(n):
        if b[i][j] > s:
            c += 1
    print(c)
    c = 0
