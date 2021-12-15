import random
with open('random.txt', 'a') as output:
    [print(random.randint(111, 777), file=output) for _ in range(25)]