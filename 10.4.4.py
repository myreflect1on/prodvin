s = dict([input().split() for _ in range(int(input()))])
s.update([*zip(s.values(), s.keys())])
print(s.get(input(), 'Не найдено'))