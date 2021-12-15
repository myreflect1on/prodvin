a = list(input())
b = list(input())
c = {'1','2','3','4','5','6','7','8','9','0'}
r = set(a + b)
if len(set(a + b)) == 10:
    print('YES')
else:
    print('NO')
