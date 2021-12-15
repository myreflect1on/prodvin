m = []
n = int(input())
a, b = complex(input()), complex(input())
for i in range(1, n + 1):
    m.append(a**i + b**i)
print(sum(m))