def fancy(length, char1, char2):
    return (char1 + char2) * length + char1
print(fancy(5, '-', '*'))
def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1
print(fancy(3))
def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1
print(fancy(3, '.'))
def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1
print(fancy(2, ':', '|'))
def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1
print(fancy(4, char2='#'))
def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1
print(fancy(char2='$', length=3))