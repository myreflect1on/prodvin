import random
# for i in range(int(input())):
#     print(('Орел','Решка')[random.randrange(0,2)])


# [print(('Орел','Решка')[random.randint(0,1)] for _ in range(int(input())))]
print(*[random.randint(1,6) for i in range(int(input()))], sep = '\n')