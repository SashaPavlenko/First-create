def weekday(year, month, day):
    if month < 3:
        year -= 1
        month += 10
    else:
        month -= 2
    return (day + 31*month//12 + year + year//4 - year//100 + year//400) % 7

print(weekday(2019, 9, 23))