def info_kwargs(**kwargs):
    sort_dict = sorted(kwargs, keys)
    for k, v in sort_dict:
        print(f'{k}: {v}')

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

# age: 28
# first_name: Timur
# job: teacher
# last_name: Guev