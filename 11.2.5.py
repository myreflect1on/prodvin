def merge(m):
    l = {}
    for i in m:
        for j, k in i.items():
            l[j] = l.get(j, set())
        for j, k in i.items():
            l[j].add(k)
    return l


print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))