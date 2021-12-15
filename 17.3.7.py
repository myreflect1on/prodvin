with open('text1.txt', encoding='utf-8') as file:
    print(*list(map(lambda x: x[::-1], file.readline().split()[::-1])))