# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 04.09.2025

print('Расчет общего произведния файлов и запись в новый output.txt')
with open('data/data_lab_2_2/input.txt', 'r') as numbers_file:
    print('Открытие файла')
    numbers = numbers_file.readline().strip()
    clearNum = numbers.split(' ')
    numbersList = list(map(int, clearNum))

    proizvedenie = 1
    for num in numbersList:
        proizvedenie *= num

    print('Общее произведение: ', str(proizvedenie))

    with open('data/data_lab_2_2/output.txt', 'w') as output_file:
        output_file.write(str(proizvedenie))
        print('Произвдение записано')

print('Файлы были закрыты')