

is_non_negative_num = lambda x: set(x).issubset('0123456789.') and list(x).count('.') <= 1
print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num(987, 45, 55))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))
print(set('987'))
print(set('0123456789'))
print(set('987').issubset('0123456789'))
