s = [i.strip('(.,;:-?!)') for i in input().lower().split()]

result = {}
c_min = 100
r_min = ''
for num in s:
    result[num] = result.get(num, 0) + 1
for i in sorted(result):
    if result[i] < c_min:
        c_min = result[i]
        r_min = i
print(r_min)
# print(s)
# print(result)