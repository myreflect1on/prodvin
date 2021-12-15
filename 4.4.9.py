def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

n = int(input())
m = int(input())
b = [[''] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        b[i][j] = input()
print_matrix(b,n,m)
print()
for i in range(m):
    for j in range(n):
        print(b[j][i], end=' ')
    print()