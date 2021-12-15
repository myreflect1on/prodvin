import random as r
a=set()
while len(a) < 75:
    a.add(r.randint(1, 75))
l = r.sample(a, 25)
matrix = [[l[i * 5 + j] for j in range(5)] for i in range(5)]
matrix[2][2] = 0
for i in range(5):
    for j in range(5):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
