with open('grades.txt', encoding='utf-8') as file:
    data = list(map(str.rstrip, file.readlines()))
m =[]
for i in data:
    m.append([i.split()[0], int(i.split()[1]), int(i.split()[2]), int(i.split()[3])])
print(len(list(filter(lambda x: x[1]>= 65 and x[2]>= 65 and x[3]>= 65,m))))
# for i in :
#     print(*i)

