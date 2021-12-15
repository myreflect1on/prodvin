s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
def max_str(s):
    result = {}
    c_max = 0
    r_max = ''
    for num in s.split():
        result[num] = result.get(num, 0) + 1
    for i in sorted(result):
        if result[i] > c_max:
            c_max = result[i]
            r_max = i
    print(result)
    return r_max
print(max_str(s))