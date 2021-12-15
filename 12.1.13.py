import random as r
chars = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
print(*[chars[r.randint(1, 50)] for _ in range(int(input()))], sep='')
