digits3 = {frozenset(int(i) for i in input().split()) for _ in range(int(input()))}
digits4 = [{int(c) for c in input().split()} for _ in range(int(input()))]
# digits4 = set(digits3)
print(*digits3)
print(*digits4)