def is_magic(date):
    seq = date.split(".")
    day, month, year = int(seq[0]), int(seq[1]), int(seq[2])
    
    return day * month == year % 100


date = input()

print(is_magic(date))