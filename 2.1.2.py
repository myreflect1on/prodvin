m = float(input())
r = float(input())

imt =  m/r**2
if 18.5 <= imt <= 25:
    print('Оптимальная масса')
elif 18 > imt:
    print('Недостаточная масса')
else:
    print('Избыточная масса')