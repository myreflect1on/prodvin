def read_csv():
    with open('data.csv', encoding='utf-8') as file:
        keys = file.readline().strip().split(',')
        data = [i.strip().split(',') for i in file.readlines()]
    resalt = []
    m = []
    for j in data:
        for i in range(len(keys)):
            m.append([keys[i],j[i]])
        resalt.append(dict(m))
        m.clear()
    print(resalt, end='')
read_csv()