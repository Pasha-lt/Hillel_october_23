# Розбір домашки
# else if, elif
# age = int(input("скільки тобі років?"))
# if age <= 50:
#     print("!!!")
# else:
#     if age < 100:
#         print("!!!")
#     else:
#         if age <= 100000:
#             print("!!!")
#         else:
#             print("!!!")
#
# # краще переписати ось так
# if age <= 50:
#     print("!!!")
# elif age < 100:
#     print("!!!")
# elif age <= 100000:
#     print("!!!")
# else:
#     print("!!!")


# int_number = 100
# if int_number > 10:
#     print(">10")
#
#     if int_number > 100:
#         print(">100")
#
# # краще ось так
# if int_number > 10:
#     print(">10")
#
# if int_number > 100:
#     print(">100")

# квадратне рівняння
# print("ax**2 + Bx + C = 0")
# a = (input("введіть цифру a"))

# a = int(input("введіть цифру a"))  # 1-2
# # розбиваємо на просту структуру
# a = input("введіть цифру a")  # 1
# a = int(a)  # 2


# or,  and
# print(True or True)  # True
# print(True or False)  # True
# print(False or False)  # False
# print(True and False)  # False
# print(False and False)  # False
# print(True and bool(1))  # True


# # форматування коду в пайчармі.  # MAC option+command + l  Windows/Linux cntr + alt + L
# a        =  23 + 999
# print(   a)

# # round()
# print(0.0001  + 0.0002)
# print((1 + 2)/10000)  # вихід 1
# # import decimal  # імпортування нового типу даних який працює з флоат без помилок
# a = 0.0001  + 0.0002
# print(a)  # 0.00030000000000000003
# a = round(a, 2)  # 0.0003  кількість знаків після коми до округлення.
# print(a)

# in str
# string_a = "fdsjlf dfljdsj fljds klfd lfldks"
# print("ljd" in string_a)  # перевіряємо чи буква або стрічка входе в стрічку, чутливий до регісту

# f string
# name = "Ivan"
# age = 32
# print(f"Hi {name}, you are {age} old")   # =  print("Hi",  name, "you are", age, "old")
# print(f"Hi {name}, you are {age + 32} old")
# new_string = f"Hi {name}, you are {age + 32} old"
# print(new_string)


# len кількість символів або елементів в масиві повертає int
# print(len(new_string))


# strip, lstrip, rstrip - повертає стрічку
# my_string = "+++ abc +++ fdfds +++"
# print(my_string.strip("+"))  # abc +++ fdfds
# print(my_string.lstrip("+"))  # abc +++ fdfds +++
# print(my_string.rstrip("+"))  # +++ abc +++ fdfds

#   count
# print(my_string.count("ab"))  # кількість елементів або слів, складів в колекції

# isdigit, isalpha - повертає результат в булевому типі даних
# var_1 = "999"
# var_2 = "text"
# print(var_2.isdigit())  # перевірка чи це число, підійте тільки для int, float флоат поверне помилку
# print(var_2.isalpha())  # перевірка чи це букви, якщо там будуть числа то зломається
# number_a = input()
# number_b = input()
#
# if number_a.isdigit() and number_b.isdigit():  # перевіряємо чи в нас числа
#     print((int(number_a) + int(number_b))*3)
# else:
#     print("ми працюємо тільки з цілими числами")

# зрізи в стр find,

# string_a = "Првиіт, як справи? як твій день?"
# index_1 = 10
# print(string_a[0])
# print(string_a[4])
# print(string_a[0:4])
# print(string_a[0:index_1])
# print(string_a[:10])
# print(string_a[10:])
# print(string_a[:])
# print(string_a[:1000])
# print(string_a[-5:-1])
# print(string_a[-0:4])
# print(string_a[::2])
# print(string_a[len(string_a )//2 +4:])

# приоритети операцій
# print(1 + 2 * 3)
# print((1 + 2) * 3)
# () - Дужки
# ** - Піднесення до степеня
# +x, -x, ~x - Унарні плюс, мінус і бітове заперечення
# *, /, //, %
# *, /, //, % - Множення, ділення, цілочисельне ділення, остача від ділення
# +, - - Додавання та віднімання
# <<, >> - Бітові зсуви
# & - Бітове І (AND)
# ^ - Бітове виключне АБО (XOR)
# | - Бітове АБО (OR)
# ==, !=, >, >=, <, <=, is, is not, in, not in - Порівняння, перевірка ідентичності, перевірка належності
# not - Логічне НЕ (NOT)
# and - Логічне І (AND)
# or - Логічне АБО (OR)

# list, списка
# list_a = []  # empty list
# print(type(list_a), list_a)
# list_b =[1, 23.0, 1, 1, None, True, "rerer", [324,434,43]]
# print(type(list_b), list_b)
# print(list_b[-2].upper())
# print(list_b[-1][1])

# list_a = [23,45,656]
# list_b = list_a
# print(id(list_a), id(list_b), sep="\n", end="\nце все\n")
#
# print(list_a)
# print(list_b)
# list_b.append(100)
# print(list_a)
# print(list_b)
#
# del_element = list_b.pop()  # можем і не зберігати.
# print(list_a)
# print(list_b)
# print(type(del_element), del_element)

# list_a = [23,45,656]
# list_b = list_a[:]  # 1 варіант
# print(list_a)
# print(list_b)
# list_a.append(200)
# print(list_a)
# print(list_b)
#
# # second variant Більш приорітетний і правильний
# import copy
# list_c = [23,45,656]
# list_d = copy.deepcopy(list_c)
# print(list_c)
# print(list_d)
# list_c.append(200)
# print(list_c)
# print(list_d)

# list_a = [12, 10, 4, 12, 11]
# print(sum(list_a)/len(list_a))
#
# string_a = "345 678 12"
# list_of_number = string_a.split()
# print(type(list_of_number), list_of_number)
# print(list_of_number[1])

