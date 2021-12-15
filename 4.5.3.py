n = int(input())
m = int(input())
b = [list(map(int, input().split())) for i in range(n)]
s = list(map(int, input().split()))

for i in range(n):
        b[i][s[0]], b[i][s[1]] = b[i][s[1]], b[i][s[0]]

for i in b:
    print(*i)