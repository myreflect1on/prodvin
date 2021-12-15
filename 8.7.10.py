a, b, c = [set(map(int, input().split())) for _ in range(3)]

print(*sorted(a.intersection(b).difference(c), reverse=1))