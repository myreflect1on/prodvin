from string import ascii_uppercase as a
from random import randint as r, sample as s
def generate_index():
    return ''.join(s(a,2))+str(r(0, 99))+'_'+str(r(0, 99))+''.join(s(a,2))
print(generate_index())