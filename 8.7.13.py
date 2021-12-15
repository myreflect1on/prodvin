a, b, c = [set(map(int, input().split())) for _ in range(3)]
f = {0,1,2,3,4,5,6,7,8,9,10}
s = a | b | c

l = f - c - a - b
n = a ^ c
m = b ^ c
s2 = l | n | m

r = s - s2

r2 = a - r
print(*sorted(l))