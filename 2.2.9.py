n = int(input())
b = []
c = []
d = ['a', 'n', 't', 'o', 'n']
l = []
e = []
k = 0
for i in range(n):
    b.append(input())

for i in range (len(b)):
    for j in range(len(d)):
        k = b[i][k:].find(d[j])
        print(b[i][k:])
        c.append(b[i][k])
        l.append(k)
    print(*l)
    print(*c)
    if c == d:
        e.append(i+1)
        l.clear()
        c.clear()
    else:
        l.clear()
        c.clear()
print(e)



