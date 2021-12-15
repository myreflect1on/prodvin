n = list(map(int, input().split()))
k = set()
for i in n:
    if i in k:
        print('YES')
    else:
        print('NO')
        k.add(i)