n = int(input())
s = [(set(list(input().lower()))) for _ in range(n)]
k =set()
for i in s:
    for j in i:
        k.add(j)
print(len(k))