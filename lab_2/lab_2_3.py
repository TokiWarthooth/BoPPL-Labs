# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 04.09.2025

# импортирую билеотеку, позволяющую работать с регулярками
import re

print('Запись всех слов из двух файлов input_x.txt в новый output.txt')
with open('../data/data_lab_2/data_lab_2_3/input_1.txt', 'r') as wordsFromFile1:
    print('Открытие файла input_1.txt')
    words1 = wordsFromFile1.read()

    # Тут спользую регулярные выражения для отчистки от спецсимволов, можно же было так? (
    cleanedTextFromInput1 = re.sub(r'[^a-zA-Zа-яА-Я\s\^0-9]', '', words1)
    print(cleanedTextFromInput1)

    with open('../data/data_lab_2/data_lab_2_3/input_2.txt', 'r') as wordsFromFile2:
        print('Открытие файла input_2.txt')
        words2 = wordsFromFile2.read()

        cleanedTextFromInput2 = re.sub(r'[^a-zA-Zа-яА-Я\s\^0-9]', '', words2)
        print(cleanedTextFromInput2)

        with open('data/data_lab_2_3/output.txt', 'w') as outputFile:
            outputFile.write(cleanedTextFromInput1 + ' ' + cleanedTextFromInput2)
            print('Запись в output.txt')

print('Файлы были закрыты')