# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 04.09.2025

import re
# Библиотека для считывания частоты
from collections import Counter

print('Определитель частоты повторяемости каждой кириллической буквы в тексте, сортировка в порядке убывания частоты, и запись результата в файл output.txt')
with open('data/data_lab_2_4/input.txt', 'r') as wordsFromFile1:
    print('Открытие файла input.txt')
    allText = wordsFromFile1.read()

    # Токже использую регулярку, сначала чищу текст полностью от всего, оставляю только русские слова без пробелов, привож в нижний регистр все символы
    russianWords = re.sub(r'[^а-яА-Я]', '', allText).lower()

    # Считаю каждый символ (частоту)
    symbCounter = Counter(russianWords)

    pairListOfSymb = list(symbCounter.items())

    n = len(pairListOfSymb)
    for i in range(n):
        for j in range(0, n - i - 1):
            if pairListOfSymb[j][1] < pairListOfSymb[j + 1][1]:
                pairListOfSymb[j], pairListOfSymb[j + 1] = pairListOfSymb[j + 1], pairListOfSymb[j]

    with open('data/data_lab_2_4/output.txt', 'w', encoding='utf-8') as output_file:
        for russianSymb, pair in pairListOfSymb:
            line = f"{russianSymb}: {pair}\n"
            print(line.strip())
            output_file.write(line)

print('Файлы были закрыты')