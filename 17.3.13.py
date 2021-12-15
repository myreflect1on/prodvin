with open('population.txt', encoding='utf-8') as file:
    l = list(map(lambda x: x.split('\t'), map(str.rstrip, file.readlines())))
print(*[f'{x}' for x, y in list(filter(lambda x: x[0][0] == 'G' and int(x[1]) > 500_000, l))], sep='\n')