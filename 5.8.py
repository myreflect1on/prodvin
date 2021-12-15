n = int(input())
mat = [['.' for _ in range(n)] for _ in range(n)]
c = 0
m = 0
for i in range(n):
    for j in range(n):
        if i == j:
            # mat[i][j] = 0
            for k in range(i, n):
                mat[i][k] = c
                c += 1

            for m in range(i, n):
                mat[i][m  -j] = m
                m -= 1


            c = 0
            m = 0
for i in mat:
    print(*i)