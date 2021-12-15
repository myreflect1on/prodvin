def comparator(pair):
    return sum([int(i) for i in pair])
print(sorted(input().split(), key=comparator))
print(sorted(input().split(), key = lambda x: sum([int(i) for i in x])))