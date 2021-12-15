result = set()
for i in range(int(input())):
    if i == 0:
        result = result | set([input() for j in range(int(input()))])
    else:
        result = result & set([input() for j in range(int(input()))])
print(*sorted(result), sep='\n')


