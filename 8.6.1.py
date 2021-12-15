myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset1 -= myset2
print(myset1)

set1 = {'a', 'b', 'c', 'd', 'h'}
set2 = {'b', 'd', 'f', 'h'}

set3 = set1 - set2 & set1

print(set3)