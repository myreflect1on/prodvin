import random as r
n = [input() for _ in range(int(input()))]
l = [i for i in n]
k =[]
r.shuffle(l)
i = 0
while len(l) > 0:
    m = n.pop()
    if m != l[i]:
        k.append([m, l[i]])
        del l[i]
    else:
        k.append([m, l[i+5]])
        del l[i+1]
for i in k:
    print(i[0],'-',i[1])

