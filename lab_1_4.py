# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 04.09.2025

print('Определитель високосного года')
while True:
    year = int(input('Введите год: '))

    if year % 4 != 0:
        print('Год не был високосным')
    elif year % 100 != 0:
        print('Год не был високосным')
    elif year % 400 != 0:
        print('Год не был високосным')
    else:
        print(str(year) + ' год был високосным!')
        break