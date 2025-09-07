# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 05.09.2025

import math

print('Счетчик среднего арифмитического')

def main():
    numbers = input('Введите числа через пробел: ')
    numbers = list(map(int, numbers.split()))
    result = process(*numbers)
    print(result)

# счетчик суммы
def process(*numbers):
    total = 0
    for num in numbers:
        total += num

    count = len(numbers)
    result = total / count
    return result

main()