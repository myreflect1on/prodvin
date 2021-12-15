m, n = [int(input()) for _ in 'mn']
s = [input() for _ in range(m+n)]
r = 0
for i in s:
    if s.count(i) == 1:
        r += 1
print(r if r > 0 else 'NO')