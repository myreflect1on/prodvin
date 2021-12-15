file = open('C:/Users/Reflection/PycharmProjects/prodvin/prices.txt')
m = list(map(int, (filter(lambda x: x.isdigit(), file.read().split()))))
file.close()
print(sum([m[i]*m[i+1] for i in range(0, len(m), 2)]))





