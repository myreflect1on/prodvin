
print('NO' if len(set(map(int, input().split())).symmetric_difference(set(map(int, input().split())))) > 0 else ['YES'])
