def numOfYear(year):
    '''
    Принимает номер года, выводит номер года в столетии.

    '''
    if year % 100 == 0:
        year = 100
    else:
        year = year % 100
    return year
