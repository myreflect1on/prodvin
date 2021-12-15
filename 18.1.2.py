with open('ledger.txt', encoding='utf-8') as file:
    data = list(map(int, map(lambda x: x[1:], map(str.rstrip, file.readlines()))))
print('$'+str(sum(data)))