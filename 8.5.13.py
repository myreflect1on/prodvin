s = list(input().lower().split())
r = []
k =set()

for i in s:
    for j in i:
        if j not in '.,;:-?!':
            r.append(j)
    b = ''.join(r)
    k.add(b)
    r.clear()
print(len(k))