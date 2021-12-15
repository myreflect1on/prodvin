import math

n = int(input())
shag = int(input())
sp = list(range(1, n + 1))
i = 0
while len(sp)>1:
    i = (i+(shag)-1)%(len(sp))
    del sp[i]
print(sp[0])