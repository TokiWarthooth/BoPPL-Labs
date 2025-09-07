# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 04.09.2025

print('Определитель сумм положительных и отрицательных чисел')
while True:
    print('Для остановки введи "стоп"')
    print('Введите числа через запятую, кроме нуля: ')

    data = input()
    arr = []

    if data != '' and data != 'стоп':
        for num_str in data.split(', '):
            arr.append(int(num_str.strip()))

        majorNums = []
        minorNums = []
        flag = True
        for num in arr:
            if num > 0:
                majorNums.append(num)
            elif num < 0:
                minorNums.append(num)
            elif num == 0:
                flag = False
                print('Вы ввели 0!')
                break
        if flag != False:
            majorSum = 0
            minorSum = 0
            for num in majorNums:
                majorSum += num

            for num in minorNums:
                minorSum += num

            print('Сумма пололжительных чисел: ', majorSum)
            print('Сумма отрицательных чисел: ', minorSum)
        else:
            break
    elif data == '':
        print('Вы ничего не ввели')
    elif data == 'стоп':
        break
    else:
        break