file = open('C:/Users/Reflection/PycharmProjects/prodvin/' + input())
st = file.readlines()
file.close()
print(st[len(st)-2])