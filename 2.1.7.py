num  = input()
s = ''
while len(num) > 0:
    s = s + str(num[-3:])+ ' '
    num = num[:-3]
k = []
k = s.split()
k = k[::-1]
r = ','.join(k)
print(r)