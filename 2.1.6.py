num = input()
k = num[:-5]
b = num[-5:]
s = int(k+b[::-1])
print(s)