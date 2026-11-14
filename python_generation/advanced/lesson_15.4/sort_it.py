def sort_by_field(lst, field):
    def get_key(athlete):
        return athlete[field - 1]
    return sorted(lst, key=get_key)

athletes = [
    ('Дима', 10, 130, 35),
    ('Тимур', 11, 135, 39),
    ('Руслан', 9, 140, 33),
    ('Рустам', 10, 128, 30),
    ('Амир', 16, 170, 70),
    ('Рома', 16, 188, 100),
    ('Матвей', 17, 168, 68),
    ('Петя', 15, 190, 90)
]
n = int(input())
athl_sorted = sort_by_field(athletes, n)
for a in athl_sorted:
    print(*a)