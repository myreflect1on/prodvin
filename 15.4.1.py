def generator_square_polynom(a, b, c):
    def square_polynom(x):
        return a*x + b*x + c
    return square_polynom

f = generator_square_polynom(a=2, b=-4.5, c=25)
g = generator_square_polynom(a=2, b=0, c=-3)
h = generator_square_polynom(a=-3, b=-10, c=50)

print(f(1))
print(g(2))
print(h(-1))

s1 = 'python'
s2 = 'stepicon'
s3 = 'beegeek'

print(min(s1, s2, s3))
print(max(s1, s2, s3))