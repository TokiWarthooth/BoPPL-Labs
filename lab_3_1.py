# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 05.09.2025

print('Переместитель слов в предложении в обратном порядке')
words = input('Введите слова: ')

wordsList = words.split()
reversedWordsList = wordsList[::-1]

string = " ".join(map(str, reversedWordsList))

print(string)
