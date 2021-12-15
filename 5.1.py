n = input().split()
k = int(input())
b = []
l = [[0 for j in range(0)] for i in range(k)]
c = 0
for i in range(k):
    for j in range(c, int(len(n)), k):
        # print(n[j])
        l[i].append(n[j])
    c += 1
print(l)

