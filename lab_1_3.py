# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 04.09.2025

print('Чистка повторяющихся чисел')

while True:
    print('Введите n целые числа через запятую: ')

    data = input()
    arr = []

    for num_str in data.split(', '):
        arr.append(int(num_str.strip()))

    unic_arr = []
    for num in arr:
        if num not in unic_arr:
            unic_arr.append(num)

    for num in unic_arr:
        print(num)