with open('lines.txt', encoding='utf-8') as file:
    m = max([i for i in file.readlines()], key=len)
    file.seek(0)
    print(*[i.rstrip() for i in file.readlines() if len(i) == len(m)], sep='\n')