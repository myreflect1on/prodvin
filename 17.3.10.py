with open('numbers.txt', encoding='utf-8') as file:
    print(*[sum([int(j) for j in i.split()]) for i in file.readlines()], sep='\n')
    # print(m)
    # print(*[sum(map(int, i)) for i in file.readline().split()], sep='\n')

