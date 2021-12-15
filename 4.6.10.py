num = list(input().split())
n = int(num[0])
m = int(num[1])
n_list = [[0 for _ in range(m)] for _ in range(n)]
c = 1
low = 0
high1 =  m - 1
high2 = n - 1
count = 0
res = m * n
if n != m and m != 1 and n != 1:
    count =  int((n+m)/4)
    print(count)
elif n == m:
    count = int(((n + m) / 4) + 1)
elif n == 1:
    for i in range(n):
        for j in range(m):
            n_list[i][j] = j + 1
elif m == 1:
    for i in range(n):
        for j in range(m):
            n_list[i][j] = i + 1

# print('count',count)
for i in range(count):
    for j in range(low, high1 + 1):
        # print(i, j)
        if c <= res:
             if n_list[i][j] == 0:
                 n_list[i][j] = c
                 c += 1
        else:
            break
    for j in range(low + 1, high2 + 1):
         # print(j, high1)
         if c <= res:
             if n_list[j][high1] == 0:
                 n_list[j][high1] = c
                 c += 1
         else:
             break
    for j in range(high1 - 1, low - 1, -1):
        # print(high2, j)
        if c <= res:
            if n_list[high2][j] == 0:
                n_list[high2][j] = c
                c += 1
        else:
            break

    for j in range(high2 - 1, low, -1):
         # print(j, low)
         if c <= res:
             if n_list[j][low] == 0:
                n_list[j][low] = c
                c += 1
         else:
             break
    low = low + 1
    high1 = high1 - 1
    high2 = high2 - 1

for i in range(n):
    for j in range(m):
        print(str(n_list[i][j]).ljust(3), end=' ')
    print()