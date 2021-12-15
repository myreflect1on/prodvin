list1 = [[1] * 3] * 3
list1[0][1] = 5
print(list1[1][1])
for i in list1:
    print(i)

my_list = [[1], [2, 3], [4, 5, 6]]
total = 0

for row in my_list:
    total += sum(row)

print(type(total))

my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    maximum = max(row)
    minimum = min(row)

print(maximum + minimum)

my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    if max(row) > maximum:
        maximum = max(row)
    if min(row) < minimum:
        minimum = min(row)

print(maximum + minimum)