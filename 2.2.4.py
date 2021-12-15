# put your python code here
s = input()
b = s.split()
for i in range(len(b)):
    b[i] = int(b[i])


b.insert(0, b[-1])
del b[-1]
print(*b)