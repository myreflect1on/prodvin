s = dict([input().split(' ', 1) for _ in range(int(input()))])
l = [input() for i in range(int(input()))]
for j in l:
    for k, v in s.items():
        if j in v:
            print(k)

