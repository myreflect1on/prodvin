k = {'execute':'X', 'write':'W', 'read':'R'}
m ={k: v for k, v in [input().split(' ', 1) for _ in range(int(input()))]}
for i in range(int(input())):
    r = input().split()
    a = k[r[0]]
    if a in ''.join(m[r[1]]):
        print('OK')
    else:
        print('Access denied')
