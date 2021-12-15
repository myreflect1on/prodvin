from fractions import Fraction as F
print(sum([F(1, i**2) for i in range(1, int(input())+1)]))