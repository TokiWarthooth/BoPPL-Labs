# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 05.09.2025

import time
print('Переместитель слов в предложении в обратном порядке')
time.sleep(1)
words = input('Введите слова: ')

wordsList = words.split()
reversedWordsList = wordsList[::-1]

string = " ".join(map(str, reversedWordsList))

print(string)
