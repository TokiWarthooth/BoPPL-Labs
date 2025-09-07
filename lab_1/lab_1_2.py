# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 04.09.2025

print('Сокращение инициалов полного имени')
while True:
    print('Для остановки введи "стоп"')
    data = input('Введите полное имя фамилию и отчество: ')
    if data.lower() == 'стоп':
        break
    nssArr = data.split()
    shortName = nssArr[0][:1]
    shortSurname = nssArr[1][:1]

    if len(nssArr) > 2:
        secondName = nssArr[2]
    else:
        secondName = ''

    print(shortName + '.' + shortSurname + '. ' + secondName)