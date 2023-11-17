# багато домашки, ні не багато
# пробіл в кінці коду POSIX, git merge, компілятор


# формат і ф стрінг
# Ще одне форматування з відсотками
# name, mid_name, balance = 'Ігор', 'Васильович', 32.56
# text = "Шановний %s %s, баланс вашого рахунку складає %s грн." %(name, mid_name, balance)
# print(text)


# range що б сформувати список, щоб в форі пройти певну кількість кроків.
# range_1 = range(2, 11, 2)
# print(range_1)
# print(list(range_1))

# case 1 range
# number = int(input("введіть до скількох ви хочте порахувати"))
# for i in range(number):
#     print(i + 1)

list_a = [0, 30, 2]

# for i in range(*list_a):  # в майбутньому розберемо
#     print(i)

# a = 2; b = 16; c = 2
# for i in range(a, b, c):  # підставляємо зміні
#     print(i)

list_a = [777, 30, 21, 43, 13, 23, 43]

# замісь цього
# for i in range(7):  # Не використовуємо рендж коли проходимось по індексам
#     print(list_a[i])

# пиши це
# for i, j in enumerate(list_a):
#     print(f"{i=}, {j=}")
#     print(j)

# коли треба назначити елемент але його не використовувати пишемо нижнє підкреслення(_)


# for i in for, while, чого не можна на ходу міняти ліст, else != break
list_a = [2, 34, 45, 65, 765, 88, 5, 66]
# for i in list_a:
#     if i == 5:
#         print("we find it", i)
#         break
#     else:
#         print(i)
# else:
#     print("ми не знайшли 5")

# counter = 0
# while counter < 20:
#     if counter == 5:
#         print("we find it", counter)
#         break
#     else:
#         print(counter)
#     counter += 2
# else:
#     print(counter, " - не знайдено")

# це впринципі нормально але будь ласка уникайте такого
# print(list_a)
# for index, value  in enumerate(list_a):
#     list_a[index] = value * 2
# print(list_a)

# МИ НЕ ВЗАЄМОДІЄМО З ТИМ СПИСКОМ ПО ЯКОМУ ПРОХОДИМОСЬ, якщо треба то записуємо в новий список.
# Приклад 1
# print(list_a)
# list_b = []
# for i in list_a:
#     if i % 2 == 1:
#         list_b.append(i*2)
#     else:
#         list_b.append(i)
# print(list_b)

# приклад 2
# a = ["a", "b", "c", "d", "e", "y"]
# b = a[:]
# for i in b:
#     del_item = a.pop(0)
#     print(del_item)
#     print(a, i)


# set - приймає тільки не зміні типи даних. Зміний тип даних. SET - mutable, FROZENSET - immutable
# set_a = {3, 4, 5, 6, 6, 3, 4, 5, (3,4,5), 90}
# print(set("djfjdsjkdshfkdjshfdkjhkd fdfdsfh dkjfhds"))
# print(set_a, type(set_a))
# empty_set = set()
# list_a = [3, 4, 5, 6, 6, 3, 4, 5]
# print(list(set(list_a)))  # єдиний варіант запису


list_a = [3, 4, 5]
tuple_a = (3, 4, 5)
set_a = {3, 4, 5}

#  __sizeof__() - скільки займає памяті
# print(list_a.__sizeof__())  # 72
# print(tuple_a.__sizeof__())  # 48
# print(set_a.__sizeof__())  # 200

# dir - подивитись методи
# print(dir(list_a))
# print(dir(tuple_a))
# print(dir(set_a))


# цикл в циклі
# for i in range(2, 10):
#     for j in range(2, 10):
#         print(f"{i}*{j}={i*j}", end=" ")
#     print()


# KISS - keep it simple - пишемо просто, не пишемо зайвого

# # hash - може бути використаний тільки для не змінних типів даних.
# list_a = "[]"
# print(hash(list_a))


# DICT записати
# dict_1 = {}
# dict_2 = dict()
# dict_3 = dict(city="Odesa", village="Myrne")
# dict_4 = dict([(1, 2), ("key", "value")])
# dict_5 = dict.fromkeys([3,4,5], "None")
# dict_6 = {"Павло":["AQA", "Python"], "Dmytro":["DevOps", "bash"]}  # найпоширеніший
#
# print(dict_1, type(dict_1))
# print(dict_2, type(dict_2))
# print(dict_3, type(dict_3))
# print(dict_4, type(dict_4))
# print(dict_5, type(dict_5))
# print(dict_6, type(dict_6))


# dict_6 = {"Павло":["AQA", "Python"], "Dmytro":["DevOps", "bash"]}
# print(dict_6["Павло"])
# print(dict_6.get("Павло", "немає такого"))  # краще перевіряти так, що б ваша программа не впала з помилкою
# print(dict_6.get("Dmytro2", "немає такого"))  # краще перевіряти так, що б ваша программа не впала з помилкою
# print(dict_6)
# dict_6["Павло"].append("AWS")  # додавання в значення
# print(dict_6)
# dict_6["Павло"] = ["PM"]  # зміна зміної (перезапис)
# print(dict_6)
# dict_6["Dmytro"][1] = "AWS"
# print(dict_6)
