coor_j = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
coor_i = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
c = [['.' for _ in range(8)] for _ in range(8)]

k = list(input())
x = coor_j[k[0]]
y = coor_i[k[1]]

print(x, y)
c[y][x] = 'N'

for i in range(8):
    for j in range(8):
        if (x - j) * (y - i) == 2 or (x - j) * (y - i) == -2:
            c[i][j] = '*'
for i in c:
    print(*i)


