l = set(map(int, input().split())).intersection(set(map(int, input().split())))
print(*sorted(l, reverse=1) if len(l) > 0 else ['BAD DAY'])
