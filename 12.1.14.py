import random as r
sort=set()
while len(sort) < 7:
    sort.add(r.randint(1, 49))
print(*sorted(sort), end=' ')