# # Наслідування
#
# class User:
#     name = "Taras"
#     _phone = "0931234567"  # protected
#
#     def say_hello(self):
#         return f"імя {self.name} телефон - {self._phone}"
#
#     def get_contact(self):
#         return self.contact
#
#
# class Developer(User):
#     program_language = "HTML"
#     english_level = "C1"
#
#     def say_hello(self):
#         return f"імя {self.name} телефон - {self._phone} Я багато заробляю"
#
#
# class Admin(User):
#     program_language = "Bash"
#
# class ThirdClass(Admin, Developer):  # від першого наслідника візьмуться основні речі.
#     pass
#
#
#
# user_1 = User()
# user_2 = Developer()
#
# print(user_1.name)
# print(user_2.name)
# print(user_1.say_hello())
# print(user_2.say_hello())
#
# user_3 = ThirdClass()
# print(user_3.name)
# print(user_3.program_language)

# ПЕРЕЗАВАНТАЖЕННЯ МЕТОДІВ, тобто перезапис

# class User2:
#     # todo init - це не конструктор класу. в конструктор класу входить ще __prepare__, __new__, __init__
#     def __init__(self, name, age):
#         self.name = self.fix_name(name)
#         self.age = age
#
#     def fix_name(self, name):
#         new_name = name.title()
#         return new_name
#
#     def say_hello(self):
#         return f"привіт, я {self.name}"
#
#     def __str__(self):  # те що треба для прінта
#         return f"я обʼєкт классу User2, моє імя {self.name}"
#
#     def __repr__(self):  # ще один метод виводу, який наглядно демонcтрує що все не треба вчити.
#         return f"Моє імя {self.name}, Це не вчіть"
#
# user_1_1 = User2("irina", 32)
# print(user_1_1.say_hello())
#
# user_1_2 = User2("Igor", 32)
# print(user_1_2.say_hello())
#
# print(user_1_1)

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


# class Point:
#     x = None
#     y = None
#
#     def __init__(self, x_coord, y_coord):
#         self.x = x_coord
#         self.y = y_coord
#
#
# point_1 = Point(0, 1)
# point_2 = Point(10, 15)
#
#
# class Line:
#     begin = None
#     end = None
#
#     def __init__(self, begin_point, end_point):
#         self.begin = begin_point
#         self.end = end_point
#
#     def __str__(self):
#         return (f"Наша лінія з початковими координатами {self.begin.x}:{self.begin.y}, "
#                 f"та кінцевими координатами {self.end.x}:{self.end.y}")
#
#
# line_1 = Line(point_1, point_2)
#
# print(line_1.end.x)
# print(line_1.end.y)
#
# print(line_1)

class A:
    def __init__(self, text):
        self.text = text

    def __bool__(self):
        if len(self.text) < 20:
            return False
        return True

    def __eq__(self, other):  # ==
        print(abs(len(self.text) - len(other.text)))
        if not isinstance(other, type(self)):
            raise TypeError
        elif abs(len(self.text) - len(other.text)) < 10:
            return True
        else:
            return False

a = A("привіт")
a_2 = A("привіт, мене звуть павло бла бла бла бла бла блабла бла блабла бла блабла бла блабла бла блабла бла бла")
a_3 = A("привіт, мене звуть павло бла бла бла бла бла блабла бла блабла бла блабла бла блабла бла блабла")
print(a == a_2)
print(a_2 == a_3)