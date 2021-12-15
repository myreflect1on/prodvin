s = input()
b = list(s)
count = 0
max = 0
for i in range(len(b)):
    if b[i] == 'Р':
        # if b[i] == b[i+1]:
        count += 1
        if count > max:
            max = count
    else:

        count = 0
print(max)

