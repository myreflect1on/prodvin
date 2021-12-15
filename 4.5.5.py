n = int(input())
b = [list(map(int, input().split())) for i in range(n)]
l = n - 1
c = [[0] * n for _ in range(n)]
for i in b:
    c[l] = i
    print(*i)
    print(l)
    l -= 1

for i in c:
    print(*i)