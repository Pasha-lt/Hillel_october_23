# перенос
# shopping_list = [32, 32]
# delete_item = int(input(f'Введіть номер товару який хочете видалити зі списку (від 1 до {len(shopping_list)}): '))

# перенос словника
# dict_6 = {
#     "Павло":["AQA", "Python"],
#     "Dmytro":["DevOps", "bash"],
#     "Dmytro2":["DevOps", "bash"],
#     "Dmytro3":["DevOps", "bash"],
#     "Dmytro4":["DevOps", "bash"],
#     "Dmytro5":["DevOps", "bash"],
#     "Dmytro6":["DevOps", "bash"],
#     "Dmytro7":["DevOps", "bash"]
# }
# print(dict_6)

# однакова кількість кавичок. Взагалі нормальна практика однакова кількість кавичок по всьому проекту.
# age = 10
# print("Hello")
# print('my name ...')
# print("""age ...""")
# print(f"my age \"{age}\" \\n")  # -екранування символів
# print('m')


# dir(__builtins__) зарезервовані слова
# for i in dir(__builtins__):
#     print(i)

# # capitalize VS title
# our_string = "Привіт мене звуть Андрій. мене звуть "
# print(our_string.capitalize())  # Привіт мене звуть андрій. мене звуть
# print(our_string.title())  # Привіт Мене Звуть Андрій. Мене Звуть

# Пріорітети 1 читабельність коду 2 швидкість коду(set) 3 память - advance
# if coupon == 'так' or coupon == 'т' and coupon == 'yes' or coupon == 'y':
# if coupon in ['так', 'т', 'yes', 'y']:
# if coupon in ('так', 'т', 'yes', 'y'):
# if coupon in {'так', 'т', 'yes', 'y'}:


# dict
# dict_6 = {"Павло":["AQA", "Python"]}
# dict_7 = dict_6
# dict_8 = {"OOO": 77777, "f13s": 6789}
# dict_7.update({"fd": 77777, "fds": 6789})  # додати два словника то ж саме dict_6 |= dict_8
#
# print(dict_6)
# print(dict_7)
# print(dir(dict_8))

# dict_6 = {"Павло":["AQA", "Python"], "fd": 77777, "fds": 6789}

# for key in dict_6: # keys
#     print(key)
#
# for key in dict_6.keys(): # keys
#     print(key)
#
# for value in dict_6.values(): # values
#     print(value)
#
# for key, value in dict_6.items(): # keys and values
#     print(f"{key=}")
#     print(f"{value=}")

# print(dir(dict_6))
# dict_6.clear()
# print(dict_6)

# print(dict_6)
# del dict_6["fds"]  # не треба використовувати робіть pop()
# print(dict_6)
#
# print(dict_6)
# dict_6.pop('fd')
# print(dict_6)

# print(["1234", 213] > ["123", 213, 5435, 432432, 432423, 4324])  # непотрібні порівняння треба розуміти як воно працює!!!


# PEP8 - https://peps.python.org/pep-0008/ - як оформлювати код.

# func
# Найпростіший
# def my_print():
#     print("старт роботи")
#
# my_print()

# bar foo
# def foo(name, age):
#     print(f"my name {name}, I  {age} y.o.")
#
# foo("Pavlo", 67)
# foo(67, "Pavlo")  # порядок важливий
# foo(name="Ярослав", age=16)  # Найбільш коректний
# foo(age=16, name="Ярослав")


# def foo(age, name="Noname"):
#     if name == "Noname":
#         print(f"I {age} y.o.")
#     else:
#         print(f"my name {name}, I  {age} y.o.")
#
# foo(67, "Pavlo")  # порядок важливий
# foo(88)  # порядок важливий

# розширення функцій які існують VS власний функціонал
# def my_print(string):
#     print("#" * 50)
#     print(string)
#     print("#" * 50)

#
# my_string = "next level"
# my_print(string=my_string)


def my_print(string):
    new_string = f"{'#' * 30}\n{string}\n{'#' * 30}"
    return new_string


my_string = "next level"
new_result = my_print(string=my_string)


# print(new_result)

# випадок з апенд list_a = [1,2,3]; print(list_a.append(777)) None
# list_a = [1,2,3]
# print(list_a.append(777))


# function Атомарність одна функція одна дія VS god object
# def foo(number_1, number_2):
#     result = number_1 * number_2
#     return result


# def bar(string):
#     new_string_1 = f"ваш добуток {string}"
#     return new_string_1
#
# # виклик 1
# result_mult = foo(number_1=12, number_2=3)
# new_string = bar(string=result_mult)
# print(new_string)
#
# # виклик 2
# new_string = bar(foo(5, 2))
# print(new_string)
#
# # виклик 3
# user_number_1 = int(input("please putt first number: "))
# user_number_2 = int(input("please putt second number: "))
# result_mult = foo(number_1=user_number_1, number_2=user_number_2)
# new_string = bar(string=result_mult)
# print(new_string)
#
# # виклик 4
# user_number_1 = 9
# user_number_2 = 3
# result_mult = foo(number_1=user_number_1, number_2=user_number_2)
# new_string = bar(string=result_mult)
# print(new_string)


# pass - затичка/заглушка
# def foo():
#     pass
#
# for i in "fdsfdsf":
#     if i == "f":
#         pass
#     else:
#         print(i)
#
# fd = 1234324

# Типізації
list_a : list = [32,43,43]  # не обовзяково

def foo(number_1 : int | float, number_2 : int | float):  # РЕКОМЕНДУЮ
    result = number_1 + number_2
    return result

print(foo(number_1=3, number_2=4))

