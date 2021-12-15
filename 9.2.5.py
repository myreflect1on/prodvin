n = int(input())
m = int(input())
n_ = {input() for _ in range(n)}
m_ = [input() for _ in range(m)]
for i in m_:
    print('YES' if i in n_ else 'NO' )