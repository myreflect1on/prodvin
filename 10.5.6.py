numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
l = ['1:men', '2:kind', '90:number', '0:sun', '34:book', '56:mountain', '87:wood', '54:car', '3:island', '88:power', '7:box', '17:star', '101:ice']
result = {i: numbers[i]**2 for i in range(len(numbers))}
result2 = {i: l[i] for i in range(len(l))}
print(result2)
