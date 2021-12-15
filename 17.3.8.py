with open('data.txt', encoding='utf-8') as file:
     print(*list(map(str.rstrip, [i for i in file.readlines()]))[::-1], sep='\n')