fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
s_fruits = sorted(fruits, reverse=True)
for i in s_fruits:
    print(*i)