is_num = lambda x: set(x).issubset('-0123456789.') and list(x).count('.') <= 1 and (list(x).count('-') < 1 or list(x).count('-') == 1 and x[0] == '-')
print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
print(is_num('1-1'))
print(is_num('-abcd'))