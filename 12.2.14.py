from random import choice as c, shuffle as sh
n, m =  int(input()), int(input())
def generate_index():
    s = c('23456789')
    l = m // 2
    for _ in range(l):
        s += c('abcdefghijkmnpqrstuvwxyz')
    for _ in range(m-l-1):
        s += c('ABCDEFGHJKLMNPQRSTUVWXYZ')
    b = list(s)
    sh(b)
    return ''.join(b)
for _ in range(n):
    print(generate_index())