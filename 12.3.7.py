import random
def pi_my():
    n = 10**4
    rez = set()
    for _ in range(50):
        rez.add(sum((random.uniform(-1, 1) ** 2 + random.uniform(-1, 1) ** 2 <= 1 for _ in range(n))) / n * 4)
    return sum(rez) / len(rez)

n = 10**6
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)     # случайное число с плавающей точкой от 0 до 1
    y = random.uniform(-1, 1)     # случайное число с плавающей точкой от 0 до 1

    if x**2 + y**2 <= 1:                # если попадает в нужную область
        k += 1
print((k/n)*s0)
print(pi_my())