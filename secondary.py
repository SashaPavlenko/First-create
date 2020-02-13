from test import test
from weekday import weekday
from monthToNum import month
from week import week
from rome_century import age
from season import season

date_list = '13 февраля 2020'
print('Введите дату >>> ', date_list)
date_list_txt = 'Введите дату >>> ' + date_list
date_list = date_list.split()
date_list[0] = int(date_list[0])
date_list[2] = int(date_list[2])

# Номер месяца.
m = month[date_list[1]]

# День недели.
# Примечание: нумерация в списке month начинается с марта, в функции weekday требуется нумерация с января.
day_of_week = weekday(date_list[2], (m+2) % 12, date_list[0])

print('----------------')
print('День недели: %s' % week[day_of_week % 7])
print('Век: %s' % age(date_list[2]))
print('Сезон: %s' % season(m))

f = open('Vima_secondary.tex', 'w+')
b = '\\documentclass{article}\n\\usepackage[cp1251]{inputenc}\n\\usepackage[russian]{babel}\n\n\\begin{document}'
b += '\n' + date_list_txt + '\n\n' + '----------------' + '\n\n' + 'День недели: %s' %week[day_of_week] + \
'\n\n' + 'Век: %s' % age(date_list[2]) + '\n\n' + 'Сезон: %s' %season(m)
b += '\n\\end{document}'
f.write(b)
f.close()