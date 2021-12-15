n = int(input())
s = [len(set(list(input().lower()))) for _ in range(n)]
for i in s:
    print(i)