def info_kwargs(**kwargs):
    print(*[k+': '+str(v) for k, v in sorted(kwargs.items())], sep='\n')




info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')