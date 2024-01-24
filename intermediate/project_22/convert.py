def convert_time(give_time):
    h, m, s = map(int, give_time.split(':'))
    return f'{h} - {m} - {s}'

print(convert_time('18:20:60'))