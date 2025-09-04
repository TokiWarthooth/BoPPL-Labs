# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 04.09.2025

with open("data/data_lab_2_1/numbers", "r") as numbers_file:
    print('Открытие файла')
    numbers = numbers_file.readline().strip()
    clearNum = numbers.split(',')
    arr = []

    for num in clearNum:
        arr.append(int(num))

    maximum = max(arr)
    minimum = min(arr)

    print('Минимальное число в файлу: ', minimum)
    print('Максимальное число в файле:', maximum)
    print('Файл был закрыт')