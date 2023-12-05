# Декораторів на функції можна вішати багато.

# Exception part 2

#
# try:
#     print(40/1)
# except:
#     print("На нуль у пайтоні ділити не можна")
# else:
#     print("Все ок")
#
# print("Все ок 2")


# try:
#     print(40/0)
# except:
#     print("На нуль у пайтоні ділити не можна")
#     exit()
# finally:  # завжди відпрацює
#     print("finally")

# def foo(a: int) -> int:
#     if isinstance(a, int):
#         result = a ** 2
#         return result
#     else:
#         raise TypeError("В нашій програмі ми працюємо тільки з цілими числами")
#
# print(foo(3.17))


# рекурсія
# def my_factorial(number: int) -> int:
#     if number <= 1:
#         return 1
#     return number * my_factorial(number - 1)
# print(my_factorial(5))

# import functools
# @functools.lru_cache()  # Зберігає попередні обрахунки і їх не потрібно ще раз обраховувати.
# def fib_rec(number: int) -> int:
#     if number in (1, 2):
#         return 1
#     return fib_rec(number -1) + fib_rec(number -2)
# print(fib_rec(145))

# дз яке не оцінюється вирішити це завжання без рекурсії і сторініх бібліотек
# ВИПАДОК ДЕ РЕКУРСІЯ ТРЕБА
# list_a = [1, 2, 3, ["f", "d", ["434", 78]], 2, 5, 10, [12, 34, 54]]
# list_a2 = [1, 2, 3, 2, 5, 10, [12, 34, 54]]
#
# def dig_into_list(my_list: list) -> None:
#     for list_item in my_list:
#         if isinstance(list_item, list):
#             dig_into_list(list_item)
#         else:
#             print(list_item, end=" ")
#
# dig_into_list(list_a)
# print()
# dig_into_list(list_a2)
# print()
# dig_into_list([34, 43, 432])


# import
import lesson_10_import

import random  # вся бібліотека - найпріоритетніший
# random.randint

from random import randint  # імпорт конкретную функції
# randint

from random import randint as rrandint
# rrandint

from random import *  # імпортує всі функції == так не робіть

# ВЗАЄМОДІЯ З ФАЙЛАМИ
# file = open("text.txt", "r")  # читання файла
# for i in file:
#     print(i)
#     print("---")
# file.close()

# with open("text.txt", "r") as file:  # контекстний менеджер сам закриває. Краще використовувати його.
#     for i in file:
#         print(i)


# with open("text.txt", "w") as file:  # w - write затирає старий файл.
#     file.write("Hello")


# with open("tex2t.txt", "a") as file:  # a - дозапис файлу.
#     file.write("\n")
#     file.write("++-=-=-=-=-")


# ФУНКЦІОНАЛЬНЕ Програмування
# map
# a, b, d, c = map(float, input("введіть ціни").split())
# print(a, type(a))


# ZIP зшиває дві послідовності, повині мати однакову кількість елементів
# list_1 = [1, 23, 4, 6, 43]
# list_2 = [0, 43, 4, 7]
# list_1 = "123"
# list_2 = "567"
# zipped = list(zip(list_2, list_1))  # [(1, 0), (23, 43), (4, 4), (6, 7)] <class 'list'>
# print(zipped, type(zipped))
#
# for i in zipped:
#     print(i)
#
# for i, j in zipped:
#     print(i)
#     print(j)

# filter
list_1 = [1, 23, 4, 6, 43, 500, 1000, 999]
filtered = filter(lambda x: x%2 == 0, list_1)
print(type(filtered))
print(list(filtered))
