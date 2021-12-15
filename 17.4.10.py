with open('input.txt', encoding='utf-8') as file, open('output.txt', 'a') as output:
    data = list(map(str.rstrip, file.readlines()))
    print(*list(map(lambda x: str(data.index(x) + 1) + ') ' + x , data)),sep='\n', file=output)
    # print(, file=output)