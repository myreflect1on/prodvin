m = list(input())
l = []
if len(m) < 7:
    l.append(False)
l.append(any(map(lambda x: x.islower(), m)))
l.append(any(map(lambda x: x.isupper(), m)))
l.append(any(map(lambda x: x.isdigit(), m)))
print('YES' if all(l) else 'NO')
