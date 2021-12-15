s = [input().split(': ') for _ in range(int(input()))]
for i in s:
    i[0] = i[0].lower()
sl = dict(s)
for i in [input().lower() for _ in range(int(input()))]:print(sl.get(i, 'Не найдено'))
