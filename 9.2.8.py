m, n = [int(input()) for _ in 'mn']
print(len({input() for _ in range(m)} - {input() for _ in range(n)}))