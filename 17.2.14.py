file = open('C:/Users/Reflection/PycharmProjects/prodvin/numbers.txt')
print(*[sum(map(int, map(str.rstrip, file.readlines())))])
file.close()
# print(st[random.randint(0, len(st))])