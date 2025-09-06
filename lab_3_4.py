# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 05.09.2025

import time
from datetime import datetime

while True:
    print('Определитель названия месяца по числу месяца')

    def main():
        numMonth = int(input('Введите числа месяца: '))
        enMonth = process(numMonth)
        result = 'Текущий месяц: ' + ruMonth(enMonth)
        print(result)

    def process(numMonth):
        if numMonth != 0 and numMonth <=12 and  numMonth > 0:
            date = datetime(1999, numMonth, 1)
            return date.strftime('%B')
        else:
            return

    def ruMonth(enMonth):
        if (enMonth == 'January'):
            return 'Январь'
        elif (enMonth == 'February'):
            return 'Февраль'
        elif (enMonth == 'March'):
            return 'Март'
        elif (enMonth == 'April'):
            return 'Апрель'
        elif (enMonth == 'May'):
            return 'Май'
        elif (enMonth == 'June'):
            return 'Июнь'
        elif (enMonth == 'July'):
            return 'Июль'
        elif (enMonth == 'August'):
            return 'Август'
        elif (enMonth == 'September'):
            return 'Сентябрь'
        elif (enMonth == 'October'):
            return 'Октябрь'
        elif (enMonth == 'November'):
            return 'Ноябрь'
        elif (enMonth == 'December'):
            return 'Декабрь'
        else:
            return 'Такого месяца не существует'

    main()