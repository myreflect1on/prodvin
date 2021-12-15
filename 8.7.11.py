a, b, c = [set(map(int, input().split())) for _ in range(3)]

s = a | b | c

l = a ^ b
n = a ^ c
m = b ^ c
s2 = l | n | m

r = s - s2

r2 = a - r
print(*sorted(s2))