n = int(input())
b = [input().split() for _ in range(n)]
c =[]
for i in b:
    if int(i[1]) > 3:
        c += [i]
for i in b:
    print(*i)
print()
for i in c:
    print(*i)