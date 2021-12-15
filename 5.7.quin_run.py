coor_j = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
coor_i = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
c = [['.' for _ in range(8)] for _ in range(8)]

k = list(input())
x = coor_j[k[0]]
y = coor_i[k[1]]
for i in range(8):
    for j in range(8):
        if x == j:
            c[i][j] = '*'
        if y == i:
            c[i][j] = '*'
        if i - y == j - x:
            c[i][j] = '*'
        if abs(y - i) == abs(x - j):
            c[i][j] = '*'
c[y][x] = 'Q'
for i in c:
    print(*i)