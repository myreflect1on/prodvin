s = input()
b = s.split()
for i in range(len(b)):
    b[i] = int(b[i])
if len(b) % 2 == 0:
    for i in range(0, len(b), 2):
        b[i], b[i + 1] = b[i + 1], b[i]
else:
    for i in range(0, len(b) - 1, 2):
        b[i], b[i + 1] = b[i + 1], b[i]
print(b)