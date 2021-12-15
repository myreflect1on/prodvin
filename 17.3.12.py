import random
with open('first_names.txt', encoding='utf-8') as first_names, open('last_names.txt', encoding='utf-8') as last_names:
        for _ in range(3):
                print(random.choice(first_names.readlines()).strip(), random.choice(last_names.readlines()).strip())
                first_names.seek(0)
                last_names.seek(0)


# with open('first_names.txt', encoding='utf-8') as first_names, open('last_names.txt', encoding='utf-8') as last_names:
#         print(random.choice(first_names.readlines()).strip(), random.choice(last_names.readlines()).strip())
# with open('first_names.txt', encoding='utf-8') as first_names, open('last_names.txt', encoding='utf-8') as last_names:
#         print(random.choice(first_names.readlines()).strip(), random.choice(last_names.readlines()).strip())
