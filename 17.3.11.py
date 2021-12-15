import string
with open('file.txt', encoding='utf-8') as file:
    m = file.readlines()
    file.seek(0)
    l = file.read()

print('Input file contains:')
print(len(list(filter(lambda x: x in string.ascii_letters, l))), 'letters')
print(len(l.split()), 'words ')
print(len(m), 'lines')

