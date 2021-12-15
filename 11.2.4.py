def build_query_string(params):
    str_ = []
    for i, k in sorted(params.items()):
        str_.append(str(i)+'='+str(k))
    return '&'.join(str_)
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))