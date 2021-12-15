# m = [set(input().split()[1] for _ in range(int(input()))) for _ in range(int(input()))]
# l = []
# for i in m:
#     l.append(any(map(lambda x: int(x) == 5, i)))
m = [set(input().split()[1] for _ in range(int(input()))) for _ in range(int(input()))]
print('YES' if all([any(map(lambda x: int(x) == 5, i)) for i in m]) else 'NO')
