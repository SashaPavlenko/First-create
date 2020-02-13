from monthToNum import month
from numOfYear import numOfYear
from century import century
from season import season
from rome_century import age
from test import test
from week import week

date_list = input('Введите дату >>> ')
date_list_txt = 'Введите дату >>> ' + date_list
date_list = date_list.split()
date_list[0] = int(date_list[0])
date_list[2] = int(date_list[2])

# Число месяца.
d = date_list[0]

# Номер месяца.
m = month[date_list[1]]

# Номер столетия.
c = century(date_list[2])

# Номер года в столетии.
y = numOfYear(date_list[2])

# День недели.
day_of_week = (d + (13*m-1)//5 + y + y//4 - c//4 + 777) % 7

print('----------------')
print('День недели: %s' %week[day_of_week])
print('Век: %s' % age(date_list[2]))
print('Сезон: %s' %season(m))

# Просим прощения. Не против прослушать лекцию по правильному оформлению :).
f = open('Vima.tex', 'w+')
b = '\\documentclass{article}\n\\usepackage[cp1251]{inputenc}\n\\usepackage[russian]{babel}\n\n\\begin{document}'
b += '\n' + date_list_txt + '\n\n' + '----------------' + '\n\n' + 'День недели: %s' %week[day_of_week] + \
'\n\n' + 'Век: %s' % age(date_list[2]) + '\n\n' + 'Сезон: %s' %season(m)
b += '\n\\end{document}'
f.write(b)
f.close()