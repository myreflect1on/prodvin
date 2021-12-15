import random
file = open('C:/Users/Reflection/PycharmProjects/prodvin/' + input())
st = file.readlines()
file.close()
print(st[random.randint(0, len(st))])