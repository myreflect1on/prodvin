file = open('C:/Users/Reflection/PycharmProjects/prodvin/nums.txt')
print(sum(map(int, file.read().split())))

file.close()