# # на наступний урок генератор компрехеншн
# list_comp = [i ** 2 for i in range(10)]
# gen_comp = (i ** 2 for i in range(10))

# задача 1
# class Student:
#     DICT_MARKS = {
#         2: "Погано",
#         3: "Задовільно",
#         4: "Добре",
#         5: "Відмінно"
#     }
#
#     name = "Pasha"
#     list_grade = [3, 4, 5, 5]
#
#
#
#     def min_grade(self, list_grade: list[int]):
#         min_mark = min(list_grade)
#         return self.DICT_MARKS.get(min_mark)
#
#     def __str__(self):
#         text = f"{self.name} {self.min_grade(self.list_grade)}"
#         return text
#
# a = Student()
# print(a)
# a.list_grade[0] = 4
# print(a)


# задача 2 Декоратор
# def type_checker(func):
#     def _wrapper(*args, **kwargs):
#         print("type checker")
#         for arg in args:
#             if not isinstance(arg, int):
#                 raise TypeError
#         result = func(*args, **kwargs)
#         return result
#     return _wrapper
#
# @type_checker
# def foo(*args, **kwargs):
#     return 200
#
# foo(1,2,3)
# foo(1,2, 3.0)
# Ускладнюємо наш декоратор, тепер він буде приймату аргумент на який треба перервірити тип даних

# def type_checker_param(*types):
#     def type_checker(func):
#         def _wrapper(*args, **kwargs):
#             print("new type checker")
#             for arg in args:
#                 if not isinstance(arg, types):
#                     raise TypeError
#             result = func(*args, **kwargs)
#             return result
#         return _wrapper
#     return type_checker
#
#
# @type_checker_param(int, float)
# def foo(*args, **kwargs):
#     return 200
#
#
# foo(1, 2, 3)
# foo(1, 2, 3.0)
# foo(1, "2", 3.0)

# # args kwarg
# def foo(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
#
# print(foo(2,3,10,1,1,2))

# # lambda
# def foo(x):
#     return x ** 2
#
# print(foo(2))
# foo_2 = lambda x: x**2  # це лише для розуміння, так не пишемо.
# print(foo_2(3))
#
# foo_3 = lambda : "hello"  # це лише для розуміння, так не пишемо.
# print(foo_3())

# Помилки
# class WrongLang(Exception):
#     def __str__(self):
#         print("Ми не використовуємо рус мову.")
#
# class TextCreator:
#     def __init__(self, text):
#         for i in text:
#             if ord(i) in (1099, 1105, 1098, 1101):
#                 raise WrongLang
#         self.text = text
#
#     def __str__(self):
#         return f"{'*'*20} \n\n {self.text} \n {'*'*20}"
#
# text_1 = TextCreator("привіт, це Павло я займаюсь автоматизацією на Python")
# print(text_1)
# text_2 = TextCreator("привет это Павел, я занимаюсь автоматизацией на Python" )
# print(text_2)

# --> iterator(__iter__() __next__()) VS generator(yield) <--

# Як елсе працює не з іфом.
# for i in for, while, чого не можна на ходу міняти ліст, else != break
list_a = [2, 34, 45, 65, 765, 88, 105, 66]


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
#     print("не знайдено число яке шукали")

# Області видимості.


# GIT BRANCHES
# L - local, E - nonlocal(enclosing)(# Замикання області видимості нон локал  - кому цікаво.) G -global  B - builtins(print)

def foo():
    a = 200  # локальна область видимості
    print(a)  # саме print() в нас builtins

a = "hello"  # глобал область видимості


