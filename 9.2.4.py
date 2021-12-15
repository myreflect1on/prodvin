n = int(input())
k = set()
for i in range(n):
    k.add(input())
print('REPEAT' if input() in k else 'OK')

