n = input().split('.')
l = []
for i in n:
    if i.isdigit():
        if 0 <= int(i) <= 255:
            l.append(1)
        else:
            l.append(0)
    else: l.append(0)
print(all(l))