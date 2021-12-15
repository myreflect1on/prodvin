with open('class_scores.txt', encoding='utf-8') as file, open('new_scores.txt', 'w') as output:
    data = list(map(lambda x: [x[0], int(x[1]) + 5] if int(x[1]) + 5 < 100 else [x[0], 100], [i.rstrip().split() for i in file]))
    [print(*i, file=output) for i in data]
