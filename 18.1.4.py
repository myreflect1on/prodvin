with open('words.txt', encoding='utf-8') as file:
    data = list(map(str.rstrip, file.read().split()))
print(*filter(lambda x: len(x) == len(max(data, key=len)), data), sep='\n')
# print(data)# print(len(max(data, key=len)))