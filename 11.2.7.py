m = {}
s = []
for i in range(int(input())):
    name, prod, co = input().split()
    m[name] = m.get(name, {})
    m[name][prod] = m[name].get(prod, 0) + int(co)
for i, k in sorted(m.items()):
    print(i+':')
    for j in sorted(k):
        print(j,k[j])



