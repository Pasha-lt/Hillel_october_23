# Назва функції дієслово
# def foo(age: int, username: str = "default") -> str:
#     string = f"{username}, {age}"
#     return string


# Namespace BGLN (built in, global, local, non-local)

# point_b = 777  # global
#
# def foo(age: int, username: str = "default") -> str:
#     point_a = 999  # local
#     string = f"{username}, {age}"
#     print(point_b)
#
#     return string
#
# print(point_b)

# Можна використовувати одну назву зміних в різних функція так як в функції локальна область видимості.
# d = 32
# def foo(d):
#     d = d + 32
#     print(d)
#     return "no None"
#
# def foo1(d):
#     d = d + 32
#     print(d)
#     return "no None"
#
# def foo2(d):
#     d = d + 32
#     print(d)
#     return "no None"
#
#
# foo(d=10)
# foo1(d=20)
# foo2(d=30)


# в функції ми не обьявляємо список, сет, дікт бо це зміний тип даних і для різних викликів буде одне і те ж айді.
# def foo(arg_a, list_1=tuple([])):
#     list_1 = list(list_1)
#     list_1.append(arg_a)
#     return list_1
# print(foo(13))
# print(foo(15))
# print(foo(34))

# Lambda, анонімно функція

calc_dict = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "-": lambda a, b: a - b
}
#
# print(calc_dict["+"](199, 1))
# print(calc_dict["*"](4, 3))
def concatenate(string_a : str, string_b : str) -> str:
    result = string_a + string_b
    return result



# sorted
# list_1 = [34, 456, 11, 12, -100, 77, 100, 35, 100.0, 100]
# list_2 = ['груша', 'грушаa', 'банан',  'яблуко', 'диня', "слива", "апельсин"]
# print(sorted(list_1, reverse=True))
# print(sorted(list_1, key=lambda x: x%2))
# print(sorted(list_2, key=len))
# print(sorted(list_2, key=lambda a: a[-1]))
#


# todo Питають на співбесіді: Що таке args і kwargs -> *args - аргументи , **kwargs - іменовані аргументи
# a, b, *c = [2, 3, 4, 4, 5, 6]
# print(a, b, c)

# def foo(*args) ->int|float:
#     age, height, *list_2 = args
#     if list_2 != []:
#         for i in list_2:
#             print(i)
#
#     print(age, height)
#     return "sum(list_1)"
#
# print(foo(34, 43))



# def foo2(*args, **kwargs):
#     grades_list = args
#     dict_1 = kwargs
#     print(dict_1)
#     print(grades_list)
#
# foo2(33, 200, 90, a=22, b=77, c=45)
# dict_a = {33:32}
# dict_b = {30:100}
#
# dict_c = {**dict_a, **dict_b}
# print(dict_c)


# import



# Постмен-> requests
# test_postman

# Selenium
# test_selenium


# YAGNI (You Aren't Going to Need It — «Вам це не знадобиться»)

# Selenium, requests, python, postman, API, pytest, - додати в лінкедін і підтвердити навички





# ascii (укрстрінг), ord VS chr
print(ascii("c"))  # eng c
print(ascii("с"))  # укр c

print(ord("F"))  # 70
print(ord("f"))  # 102

print(chr(102))  # f
print(chr(72))  # H




