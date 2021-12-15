n = int(input())
s = 0
c = 0
max = -1 / 10**50
b = [list(map(int, input().split())) for i in range(n)]
s1 = 0
s2 = 0
s3 = 0
s4 = 0


for i in range(n):
    for j in range(n):
        if i <= j and i <= n - 1 - j:
            s1 += b[i][j]
        elif i <= j and i >= n - 1 - j:
            s2 += b[i][j]
        elif i >= j and i >= n - 1 - j:
            s3 += b[i][j]
        elif i >= j and i <= n - 1 - j:
            s4 += b[i][j]


print('Верхняя четверть:', s1)
print('Правая четверть:', s2)
print('Нижняя четверть:', s3)
print('Левая четверть:', s4)