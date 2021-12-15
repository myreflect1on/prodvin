file = open('test.txt')
l = file.read().encode('utf-8')
file.close()
print(l)