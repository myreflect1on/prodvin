dct = {}
for _ in range(int(input())):
    phone, fio = input().lower().split()
    dct.setdefault(fio, []).append(phone)
for _ in range(int(input())):
    print(*dct.get(input().lower(), ['абонент не найден']))