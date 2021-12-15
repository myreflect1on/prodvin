n = int(input())
m = []
for i in range(n):
    m.append(input())
l = sorted(m, key=lambda x: int(x.split('.')[0])*256**3 + int(x.split('.')[1])*256**2 + int(x.split('.')[2])*256**1 +int(x.split('.')[3])*256**0)
print(*l, sep='\n')
