from random import choice as c
st = '23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
n, m =  int(input()), int(input())
def generate_index():
    s = ''
    for _ in range(m):
        s += c(st)
    return s
for _ in range(n):
    print(generate_index())