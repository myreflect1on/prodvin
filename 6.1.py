numbers = (0, 1, 3, 14, 2, 7, 9, 8, 10)
print(numbers)
numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)



countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
index = countries.index('Slovenia')
print(index)

countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
number = countries.count('Spain')
print(number)

numbers1 = (1, 2, 3)
numbers2 = (6,)
numbers3 = (7, 8, 9, 10, 11, 12, 13)
l = numbers1*2 + numbers2*9 + numbers3
print(l)

city_name = input()
city_year = int(input())

city = (city_name, city_year)
print(city)