m = input()+ ' запретил букву'
s = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
for i in s:

    if i in m:
        print(m+' '+i)
        m = m.replace(i, '').replace('  ', ' ')
        m = m.rstrip()
        m = m.lstrip()