n = int(input())
s = 1
b = []
c = 0
for i in range(n):
    b.append(int(input()))
r = int(input())

for i in range(len(b)):
    for j in range(len(b)):
        if i != j:
            if (b[i] * b[j]) == r:
                c += 1
if c > 0:
    print('ДА')
else:
    print('НЕТ')

