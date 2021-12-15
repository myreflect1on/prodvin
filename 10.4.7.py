s = list(input())
d = {k.lower(): v for _ in range(int(input())) for k, v in [input().split(': ', 1)]}
slov = ''
for i in s:
    slov += d.get(s.count(i))
print(slov)

