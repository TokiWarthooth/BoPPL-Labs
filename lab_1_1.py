# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 04.09.2025

print("Проверка на регистр строк")
while True:
    print('Для остановки введи "стоп"')
    data = input("Введите текст: ")
    if data.lower() == data and data.lower() != 'стоп':
        print('NO')
    elif data.lower() == 'стоп':
        break
    else:
        print('YES')