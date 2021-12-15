c = 0
s = input()
b = s.split()
for i in range(len(b)):
    b[i] = int(b[i])
for i in range(1, len(b)):
    if b[i] > b[i - 1]:
        c += 1
print(c)