# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения. Например, в первом задании выводим целые числа,
# начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle


def integer_generator(first_number, last_number):
    for el in count(first_number):
        if el > last_number:
            break
        print(el)


def repeating_list_elements(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i += 1


integer_generator(first_number=int(input("Enter start number: ")),
                  last_number=(int(input("Enter last number: "))))
repeating_list_elements(my_list=[1,2,3], iteration=int(input("enter iteration: ")))
