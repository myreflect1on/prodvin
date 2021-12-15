import random as r
sort=set()
while len(sort) < 100:
    sort.add(r.randint(1000000, 9999999))
print(*sorted(sort), sep='\n')