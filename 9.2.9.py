m, n = [int(input()) for _ in 'mn']
k = len({input() for _ in range(m)} ^ {input() for _ in range(n)})
print(k if k > 0 else 'NO')