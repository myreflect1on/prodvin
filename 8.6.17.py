set1 = {1, 2, 3, 4, 5}
set2 = [5, 6, 7]
set3 = (7, 8, 9)

print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
# print(set2.isdisjoint(set3))
word = 'beegeek'
set1 = set(word*3)
set2 = set(word[::-1]*2 + 'stepik')

print(set1 < set2)

set1 = set(range(1, 10))
set2 = set(range(10, 20))
print(set1)
print(set2)

print(set1.isdisjoint(set2))