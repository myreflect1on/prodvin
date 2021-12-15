s = [input().lower().split() for _ in range(int(input()))]
z = [input().lower() for _ in range(int(input()))]
c = 0
for i in z:
    for k, v in s:
        if i == v:
            print(k, end=' ')
            c+=1
    if c == 0:
        print('абонент не найден')
    else:
        c = 0
    print()
