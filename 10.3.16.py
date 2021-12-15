result = {}
for num in input().split():
    result[num] = result.get(num, 0) + 1
    if result.get(num, 0) > 1:
        print(num + '_' + str(result.get(num, 0)-1), end=' ')
    else: print(num, end=' ')
