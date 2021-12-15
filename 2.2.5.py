s = input()
b = s.split()
b.sort()
c = 0
for i in range(len(b) - 1):
    if b[i] == b[i + 1]:
        b[i] = ''
for i in range(len(b)):
    if b[i].isdigit():
        c += 1
print(c)