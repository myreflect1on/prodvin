from decimal import *
b = str(Decimal(input())).replace('-','').replace('.','')
print(int(min(b))+ int(max(b)))
