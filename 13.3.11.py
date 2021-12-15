n, m = complex(input()), complex(input())
print(f'{n} + {m} = {n + m}')
print(f'{n} - {m} = {n - m}')
print(f'{n} * {m} = {n * m}')
[print(f"{n} {i} {m} =", eval(f"{n}{i}{m}")) for i in "+-*"]