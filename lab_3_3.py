# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 05.09.2025

import time
import math

print('Создание кортежа четных чисел')
time.sleep(1)

def main():
    time.sleep(1)
    numbers = input('Введите числа через пробел: ')
    numbers = list(map(int, numbers.split()))
    result = process(*numbers)
    print(result)

# счетчик суммы
def process(*numbers):
    evenNumvers = []
    for num in numbers:
        if num % 2 == 0:
            evenNumvers.append(num)
        else:
            continue

    # функция zip объединение в кортежи
    result = list(zip(evenNumvers))
    return result

main()