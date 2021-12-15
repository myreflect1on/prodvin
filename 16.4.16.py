def comparator(pair):
    return sum([int(i) for i in pair])
m = list(input().split())
n = tuple(m.copy())
print(m)
print(n)
m.sort
print(m)
print(tuple(sorted(n)))

print(sorted(m, key=comparator))
print(tuple(sorted(n, key = lambda x: sum((int(i) for i in x)))))