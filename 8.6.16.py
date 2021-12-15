a = [set(map(int, list(input()))) for _ in range(int(input()))]
for i in range(len(a)- 1):
    a[0].intersection_update(a[i + 1])
print(*sorted(a[0]))