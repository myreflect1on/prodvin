num = int(input())
i = 0
ii = 0
iii = 0
iv = 0

for i in range(num):
    s = input()
    b = s.split()
    for i in range(2):
        b[i] = int(b[i])
    if b[0] >= 0 and b[1] >= 0:
        i += 1
    if b[0] <= 0 and b[1] >= 0:
        ii += 1
    if b[0] <= 0 and b[1] <= 0:
        iii += 1
    if b[0] >= 0 and b[1] <= 0:
        iv += 1
print('Первая четверть:', i)
print('Вторая четверть:', ii)
print('Третья четверть:', iii)
print('Четвертая четверть:', iv)

